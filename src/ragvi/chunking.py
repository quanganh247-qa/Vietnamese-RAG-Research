"""Phân đoạn: C1 (cố định), C3 (theo câu), C4 (nguyên tài liệu), C5 ViStructChunk (Điều → Khoản → Điểm).

Mọi hàm trả về danh sách (chunk_id, doc_id, start, end, text); start/end là vị trí ký tự trong
tài liệu gốc và text là lát cắt nguyên văn text[start:end] (riêng C5 có thể gắn thêm tiêu đề cha
ở phía trước). Token được đếm bằng một tokenizer tham chiếu truyền từ ngoài vào (D7: BAAI/bge-m3).

Chạy (Zalo):   PYTHONPATH=src python -m ragvi.chunking <processed>/zalo_legal --methods c1,c3,c4,c5,c5_nohead
Chạy (ViQuAD): PYTHONPATH=src python -m ragvi.chunking <eval>/viquad/corpus.jsonl   (chỉ c1, c3, c4)
Phiếu đối chiếu tay C5: PYTHONPATH=src python -m ragvi.chunking <processed>/zalo_legal --review c5_review.md
"""
import argparse
import json
import math
import random
import re
import statistics
from bisect import bisect_left
from pathlib import Path

SIZE = 256
EMBED_LIMIT = 512  # mô hình nhúng cắt ở 512 token (D7)
METHODS = ('c1', 'c3', 'c4', 'c5', 'c5_nohead')
CLAUSE = re.compile(r'^(\d+)\.\s', re.M)      # Khoản: "1. ..."
POINT = re.compile(r'^([a-zđ])\)\s', re.M)    # Điểm: "a) ..."


def _offsets(text, tok):
    """Trả về (offset_mapping, danh sách vị trí bắt đầu của từng token)."""
    off = tok(text, add_special_tokens=False, return_offsets_mapping=True)['offset_mapping']
    return off, [o[0] for o in off]


def _ntok(starts, s, e):
    """Số token bắt đầu trong khoảng ký tự [s, e)."""
    return bisect_left(starts, e) - bisect_left(starts, s)


def _fixed_spans(off, starts, s, e, size):
    """Cắt khoảng [s, e) thành các đoạn `size` token, không chồng lấn.

    XLM-R (bge-m3) có token "▁" đứng riêng mang offset trùng ký tự đầu của token sau (ví dụ "ỦY", "QĐ", "≥"),
    nên đầu cuối của mỗi đoạn bị chặn tại điểm bắt đầu của đoạn kế tiếp.
    """
    i0, i1 = bisect_left(starts, s), bisect_left(starts, e)
    return [(max(off[i][0], s), min(off[min(i + size, i1) - 1][1], off[i + size][0] if i + size < i1 else e, e))
            for i in range(i0, i1, size)]


def _sentence_spans(text, s, e, sent_split):
    """Vị trí (start, end) của từng câu trong text[s:e]; phần chữ hàm tách câu bỏ sót được giữ lại."""
    spans, pos = [], s
    for sent in sent_split(text[s:e]):
        sent = sent.strip()
        if not sent:
            continue
        a = text.find(sent, pos, e)
        b = a + len(sent)
        if a < 0:  # hàm tách câu đã đổi khoảng trắng: so khớp bỏ qua khoảng trắng
            m = re.compile(r'\s*'.join(map(re.escape, sent.split()))).search(text, pos, e)
            if not m:
                raise ValueError(f'Không tìm thấy câu trong văn bản gốc: {sent[:80]!r}')
            a, b = m.span()
        a -= len(text[pos:a].lstrip())  # chữ nằm giữa hai câu thuộc về câu sau
        spans.append((a, b))
        pos = b
    tail = text[pos:e]
    if tail.strip():
        spans.append((e - len(tail.lstrip()), pos + len(tail.rstrip())))
    return spans


def _sentence_merge_spans(text, off, starts, s, e, size, sent_split):
    """C3 trên khoảng [s, e): gộp câu tới `size` token; câu dài hơn `size` thì cắt bằng C1."""
    out, cur = [], None
    for a, b in _sentence_spans(text, s, e, sent_split):
        if cur and _ntok(starts, cur[0], b) <= size:
            cur = (cur[0], b)
            continue
        if cur:
            out.append(cur)
            cur = None
        if _ntok(starts, a, b) > size:
            out += _fixed_spans(off, starts, a, b, size)
        else:
            cur = (a, b)
    return out + [cur] if cur else out


def _default_sent_split():
    from underthesea import sent_tokenize
    return sent_tokenize


def _records(doc_id, text, spans):
    return [(f'{doc_id}#{i}', doc_id, s, e, text[s:e]) for i, (s, e) in enumerate(spans)]


def chunk_fixed(doc_id, text, tok, size=SIZE):
    """C1: mỗi chunk `size` token, không chồng lấn, cắt theo vị trí ký tự do tokenizer trả về."""
    off, starts = _offsets(text, tok)
    return _records(doc_id, text, _fixed_spans(off, starts, 0, len(text), size))


def chunk_sentence(doc_id, text, tok, size=SIZE, sent_split=None):
    """C3: tách câu (mặc định `underthesea.sent_tokenize`), gộp câu tới `size` token."""
    off, starts = _offsets(text, tok)
    spans = _sentence_merge_spans(text, off, starts, 0, len(text), size, sent_split or _default_sent_split())
    return _records(doc_id, text, spans)


def chunk_document(doc_id, text):
    """C4: nguyên tài liệu (đoạn ViQuAD / nguyên điều luật Zalo) là một chunk."""
    return [(f'{doc_id}#0', doc_id, 0, len(text), text)]


def has_clause(body):
    """Điều luật có ít nhất một khoản được nhận diện hay không."""
    return bool(CLAUSE.search(body))


def struct_heading(doc_id, title):
    """Hai phần tiêu đề cha của C5: ("Văn bản X", "Văn bản X, <tiêu đề Điều>")."""
    doc = 'Văn bản ' + doc_id.rsplit('+', 1)[0].upper()
    return doc, ', '.join(filter(None, [doc, title.strip()]))


def chunk_struct(doc_id, title, body, tok, size=SIZE, heading=True, sent_split=None):
    """C5 ViStructChunk cho một điều luật; `heading=False` là biến thể không tiêu đề (cùng ranh giới).

    Tài liệu gốc là `title + "\\n" + body` (giống `ragvi.data.load_zalo_corpus`), start/end tính trên
    chuỗi đó. Đơn vị chunk là Khoản; Khoản dài hơn `size` token thì tách theo Điểm; phần mở đầu trước
    khoản 1 (kèm dòng tiêu đề Điều) là một chunk riêng; điều luật không có khoản là một chunk, trùng C4.
    Mảnh nào vẫn dài hơn `size` token thì cắt bằng C3.
    Tiêu đề cha: "Văn bản 01/2009/TT-BNN, Điều 1. ..., Khoản 2[, Điểm a]: " + nội dung. Chunk bắt đầu
    từ đầu tài liệu đã chứa dòng tiêu đề Điều nên chỉ gắn "Văn bản ..., ".
    """
    text = title + '\n' + body
    off, starts = _offsets(text, tok)
    doc, full = struct_heading(doc_id, title)

    def cut(s, e, head):
        e = s + len(text[s:e].rstrip())
        if s >= e:
            return []
        if _ntok(starts, s, e) <= size:
            spans = [(s, e)]
        else:
            spans = _sentence_merge_spans(text, off, starts, s, e, size, sent_split or _default_sent_split())
        return [(a, b, f'{doc}, ' if a == 0 else f'{head}: ') for a, b in spans]

    # ponytail: nhận diện khoản chỉ bằng regex đầu dòng, không kiểm tra số khoản tăng dần;
    # nếu đối chiếu tay 30 điều (Ngày 7) thấy nhận nhầm danh sách đánh số thì thêm kiểm tra đó.
    clauses = list(CLAUSE.finditer(text, len(title) + 1))
    if not clauses:
        pieces = [(0, len(text), f'{doc}, ')] if len(off) <= size else cut(0, len(text), full)
    else:
        # Luôn giữ phần trước khoản 1, kể cả khi chỉ còn dòng tiêu đề Điều; bỏ đi thì c5_nohead mất tiêu đề.
        pieces = cut(0, clauses[0].start(), full)
        for m, nxt in zip(clauses, clauses[1:] + [None]):
            s, e = m.start(), nxt.start() if nxt else len(text)
            head = f'{full}, Khoản {m[1]}'
            points = list(POINT.finditer(text, s, e)) if _ntok(starts, s, e) > size else []
            if not points:
                pieces += cut(s, e, head)
                continue
            pieces += cut(s, points[0].start(), head)
            for p, q in zip(points, points[1:] + [None]):
                pieces += cut(p.start(), q.start() if q else e, f'{head}, Điểm {p[1]}')
    return [(f'{doc_id}#{i}', doc_id, s, e, (prefix if heading else '') + text[s:e])
            for i, (s, e, prefix) in enumerate(pieces)]


def chunk_stats(chunks, tok):
    """Số chunk và phân phối độ dài theo token (tính trên `text` của chunk, kể cả tiêu đề cha)."""
    # ponytail: token hóa lại từng chunk; nếu chậm trên toàn kho thì token hóa theo lô.
    # `chunks` có thể là generator: chỉ giữ danh sách độ dài, không giữ chunk trong bộ nhớ.
    lengths = sorted(len(_offsets(c[4], tok)[0]) for c in chunks)
    if not lengths:
        return {'n_chunks': 0, 'tok_mean': 0, 'tok_median': 0, 'tok_p95': 0, 'tok_max': 0, 'over_512': 0.0}
    return {'n_chunks': len(lengths), 'tok_mean': statistics.fmean(lengths),
            'tok_median': statistics.median(lengths),
            'tok_p95': lengths[math.ceil(0.95 * len(lengths)) - 1], 'tok_max': lengths[-1],
            'over_512': sum(n > EMBED_LIMIT for n in lengths) / len(lengths)}


def clause_rate(bodies):
    """Tỷ lệ điều luật có ít nhất một khoản được nhận diện."""
    bodies = list(bodies)
    return sum(map(has_clause, bodies)) / len(bodies) if bodies else 0.0


REVIEW_GUIDE = """# Phiếu đối chiếu tay C5 (ViStructChunk)

Hướng dẫn: với mỗi điều luật, đọc nguyên văn rồi so với danh sách chunk C5 bên dưới.
Đánh "đúng" nếu mỗi khoản (và điểm, khi khoản dài) thành đúng một chunk với tiêu đề cha đúng số khoản/điểm.
Đánh "khoản nhận nhầm" nếu một dòng không phải khoản (ví dụ danh sách đánh số trong một khoản) bị tách thành khoản; "bỏ sót khoản/điểm" nếu một khoản hay điểm có trong nguyên văn mà không thành chunk riêng.
Lỗi khác (tiêu đề cha sai, cắt giữa câu bất thường...) ghi vào ô "khác".
"""


def review_sheet(docs, titles, n=30, seed=0, tok=None, size=SIZE, sent_split=None, max_chars=3000):
    """Markdown gồm `n` điều luật chọn ngẫu nhiên theo `seed`: nguyên văn và danh sách chunk C5."""
    out = [REVIEW_GUIDE, f'Seed: {seed}; số điều luật: {min(n, len(docs))}.\n']
    for k, doc_id in enumerate(random.Random(seed).sample(sorted(docs), min(n, len(docs))), 1):
        text = docs[doc_id]
        shown = text if len(text) <= max_chars else (
            text[:max_chars] + f'\n[... ĐÃ CẮT: chỉ hiện {max_chars}/{len(text)} ký tự đầu]')
        out += [f'## {k}. `{doc_id}`\n', '````text', shown, '````\n', 'Chunk C5:\n']
        for cid, _, s, e, ctext in chunk_struct(doc_id, titles[doc_id], text[len(titles[doc_id]) + 1:], tok,
                                                size, sent_split=sent_split):
            head = ctext[:len(ctext) - (e - s)]
            out.append(f'- `{cid}` [{s}:{e}] **{head.strip()}** {text[s:e][:120]!r}')
        out.append('\nĐánh giá: [ ] đúng  [ ] khoản nhận nhầm  [ ] bỏ sót khoản/điểm  [ ] khác:\n')
    return '\n'.join(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('processed_dir', help='thư mục <processed>/zalo_legal, hoặc file corpus.jsonl (ViQuAD)')
    parser.add_argument('--methods', help=f'mặc định {",".join(METHODS)} (Zalo) hoặc c1,c3,c4 (ViQuAD)')
    parser.add_argument('--tokenizer', default='BAAI/bge-m3')
    parser.add_argument('--size', type=int, default=SIZE)
    parser.add_argument('--review', help='ghi phiếu đối chiếu tay C5 ra file Markdown này thay vì in thống kê')
    parser.add_argument('--review-n', type=int, default=30)
    parser.add_argument('--seed', type=int, default=0)
    args = parser.parse_args()
    viquad = args.processed_dir.endswith('.jsonl')
    methods = (args.methods or ('c1,c3,c4' if viquad else ','.join(METHODS))).split(',')
    allowed = ('c1', 'c3', 'c4') if viquad else METHODS
    if set(methods) - set(allowed):
        parser.error(f'Cách phân đoạn không hợp lệ: {sorted(set(methods) - set(allowed))}; chọn trong {allowed}')
    if viquad and args.review:
        parser.error('Phiếu đối chiếu C5 chỉ dùng cho kho Zalo')

    from transformers import AutoTokenizer

    tok = AutoTokenizer.from_pretrained(args.tokenizer)
    if viquad:
        with open(args.processed_dir, encoding='utf-8') as f:
            docs = {r['doc_id']: r['text'] for r in map(json.loads, f)}
    else:
        from datasets import load_from_disk

        from ragvi.data import load_zalo_corpus

        docs = load_zalo_corpus(args.processed_dir)
        # C5 cần tiêu đề riêng, dict {doc_id: title + "\n" + text} không tách được chắc chắn nên đọc thẳng cột title.
        corpus = load_from_disk(str(Path(args.processed_dir) / 'corpus')).select_columns(['id', 'title'])
        titles = {row['id']: row['title'] for row in corpus}
        bodies = {}
        for doc_id, text in docs.items():
            if not text.startswith(titles[doc_id] + '\n'):
                raise ValueError(f'Tài liệu {doc_id} không có dạng title + "\\n" + text')
            bodies[doc_id] = text[len(titles[doc_id]) + 1:]

    if args.review:
        Path(args.review).write_text(review_sheet(docs, titles, args.review_n, args.seed, tok, args.size),
                                     encoding='utf-8')
        print(f'Đã ghi phiếu đối chiếu {min(args.review_n, len(docs))} điều luật (seed {args.seed}) vào {args.review}')
        raise SystemExit

    run = {
        'c1': lambda d: chunk_fixed(d, docs[d], tok, args.size),
        'c3': lambda d: chunk_sentence(d, docs[d], tok, args.size),
        'c4': lambda d: chunk_document(d, docs[d]),
        'c5': lambda d: chunk_struct(d, titles[d], bodies[d], tok, args.size),
        'c5_nohead': lambda d: chunk_struct(d, titles[d], bodies[d], tok, args.size, heading=False),
    }
    print(f'Số tài liệu: {len(docs)}')
    print(f'{"cách":<10}{"số chunk":>10}{"tb":>9}{"trung vị":>10}{"p95":>8}{"max":>8}{">512":>8}')
    for name in methods:
        st = chunk_stats((c for d in docs for c in run[name](d)), tok)
        print(f'{name:<10}{st["n_chunks"]:>10}{st["tok_mean"]:>9.1f}{st["tok_median"]:>10.1f}'
              f'{st["tok_p95"]:>8}{st["tok_max"]:>8}{st["over_512"]:>8.2%}')
    if not viquad:
        print(f'Tỷ lệ điều luật có ít nhất một khoản: {clause_rate(bodies.values()):.1%}')
    if 'c5' in methods:
        # Chẩn đoán: độ dài token của phần tiêu đề cha chung cho mọi chunk của một điều ("Văn bản X, <title>").
        heads = sorted(((len(_offsets(struct_heading(d, titles[d])[1], tok)[0]), d) for d in docs), reverse=True)
        n = sorted(h for h, _ in heads)
        print(f'Tiêu đề cha C5 (token, mỗi điều luật): trung vị {statistics.median(n):.1f}, '
              f'p95 {n[math.ceil(0.95 * len(n)) - 1]}, max {n[-1]}')
        print('5 điều luật có tiêu đề cha dài nhất (token, doc_id, 200 ký tự đầu title):')
        for h, d in heads[:5]:
            print(f'  {h:>6}  {d}  {titles[d][:200]!r}')
