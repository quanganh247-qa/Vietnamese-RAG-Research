"""Kiểm tra mô-đun run.py và giao diện demo app.py (Ngày 16, 21, 23)."""
import json

from ragvi import app, run


def test_method_and_config_and_source_formatting():
    assert run.method_name('C5', 'E5', 'R1') == 'hybrid[c5][word]+r1'
    assert run.method_name('C3', 'E3', 'R0') == 'dense[c3]'
    assert run.config_name('C5_nohead', 'E3', 'R0') == 'C5_nohead-E3-R0'
    src_zl = run.format_source('zalo', '43/2019/qh14+30#1', 'Văn bản 43/2019/QH14, Điều 30, Khoản 2: Nội dung')
    assert '43/2019/QH14' in src_zl and 'Điều 30' in src_zl and 'Khoản 2' in src_zl
    src_vq = run.format_source('viquad', '56d44d9cbf66d849#0', 'Bạc Liêu...', {'56d44d9cbf66d849': 'Bạc Liêu'})
    assert src_vq == 'Wikipedia: Bạc Liêu (56d44d9cbf66d849#0)'


def test_retrieve_and_generate_from_cache(tmp_path):
    cdir = tmp_path / 'cache'
    rdir = tmp_path / 'results'
    (cdir / 'chunks').mkdir(parents=True)
    rdir.mkdir(parents=True)

    q_row = {'qid': 'q1', 'question': 'Bạc Liêu nằm ở đâu?', 'answerable': True,
             'gold_doc_id': 'doc1', 'title': 'Bạc Liêu'}
    (rdir / 'viquad_source.jsonl').write_text(json.dumps(q_row, ensure_ascii=False) + '\n', encoding='utf-8')
    chunk_row = ['doc1#0', 'doc1', 0, 35, 'Bạc Liêu nằm ở đồng bằng sông Cửu Long.']
    (cdir / 'chunks/viquad__c3.jsonl').write_text(json.dumps(chunk_row, ensure_ascii=False) + '\n', encoding='utf-8')
    ret_row = {'method': 'dense[c3]+r1', 'qid': 'q1', 'top': ['doc1#0']}
    (cdir / 'retrieval_viquad_phase_a.jsonl').write_text(json.dumps(ret_row, ensure_ascii=False) + '\n', encoding='utf-8')
    ans_row = {'config': 'C3-E3-R1', 'qid': 'q1', 'answer': 'Bạc Liêu ở đồng bằng sông Cửu Long.',
               'context_ids': ['doc1#0']}
    (cdir / 'answers_viquad_test.jsonl').write_text(json.dumps(ans_row, ensure_ascii=False) + '\n', encoding='utf-8')

    passages = run.retrieve('viquad', 'C3', 'E3', 'R1', 'Bạc Liêu nằm ở đâu?',
                            top_n=5, cache_dir=cdir, results_dir=rdir)
    assert len(passages) == 1 and passages[0].source == 'Wikipedia: Bạc Liêu (doc1#0)'
    ans = run.generate('Bạc Liêu nằm ở đâu?', passages, dataset='viquad', c='C3', e='E3', r='R1',
                       cache_dir=cdir, results_dir=rdir)
    assert ans == 'Bạc Liêu ở đồng bằng sông Cửu Long.'
    assert '2021' in app.DISCLAIMER and 'tư vấn pháp lý' in app.DISCLAIMER
