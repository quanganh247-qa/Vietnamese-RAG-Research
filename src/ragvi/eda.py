"""Đếm token và gom câu hỏi gần nhau về mặt câu chữ cho notebook EDA."""
from collections import defaultdict
from itertools import islice
import unicodedata


def token_lengths(texts, tokenizer, batch_size=32):
    """Đếm token theo thứ tự dòng, không cắt và không thêm token đặc biệt."""
    texts = iter(texts)
    lengths = []
    while batch := list(islice(texts, batch_size)):
        lengths.extend(len(encoding.ids) for encoding in tokenizer.encode_batch(batch, add_special_tokens=False))
    return lengths


def wording_groups(questions, threshold=0.60):
    """Nhóm chỉ số câu hỏi nối với nhau bởi cosine TF-IDF ký tự đủ cao."""
    from scipy.sparse.csgraph import connected_components
    from sklearn.feature_extraction.text import TfidfVectorizer

    normalized = [' '.join(unicodedata.normalize('NFC', q).casefold().split()) for q in questions]
    eligible = [(i, q) for i, q in enumerate(normalized) if len(q) >= 3]
    if len(eligible) < 2:
        return []
    vectors = TfidfVectorizer(analyzer='char', ngram_range=(3, 5)).fit_transform(q for _, q in eligible)
    # shortcut: ma trận cặp chỉ dùng cho dev nhỏ; dùng tìm láng giềng khi mở rộng toàn kho.
    neighbors = (vectors @ vectors.T).tocsr()
    neighbors.data[neighbors.data < threshold] = 0
    neighbors.eliminate_zeros()
    _, labels = connected_components(neighbors, directed=False)
    groups = defaultdict(list)
    for (i, _), label in zip(eligible, labels):
        groups[label].append(i)
    return sorted((group for group in groups.values() if len(group) > 1), key=lambda group: (-len(group), group[0]))
