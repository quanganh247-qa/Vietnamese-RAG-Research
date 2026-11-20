import pytest

import ragvi
from pathlib import Path


def test_token_counts_are_per_row_without_special_tokens():
    pytest.importorskip('tokenizers')
    from tokenizers import Tokenizer, models, pre_tokenizers

    assert (Path(ragvi.__file__).parent / 'eda.py').is_file(), 'Thiếu mô-đun EDA'
    from ragvi.eda import token_lengths

    tokenizer = Tokenizer(models.WordLevel({'Hà': 0, 'Nội': 1, '[UNK]': 2}, unk_token='[UNK]'))
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
    assert token_lengths(['Hà Nội', '', 'Hà'], tokenizer, batch_size=2) == [2, 0, 1]


def test_wording_groups_keep_similar_questions_without_unrelated_rows():
    pytest.importorskip('sklearn')
    assert (Path(ragvi.__file__).parent / 'eda.py').is_file(), 'Thiếu mô-đun EDA'
    from ragvi.eda import wording_groups

    questions = ['Mức hưởng bảo hiểm xã hội là bao nhiêu?', 'Mức hưởng bảo hiểm xã hội là bao nhiêu',
                 'Kinh đô của nhà Hồ ở đâu?', '   ']
    assert wording_groups(questions) == [[0, 1]]
    assert wording_groups(['  ']) == []
