import json

import pytest

from ragvi.benchmark import end_to_end_summary, retrieval_summary, viquad_source_questions, verify_frozen


def test_source_questions_keep_all_splits_and_never_use_unlabeled_test_as_gold():
    base = {'id': '1', 'title': 'A', 'context': 'Đáp án', 'question': 'Gì?',
            'is_impossible': False, 'answers': {'text': ['Đáp'], 'answer_start': [0]}}
    source = [{**base, 'split': 'train'}, {**base, 'split': 'validation', 'answers': None},
              {**base, 'split': 'test', 'is_impossible': True}]
    questions = viquad_source_questions(source)
    assert {q['qid']: q['answerable'] for q in questions} == {
        'train:1': True, 'validation:1': None, 'test:1': None,
    }


def test_verify_frozen_hashes(tmp_path):
    (tmp_path / 'dev.jsonl').write_bytes(b'')
    (tmp_path / 'manifest.json').write_text(json.dumps({'sha256': {'dev.jsonl': 'bad'}}), encoding='utf-8')
    with pytest.raises(ValueError, match='dev.jsonl'):
        verify_frozen(tmp_path, ('dev.jsonl',))


def test_retrieval_summary_counts_measurements_and_keeps_null_metrics():
    questions = [{'qid': 'a', 'answerable': True}, {'qid': 'b', 'answerable': None}]
    score = dict.fromkeys(('r5', 'r20', 'mrr10', 'ndcg5'), 1.0)
    rows = [{'qid': 'a', **score}, {'qid': 'b', **dict.fromkeys(score)}]
    assert retrieval_summary(rows, questions) == {'n': 2, 'n_scored': 1, **score}
    assert retrieval_summary(rows[1:], questions[1:])['r5'] is None
    with pytest.raises(ValueError):
        retrieval_summary(rows[:-1], questions)


def test_rah_uses_only_judged_non_refused_pairs_and_reports_errors():
    configs = ('closed_book', 'oracle', 'C3-E3-R0')
    questions = [{'qid': qid, 'answerable': qid != 'd'} for qid in 'abcd']
    answers = [{'config': config, **q, 'refused': config == 'oracle' and q['qid'] == 'b', 'seconds': 1.5}
               for config in configs for q in questions if config != 'oracle' or q['answerable']]
    judgments = [{'config': a['config'], 'qid': a['qid'], 'correctness': 0 if a['refused'] else 2,
                  'h_gold': None if a['refused'] else int(a['config'] != 'oracle'),
                  'h_ctx': None, 'error': 'bad JSON' if a['qid'] == 'c' else None}
                 for a in answers if a['answerable']]
    summary = end_to_end_summary(questions, answers, judgments)
    assert summary['rah_against_oracle'] == {'n_pairs': 1, 'value': 1.0}
    anchor = summary['configs']['C3-E3-R0']
    assert anchor['correctness'] == 2.0 and anchor['n_correctness'] == 2
    assert anchor['n_judge_errors'] == 1 and anchor['n_judge_missing'] == 0
    assert anchor['fabrication'] == 1.0 and anchor['p50_seconds'] == 1.5
    assert summary['configs']['oracle']['fabrication'] is None
    with pytest.raises(ValueError):
        end_to_end_summary(questions, answers[:-1], judgments)
