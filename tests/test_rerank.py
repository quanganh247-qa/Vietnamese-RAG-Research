"""Kiểm tra reranking R1 trên dữ liệu giả (không tải mô hình)."""
import json

from ragvi.rerank import main, rerank_top, run_rerank
from ragvi.retrieval import read_rows


def test_rerank_top_reorders_and_keeps_recall20_set():
    text_of = {'d1': 'văn bản nhiễu', 'd2': 'mức phạt không đội mũ bảo hiểm', 'd3': 'thuế thu nhập'}
    scorer = lambda q, ps: [1.0 if 'mũ bảo hiểm' in p else 0.1 for p in ps]
    top = rerank_top('mũ bảo hiểm', ['d1', 'd2', 'd3'], text_of, scorer)
    assert top == ['d2', 'd1', 'd3']


def test_run_rerank_and_cli(tmp_path, monkeypatch):
    import ragvi.rerank

    corpus = [
        {'doc_id': 'd1', 'title': 'T1', 'text': 'Đoạn nhiễu không liên quan.'},
        {'doc_id': 'd2', 'title': 'T2', 'text': 'Đáp án đúng là Hà Nội ngàn năm văn hiến.'},
    ]
    questions = [
        {'qid': 'q1', 'question': 'Thủ đô là gì?', 'answerable': True, 'gold_doc_id': 'd2',
         'answers': [{'text': 'Hà Nội', 'start': 15, 'end': 21}]},
        {'qid': 'q2', 'question': 'Câu không trả lời được?', 'answerable': False, 'gold_doc_id': 'd1', 'answers': []},
    ]
    ret_rows = [
        {'method': 'dense', 'qid': 'q1', 'r5': 1.0, 'r20': 1.0, 'mrr10': 0.5, 'ndcg5': 0.6309, 'top': ['d1', 'd2']},
        {'method': 'dense', 'qid': 'q2', 'r5': None, 'r20': None, 'mrr10': None, 'ndcg5': None, 'top': ['d1', 'd2']},
    ]
    for name, rows in [('corpus.jsonl', corpus), ('questions.jsonl', questions), ('ret.jsonl', ret_rows)]:
        (tmp_path / name).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows), encoding='utf-8')

    monkeypatch.setattr(ragvi.rerank, 'load_reranker',
                        lambda *a, **kw: (lambda q, ps: [1.0 if 'Hà Nội' in p else 0.0 for p in ps]))
    out = tmp_path / 'rerank.jsonl'
    main([str(tmp_path / 'ret.jsonl'), str(tmp_path / 'questions.jsonl'), str(tmp_path / 'corpus.jsonl'),
          str(out), '--method', 'dense'])
    rows = {(r['method'], r['qid']): r for r in read_rows(out)}
    assert rows[('dense+r1', 'q1')]['top'] == ['d2', 'd1']
    assert rows[('dense+r1', 'q1')]['mrr10'] == 1.0
    assert rows[('dense+r1', 'q2')]['r5'] is None
    # Chạy lại thì bỏ qua dòng đã có
    assert run_rerank(ret_rows, {'q1': '?', 'q2': '?'}, {'q1': {'d2'}, 'q2': None},
                      {'d1': '', 'd2': ''}, out, lambda q, ps: [0, 0], 'dense') == 0
