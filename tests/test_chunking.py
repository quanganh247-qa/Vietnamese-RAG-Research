"""Kiểm tra phân đoạn bằng tokenizer giả và hàm tách câu giả (không tải mô hình)."""
import re

from ragvi.chunking import (chunk_document, chunk_fixed, chunk_sentence, chunk_stats, chunk_struct,
                            clause_rate, review_sheet)


def tok(text, add_special_tokens=False, return_offsets_mapping=True):
    """Tokenizer giả: mỗi cụm không chứa khoảng trắng là một token."""
    return {'offset_mapping': [m.span() for m in re.finditer(r'\S+', text)]}


def sent_split(text):
    return re.split(r'(?<=\.)\s+', text)


def ntok(text):
    return len(text.split())


def check_cover(chunks, text):
    """Chunk là lát cắt nguyên văn, không chồng lấn và phủ hết mọi ký tự khác khoảng trắng."""
    assert all(c[4] == text[c[2]:c[3]] for c in chunks)
    assert all(a[3] <= b[2] for a, b in zip(chunks, chunks[1:]))
    assert ''.join(''.join(c[4].split()) for c in chunks) == ''.join(text.split())
    assert [c[0] for c in chunks] == [f'd#{i}' for i in range(len(chunks))]


TEXT = 'Một hai ba bốn.  Năm sáu.\nBảy tám chín mười mười_một mười_hai mười_ba.\n\nMười_bốn mười_lăm.'


def test_fixed_covers_without_overlap():
    chunks = chunk_fixed('d', TEXT, tok, size=4)
    check_cover(chunks, TEXT)
    assert [ntok(c[4]) for c in chunks] == [4, 4, 4, 3]
    assert chunk_fixed('d', '', tok) == []


def test_sentence_merges_and_covers():
    chunks = chunk_sentence('d', TEXT, tok, size=6, sent_split=sent_split)
    check_cover(chunks, TEXT)
    # câu 1 + câu 2 = 6 token gộp lại; câu 3 dài 7 token rơi về C1 (6 + 1); câu 4 đứng riêng
    assert [c[4] for c in chunks] == ['Một hai ba bốn.  Năm sáu.', 'Bảy tám chín mười mười_một mười_hai',
                                      'mười_ba.', 'Mười_bốn mười_lăm.']


def test_sentence_too_long_falls_back_to_fixed():
    text = ' '.join(f't{i}' for i in range(10)) + '.'
    assert chunk_sentence('d', text, tok, size=4, sent_split=sent_split) == chunk_fixed('d', text, tok, size=4)


def test_sentence_keeps_text_the_splitter_changed_or_dropped():
    # hàm tách câu gộp khoảng trắng và bỏ sót phần cuối: chunk vẫn phải phủ hết văn bản gốc
    chunks = chunk_sentence('d', TEXT, tok, size=6, sent_split=lambda t: [' '.join(s.split()) for s in sent_split(t)][:2])
    check_cover(chunks, TEXT)


def test_document_is_one_chunk():
    assert chunk_document('d', TEXT) == [('d#0', 'd', 0, len(TEXT), TEXT)]


DOC_ID = '01/2009/tt-bnn+1'
TITLE = 'Điều 1. Phạm vi áp dụng'
BODY = ('Thông tư này quy định như sau:\n'
        '1. Khoản một rất ngắn.\n'
        '2. Khoản hai gồm các trường hợp sau:\n'
        'a) trường hợp thứ nhất của khoản hai;\n'
        'b) trường hợp thứ hai của khoản hai.')
HEAD = 'Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng'


def test_struct_two_clauses():
    chunks = chunk_struct(DOC_ID, TITLE, BODY, tok, size=30, sent_split=sent_split)
    assert [c[4] for c in chunks] == [
        'Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng\nThông tư này quy định như sau:',
        HEAD + ', Khoản 1: 1. Khoản một rất ngắn.',
        HEAD + ', Khoản 2: 2. Khoản hai gồm các trường hợp sau:\n'
               'a) trường hợp thứ nhất của khoản hai;\nb) trường hợp thứ hai của khoản hai.',
    ]


def test_struct_long_clause_splits_by_point_and_nohead_shares_boundaries():
    text = TITLE + '\n' + BODY
    chunks = chunk_struct(DOC_ID, TITLE, BODY, tok, size=13, sent_split=sent_split)
    assert len(chunks) == 5  # mở đầu, khoản 1, phần dẫn khoản 2, điểm a, điểm b
    assert [c[4] for c in chunks[2:]] == [
        HEAD + ', Khoản 2: 2. Khoản hai gồm các trường hợp sau:',
        HEAD + ', Khoản 2, Điểm a: a) trường hợp thứ nhất của khoản hai;',
        HEAD + ', Khoản 2, Điểm b: b) trường hợp thứ hai của khoản hai.',
    ]
    assert all(c[4].endswith(text[c[2]:c[3]]) and c[1] == DOC_ID for c in chunks)

    plain = chunk_struct(DOC_ID, TITLE, BODY, tok, size=13, heading=False, sent_split=sent_split)
    assert [c[:4] for c in plain] == [c[:4] for c in chunks]
    assert all(c[4] == text[c[2]:c[3]] for c in plain)
    assert all(a[3] <= b[2] for a, b in zip(plain, plain[1:]))
    assert ''.join(''.join(c[4].split()) for c in plain) == ''.join(text.split())


def test_struct_without_clause_matches_document_chunk():
    body = 'Thông tư này có hiệu lực từ ngày ký.'
    text = TITLE + '\n' + body
    assert chunk_struct(DOC_ID, TITLE, body, tok, heading=False) == chunk_document(DOC_ID, text)
    assert chunk_struct(DOC_ID, TITLE, body, tok)[0][4] == 'Văn bản 01/2009/TT-BNN, ' + text
    # không có khoản nhưng dài: cắt bằng C3, mảnh sau mang tiêu đề Điều
    long = chunk_struct(DOC_ID, TITLE, body + ' Câu thứ hai dài hơn một chút.', tok, size=15, sent_split=sent_split)
    assert [c[4] for c in long] == ['Văn bản 01/2009/TT-BNN, ' + text, HEAD + ': Câu thứ hai dài hơn một chút.']


def test_stats_and_clause_rate():
    stats = chunk_stats(chunk_fixed('d', TEXT, tok, size=4), tok)
    assert stats == {'n_chunks': 4, 'tok_mean': 3.75, 'tok_median': 4, 'tok_p95': 4, 'tok_max': 4, 'over_512': 0.0}
    long = ' '.join(['x'] * 513)
    assert chunk_stats(iter([('a', 'd', 0, 0, long), ('b', 'd', 0, 0, 'x')]), tok)['over_512'] == 0.5
    assert clause_rate([BODY, 'Không có khoản nào.', 'a) chỉ có điểm']) == 1 / 3


def test_fixed_no_overlap_with_xlmr_lone_underscore_token():
    # bge-m3 tách "ab ỦY" thành "▁ab" (0,2), "▁" (3,4), "ỦY" (3,5): hai token cùng bắt đầu ở 3
    xlmr = lambda text, **kw: {'offset_mapping': [(0, 2), (3, 4), (3, 5)]}
    chunks = chunk_fixed('d', 'ab ỦY', xlmr, size=2)
    assert [c[2:4] for c in chunks] == [(0, 3), (3, 5)]


def test_struct_keeps_title_when_body_starts_with_clause():
    body = '1. Khoản một.\n2. Khoản hai.'
    plain = chunk_struct(DOC_ID, TITLE, body, tok, heading=False)
    assert ''.join(''.join(c[4].split()) for c in plain) == ''.join((TITLE + body).split())
    assert plain[0][4] == TITLE


def test_review_sheet_lists_sampled_articles_and_their_chunks():
    docs = {f'01/2009/tt-bnn+{i}': f'Điều {i}. Tên\n' + BODY for i in range(5)}
    titles = {d: t.split('\n')[0] for d, t in docs.items()}
    md = review_sheet(docs, titles, n=3, seed=0, tok=tok, size=30, sent_split=sent_split, max_chars=40)
    assert md == review_sheet(docs, titles, n=3, seed=0, tok=tok, size=30, sent_split=sent_split, max_chars=40)
    assert md.count('## ') == 3 and md.count('[ ] khoản nhận nhầm') == 3 and 'ĐÃ CẮT' in md
    assert '**Văn bản 01/2009/TT-BNN, Điều' in md and ', Khoản 2:**' in md
