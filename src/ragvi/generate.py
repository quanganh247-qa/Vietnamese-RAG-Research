"""Sinh câu trả lời đầu-cuối cho cấu hình RAG, closed-book và oracle (Tuần 2: Ngày 8–9).

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.generate <questions.jsonl> <units_path> <out.jsonl> --config oracle --model Qwen/Qwen3-8B
    PYTHONPATH=src python -m ragvi.generate <questions.jsonl> <units_path> <out.jsonl> --config closed_book --model Qwen/Qwen3-8B
    PYTHONPATH=src python -m ragvi.generate <questions.jsonl> <units_path> <out.jsonl> --config C3-E3-R0 \\
        --retrieval <retrieval.jsonl> --method dense[c3] --model Qwen/Qwen3-8B
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import re
import time
from pathlib import Path

from ragvi.chunking import _offsets, chunk_document, chunk_fixed, chunk_sentence, chunk_struct
from ragvi.metrics import em_f1, normalize_answer
from ragvi.rerank import load_units
from ragvi.retrieval import DEFAULT_MODEL, load_jsonl, open_append, read_rows

REFUSAL_PHRASE = 'Không tìm thấy thông tin'
CTX_LIMIT = 1024     # mỗi đoạn đưa vào prompt cắt ở 1.024 token tham chiếu (D7)
ORACLE_LIMIT = 4000  # điều luật vàng ở điều kiện oracle cắt ở 4.000 token tham chiếu (D5)
TOP_N = 5


def chunking_of_config(config):
    """Trích cách phân đoạn ('c1', 'c3', 'c4', 'c5', 'c5_nohead') từ nhãn cấu hình (ví dụ 'C5_nohead-E3-R0')."""
    head = (config or '').split('-', 1)[0].strip().lower()
    return head if head in ('c1', 'c3', 'c4', 'c5', 'c5_nohead') else None


def subset_chunks(corpus_docs, chunking, doc_ids, tok=None, tokenizer_name=DEFAULT_MODEL):
    """Phân đoạn theo nhu cầu chỉ cho tập `doc_ids` cần dùng; trả về `{chunk_id: chunk_text}`."""
    need = [d for d in dict.fromkeys(doc_ids) if d in corpus_docs]
    if not need:
        return {}
    if tok is None and chunking != 'c4':
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(tokenizer_name)
    out = {}
    for d in need:
        text = corpus_docs[d]
        if chunking == 'c1':
            rows = chunk_fixed(d, text, tok)
        elif chunking == 'c3':
            rows = chunk_sentence(d, text, tok)
        elif chunking == 'c4':
            rows = chunk_document(d, text)
        elif chunking in ('c5', 'c5_nohead'):
            title = text.split('\n', 1)[0]
            body = text[len(title) + 1:] if text.startswith(title + '\n') else ''
            rows = chunk_struct(d, title, body, tok, heading=(chunking == 'c5'))
        else:
            raise ValueError(f'Cách phân đoạn không hợp lệ: {chunking}')
        for cid, _, _, _, ctext in rows:
            out[cid] = ctext
    return out

PROMPT_CTX = (
    'Chỉ dùng thông tin trong phần Ngữ cảnh để trả lời câu hỏi. Nếu ngữ cảnh không đủ thông tin, '
    'hãy trả lời đúng một câu: "Không tìm thấy thông tin". Trả lời ngắn gọn bằng tiếng Việt.\n\n'
    'Ngữ cảnh:\n{context}\n\n'
    'Câu hỏi: {question}'
)

PROMPT_CB = (
    'Hãy trả lời câu hỏi dưới đây. Nếu không biết chắc chắn câu trả lời, '
    'hãy trả lời đúng một câu: "Không tìm thấy thông tin". Trả lời ngắn gọn bằng tiếng Việt.\n\n'
    'Câu hỏi: {question}'
)

REFUSAL_PATTERNS = (
    'không tìm thấy thông tin',
    'không có thông tin',
    'không đủ thông tin',
    'ngữ cảnh không cung cấp',
    'ngữ cảnh không đề cập',
    'không được đề cập trong ngữ cảnh',
)


def truncate_tokens(text, tok, limit):
    """Cắt `text` ở `limit` token tham chiếu; trả về `(văn_bản_đã_cắt, có_bị_cắt_không)`."""
    if tok is None or limit is None or not text:
        return text, False
    off, _ = _offsets(text, tok)
    if len(off) <= limit:
        return text, False
    return text[:off[limit - 1][1]], True


def build_prompt(question, passages=None, tok=None, limit=CTX_LIMIT):
    """Dựng prompt cố định (closed-book khi `passages is None`) và đếm số đoạn bị cắt token."""
    if passages is None:
        return PROMPT_CB.format(question=question), 0
    blocks, n_trunc = [], 0
    for i, p in enumerate(passages, 1):
        cut, was_trunc = truncate_tokens(p, tok, limit)
        n_trunc += int(was_trunc)
        blocks.append(f'[{i}] {cut}')
    return PROMPT_CTX.format(context='\n'.join(blocks), question=question), n_trunc


def clean_generation(text):
    """Bỏ khối `<think>...</think>` (nếu có) và khoảng trắng thừa ở hai đầu."""
    text = re.sub(r'<think>.*?</think>', '', text or '', flags=re.S)
    return text.strip()


def is_refusal(answer):
    """Nhận diện câu từ chối trả lời: chuẩn hóa chữ thường/dấu câu và khớp cụm từ từ chối."""
    norm = normalize_answer(clean_generation(answer))
    if not norm:
        return True
    return any(pat in norm for pat in REFUSAL_PATTERNS)


def contains_gold_answer(answer, answers):
    """Kiểm tra câu trả lời có chứa nguyên chuỗi chuẩn hóa của ít nhất một đáp án vàng hay không (Ngày 8)."""
    if not answers:
        return None
    norm = f' {normalize_answer(answer)} '
    return any(f' {normalize_answer(a["text"] if isinstance(a, dict) else a)} ' in norm
               for a in answers if normalize_answer(a['text'] if isinstance(a, dict) else a))


def load_generator(model_name, max_new_tokens=256, load_in_4bit=True, max_input_tokens=None):
    """Nạp mô hình sinh cục bộ (4-bit NF4, temperature=0 / do_sample=False) và trả về hàm `generate(prompt)`."""
    import os
    os.environ.setdefault('PYTORCH_CUDA_ALLOC_CONF', 'expandable_segments:True')
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    tok = AutoTokenizer.from_pretrained(model_name)
    kwargs = {'device_map': 'auto'}
    if torch.cuda.is_available():
        vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
        compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        kwargs['torch_dtype'] = compute_dtype
        if max_input_tokens is None:
            max_input_tokens = 4096 if vram_gb >= 20 else 2048
        if load_in_4bit:
            kwargs['quantization_config'] = BitsAndBytesConfig(
                load_in_4bit=True, bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=compute_dtype, bnb_4bit_quant_type='nf4')
    else:
        max_input_tokens = max_input_tokens or 2048
    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    model.eval()

    def generate(prompt):
        messages = [{'role': 'user', 'content': prompt}]
        if hasattr(tok, 'apply_chat_template') and getattr(tok, 'chat_template', None):
            try:
                rendered = tok.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
            except TypeError:
                rendered = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            rendered = prompt
        inputs = tok(rendered, return_tensors='pt', truncation=True, max_length=max_input_tokens).to(model.device)
        with torch.no_grad():
            out = model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False,
                pad_token_id=tok.eos_token_id)
        new_tokens = out[0][inputs['input_ids'].shape[1]:].cpu()
        del inputs, out
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        return clean_generation(tok.decode(new_tokens, skip_special_tokens=True))

    return generate


def load_llamacpp(base_url, model_name, max_new_tokens=256):
    """Dùng llama-server qua API chat; không đổi prompt hoặc cách chấm."""
    from urllib.request import Request, urlopen

    url = base_url.rstrip('/') + '/v1/chat/completions'

    def generate(prompt):
        payload = {'model': model_name, 'messages': [{'role': 'user', 'content': prompt}],
                   'temperature': 0, 'seed': 0, 'max_tokens': max_new_tokens}
        request = Request(url, data=json.dumps(payload).encode('utf-8'),
                          headers={'Content-Type': 'application/json'})
        with urlopen(request, timeout=300) as response:
            answer = json.load(response)['choices'][0]['message']['content']
        if not isinstance(answer, str):
            raise ValueError('llama-server không trả về câu trả lời dạng văn bản.')
        return clean_generation(answer)

    return generate


def select_questions(questions, limit=None):
    """Chọn `limit` câu hỏi; riêng `limit=50` trên tập có cả hai loại (như dev ViQuAD) lấy đúng 35 trả lời được + 15 không (Ngày 8)."""
    if not limit or limit >= len(questions):
        return list(questions)
    ans = [q for q in questions if q.get('answerable')]
    unans = [q for q in questions if not q.get('answerable')]
    if limit == 50 and len(ans) >= 35 and len(unans) >= 15:
        return ans[:35] + unans[:15]
    return list(questions[:limit])


def run_generate(config, questions, contexts_of, out_path, generate_fn, tok=None, limit=CTX_LIMIT,
                 model_name='', workers=1):
    """Chạy sinh câu trả lời cho danh sách `questions`, ghi từng dòng ngay vào `out_path` và bỏ qua cặp đã có.

    `contexts_of(q)` có thể trả về `None` (closed-book), `[text, ...]`, hoặc `([cid, ...], [text, ...])`.
    Khi `workers > 1` (ví dụ gọi `llama-server` có continuous batching), gửi song song `workers` yêu cầu.
    Tự động tái sử dụng câu trả lời khi `(chunking, qid, context_ids)` hoặc `prompt` trùng khít với cấu hình đã chạy.
    """
    existing = read_rows(out_path)
    done = {(r['config'], r['qid']) for r in existing}
    pending = [q for q in questions if (config, q['qid']) not in done]
    if not pending:
        return 0

    cfg_chunking = chunking_of_config(config)
    ctx_cache = {
        (chunking_of_config(r.get('config')), r['qid'], tuple(r.get('context_ids') or ())): r['answer']
        for r in existing if r.get('context_ids') and chunking_of_config(r.get('config')) and 'answer' in r
    }
    prompt_cache = {}
    trunc_cache = {}

    def _build_cached_prompt(question, passages):
        if passages is None:
            return PROMPT_CB.format(question=question), 0
        blocks, n_trunc = [], 0
        for i, p in enumerate(passages, 1):
            hit = trunc_cache.get(p)
            if hit is None:
                hit = truncate_tokens(p, tok, limit)
                trunc_cache[p] = hit
            cut, was_trunc = hit
            n_trunc += int(was_trunc)
            blocks.append(f'[{i}] {cut}')
        return PROMPT_CTX.format(context='\n'.join(blocks), question=question), n_trunc

    def _one(q):
        qid = q['qid']
        ctx = contexts_of(q)
        if isinstance(ctx, tuple):
            cids, passages = ctx
        else:
            cids, passages = [], ctx
        prompt, n_trunc = _build_cached_prompt(q['question'], passages)
        ctx_key = (cfg_chunking, qid, tuple(cids)) if (cfg_chunking and cids) else None
        cached_ans = (ctx_cache.get(ctx_key) if ctx_key else None) or prompt_cache.get(prompt)
        if cached_ans is not None:
            answer, seconds = clean_generation(cached_ans), 0.0
        else:
            t0 = time.perf_counter()
            answer = clean_generation(generate_fn(prompt))
            seconds = time.perf_counter() - t0
            prompt_cache[prompt] = answer
            if ctx_key:
                ctx_cache[ctx_key] = answer
        refused = is_refusal(answer)
        answers = q.get('answers') or []
        scores = em_f1(answer, answers) if answers else {'em': None, 'f1': None}
        return {
            'config': config, 'model': model_name, 'qid': qid, 'answerable': q['answerable'],
            'answer': answer, 'refused': refused,
            'contains_gold': contains_gold_answer(answer, answers),
            **scores,
            'context_ids': cids,
            'n_passages': 0 if passages is None else len(passages),
            'truncated_passages': n_trunc,
            'seconds': round(seconds, 3),
        }

    written = 0
    with open_append(out_path) as f:
        if workers and workers > 1:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                for row in ex.map(_one, pending):
                    f.write(json.dumps(row, ensure_ascii=False) + '\n')
                    f.flush()
                    written += 1
        else:
            for q in pending:
                row = _one(q)
                f.write(json.dumps(row, ensure_ascii=False) + '\n')
                f.flush()
                written += 1
    return written


def summarize_generation(rows, config=None, total_runs=6400):
    """Tổng hợp tỷ lệ từ chối đúng, fabrication rate, false refusal, EM/F1 và ước lượng giờ GPU cho 6.400 lượt."""
    own = [r for r in rows if config is None or r.get('config') == config]
    if not own:
        return {}
    ans = [r for r in own if r.get('answerable')]
    unans = [r for r in own if not r.get('answerable')]
    with_em = [r for r in ans if r.get('em') is not None]
    with_cg = [r for r in ans if r.get('contains_gold') is not None]
    total_sec = sum(r.get('seconds') or 0.0 for r in own)
    mean_sec = total_sec / len(own) if own else 0.0
    return {
        'n': len(own), 'n_ans': len(ans), 'n_unans': len(unans),
        'correct_refusal': sum(bool(r['refused']) for r in unans) / len(unans) if unans else None,
        'fabrication': sum(not r['refused'] for r in unans) / len(unans) if unans else None,
        'false_refusal': sum(bool(r['refused']) for r in ans) / len(ans) if ans else None,
        'contains_gold': sum(bool(r['contains_gold']) for r in with_cg) / len(with_cg) if with_cg else None,
        'em': sum(r['em'] for r in with_em) / len(with_em) if with_em else None,
        'f1': sum(r['f1'] for r in with_em) / len(with_em) if with_em else None,
        'truncated_passages': sum(r.get('truncated_passages', 0) for r in own),
        'q_per_min': 60.0 / mean_sec if mean_sec > 0 else None,
        'est_gpu_hours_6400': (mean_sec * total_runs) / 3600.0 if mean_sec > 0 else None,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('questions_path', help='dev.jsonl hoặc test.jsonl')
    parser.add_argument('units_path', help='thư mục zalo_legal, corpus.jsonl ViQuAD, hoặc chunks/*.jsonl')
    parser.add_argument('out_path', help='file JSONL lưu câu trả lời')
    parser.add_argument('--config', required=True,
                        help='closed_book, oracle, hoặc nhãn cấu hình (có thể phân tách bằng dấu phẩy)')
    parser.add_argument('--retrieval', help='file retrieval_*.jsonl (bắt buộc khi config khác closed_book/oracle)')
    parser.add_argument('--method',
                        help='nhãn phương pháp trong file retrieval (có thể phân tách bằng dấu phẩy khớp --config)')
    parser.add_argument('--model', default='Qwen/Qwen3.5-9B')
    parser.add_argument('--llama-url', help='URL gốc của llama-server (mặc định dùng Transformers)')
    parser.add_argument('--workers', type=int, default=0,
                        help='số luồng gửi batch song song tới llama-server (0 = tự chọn 8 khi có --llama-url)')
    parser.add_argument('--ref-tokenizer', default=DEFAULT_MODEL)
    parser.add_argument('--limit', type=int, help='chỉ chạy trên N câu đầu (ví dụ 50 câu dev ở Ngày 8–9)')
    parser.add_argument('--top-n', type=int, default=TOP_N)
    args = parser.parse_args(argv)

    configs = [c.strip() for c in args.config.split(',') if c.strip()]
    methods = [m.strip() for m in (args.method or '').split(',') if m.strip()]
    if any(c not in ('closed_book', 'oracle') for c in configs):
        if not args.retrieval or len(methods) != len(configs):
            raise SystemExit('Cấu hình RAG cần --retrieval và số lượng --method khớp với --config.')
    else:
        methods = [''] * len(configs)

    questions = select_questions(load_jsonl(args.questions_path), args.limit)
    done = {(r['config'], r['qid']) for r in read_rows(args.out_path)}
    need = any((cfg, q['qid']) not in done for cfg in configs for q in questions)
    if need:
        from transformers import AutoTokenizer
        ref_tok = None if configs == ['closed_book'] else AutoTokenizer.from_pretrained(args.ref_tokenizer)
        gen_fn = load_llamacpp(args.llama_url, args.model) if args.llama_url else load_generator(args.model)
    else:
        ref_tok, gen_fn = None, (lambda p: '')

    base_units, _, _ = load_units(args.units_path)
    ret_rows = read_rows(args.retrieval) if args.retrieval else []
    chunk_cache = {}
    workers = args.workers or (8 if args.llama_url else 1)

    for cfg, method in zip(configs, methods):
        if cfg == 'closed_book':
            contexts_of = lambda q: None
            tok_limit = CTX_LIMIT
        elif cfg == 'oracle':
            # Oracle chỉ tính trên câu trả lời được (D5), trừ khi thử dev ViQuAD có đoạn gốc (Ngày 8).
            def contexts_of(q):
                ids = [d for d in (q.get('gold_doc_ids') or ([q['gold_doc_id']] if 'gold_doc_id' in q else []))
                       if d in base_units]
                return ids, [base_units[d] for d in ids]
            tok_limit = ORACLE_LIMIT
        else:
            top_map = {r['qid']: r['top'] for r in ret_rows if r.get('method') == method and 'top' in r}
            missing = [q['qid'] for q in questions if q['qid'] not in top_map]
            if missing:
                raise SystemExit(f'Thiếu {len(missing)} câu hỏi cho method={method!r} trong {args.retrieval}.')
            needed_cids = [cid for q in questions for cid in top_map[q['qid']][:args.top_n]]
            c_name = chunking_of_config(cfg)
            if all(cid in base_units for cid in needed_cids):
                unit_map = base_units
            else:
                if c_name not in chunk_cache:
                    chunk_cache[c_name] = dict(base_units)
                missing_docs = [cid.rsplit('#', 1)[0] for cid in needed_cids if cid not in chunk_cache[c_name]]
                if missing_docs:
                    chunk_cache[c_name].update(
                        subset_chunks(base_units, c_name, missing_docs, tok=ref_tok, tokenizer_name=args.ref_tokenizer))
                unit_map = chunk_cache[c_name]

            def contexts_of(q, _top=top_map, _units=unit_map):
                ids = _top[q['qid']][:args.top_n]
                return ids, [_units[cid] for cid in ids]
            tok_limit = CTX_LIMIT

        written = run_generate(cfg, questions, contexts_of, args.out_path, gen_fn,
                               tok=ref_tok, limit=tok_limit, model_name=args.model, workers=workers)
        summary = summarize_generation(read_rows(args.out_path), config=cfg)
        print(f'Ghi thêm {written} câu trả lời ({cfg}, model={args.model}) vào {args.out_path}')
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
