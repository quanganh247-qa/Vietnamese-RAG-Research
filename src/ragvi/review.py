"""Dựng phiếu đọc tay câu "không trả lời được" (quyết định D6) và đếm phiếu đã chấm.

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.review <retrieval.jsonl> <test.jsonl> <kho> <out.md> [--method hybrid] [--n 30] [--seed 0]
    PYTHONPATH=src python -m ragvi.review --tally <out.md đã chấm>
<kho> là thư mục <processed>/zalo_legal hoặc file corpus.jsonl của ViQuAD.
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

THRESHOLD = 0.20
MAX_CHARS = 1200
BOX_NO, BOX_YES = 'không trả lời được', 'VẪN trả lời được'

HEADER = f"""# Phiếu đọc tay câu "không trả lời được" (D6)

Với mỗi câu, đọc câu hỏi và 5 đoạn đầu của truy xuất rồi tự hỏi: "Chỉ dựa vào 5 đoạn dưới đây, có trả lời đúng và đầy đủ được câu hỏi không?"
Nếu không, đánh `[x]` vào ô "{BOX_NO}"; nếu có, đánh `[x]` vào ô "{BOX_YES}" và ghi số thứ hạng của đoạn chứa đáp án.
Chỉ đánh đúng một ô mỗi câu; câu phân vân thì ghi lý do vào Ghi chú.
Đoạn có nhãn **[ĐOẠN GỐC]** là đoạn vàng của câu hỏi (ViQuAD: đoạn đối kháng mà câu hỏi được viết dựa vào; Zalo: điều luật lẽ ra đã bị loại khỏi kho).
Nếu tỷ lệ "{BOX_YES}" trên {THRESHOLD:.0%}, phải thay các câu đó trước khi đóng băng tập test.
Đếm kết quả: `PYTHONPATH=src python -m ragvi.review --tally <file này>`.
"""


def pick(test_rows, results, n=30, seed=0):
    """Chọn ngẫu nhiên theo seed n câu answerable=False có trong results ({qid: top}).

    Trả về danh sách câu hỏi theo thứ tự đọc.
    """
    pool = sorted((q for q in test_rows if not q['answerable']), key=lambda q: q['qid'])
    if not pool:
        raise ValueError('Tập test không có câu "không trả lời được" nào.')
    with_result = [q for q in pool if q['qid'] in results]
    if len(with_result) < n:
        raise ValueError(f'Chỉ {len(with_result)}/{len(pool)} câu không trả lời được có kết quả truy xuất, '
                         f'cần {n}. Kiểm tra --method hoặc chạy lại truy xuất cho đủ.')
    return random.Random(seed).sample(with_result, n)


def render(picked, results, corpus, k=5, max_chars=MAX_CHARS):
    """Trả về nội dung Markdown của phiếu. corpus: {doc_id: (title, text)}."""
    out = [HEADER]
    for i, q in enumerate(picked, 1):
        gold = set(q.get('gold_doc_ids') or [q.get('gold_doc_id')])
        out.append(f'\n---\n\n## Câu {i} — `{q["qid"]}`\n\n**Câu hỏi:** {q["question"]}\n')
        for rank, doc_id in enumerate(results[q['qid']][:k], 1):
            title, text = corpus.get(doc_id, ('(không có trong kho)', ''))
            if len(text) > max_chars:
                text = text[:max_chars].rstrip() + ' … (đã cắt)'
            mark = ' **[ĐOẠN GỐC]**' if doc_id in gold else ''
            body = '\n'.join('> ' + line for line in text.splitlines()) or '>'
            out.append(f'\n**Đoạn {rank}** — `{doc_id}`{mark} — {title}\n\n{body}\n')
        out.append(f'\nKết luận: [ ] {BOX_NO}   [ ] {BOX_YES} (đoạn số: __)   Ghi chú:\n')
    out.append('\n---\n\n## Tổng kết\n\n| Số câu đã đọc | Số câu vẫn trả lời được | Tỷ lệ |\n|---|---|---|\n|  |  |  |\n')
    return ''.join(out)


def tally(markdown):
    """Đếm phiếu đã chấm. Trả về dict: total, yes, no, unmarked [qid], both [qid], rate, over."""
    res = {'total': 0, 'yes': [], 'no': [], 'unmarked': [], 'both': []}
    for block in re.split(r'^## Câu \d+ — ', markdown, flags=re.M)[1:]:
        qid = block.split('`')[1]
        line = next((l for l in block.splitlines() if l.startswith('Kết luận:')), '')
        no = re.search(r'\[[xX]\]\s*' + BOX_NO, line) is not None
        yes = re.search(r'\[[xX]\]\s*' + BOX_YES, line) is not None
        res['total'] += 1
        res['both' if no and yes else 'yes' if yes else 'no' if no else 'unmarked'].append(qid)
    graded = len(res['yes']) + len(res['no'])
    res['rate'] = len(res['yes']) / graded if graded else None
    res['over'] = res['rate'] is not None and res['rate'] > THRESHOLD
    return res


def read_jsonl(path):
    """Đọc JSONL, bỏ qua dòng không parse được (dòng cuối có thể bị cắt dở)."""
    rows = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return rows


def load_corpus(path):
    """Trả về {doc_id: (title, text)} từ corpus.jsonl ViQuAD hoặc thư mục Zalo đã xử lý."""
    if str(path).endswith('.jsonl'):
        return {r['doc_id']: (r['title'], r['text']) for r in read_jsonl(path)}
    from ragvi.data import load_zalo_corpus
    return {d: tuple(v.split('\n', 1)) if '\n' in v else (v, '') for d, v in load_zalo_corpus(path).items()}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('paths', nargs='*', help='<retrieval.jsonl> <test.jsonl> <kho> <out.md>')
    p.add_argument('--method', default='hybrid')
    p.add_argument('--n', type=int, default=30)
    p.add_argument('--seed', type=int, default=0)
    p.add_argument('--tally', metavar='PHIEU_DA_CHAM')
    a = p.parse_args(argv)

    if a.tally:
        r = tally(Path(a.tally).read_text(encoding='utf-8'))
        graded = len(r['yes']) + len(r['no'])
        print(f'Số câu trong phiếu: {r["total"]}; đã chấm: {graded}; vẫn trả lời được: {len(r["yes"])}')
        if r['unmarked']:
            print('Chưa chấm:', ', '.join(r['unmarked']))
        if r['both']:
            print('Chấm cả hai ô (cần sửa):', ', '.join(r['both']))
        if r['rate'] is None:
            print('Chưa có câu nào chấm hợp lệ.')
        else:
            verdict = 'VƯỢT ngưỡng, phải thay câu' if r['over'] else 'không vượt ngưỡng'
            print(f'Tỷ lệ vẫn trả lời được: {len(r["yes"])}/{graded} = {r["rate"]:.1%} ({verdict} {THRESHOLD:.0%})')
            if r['unmarked'] or r['both']:
                print('Lưu ý: tỷ lệ chỉ tính trên các câu đã chấm hợp lệ; hoàn tất phiếu trước khi ghi vào D6.')
        return
    if len(a.paths) != 4:
        p.error('cần đủ 4 đường dẫn: <retrieval.jsonl> <test.jsonl> <kho> <out.md>, hoặc dùng --tally')
    retrieval, test, corpus_path, out = a.paths
    if Path(out).exists():
        sys.exit(f'{out} đã tồn tại; không ghi đè phiếu có thể đã chấm. Chọn tên khác.')
    results = {r['qid']: r['top'] for r in read_jsonl(retrieval) if r.get('method') == a.method and 'top' in r}
    if not results:
        sys.exit(f'Không có dòng kết quả nào với method={a.method!r} trong {retrieval}.')
    try:
        picked = pick(read_jsonl(test), results, a.n, a.seed)
    except ValueError as e:
        sys.exit(str(e))
    Path(out).write_text(render(picked, results, load_corpus(corpus_path)), encoding='utf-8')
    print(f'Đã ghi {out}: {len(picked)} câu, method={a.method}, seed={a.seed}')


if __name__ == '__main__':
    main()
