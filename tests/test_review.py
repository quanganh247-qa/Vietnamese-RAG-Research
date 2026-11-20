"""Kiểm tra dựng phiếu đọc tay D6 trên dữ liệu giả. Chạy: PYTHONPATH=src python -m pytest -q tests/test_review.py"""
import json
import tempfile
from pathlib import Path

import pytest

from ragvi.review import main, pick, render, tally

TEST = [{'qid': f'q{i:02d}', 'question': f'Câu hỏi {i}?', 'answerable': i % 2 == 0, 'gold_doc_id': f'd{i}'}
        for i in range(40)]
RESULTS = {q['qid']: [f'd{j}' for j in range(int(q['qid'][1:]), int(q['qid'][1:]) + 20)] for q in TEST}
CORPUS = {f'd{j}': (f'Tiêu đề {j}', ('x' * 2000) if j == 3 else f'Nội dung {j}') for j in range(80)}


def test_pick_is_deterministic_and_unanswerable_only():
    a, b = pick(TEST, RESULTS, n=10, seed=0), pick(TEST, RESULTS, n=10, seed=0)
    assert a == b and len({q['qid'] for q in a}) == 10
    assert all(not q['answerable'] for q in a)
    assert a != pick(TEST, RESULTS, n=10, seed=1)


def test_pick_errors_when_short():
    with pytest.raises(ValueError, match='có kết quả truy xuất'):
        pick(TEST, {'q01': ['d1']}, n=2)


def test_render_top5_truncation_and_gold_mark():
    q = next(q for q in TEST if q['qid'] == 'q03')
    md = render([q], RESULTS, CORPUS)
    block = md.split('## Câu 1')[1]
    assert [l.split('`')[1] for l in block.splitlines() if l.startswith('**Đoạn ')] == ['d3', 'd4', 'd5', 'd6', 'd7']
    assert '`d3` **[ĐOẠN GỐC]**' in block and block.count('[ĐOẠN GỐC]') == 1
    assert '(đã cắt)' in block and 'x' * 1201 not in block
    assert 'Kết luận: [ ] không trả lời được   [ ] VẪN trả lời được (đoạn số: __)' in block
    assert '## Tổng kết' in md and '20%' in md


def test_zalo_gold_list_marked():
    q = {'qid': 'z', 'question': '?', 'answerable': False, 'gold_doc_ids': ['d2', 'd4']}
    assert render([q], {'z': ['d1', 'd2', 'd3', 'd4']}, CORPUS).count('[ĐOẠN GỐC]') == 3  # 2 đoạn + 1 ở hướng dẫn


def test_tally_counts_and_lists_ungraded():
    md = render(pick(TEST, RESULTS, n=6, seed=0), RESULTS, CORPUS)
    qids = [b.split('`')[1] for b in md.split('## Câu ')[1:]]
    boxes = iter(['[x] không trả lời được   [ ]', '[ ] không trả lời được   [X]', '[x] không trả lời được   [ ]',
                  '[x] không trả lời được   [ ]', '[ ] không trả lời được   [ ]', '[x] không trả lời được   [x]'])
    md = '\n'.join(l.replace('[ ] không trả lời được   [ ]', next(boxes)) if l.startswith('Kết luận:') else l
                   for l in md.splitlines())
    r = tally(md)
    assert (r['total'], r['yes'], len(r['no'])) == (6, [qids[1]], 3)
    assert r['unmarked'] == [qids[4]] and r['both'] == [qids[5]]
    assert r['rate'] == 0.25 and r['over']


def test_cli_end_to_end(capsys):
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        lines = [json.dumps({'method': m, 'qid': q, 'r5': 0, 'r20': 0, 'mrr10': 0, 'ndcg5': 0, 'top': t})
                 for q, t in RESULTS.items() for m in ('hybrid', 'bm25')]
        (d / 'ret.jsonl').write_text('\n'.join(lines) + '\n{"method": "hyb', encoding='utf-8')
        (d / 'test.jsonl').write_text('\n'.join(json.dumps(q, ensure_ascii=False) for q in TEST), encoding='utf-8')
        (d / 'corpus.jsonl').write_text('\n'.join(json.dumps({'doc_id': k, 'title': t, 'text': x}, ensure_ascii=False)
                                                  for k, (t, x) in CORPUS.items()), encoding='utf-8')
        out = d / 'phieu.md'
        main([str(d / 'ret.jsonl'), str(d / 'test.jsonl'), str(d / 'corpus.jsonl'), str(out), '--n', '5'])
        assert out.read_text(encoding='utf-8').count('Kết luận:') == 5
        main(['--tally', str(out)])
        assert 'Chưa chấm' in capsys.readouterr().out
        with pytest.raises(SystemExit):
            main([str(d / 'ret.jsonl'), str(d / 'test.jsonl'), str(d / 'corpus.jsonl'), str(d / 'b.md'), '--n', '50'])
