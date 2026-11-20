"""Kiểm tra việc tách tập Zalo và ViQuAD trên dữ liệu giả. Chạy: PYTHONPATH=src python3 tests/test_data.py"""
import json
import random
import tempfile
from pathlib import Path

from ragvi.data import (build_viquad_eval, build_zalo_eval, expand_zalo_doc_ids, gold_groups, locate_answers,
                        split_viquad, split_zalo, viquad_corpus, viquad_questions)


def fake_gold(n=800, n_docs=450, seed=1):
    """Giống Zalo về hình dạng: khoảng 800 truy vấn trỏ tới khoảng 450 điều luật, vài truy vấn có 2 điều luật vàng."""
    rng = random.Random(seed)
    return {f'q{i:04d}': {f'd{rng.randrange(n_docs)}' for _ in range(2 if i % 100 == 0 else 1)} for i in range(n)}


def test_chain_stays_together():
    gold = {'a': {'d1'}, 'b': {'d1', 'd2'}, 'c': {'d2'}, 'x': {'d9'}}
    assert gold_groups(gold) == [['a', 'b', 'c'], ['x']]
    # Bản trùng mã nd-cp và nđ-cp thuộc cùng một nhóm liên thông (D6)
    assert gold_groups({'q1': {'24/2020/nđ-cp+14'}, 'q2': {'24/2020/nd-cp+14'}}) == [['q1', 'q2']]
    assert expand_zalo_doc_ids({'24/2020/nđ-cp+14'}, {'24/2020/nđ-cp+14', '24/2020/nd-cp+14', 'other+1'}) == {
        '24/2020/nđ-cp+14', '24/2020/nd-cp+14'}


def test_split_has_no_leak_and_is_deterministic():
    gold = fake_gold()
    parts, group_of = split_zalo(gold)
    assert (parts, group_of) == split_zalo(gold)
    assert sorted(q for qids in parts.values() for q in qids) == sorted(gold)
    assert [len(parts[n]) for n in ('unanswerable', 'dev', 'answerable')] == [120, 100, 280]
    docs = {name: set().union(*(gold[q] for q in qids)) for name, qids in parts.items()}
    names = list(docs)
    assert all(not docs[a] & docs[b] for i, a in enumerate(names) for b in names[i + 1:])


def test_build_writes_frozen_files():
    gold = fake_gold()
    questions = {q: f'Câu hỏi {q}?' for q in gold}
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / 'zalo'
        manifest = build_zalo_eval(questions, gold, out)
        test = [json.loads(line) for line in (out / 'test.jsonl').read_text(encoding='utf-8').splitlines()]
        removed = set(json.loads((out / 'removed_doc_ids.json').read_text(encoding='utf-8')))
        assert sum(r['answerable'] for r in test) == 280 and len(test) == 400
        assert all(set(r['gold_doc_ids']) <= removed for r in test if not r['answerable'])
        assert all(not set(r['gold_doc_ids']) & removed for r in test if r['answerable'])
        assert manifest['actual_sizes']['reserve'] == 300
        try:
            build_zalo_eval(questions, gold, out)
        except FileExistsError:
            pass
        else:
            raise AssertionError('Phải từ chối ghi đè tập đã đóng băng')


def fake_viquad(n_titles=30, n_passages=20):
    """Giống ViQuAD về hình dạng: mỗi đoạn 2 câu trả lời được + 1 câu is_impossible; id lặp lại giữa các split;
    split test không có đáp án; một đáp án có answer_start lệch."""
    rows = []
    for t in range(n_titles + 2):
        split = 'test' if t >= n_titles else 'validation' if t >= n_titles - 5 else 'train'
        for p in range(n_passages):
            answer = f'giá trị {t * 100 + p}'
            context = f'Đoạn {p} của bài {t}. Đáp án là {answer} ở đây, không phải giá trị khác.'
            start = context.index(answer)
            for k in range(3):
                impossible = k == 2
                rows.append({
                    'split': split, 'id': f'{t % (n_titles - 5):02d}-{p:02d}-{k}', 'title': f'Bài {t}',
                    'context': context, 'question': f'Câu {k} về đoạn {p} bài {t}?', 'is_impossible': impossible,
                    'answers': None if split == 'test' else {'text': [], 'answer_start': []} if impossible
                    else {'text': [answer], 'answer_start': [start + 3 * k]},  # k = 1: vị trí lệch 3 ký tự
                })
    return rows


def test_locate_answers_fixes_shifted_start():
    context = 'Hà Nội là thủ đô. Hà Nội có 36 phố phường.'
    assert locate_answers(context, {'text': ['Hà Nội', 'Huế'], 'answer_start': [20, 0]}) == [
        {'text': 'Hà Nội', 'start': 18, 'end': 24}]
    assert locate_answers(context, [{'text': 'thủ đô', 'answer_start': 10}]) == [
        {'text': 'thủ đô', 'start': 10, 'end': 16}]
    assert locate_answers(context, None) == []


def test_viquad_split_sizes_no_leak_one_per_passage():
    rows = fake_viquad()
    questions = viquad_questions(rows)
    assert len({q['qid'] for q in questions}) == len(questions) == 30 * 20 * 3
    parts = split_viquad(questions)
    assert parts == split_viquad(viquad_questions(rows))
    assert parts != split_viquad(questions, seed=1)
    assert {n: len(qs) for n, qs in parts.items()} == {'unanswerable': 120, 'dev': 100, 'answerable': 280}
    assert all(q['answerable'] == (name == 'answerable') for name in ('answerable', 'unanswerable')
               for q in parts[name])
    test = parts['answerable'] + parts['unanswerable']
    assert not {q['title'] for q in parts['dev']} & {q['title'] for q in test}
    for qs in (test, parts['dev']):
        assert len({q['gold_doc_id'] for q in qs}) == len(qs)
    context = {d: doc['text'] for d, doc in viquad_corpus(rows).items()}
    for q in test + parts['dev']:
        assert bool(q['answers']) == q['answerable']
        assert all(context[q['gold_doc_id']][a['start']:a['end']] == a['text'] for a in q['answers'])


def test_build_viquad_writes_frozen_files():
    rows = fake_viquad()
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / 'viquad'
        manifest = build_viquad_eval(rows, out)
        read = lambda name: [json.loads(line) for line in (out / name).read_text(encoding='utf-8').splitlines()]
        test, dev, corpus = read('test.jsonl'), read('dev.jsonl'), read('corpus.jsonl')
        assert (sum(r['answerable'] for r in test), len(test), len(dev)) == (280, 400, 100)
        assert len(corpus) == manifest['corpus_passages'] == 32 * 20  # gồm cả đoạn của split test
        assert {r['gold_doc_id'] for r in test + dev} <= {d['doc_id'] for d in corpus}
        assert all(q['qid'].split(':')[0] in ('train', 'validation') for q in test + dev)
        assert set(manifest['sha256']) == {'test.jsonl', 'dev.jsonl', 'corpus.jsonl'}
        with tempfile.TemporaryDirectory() as tmp2:
            assert build_viquad_eval(rows, Path(tmp2) / 'v')['sha256'] == manifest['sha256']
        try:
            build_viquad_eval(rows, out)
        except FileExistsError:
            pass
        else:
            raise AssertionError('Phải từ chối ghi đè tập đã đóng băng')


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
