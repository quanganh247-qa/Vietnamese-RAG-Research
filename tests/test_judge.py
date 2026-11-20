"""Kiểm tra LLM-as-judge, chỉ số nhầm điều luật (H1b), phiếu gán nhãn người và Cohen's κ."""
import json
import pytest

from ragvi.judge import (blind_id, build_human_sheet, cohen_kappa, derive_judge_metrics, evaluate_kappa,
                         parse_human_sheet, parse_judge_json, run_judge, wrong_article_citation)
from ragvi.retrieval import read_rows


def test_judge_llama_cli(tmp_path, monkeypatch):
    import json
    from ragvi import judge

    question = {'qid': 'a', 'question': 'Ở đâu?', 'answerable': True, 'gold_doc_id': 'd'}
    paths = [tmp_path / name for name in ('answers.jsonl', 'questions.jsonl', 'corpus.jsonl', 'judgments.jsonl')]
    for path, row in zip(paths, [{**question, 'config': 'closed_book', 'answer': 'Hà Nội'}, question,
                                 {'doc_id': 'd', 'text': 'Hà Nội'}]):
        path.write_text(json.dumps(row) + '\n', encoding='utf-8')

    def load(base, model, max_new_tokens):
        assert base == 'http://127.0.0.1:8080' and model == 'judge' and max_new_tokens >= 512
        return lambda prompt: '{"claims": [{"text": "Hà Nội", "supported_by_gold": true}], "correctness": 2}'

    monkeypatch.setattr('ragvi.generate.load_llamacpp', load)
    judge.main([*map(str, paths), '--model', 'judge', '--llama-url', 'http://127.0.0.1:8080'])
    result = json.loads(paths[-1].read_text(encoding='utf-8'))
    assert result['correctness'] == 2 and result['h_ctx'] is None


def test_wrong_article_citation():
    res = wrong_article_citation('Theo khoản 2 Điều 15 và điều 20 của Luật này, mức phạt là...', ['01/2009/tt-bnn+15'])
    assert res == {'cited_articles': ['15', '20'], 'gold_articles': ['15'], 'wrong_article': True}
    ok = wrong_article_citation('Theo Điều 15 của Thông tư...', ['01/2009/tt-bnn+15'])
    assert ok['wrong_article'] is False
    none_cited = wrong_article_citation('Mức phạt là 500.000 đồng.', ['01/2009/tt-bnn+15'])
    assert none_cited['wrong_article'] is False and none_cited['cited_articles'] == []


def test_parse_and_derive_judge_metrics():
    raw = '<think>...</think>\n```json\n{"claims": [{"text": "a", "supported_by_context": true, "supported_by_gold": false}], "correctness": 1}\n```'
    parsed = parse_judge_json(raw)
    assert derive_judge_metrics(parsed, refused=False) == {'correctness': 1, 'h_gold': 1, 'h_ctx': 0, 'n_claims': 1}
    assert derive_judge_metrics(parsed, refused=False, is_closed_book=True)['h_ctx'] is None
    assert derive_judge_metrics(parsed, refused=True) == {'correctness': 0, 'h_gold': None, 'h_ctx': None, 'n_claims': 0}
    with pytest.raises(ValueError):
        parse_judge_json('{"claims": [], "correctness": 5}')


def test_run_judge_and_human_sheet_and_kappa(tmp_path):
    questions = {
        'q1': {'qid': 'q1', 'question': 'Mức phạt?', 'answerable': True, 'gold_doc_ids': ['doc+15']},
        'q2': {'qid': 'q2', 'question': 'Không có?', 'answerable': False, 'gold_doc_ids': ['doc+99']},
    }
    answers = [
        {'config': 'C3-E3-R0', 'qid': 'q1', 'answerable': True, 'answer': 'Theo Điều 15 là 200k.', 'refused': False},
        {'config': 'closed_book', 'qid': 'q1', 'answerable': True, 'answer': 'Theo Điều 18 là 500k.', 'refused': False},
        {'config': 'C3-E3-R0', 'qid': 'q2', 'answerable': False, 'answer': 'Không tìm thấy thông tin', 'refused': True},
    ]
    out = tmp_path / 'judge.jsonl'
    fake_judge = lambda prompt: json.dumps({
        'claims': [{'text': 'mệnh đề', 'supported_by_context': True, 'supported_by_gold': 'Điều 15 là 200k' in prompt}],
        'correctness': 2 if 'Điều 15 là 200k' in prompt else 0,
    })
    assert run_judge(answers, questions, lambda c, q: 'Ngữ cảnh mẫu', lambda q: 'Điều 15: 200k', out, fake_judge) == 2
    assert run_judge(answers, questions, lambda c, q: 'Ngữ cảnh mẫu', lambda q: 'Điều 15: 200k', out, fake_judge) == 0
    out_batch = tmp_path / 'judge_batch.jsonl'
    assert run_judge(answers, questions, lambda c, q: 'Ngữ cảnh mẫu', lambda q: 'Điều 15: 200k',
                     out_batch, fake_judge, workers=4) == 2
    rows = {(r['config'], r['qid']): r for r in read_rows(out)}
    assert rows[('C3-E3-R0', 'q1')]['h_gold'] == 0 and rows[('C3-E3-R0', 'q1')]['wrong_article'] is False
    assert rows[('closed_book', 'q1')]['h_gold'] == 1 and rows[('closed_book', 'q1')]['wrong_article'] is True
    assert rows[('closed_book', 'q1')]['h_ctx'] is None

    sheet = build_human_sheet(answers, questions, lambda c, q: 'Ngữ cảnh mẫu', lambda q: 'Điều 15: 200k', n=2)
    assert 'C3-E3-R0' not in sheet and 'closed_book::' not in sheet  # ẩn hoàn toàn tên cấu hình ở tiêu đề mẫu
    # Đánh dấu [x] khớp với kết quả judge theo đúng mã ẩn danh của từng mẫu trong phiếu
    blocks = sheet.split('## Mẫu ')
    for i in range(1, len(blocks)):
        if blind_id('C3-E3-R0', 'q1') in blocks[i]:
            blocks[i] = (blocks[i].replace('Correctness: [ ] 0   [ ] 1   [ ] 2', 'Correctness: [ ] 0   [ ] 1   [x] 2')
                                  .replace('H_gold: [ ] 0   [ ] 1', 'H_gold: [x] 0   [ ] 1')
                                  .replace('H_ctx: [ ] 0   [ ] 1   [ ] NA', 'H_ctx: [x] 0   [ ] 1   [ ] NA'))
        else:
            blocks[i] = (blocks[i].replace('Correctness: [ ] 0   [ ] 1   [ ] 2', 'Correctness: [x] 0   [ ] 1   [ ] 2')
                                  .replace('H_gold: [ ] 0   [ ] 1', 'H_gold: [ ] 0   [x] 1')
                                  .replace('H_ctx: [ ] 0   [ ] 1   [ ] NA', 'H_ctx: [ ] 0   [ ] 1   [x] NA'))
    sheet = '## Mẫu '.join(blocks)
    human = parse_human_sheet(sheet)
    res = evaluate_kappa(human, list(rows.values()))
    assert res['n_shared'] == 2 and res['kappa_h_gold'] == pytest.approx(1.0)
    assert res['kappa_correctness_linear'] == pytest.approx(1.0)
    assert cohen_kappa([0, 1, 2, 0], [0, 1, 1, 0], weights='linear') > 0.5
