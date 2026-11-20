"""Dựng tập đánh giá Zalo Legal và ViQuAD theo quyết định D1 (reports/quyet-dinh-thiet-ke.md).

Chạy trên Colab, từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.data zalo <processed>/zalo_legal <thư mục đầu ra> --seed 0
    PYTHONPATH=src python -m ragvi.data viquad <processed>/viquad <thư mục đầu ra> --seed 0
"""
import argparse
import hashlib
import json
import random
import re
from pathlib import Path

# Thứ tự là thứ tự ưu tiên khi xếp nhóm vào từng phần.
SIZES = {'unanswerable': 120, 'dev': 100, 'answerable': 280}


def load_zalo_queries(processed_dir):
    """Trả về (questions: {qid: text}, gold: {qid: set(doc_id)}) cho các truy vấn có nhãn."""
    from datasets import load_from_disk

    root = Path(processed_dir)
    gold = {}
    for row in load_from_disk(str(root / 'qrels')):
        if row['score'] > 0:
            gold.setdefault(row['query-id'], set()).add(row['corpus-id'])

    questions = {}
    for row in load_from_disk(str(root / 'queries')):
        qid, text = row['id'], row['text']
        if qid not in gold:
            continue
        if questions.setdefault(qid, text) != text:
            raise ValueError(f'Truy vấn trùng mã nhưng khác nội dung: {qid}')
    return questions, gold


def zalo_doc_variants(doc_id):
    """Các biến thể mã tài liệu Zalo do lỗi chính tả nd-cp <-> nđ-cp trong kho gốc (ví dụ 24/2020/nd-cp+14)."""
    return {doc_id, doc_id.replace('/nđ-', '/nd-'), doc_id.replace('/nd-', '/nđ-')}


def expand_zalo_doc_ids(doc_ids, corpus=None):
    """Mở rộng tập doc_id với biến thể nd-cp <-> nđ-cp; nếu có `corpus` thì chỉ thêm biến thể có thật trong kho."""
    base = set(doc_ids)
    extra = {v for d in base for v in zalo_doc_variants(d)} - base
    if corpus is not None:
        extra &= set(corpus)
    return base | extra


def load_zalo_corpus(processed_dir, exclude=()):
    """Trả về {doc_id: title + "\\n" + text}; điều luật có text rỗng vẫn giữ (chỉ còn tiêu đề).

    exclude: các doc_id bị loại, ví dụ nội dung removed_doc_ids.json, để dựng kho thu hẹp (tự động loại cả
    bản trùng mã nd-cp <-> nđ-cp theo quyết định D6 ngày 18/11).
    """
    from datasets import load_from_disk

    exclude = expand_zalo_doc_ids(exclude)
    return {row['id']: row['title'] + '\n' + row['text']
            for row in load_from_disk(str(Path(processed_dir) / 'corpus')) if row['id'] not in exclude}


def gold_groups(gold):
    """Nhóm các truy vấn dùng chung điều luật vàng, trực tiếp hoặc bắc cầu (union-find)."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for qid, docs in gold.items():
        for doc in docs:
            parent[find(('q', qid))] = find(('d', doc.replace('/nd-', '/nđ-')))

    groups = {}
    for qid in gold:
        groups.setdefault(find(('q', qid)), []).append(qid)
    return sorted((sorted(g) for g in groups.values()), key=lambda g: g[0])


def split_zalo(gold, sizes=SIZES, seed=0):
    """Xếp trọn từng nhóm vào phần đầu tiên còn đủ chỗ; nhóm không vừa phần nào thì để dự trữ.

    Trả về (parts: {tên phần: [qid]}, group_of: {qid: chỉ số nhóm}).
    """
    groups = gold_groups(gold)
    random.Random(seed).shuffle(groups)
    parts = {name: [] for name in (*sizes, 'reserve')}
    group_of = {}
    for index, group in enumerate(groups):
        group_of.update((qid, index) for qid in group)
        name = next((n for n in sizes if len(parts[n]) + len(group) <= sizes[n]), 'reserve')
        parts[name] += group
    return parts, group_of


def build_zalo_eval(questions, gold, out_dir, sizes=SIZES, seed=0, tolerance=5):
    """Ghi test.jsonl, dev.jsonl, removed_doc_ids.json, manifest.json; không xuất các câu còn dư.

    Từ chối ghi đè: tập đánh giá đã đóng băng thì không dựng lại vào cùng thư mục.
    """
    out = Path(out_dir)
    if out.exists() and any(out.iterdir()):
        raise FileExistsError(f'{out} đã có dữ liệu. Tập đánh giá đã đóng băng; hãy chọn thư mục khác.')

    parts, group_of = split_zalo(gold, sizes, seed)
    for name, target in sizes.items():
        if target - len(parts[name]) > tolerance:
            raise ValueError(f'Phần {name} chỉ có {len(parts[name])}/{target} câu; thử seed khác.')

    removed = sorted(set().union(*(gold[q] for q in parts['unanswerable'])))
    kept_gold = set().union(*(gold[q] for name in ('dev', 'answerable', 'reserve') for q in parts[name]))
    assert not kept_gold & set(removed), 'Điều luật bị loại vẫn là điều luật vàng của câu ở phần khác'

    def rows(names):
        return [{'qid': q, 'question': questions[q], 'answerable': name != 'unanswerable',
                 'gold_doc_ids': sorted(gold[q]), 'group': group_of[q]}
                for name in names for q in parts[name]]

    out.mkdir(parents=True, exist_ok=True)
    files = {'test.jsonl': rows(['answerable', 'unanswerable']), 'dev.jsonl': rows(['dev'])}
    for name, data in files.items():
        (out / name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in data), encoding='utf-8')
    (out / 'removed_doc_ids.json').write_text(json.dumps(removed, ensure_ascii=False, indent=0), encoding='utf-8')

    manifest = {
        'dataset': 'zalo_legal', 'seed': seed, 'target_sizes': sizes,
        'actual_sizes': {name: len(parts[name]) for name in sizes},
        'labeled_queries': len(gold), 'groups': len(set(group_of.values())),
        'removed_docs': len(removed),
        'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir())},
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    return manifest


def load_viquad(processed_dir):
    """Trả về danh sách dòng của cả ba split, mỗi dòng thêm khóa 'split'."""
    from datasets import load_from_disk

    return [{**row, 'split': split} for split, ds in load_from_disk(str(processed_dir)).items() for row in ds]


def passage_id(context):
    """Mã tài liệu của một đoạn ViQuAD: 16 ký tự hex đầu của SHA-256 nội dung đoạn."""
    return hashlib.sha256(context.encode('utf-8')).hexdigest()[:16]


def viquad_corpus(rows):
    """Trả về {doc_id: {'title', 'text'}} gồm các context duy nhất của mọi split (kể cả test)."""
    corpus = {}
    for row in rows:
        corpus.setdefault(passage_id(row['context']), {'title': row['title'], 'text': row['context']})
    return corpus


def locate_answers(context, answers):
    """Trả về [{'text', 'start', 'end'}] sao cho context[start:end] == text.

    answer_start lệch (ví dụ do bước làm sạch gộp khoảng trắng) thì lấy lần xuất hiện gần nhất;
    đáp án không còn nằm trong đoạn thì bỏ.
    """
    if not answers:
        return []
    pairs = (zip(answers['text'], answers['answer_start']) if isinstance(answers, dict)
             else ((a['text'], a['answer_start']) for a in answers))
    spans = set()
    for text, start in pairs:
        if not text:
            continue
        if context[start:start + len(text)] != text:
            found = [m.start() for m in re.finditer(re.escape(text), context)]
            if not found:
                continue
            start = min(found, key=lambda pos: abs(pos - start))
        spans.add((start, start + len(text)))
    return [{'text': context[s:e], 'start': s, 'end': e} for s, e in sorted(spans)]


def viquad_questions(rows):
    """Câu hỏi dùng được từ train và validation; qid kèm tên split vì id lặp lại giữa các split.

    Câu trả lời được mà không định vị được đáp án nào trong đoạn thì bị bỏ.
    """
    out = []
    for row in rows:
        if row['split'] not in ('train', 'validation'):
            continue
        answers = [] if row['is_impossible'] else locate_answers(row['context'], row['answers'])
        if not row['is_impossible'] and not answers:
            continue
        out.append({'qid': f"{row['split']}:{row['id']}", 'question': row['question'],
                    'answerable': not row['is_impossible'], 'gold_doc_id': passage_id(row['context']),
                    'title': row['title'], 'answers': answers})
    return sorted(out, key=lambda q: q['qid'])


def split_viquad(questions, sizes=SIZES, seed=0):
    """Tách theo title: dev lấy trọn các title ngẫu nhiên tới khi đủ câu; test lấy từ các title còn lại.

    Mỗi đoạn tối đa một câu (cả dev lẫn test). Trả về {tên phần: [câu hỏi]}.
    """
    rng = random.Random(seed)
    questions = list(questions)
    rng.shuffle(questions)
    titles = sorted({q['title'] for q in questions})
    rng.shuffle(titles)

    parts = {name: [] for name in sizes}
    dev_titles, used = set(), set()
    for title in titles:
        if len(parts['dev']) >= sizes['dev']:
            break
        dev_titles.add(title)
        for q in questions:
            if q['title'] == title and q['gold_doc_id'] not in used and len(parts['dev']) < sizes['dev']:
                used.add(q['gold_doc_id'])
                parts['dev'].append(q)

    # Đoạn nào thuộc title của dev thì không vào test, kể cả khi nó lặp lại dưới title khác.
    used |= {q['gold_doc_id'] for q in questions if q['title'] in dev_titles}
    for q in questions:
        name = 'answerable' if q['answerable'] else 'unanswerable'
        if q['title'] not in dev_titles and q['gold_doc_id'] not in used and len(parts[name]) < sizes[name]:
            used.add(q['gold_doc_id'])
            parts[name].append(q)
    return parts


def build_viquad_eval(rows, out_dir, sizes=SIZES, seed=0):
    """Ghi test.jsonl, dev.jsonl, corpus.jsonl, manifest.json; từ chối ghi đè như build_zalo_eval."""
    out = Path(out_dir)
    if out.exists() and any(out.iterdir()):
        raise FileExistsError(f'{out} đã có dữ liệu. Tập đánh giá đã đóng băng; hãy chọn thư mục khác.')

    questions = viquad_questions(rows)
    parts = split_viquad(questions, sizes, seed)
    for name, target in sizes.items():
        if len(parts[name]) != target:
            raise ValueError(f'Phần {name} chỉ có {len(parts[name])}/{target} câu; dữ liệu không đủ.')

    corpus = viquad_corpus(rows)
    out.mkdir(parents=True, exist_ok=True)
    files = {'test.jsonl': parts['answerable'] + parts['unanswerable'], 'dev.jsonl': parts['dev'],
             'corpus.jsonl': [{'doc_id': d, **corpus[d]} for d in sorted(corpus)]}
    for name, data in files.items():
        (out / name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in data), encoding='utf-8')

    manifest = {
        'dataset': 'viquad', 'seed': seed, 'target_sizes': sizes,
        'actual_sizes': {name: len(qs) for name, qs in parts.items()},
        'dev_answerable': sum(q['answerable'] for q in parts['dev']),
        'titles': {name: len({q['title'] for q in qs}) for name, qs in parts.items()},
        'usable_questions': len(questions),
        'labeled_rows': sum(row['split'] in ('train', 'validation') for row in rows),
        'corpus_passages': len(corpus),
        'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir())},
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('dataset', choices=['zalo', 'viquad'])
    parser.add_argument('processed_dir')
    parser.add_argument('out_dir')
    parser.add_argument('--seed', type=int, default=0)
    args = parser.parse_args()
    if args.dataset == 'zalo':
        result = build_zalo_eval(*load_zalo_queries(args.processed_dir), args.out_dir, seed=args.seed)
    else:
        result = build_viquad_eval(load_viquad(args.processed_dir), args.out_dir, seed=args.seed)
    print(json.dumps(result, ensure_ascii=False, indent=2))
