"""Kiểm tra sinh câu trả lời, cắt token ngữ cảnh, nhận diện từ chối và tóm tắt (không tải LLM)."""
import re

from ragvi.generate import (PROMPT_CB, build_prompt, chunking_of_config, clean_generation, contains_gold_answer,
                            is_refusal, run_generate, select_questions, subset_chunks, summarize_generation,
                            truncate_tokens)
from ragvi.retrieval import read_rows


def fake_tok(text, add_special_tokens=False, return_offsets_mapping=True):
    return {'offset_mapping': [m.span() for m in re.finditer(r'\S+', text)]}


def test_truncate_and_build_prompt():
    cut, was_trunc = truncate_tokens('một hai ba bốn năm', fake_tok, limit=3)
    assert cut == 'một hai ba' and was_trunc
    p_cb, n_cb = build_prompt('Thủ đô là gì?', None)
    assert p_cb == PROMPT_CB.format(question='Thủ đô là gì?') and n_cb == 0
    p_ctx, n_ctx = build_prompt('Câu hỏi?', ['một hai ba bốn', 'ngắn'], tok=fake_tok, limit=2)
    assert '[1] một hai\n[2] ngắn' in p_ctx and n_ctx == 1


def test_clean_and_refusal_and_contains_gold():
    assert clean_generation('<think>\nsuy nghĩ\n</think>\nKhông tìm thấy thông tin.') == 'Không tìm thấy thông tin.'
    assert is_refusal('Không tìm thấy thông tin.')
    assert is_refusal('<think>abc</think> Ngữ cảnh không cung cấp thông tin về vấn đề này.')
    assert not is_refusal('Thủ đô của Việt Nam là Hà Nội.')
    assert contains_gold_answer('Thủ đô của Việt Nam là Hà Nội.', [{'text': 'Hà Nội'}])
    assert not contains_gold_answer('Thủ đô là Huế.', [{'text': 'Hà Nội'}])


def test_run_generate_and_summarize(tmp_path):
    questions = [
        {'qid': 'q1', 'question': 'Thủ đô là gì?', 'answerable': True, 'answers': [{'text': 'Hà Nội'}]},
        {'qid': 'q2', 'question': 'Ai phát minh máy thời gian?', 'answerable': False, 'answers': []},
    ]
    out = tmp_path / 'answers.jsonl'
    gen_fn = lambda prompt: 'Hà Nội' if 'Thủ đô' in prompt else 'Không tìm thấy thông tin'
    assert run_generate('C3-E3-R0', questions, lambda q: ['Đoạn 1'], out, gen_fn, tok=fake_tok, limit=10) == 2
    assert run_generate('C3-E3-R0', questions, lambda q: ['Đoạn 1'], out, gen_fn, tok=fake_tok, limit=10) == 0
    rows = read_rows(out)
    s = summarize_generation(rows, config='C3-E3-R0')
    assert s['correct_refusal'] == 1.0 and s['fabrication'] == 0.0 and s['false_refusal'] == 0.0
    assert s['em'] == 1.0 and s['f1'] == 1.0 and s['contains_gold'] == 1.0
    out_batch = tmp_path / 'answers_batch.jsonl'
    assert run_generate('C3-E3-R0', questions, lambda q: ['Đoạn 1'], out_batch, gen_fn,
                        tok=fake_tok, limit=10, workers=4) == 2
    assert len(read_rows(out_batch)) == 2


def test_select_questions_stratified_50():
    pool = ([{'qid': f'a{i}', 'answerable': True} for i in range(77)] +
            [{'qid': f'u{i}', 'answerable': False} for i in range(23)])
    picked = select_questions(pool, 50)
    assert len(picked) == 50
    assert sum(q['answerable'] for q in picked) == 35
    assert sum(not q['answerable'] for q in picked) == 15


def test_dedup_across_configs_and_subset_chunks(tmp_path):
    assert chunking_of_config('C5_nohead-E3-R0') == 'c5_nohead'
    assert chunking_of_config('C3-E0-R0') == 'c3'
    assert chunking_of_config('closed_book') is None
    corpus = {'01/2020/nđ-cp+1': 'Điều 1. Phạm vi\n1. Khoản một.\n2. Khoản hai.'}
    c5 = subset_chunks(corpus, 'c5', ['01/2020/nđ-cp+1'], tok=fake_tok)
    c5_nh = subset_chunks(corpus, 'c5_nohead', ['01/2020/nđ-cp+1'], tok=fake_tok)
    assert 'Văn bản 01/2020/NĐ-CP' in c5['01/2020/nđ-cp+1#1']
    assert 'Văn bản 01/2020/NĐ-CP' not in c5_nh['01/2020/nđ-cp+1#1']

    questions = [{'qid': 'q1', 'question': 'Thủ đô là gì?', 'answerable': True, 'answers': [{'text': 'Hà Nội'}]}]
    out = tmp_path / 'answers.jsonl'
    calls = []
    def gen_fn(prompt):
        calls.append(prompt)
        return 'Hà Nội'

    assert run_generate('C3-E3-R0', questions, lambda q: (['d#0'], ['Hà Nội là thủ đô.']),
                        out, gen_fn, tok=fake_tok, limit=10) == 1
    assert len(calls) == 1
    # Cấu hình C3-E3-R1 có cùng (chunking='c3', qid='q1', context_ids=['d#0']) -> tái sử dụng câu trả lời, 0 lượt gọi LLM mới
    assert run_generate('C3-E3-R1', questions, lambda q: (['d#0'], ['Hà Nội là thủ đô.']),
                        out, gen_fn, tok=fake_tok, limit=10) == 1
    assert len(calls) == 1
    rows = read_rows(out)
    assert len(rows) == 2 and rows[1]['config'] == 'C3-E3-R1' and rows[1]['seconds'] == 0.0
