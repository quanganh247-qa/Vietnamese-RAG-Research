"""Test truy xuất trên kho giả nhỏ: không cần dữ liệu thật, không tải mô hình."""
import json

import numpy as np
import pytest

from ragvi.metrics import em_f1, mean_metrics, metrics, viquad_hits, zalo_hits
from ragvi.retrieval import (bm25_scores, build_bm25, cached_chunks, cached_tokens, embed, embedding_cache_path,
                             hybrid_scores, minmax, model_prefixes, read_rows, run_retrieval, summarize,
                             tokenize_syllables, tokenize_words, top_k)

CORPUS = {
    'a+1': 'Điều 1. Phạm vi điều chỉnh\nLuật này quy định về giao thông đường bộ.',
    'a+2': 'Điều 2. Đối tượng áp dụng\nLuật này áp dụng đối với tổ chức, cá nhân.',
    'b+1': 'Điều 1. Mức phạt\nPhạt tiền người điều khiển xe máy không đội mũ bảo hiểm.',
    'b+2': 'Điều 2. Thuế thu nhập\nThuế suất thuế thu nhập doanh nghiệp là 20%.',
}
DOC_IDS, TEXTS = list(CORPUS), list(CORPUS.values())
QUESTIONS = {'q1': 'Không đội mũ bảo hiểm bị phạt thế nào?', 'q2': 'Thuế suất thuế thu nhập doanh nghiệp?'}
GOLD = {'q1': {'b+1'}, 'q2': {'b+2'}}


def test_metrics():
    assert metrics([True, False], 1) == {'r5': 1, 'r20': 1, 'mrr10': 1, 'ndcg5': 1}
    late = metrics([False] * 5 + [True], 2)
    assert late == {'r5': 0, 'r20': 0.5, 'mrr10': 1 / 6, 'ndcg5': 0}
    assert metrics([False] * 20, 1) == {'r5': 0, 'r20': 0, 'mrr10': 0, 'ndcg5': 0}


def test_zalo_hits_counts_each_gold_doc_once():
    assert zalo_hits(['a', 'a', 'b'], {'a'}) == [True, False, False]  # hai chunk cùng điều luật chỉ tính một lần


def test_mean_metrics():
    rows = [metrics([True], 1), metrics([False], 1)]
    assert mean_metrics(rows) == {'r5': 0.5, 'r20': 0.5, 'mrr10': 0.5, 'ndcg5': 0.5}
    with pytest.raises(ValueError):
        mean_metrics([])


def test_tokenize_syllables():
    assert tokenize_syllables('Điều 1. Phạm vi, ÁP DỤNG!') == ['điều', '1', 'phạm', 'vi', 'áp', 'dụng']


def test_bm25_ranks_gold_first():
    index = build_bm25(TEXTS)
    for qid, question in QUESTIONS.items():
        assert DOC_IDS[top_k(bm25_scores(index, question), 1)[0]] in GOLD[qid]


def test_bm25_custom_tokenize():
    index = build_bm25(TEXTS, tokenize=str.split)
    assert DOC_IDS[top_k(bm25_scores(index, 'Thuế suất', tokenize=str.split), 1)[0]] == 'b+2'


def test_minmax_and_top_k():
    assert minmax([2, 4, 6]).tolist() == [0, 0.5, 1]
    assert minmax([3, 3]).tolist() == [0, 0]
    assert top_k([0.1, 0.9, 0.9, 0.5], 3).tolist() == [1, 2, 3]


def test_hybrid_with_fake_dense():
    dense = np.array([[0.9, 0.1, 0.2, 0.0],    # dense chọn sai tài liệu 0 cho q1
                      [0.0, 0.1, 0.2, 0.9]])
    bm25 = np.array([0.0, 0.0, 10.0, 1.0])     # BM25 chọn đúng tài liệu 2
    assert top_k(hybrid_scores(dense[0], bm25, alpha=0.7), 1)[0] == 0   # alpha nhân với dense
    assert top_k(hybrid_scores(dense[0], bm25, alpha=0.3), 1)[0] == 2
    assert hybrid_scores(dense[0], bm25, alpha=1.0).tolist() == minmax(dense[0]).tolist()
    # 0.7 * minmax(dense) + 0.3 * minmax(bm25), tính tay cho tài liệu 2
    assert hybrid_scores(dense[0], bm25)[2] == pytest.approx(0.7 * (0.2 / 0.9) + 0.3 * 1.0)


def test_embed_reads_cache_without_loading_model(tmp_path):
    path = embedding_cache_path(tmp_path, 'zalo_legal', 'article', 'BAAI/bge-m3')
    assert path.name == 'zalo_legal__article__BAAI_bge-m3.npy'
    np.save(path, np.eye(4, dtype=np.float32))
    assert embed(TEXTS, path).shape == (4, 4)
    with pytest.raises(ValueError):
        embed(TEXTS[:3], path)


def test_run_retrieval_skips_existing_rows(tmp_path):
    out = tmp_path / 'runs' / 'retrieval.jsonl'
    index = build_bm25(TEXTS)
    calls = []

    def bm25(qid):
        calls.append(qid)
        return bm25_scores(index, QUESTIONS[qid])

    assert run_retrieval({'bm25': bm25}, QUESTIONS, GOLD, DOC_IDS, out) == 2
    assert run_retrieval({'bm25': bm25}, QUESTIONS, GOLD, DOC_IDS, out) == 0
    assert calls == ['q1', 'q2']

    # Lượt chạy bị ngắt: mất q2 và dòng cuối bị cắt dở -> chỉ chạy lại q2.
    first = out.read_text(encoding='utf-8').splitlines()[0]
    out.write_text(first + '\n{"method": "bm25", "qi', encoding='utf-8')
    assert run_retrieval({'bm25': bm25}, QUESTIONS, GOLD, DOC_IDS, out) == 1
    assert calls == ['q1', 'q2', 'q2']
    rows = read_rows(out)
    assert [(r['method'], r['qid']) for r in rows] == [('bm25', 'q1'), ('bm25', 'q2')]
    assert rows[0]['top'][0] == 'b+1' and json.dumps(rows[0])

    # Thêm phương pháp mới vào cùng file: chỉ phương pháp mới được chạy.
    assert run_retrieval({'bm25': bm25, 'other': lambda qid: np.arange(4.0)}, QUESTIONS, GOLD, DOC_IDS, out) == 2
    table = summarize(out, ['bm25', 'other', 'missing'])
    assert list(table) == ['bm25', 'other']
    assert table['bm25'] == {'n': 2, 'r5': 1, 'r20': 1, 'mrr10': 1, 'ndcg5': 1}


def test_cli_bm25_end_to_end(tmp_path, monkeypatch, capsys):
    import ragvi.data
    from ragvi.retrieval import main

    monkeypatch.setattr(ragvi.data, 'load_zalo_corpus', lambda _: CORPUS, raising=False)
    monkeypatch.setattr(ragvi.data, 'load_zalo_queries', lambda _: (QUESTIONS, GOLD))
    main(['unused', str(tmp_path), '--methods', 'bm25'])
    assert 'ghi thêm 2 dòng' in capsys.readouterr().out
    main(['unused', str(tmp_path), '--methods', 'bm25'])
    output = capsys.readouterr().out
    assert 'ghi thêm 0 dòng' in output and 'Recall@20' in output
    assert len(read_rows(tmp_path / 'retrieval_zalo.jsonl')) == 2


def test_viquad_hits_80_percent_of_any_answer():
    answers = [{'text': 'abcdefghij', 'start': 10, 'end': 20}, {'text': 'xy', 'start': 50, 'end': 52}]
    ranked = [('other', 10, 20),   # sai đoạn
              ('g', 0, 17),        # phủ 7/10 ký tự đáp án 1: chưa đủ 80%
              ('g', 12, 60),       # phủ 8/10 đáp án 1 (và trọn đáp án 2): đúng
              ('g', 0, 100)]       # đúng nữa nhưng chỉ lần trúng đầu được tính
    assert viquad_hits(ranked, 'g', answers) == [False, False, True, False]
    assert viquad_hits([('g', 49, 51)], 'g', answers) == [False]   # 1/2 ký tự đáp án 2
    assert metrics(viquad_hits(ranked, 'g', answers), 1)['mrr10'] == 1 / 3


def test_tokenize_words_and_cache(tmp_path):
    assert tokenize_words('Luật bảo hiểm xã hội, 20%.') == ['luật', 'bảo_hiểm_xã_hội', '20']
    path = tmp_path / 'tokens.jsonl'
    calls = []

    def tok(text):
        calls.append(text)
        return text.split()

    assert cached_tokens(['x', 'y'], ['a b', 'c'], path, tok) == [['a', 'b'], ['c']]
    # Kho thu hẹp và kho có thêm tài liệu: chỉ tách tài liệu chưa có trong đệm.
    assert cached_tokens(['y', 'z'], ['c', 'd e'], path, tok) == [['c'], ['d', 'e']]
    assert calls == ['a b', 'c', 'd e']


def _write_jsonl(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')


def test_cli_eval_set_with_removed_docs(tmp_path, monkeypatch, capsys):
    import ragvi.data
    from ragvi.retrieval import main

    monkeypatch.setattr(ragvi.data, 'load_zalo_corpus', lambda _: CORPUS, raising=False)
    _write_jsonl(tmp_path / 'test.jsonl', [
        {'qid': 'q1', 'question': QUESTIONS['q1'], 'answerable': True, 'gold_doc_ids': ['b+1'], 'group': 0},
        {'qid': 'q2', 'question': QUESTIONS['q2'], 'answerable': False, 'gold_doc_ids': ['b+2'], 'group': 1}])
    (tmp_path / 'removed.json').write_text('["b+2"]', encoding='utf-8')
    # Đệm embedding của kho đầy đủ (4 dòng) và của câu hỏi lượt chạy: không được nạp mô hình.
    out = tmp_path / 'out'
    (out / 'embeddings').mkdir(parents=True)
    np.save(out / 'embeddings' / 'zalo_legal__article__BAAI_bge-m3.npy', np.eye(4, dtype=np.float32))
    np.save(out / 'embeddings' / 'zalo_legal__queries_zalo_test__BAAI_bge-m3.npy',
            np.array([[0, 0, 1, 0], [0, 0, 0, 1]], dtype=np.float32))
    args = ['unused', str(out), '--run', 'zalo_test', '--questions', str(tmp_path / 'test.jsonl'),
            '--removed', str(tmp_path / 'removed.json')]
    main(args)
    main(args + ['--tokenizer', 'word'])
    assert 'ghi thêm 4 dòng' in capsys.readouterr().out   # chỉ bm25[word] và hybrid[word] là mới
    rows = {(r['method'], r['qid']): r for r in read_rows(out / 'retrieval_zalo_test.jsonl')}
    assert sorted({m for m, _ in rows}) == ['bm25', 'bm25[word]', 'dense', 'hybrid', 'hybrid[word]']
    for (method, qid), row in rows.items():
        assert 'b+2' not in row['top'] and len(row['top']) == 3
        assert (row['r5'] is None) == (qid == 'q2')
    assert rows[('dense', 'q1')]['top'][0] == 'b+1' and rows[('dense', 'q1')]['r5'] == 1
    # Giống hệt BM25 dựng trực tiếp trên kho đã loại b+2.
    kept = [d for d in DOC_IDS if d != 'b+2']
    index = build_bm25([CORPUS[d] for d in kept])
    assert rows[('bm25', 'q2')]['top'] == [kept[i] for i in top_k(bm25_scores(index, QUESTIONS['q2']))]
    assert len((out / 'tokens' / 'zalo_legal__article__underthesea.jsonl').read_text().splitlines()) == 3

    with pytest.raises(SystemExit):   # thiếu --run: không được ghi vào retrieval_zalo.jsonl
        main(['unused', str(out), '--questions', str(tmp_path / 'test.jsonl')])


def test_cli_viquad_passages(tmp_path, capsys):
    from ragvi.retrieval import main

    _write_jsonl(tmp_path / 'corpus.jsonl', [{'doc_id': d, 'title': 'T', 'text': t} for d, t in CORPUS.items()])
    _write_jsonl(tmp_path / 'test.jsonl', [
        {'qid': 'train:1', 'question': QUESTIONS['q1'], 'answerable': True, 'gold_doc_id': 'b+1',
         'answers': [{'text': 'mũ bảo hiểm', 'start': 0, 'end': 11}]},
        {'qid': 'train:2', 'question': 'Ai là tác giả?', 'answerable': False, 'gold_doc_id': 'a+1', 'answers': []}])
    main([str(tmp_path / 'corpus.jsonl'), str(tmp_path), '--run', 'viquad_test', '--methods', 'bm25',
          '--questions', str(tmp_path / 'test.jsonl')])
    rows = read_rows(tmp_path / 'retrieval_viquad_test.jsonl')
    assert [(r['qid'], r['r5'], len(r['top'])) for r in rows] == [('train:1', 1, 4), ('train:2', None, 4)]
    assert summarize(tmp_path / 'retrieval_viquad_test.jsonl', ['bm25'])['bm25']['n'] == 1


def test_em_f1_and_prefixes_and_chunking(tmp_path):
    assert em_f1('Hà Nội!', ['hà nội', 'TP. Hồ Chí Minh']) == {'em': 1.0, 'f1': 1.0}
    assert em_f1('thủ đô Hà Nội', [{'text': 'Hà Nội'}]) == {'em': 0.0, 'f1': pytest.approx(2 * 2 / (4 + 2))}
    assert model_prefixes('intfloat/multilingual-e5-large') == ('query: ', 'passage: ')
    assert model_prefixes('BAAI/bge-m3') == ('', '')
    chunks = cached_chunks(CORPUS, 'c4', tmp_path / 'chunks.jsonl')
    assert len(chunks) == 4 and chunks[0][0] == 'a+1#0'
    assert cached_chunks(CORPUS, 'c4', tmp_path / 'chunks.jsonl') == chunks


def test_embed_checkpoint_resume_and_oom_backoff(tmp_path):
    cache = tmp_path / 'zalo__c5__bge.npy'
    texts = [f'chunk {i}' for i in range(5)]
    calls = []

    def flaky_encode(batch, bs):
        calls.append((list(batch), bs))
        if len(calls) == 2:
            raise KeyboardInterrupt('ngắt phiên giữa chừng')
        return np.full((len(batch), 3), bs, dtype=np.float32)

    with pytest.raises(KeyboardInterrupt):
        embed(texts, cache, batch_size=32, checkpoint_every=2, encode_fn=flaky_encode)
    assert not cache.exists()
    assert (cache.with_suffix('.parts') / '0000000_0000002.npy').exists()

    # Lần chạy sau: bỏ qua block 0..2, gặp OOM ở bs=32 rồi tự hạ xuống 16 và hoàn tất.
    oom_once = {'fired': False}

    def resume_encode(batch, bs):
        calls.append((list(batch), bs))
        if not oom_once['fired'] and bs == 32:
            oom_once['fired'] = True
            raise RuntimeError('CUDA out of memory')
        return np.arange(len(batch) * 3, dtype=np.float32).reshape(len(batch), 3)

    vecs = embed(texts, cache, batch_size=32, checkpoint_every=2, encode_fn=resume_encode)
    assert vecs.shape == (5, 3) and cache.exists() and not cache.with_suffix('.parts').exists()
    # Block 0..2 giữ nguyên giá trị từ lần chạy đầu (32.0), không bị nhúng lại
    assert np.all(vecs[:2] == 32.0)
    assert any(bs == 16 for _, bs in calls)
