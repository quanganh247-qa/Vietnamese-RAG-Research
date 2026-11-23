"""LLM-as-judge tiếng Việt, chỉ số "nhầm điều luật" (H1b), phiếu gán nhãn người 100 câu dev và Cohen's κ (Ngày 11–13).

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.judge <answers.jsonl> <questions.jsonl> <corpus> <out_judge.jsonl> --model ...
    PYTHONPATH=src python -m ragvi.judge --human-sheet <answers.jsonl> <questions.jsonl> <corpus> <out_sheet.md>
    PYTHONPATH=src python -m ragvi.judge --kappa <graded_sheet.md> <out_judge.jsonl>
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import random
import re
import time
from pathlib import Path

from ragvi.generate import (CTX_LIMIT, chunking_of_config, clean_generation, is_refusal, load_generator,
                            subset_chunks, truncate_tokens)
from ragvi.rerank import load_units
from ragvi.retrieval import load_jsonl, open_append, read_rows

ARTICLE_RE = re.compile(r'\bđiều\s+(\d+)\b', re.I)


def blind_id(config, qid):
    """Mã ẩn danh 10 ký tự hex cho cặp (config, qid) để người gán nhãn không biết tên điều kiện (Ngày 12)."""
    return hashlib.sha256(f'{config}::{qid}'.encode('utf-8')).hexdigest()[:10]

PROMPT_JUDGE = """Bạn là giám khảo đánh giá câu trả lời của hệ thống hỏi đáp tiếng Việt.
Hãy đối chiếu "Câu trả lời" với "Ngữ cảnh đã cung cấp" và "Bằng chứng vàng", rồi trả về ĐÚNG MỘT đối tượng JSON hợp lệ (không giải thích thêm ngoài JSON) theo mẫu:
{{"claims": [{{"text": "<mệnh đề trong câu trả lời>", "supported_by_context": true, "supported_by_gold": false}}], "correctness": 1}}

Quy tắc chấm:
1. Tách "Câu trả lời" thành các mệnh đề khẳng định cụ thể trong danh sách `claims`.
2. Với mỗi mệnh đề:
   - `supported_by_context`: `true` nếu mệnh đề được "Ngữ cảnh đã cung cấp" hỗ trợ hoàn toàn, `false` nếu bịa đặt hoặc mâu thuẫn với ngữ cảnh (nếu Ngữ cảnh là "(không cung cấp - closed-book)" thì để `null`).
   - `supported_by_gold`: `true` nếu mệnh đề được "Bằng chứng vàng" hỗ trợ hoàn toàn, `false` nếu có thông tin sai hoặc không có căn cứ trong bằng chứng vàng.
3. `correctness` (điểm độ đúng của câu trả lời so với Bằng chứng vàng):
   - `0`: Sai, lạc đề, hoặc không trả lời được câu hỏi.
   - `1`: Đúng một phần nhưng còn thiếu ý quan trọng hoặc diễn đạt chưa chính xác hoàn toàn.
   - `2`: Đúng và đầy đủ theo Bằng chứng vàng.

Câu hỏi: {question}

Ngữ cảnh đã cung cấp:
{context}

Bằng chứng vàng:
{gold}

Câu trả lời:
{answer}"""


def cited_articles(answer):
    """Danh sách số Điều được viện dẫn trong `answer` (theo thứ tự xuất hiện, không trùng)."""
    seen, out = set(), []
    for num in ARTICLE_RE.findall(answer or ''):
        num = str(int(num))
        if num not in seen:
            seen.add(num)
            out.append(num)
    return out


def gold_articles(gold_doc_ids):
    """Tập số Điều của các điều luật vàng (phần sau dấu `+` trong mã tài liệu Zalo; D2)."""
    return {str(int(d.rsplit('+', 1)[1])) for d in (gold_doc_ids or []) if '+' in d and d.rsplit('+', 1)[1].isdigit()}


def wrong_article_citation(answer, gold_doc_ids):
    """Chỉ số 'nhầm điều luật' cho H1b (D2): câu trả lời dẫn số Điều không khớp số điều của điều luật vàng."""
    cited = cited_articles(answer)
    gold = gold_articles(gold_doc_ids)
    return {
        'cited_articles': cited,
        'gold_articles': sorted(gold),
        'wrong_article': bool(cited) and any(a not in gold for a in cited),
    }


def parse_judge_json(raw):
    """Trích và kiểm tra đối tượng JSON `{"claims": [...], "correctness": 0|1|2}` từ đầu ra của judge."""
    text = clean_generation(raw)
    m = re.search(r'\{.*\}', text, flags=re.S)
    if not m:
        raise ValueError(f'Không tìm thấy đối tượng JSON trong đầu ra judge: {text[:120]!r}')
    data = json.loads(m.group(0))
    if not isinstance(data, dict) or not isinstance(data.get('claims'), list):
        raise ValueError(f'JSON thiếu danh sách claims hợp lệ: {data!r}')
    if data.get('correctness') not in (0, 1, 2):
        raise ValueError(f'Trường correctness phải thuộc {{0, 1, 2}}, nhận được: {data.get("correctness")!r}')
    for c in data['claims']:
        if not isinstance(c, dict) or 'text' not in c or 'supported_by_gold' not in c:
            raise ValueError(f'Mệnh đề trong claims không hợp lệ: {c!r}')
    return data


def derive_judge_metrics(parsed, refused, is_closed_book=False):
    """Từ JSON của judge tính H_gold, H_ctx và correctness theo quyết định D3–D4.

    Câu từ chối không có mệnh đề nào, tính vào false refusal chứ không tính vào H_gold hay H_ctx.
    """
    if refused:
        return {'correctness': 0, 'h_gold': None, 'h_ctx': None, 'n_claims': 0}
    claims = parsed.get('claims') or []
    h_gold = int(any(not bool(c.get('supported_by_gold')) for c in claims))
    h_ctx = None if is_closed_book else int(any(not bool(c.get('supported_by_context')) for c in claims))
    return {'correctness': int(parsed['correctness']), 'h_gold': h_gold, 'h_ctx': h_ctx, 'n_claims': len(claims)}


def format_gold_evidence(question_row, corpus_text_of):
    """Ghép bằng chứng vàng (đoạn vàng + đáp án vàng với ViQuAD; điều luật vàng với Zalo) cho judge."""
    ids = question_row.get('gold_doc_ids') or ([question_row['gold_doc_id']] if 'gold_doc_id' in question_row else [])
    docs = [corpus_text_of[d] for d in ids if d in corpus_text_of]
    answers = [a['text'] if isinstance(a, dict) else a for a in (question_row.get('answers') or [])]
    parts = []
    if answers:
        parts.append('Đáp án vàng: ' + ' | '.join(answers))
    parts.extend(docs)
    return '\n\n'.join(parts)


JUDGE_MAX_CHARS = 15000  # khớp trần 4.000 token của oracle (~15.000 ký tự) để không cắt mất khoản cuối của điều luật dài


def _clip(text, max_chars=JUDGE_MAX_CHARS):
    return text if len(text) <= max_chars else text[:max_chars].rstrip() + ' …'


def run_judge(answer_rows, questions_by_qid, context_of, gold_of, out_path, judge_fn, model_name='', workers=1):
    """Chấm điểm các câu trả lời của câu hỏi trả lời được (`answerable=True`), ghi nối tiếp vào `out_path`.

    Khi `workers > 1` (ví dụ gọi `llama-server` có continuous batching), gửi song song `workers` yêu cầu.
    Tự động tái sử dụng kết quả chấm khi prompt `(qid, context, gold, answer)` trùng khít với cấu hình đã chấm.
    """
    existing = [r for r in read_rows(out_path) if not r.get('error')]
    done = {(r['config'], r['qid']) for r in existing}
    pending = [row for row in answer_rows
               if row.get('answerable', True) and (row['config'], row['qid']) not in done
               and row['qid'] in questions_by_qid]
    if not pending:
        return 0

    ans_by_key = {(r['config'], r['qid']): r for r in answer_rows}
    gold_cache = {}
    ctx_cache = {}
    prompt_cache = {}

    def _gold(qid):
        hit = gold_cache.get(qid)
        if hit is None:
            hit = _clip(gold_of(questions_by_qid[qid]))
            gold_cache[qid] = hit
        return hit

    def _ctx(config, qid):
        if config == 'closed_book':
            return '(không cung cấp - closed-book)'
        key = (config, qid)
        hit = ctx_cache.get(key)
        if hit is None:
            hit = _clip(context_of(config, qid))
            ctx_cache[key] = hit
        return hit

    for r in existing:
        if r.get('refused') or r.get('claims') is None or r.get('correctness') is None:
            continue
        cfg, qid = r['config'], r['qid']
        arow = ans_by_key.get((cfg, qid))
        if arow is not None and qid in questions_by_qid:
            p = PROMPT_JUDGE.format(
                question=questions_by_qid[qid]['question'], context=_ctx(cfg, qid),
                gold=_gold(qid), answer=arow.get('answer', ''))
            prompt_cache[p] = {'claims': r['claims'], 'correctness': r['correctness']}

    def _one(row):
        config, qid = row['config'], row['qid']
        q = questions_by_qid[qid]
        refused = bool(row.get('refused') or is_refusal(row.get('answer', '')))
        is_cb = config == 'closed_book'
        cite = wrong_article_citation(row.get('answer', ''), q.get('gold_doc_ids')) if 'gold_doc_ids' in q else {}
        if refused:
            scores = derive_judge_metrics({'claims': [], 'correctness': 0}, True, is_closed_book=is_cb)
            return {'config': config, 'qid': qid, 'judge_model': model_name, 'refused': True,
                    'claims': [], **scores, **cite, 'error': None}
        prompt = PROMPT_JUDGE.format(
            question=q['question'], context=_ctx(config, qid), gold=_gold(qid), answer=row.get('answer', ''))
        cached = prompt_cache.get(prompt)
        if cached is not None:
            scores = derive_judge_metrics(cached, False, is_closed_book=is_cb)
            return {'config': config, 'qid': qid, 'judge_model': model_name, 'refused': False,
                    'claims': cached['claims'], **scores, **cite, 'seconds': 0.0, 'error': None}
        t0 = time.perf_counter()
        raw = judge_fn(prompt)
        elapsed = round(time.perf_counter() - t0, 3)
        try:
            parsed = parse_judge_json(raw)
            prompt_cache[prompt] = {'claims': parsed['claims'], 'correctness': parsed['correctness']}
            scores = derive_judge_metrics(parsed, False, is_closed_book=is_cb)
            return {'config': config, 'qid': qid, 'judge_model': model_name, 'refused': False,
                    'claims': parsed['claims'], **scores, **cite, 'seconds': elapsed, 'error': None}
        except (ValueError, json.JSONDecodeError) as e:
            return {'config': config, 'qid': qid, 'judge_model': model_name, 'refused': False,
                    'claims': None, 'correctness': None, 'h_gold': None, 'h_ctx': None, 'n_claims': None,
                    **cite, 'seconds': elapsed, 'raw': raw, 'error': str(e)}

    written = 0
    with open_append(out_path) as f:
        if workers and workers > 1:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                for out_row in ex.map(_one, pending):
                    f.write(json.dumps(out_row, ensure_ascii=False) + '\n')
                    f.flush()
                    written += 1
        else:
            for row in pending:
                out_row = _one(row)
                f.write(json.dumps(out_row, ensure_ascii=False) + '\n')
                f.flush()
                written += 1
    return written


def build_human_sheet(answer_rows, questions_by_qid, context_of, gold_of, n=50, seed=0):
    """Trộn ngẫu nhiên `n` câu trả lời dev (ẩn tên cấu hình) để người gán nhãn chấm trước khi xem điểm judge."""
    pool = [r for r in answer_rows if r.get('answerable', True) and not r.get('refused')
            and r['qid'] in questions_by_qid]
    pool.sort(key=lambda r: (r['config'], r['qid']))
    picked = random.Random(seed).sample(pool, min(n, len(pool)))
    lines = [
        '# Phiếu gán nhãn tay đối chiếu Judge (Ngày 12–13)\n\n'
        'Hướng dẫn: với mỗi mẫu (đã ẩn tên cấu hình), đọc Câu hỏi, Ngữ cảnh đã cung cấp, Bằng chứng vàng và '
        'Câu trả lời rồi đánh `[x]` vào đúng một ô cho mỗi dòng:\n'
        '- `Correctness` (so với Bằng chứng vàng): `0` (sai), `1` (đúng một phần), `2` (đúng và đầy đủ).\n'
        '- `H_gold`: Câu trả lời có mệnh đề nào KHÔNG được Bằng chứng vàng hỗ trợ không? (`0` = không, `1` = có).\n'
        '- `H_ctx`: Câu trả lời có mệnh đề nào KHÔNG được Ngữ cảnh hỗ trợ không? (`0` = không, `1` = có, `NA` = không có ngữ cảnh).\n'
    ]
    for i, r in enumerate(picked, 1):
        config, qid = r['config'], r['qid']
        q = questions_by_qid[qid]
        ctx = '(không cung cấp - closed-book)' if config == 'closed_book' else context_of(config, qid)
        bid = blind_id(config, qid)
        lines.append(
            f'\n---\n\n## Mẫu {i} — `{bid}`\n\n'
            f'**Câu hỏi:** {q["question"]}\n\n'
            f'**Ngữ cảnh đã cung cấp:**\n> ' + '\n> '.join(ctx.splitlines()) + '\n\n'
            f'**Bằng chứng vàng:**\n> ' + '\n> '.join(gold_of(q).splitlines()) + '\n\n'
            f'**Câu trả lời:** {r["answer"]}\n\n'
            'Correctness: [ ] 0   [ ] 1   [ ] 2\n'
            'H_gold: [ ] 0   [ ] 1\n'
            'H_ctx: [ ] 0   [ ] 1   [ ] NA\n'
        )
    return ''.join(lines)


def cohen_kappa(y1, y2, weights=None):
    """Cohen's κ (không trọng số hoặc trọng số tuyến tính `weights='linear'`) cho hai danh sách nhãn nguyên."""
    if len(y1) != len(y2) or not y1:
        raise ValueError('Hai danh sách nhãn phải cùng độ dài và khác rỗng.')
    labels = sorted(set(y1) | set(y2))
    if len(labels) == 1:
        return 1.0
    n = len(y1)
    idx = {lab: i for i, lab in enumerate(labels)}
    k = len(labels)
    mat = [[0] * k for _ in range(k)]
    for a, b in zip(y1, y2):
        mat[idx[a]][idx[b]] += 1
    row_sum = [sum(mat[i]) for i in range(k)]
    col_sum = [sum(mat[i][j] for i in range(k)) for j in range(k)]
    max_span = max(labels[-1] - labels[0], 1)

    def w(i, j):
        if weights == 'linear':
            return abs(labels[i] - labels[j]) / max_span
        return float(i != j)

    po_dis = sum(w(i, j) * mat[i][j] for i in range(k) for j in range(k)) / n
    pe_dis = sum(w(i, j) * row_sum[i] * col_sum[j] for i in range(k) for j in range(k)) / (n * n)
    return 1.0 if pe_dis == 0 else 1.0 - po_dis / pe_dis


def parse_human_sheet(markdown):
    """Đọc các nhãn đã đánh `[x]` từ phiếu `build_human_sheet` (khóa là mã ẩn danh `blind_id` hoặc `config::qid`)."""
    out = {}
    for block in re.split(r'^## Mẫu \d+ — ', markdown, flags=re.M)[1:]:
        key = block.split('`')[1]
        if '::' in key:
            key = blind_id(*key.split('::', 1))
        c_line = next((l for l in block.splitlines() if l.startswith('Correctness:')), '')
        g_line = next((l for l in block.splitlines() if l.startswith('H_gold:')), '')
        x_line = next((l for l in block.splitlines() if l.startswith('H_ctx:')), '')
        c_hits = [int(m) for m in re.findall(r'\[[xX]\]\s*([012])', c_line)]
        g_hits = [int(m) for m in re.findall(r'\[[xX]\]\s*([01])', g_line)]
        x_hits = re.findall(r'\[[xX]\]\s*(0|1|NA)', x_line)
        if len(c_hits) == 1 and len(g_hits) == 1 and len(x_hits) == 1:
            out[key] = {
                'correctness': c_hits[0],
                'h_gold': g_hits[0],
                'h_ctx': None if x_hits[0] == 'NA' else int(x_hits[0]),
            }
    return out


def evaluate_kappa(human_labels, judge_rows):
    """Tính Cohen's κ giữa người và judge cho H_gold, H_ctx và correctness (có trọng số tuyến tính)."""
    norm_human = {(blind_id(*k) if isinstance(k, tuple) else k): v for k, v in human_labels.items()}
    judge_map = {blind_id(r['config'], r['qid']): r
                 for r in judge_rows if r.get('error') is None and not r.get('refused')}
    shared = sorted(set(norm_human) & set(judge_map))
    if not shared:
        raise ValueError('Không có cặp (config, qid) chung nào giữa phiếu nhãn người và kết quả judge.')
    h_gold_h = [norm_human[k]['h_gold'] for k in shared if judge_map[k].get('h_gold') is not None]
    h_gold_j = [judge_map[k]['h_gold'] for k in shared if judge_map[k].get('h_gold') is not None]
    ctx_keys = [k for k in shared if norm_human[k]['h_ctx'] is not None and judge_map[k].get('h_ctx') is not None]
    corr_h = [norm_human[k]['correctness'] for k in shared if judge_map[k].get('correctness') is not None]
    corr_j = [judge_map[k]['correctness'] for k in shared if judge_map[k].get('correctness') is not None]
    return {
        'n_shared': len(shared),
        'kappa_h_gold': cohen_kappa(h_gold_h, h_gold_j),
        'kappa_h_ctx': cohen_kappa([norm_human[k]['h_ctx'] for k in ctx_keys],
                                   [judge_map[k]['h_ctx'] for k in ctx_keys]) if ctx_keys else None,
        'kappa_correctness_linear': cohen_kappa(corr_h, corr_j, weights='linear'),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('paths', nargs='*', help='<answers.jsonl> <questions.jsonl> <corpus> <out.jsonl/.md>')
    parser.add_argument('--chunks', help='file chunks/*.jsonl (ví dụ __c3.jsonl) để lấy văn bản các chunk ngữ cảnh')
    parser.add_argument('--model', default='Qwen/Qwen3.5-9B')
    parser.add_argument('--llama-url', help='URL llama-server dùng mô hình judge riêng')
    parser.add_argument('--workers', type=int, default=0,
                        help='số luồng gửi batch song song tới llama-server (0 = tự chọn 8 khi có --llama-url)')
    parser.add_argument('--limit', type=int, help='chỉ chấm N câu trả lời được đầu tiên (ví dụ 20 câu dev ở Ngày 11)')
    parser.add_argument('--human-sheet', action='store_true', help='xuất phiếu gán nhãn tay (Ngày 12)')
    parser.add_argument('--kappa', nargs=2, metavar=('PHIEU_DA_CHAM', 'JUDGE_JSONL'), help='tính κ (Ngày 13)')
    parser.add_argument('--n', type=int, default=50)
    parser.add_argument('--seed', type=int, default=0)
    args = parser.parse_args(argv)

    if args.kappa:
        sheet_path, judge_path = args.kappa
        human = parse_human_sheet(Path(sheet_path).read_text(encoding='utf-8'))
        res = evaluate_kappa(human, read_rows(judge_path))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return

    if len(args.paths) != 4:
        parser.error('Cần 4 đường dẫn: <answers.jsonl> <questions.jsonl> <corpus> <out>, hoặc dùng --kappa')
    ans_path, q_path, corpus_path, out_path = args.paths
    answers = [r for r in read_rows(ans_path) if r.get('answerable', True)]
    if args.limit:
        answers = answers[:args.limit]
    questions = {q['qid']: q for q in load_jsonl(q_path)}
    corpus_text_of, _, _ = load_units(corpus_path)
    unit_text_of = dict(corpus_text_of)
    chunks_by_c = {}
    if args.chunks and Path(args.chunks).exists():
        cpath = Path(args.chunks)
        if cpath.is_file():
            chunk_text_of, _, _ = load_units(cpath)
            unit_text_of.update(chunk_text_of)
            for tag in ('c5_nohead', 'c5', 'c4', 'c3', 'c1'):
                if cpath.stem.endswith(f'__{tag}'):
                    chunks_by_c[tag] = dict(corpus_text_of, **chunk_text_of)
                    break
    ctx_ids_of = {(r['config'], r['qid']): r.get('context_ids') or [] for r in answers}
    tok = None
    for cfg in sorted({r['config'] for r in answers}):
        c_name = chunking_of_config(cfg)
        if not c_name:
            continue
        if c_name not in chunks_by_c:
            chunks_by_c[c_name] = dict(corpus_text_of)
        missing_docs = [cid.rsplit('#', 1)[0]
                        for r in answers if r['config'] == cfg and not r.get('refused')
                        for cid in (r.get('context_ids') or []) if cid not in chunks_by_c[c_name]]
        if missing_docs:
            if tok is None and c_name != 'c4':
                from transformers import AutoTokenizer
                from ragvi.retrieval import DEFAULT_MODEL
                tok = AutoTokenizer.from_pretrained(DEFAULT_MODEL)
            chunks_by_c[c_name].update(subset_chunks(corpus_text_of, c_name, missing_docs, tok=tok))
    gold_of = lambda q: format_gold_evidence(q, corpus_text_of)
    trunc_cache = {}

    def _trunc_passage(p):
        nonlocal tok
        if len(p) <= 2000:
            return p
        hit = trunc_cache.get(p)
        if hit is None:
            if tok is None:
                from transformers import AutoTokenizer
                from ragvi.retrieval import DEFAULT_MODEL
                tok = AutoTokenizer.from_pretrained(DEFAULT_MODEL)
            hit, _ = truncate_tokens(p, tok, CTX_LIMIT)
            trunc_cache[p] = hit
        return hit

    def context_of(cfg, qid):
        cids = ctx_ids_of.get((cfg, qid)) or []
        u_map = chunks_by_c.get(chunking_of_config(cfg), unit_text_of)
        passages = [_trunc_passage(u_map[c]) for c in cids if c in u_map]
        if passages:
            return '\n'.join(f'[{i}] {p}' for i, p in enumerate(passages, 1))
        return gold_of(questions[qid])

    if args.human_sheet:
        if Path(out_path).exists():
            raise SystemExit(f'{out_path} đã tồn tại; không ghi đè phiếu gán nhãn.')
        md = build_human_sheet(answers, questions, context_of, gold_of, n=args.n, seed=args.seed)
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        Path(out_path).write_text(md, encoding='utf-8')
        print(f'Đã ghi phiếu gán nhãn vào {out_path}')
        return

    done = {(r['config'], r['qid']) for r in read_rows(out_path) if not r.get('error')}
    need = any(r.get('answerable', True) and (r['config'], r['qid']) not in done for r in answers)
    if need and args.llama_url:
        from ragvi.generate import load_llamacpp

        judge_fn = load_llamacpp(args.llama_url, args.model, max_new_tokens=1024)
    else:
        judge_fn = load_generator(args.model) if need else (lambda p: '{}')
    workers = args.workers or (8 if args.llama_url else 1)
    written = run_judge(answers, questions, context_of, gold_of, out_path, judge_fn,
                        model_name=args.model, workers=workers)
    rows = [r for r in read_rows(out_path) if r.get('error') is None]
    errors = sum(r.get('error') is not None for r in read_rows(out_path))
    print(f'Đã chấm thêm {written} câu trả lời vào {out_path} (hợp lệ: {len(rows)}, lỗi JSON: {errors})')


if __name__ == '__main__':
    main()
