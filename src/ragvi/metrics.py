"""Chỉ số truy xuất (Recall@5, Recall@20, MRR@10, nDCG@5) và độ đúng ViQuAD (EM, token-F1 theo âm tiết; D2)."""
from collections import Counter
import math
import re

METRIC_KEYS = ('r5', 'r20', 'mrr10', 'ndcg5')


def normalize_answer(text):
    """Chuẩn hóa câu trả lời theo âm tiết: chữ thường, bỏ dấu câu, gộp khoảng trắng."""
    return ' '.join(re.findall(r'\w+', (text or '').lower()))


def em_f1(prediction, gold_texts):
    """EM và token-F1 theo âm tiết trên tập đáp án vàng (lấy giá trị lớn nhất qua các đáp án vàng; D2)."""
    if not gold_texts:
        return {'em': None, 'f1': None}
    pred_norm = normalize_answer(prediction)
    pred_toks = pred_norm.split()
    best_em, best_f1 = 0.0, 0.0
    for gold in gold_texts:
        gold_norm = normalize_answer(gold['text'] if isinstance(gold, dict) else gold)
        gold_toks = gold_norm.split()
        best_em = max(best_em, float(pred_norm == gold_norm))
        if not pred_toks or not gold_toks:
            best_f1 = max(best_f1, float(pred_toks == gold_toks))
            continue
        common = sum((Counter(pred_toks) & Counter(gold_toks)).values())
        if common:
            best_f1 = max(best_f1, 2 * common / (len(pred_toks) + len(gold_toks)))
    return {'em': best_em, 'f1': best_f1}


def metrics(hits, n_rel):
    """hits: danh sách True/False theo thứ hạng, mỗi tài liệu vàng chỉ True một lần."""
    dcg = sum(h / math.log2(i + 2) for i, h in enumerate(hits[:5]))
    idcg = sum(1 / math.log2(i + 2) for i in range(min(n_rel, 5)))
    return {'r5': sum(hits[:5]) / n_rel, 'r20': sum(hits[:20]) / n_rel,
            'mrr10': next((1 / (i + 1) for i, h in enumerate(hits[:10]) if h), 0.0),
            'ndcg5': dcg / idcg}


def zalo_hits(ranked_doc_ids, gold):
    """Mỗi điều luật vàng chỉ tính một lần, ở lần xuất hiện đầu tiên trong danh sách xếp hạng."""
    seen, hits = set(), []
    for d in ranked_doc_ids:
        hits.append(d in gold and d not in seen)
        seen.add(d)
    return hits


def viquad_hits(ranked_chunks, gold_doc_id, answers, min_cover=0.8):
    """Tiêu chí D2 cho ViQuAD; ranked_chunks là [(doc_id, start, end)] theo thứ hạng.

    Chunk đúng khi thuộc gold_doc_id và phủ ít nhất `min_cover` số ký tự của ít nhất một đáp án vàng
    (answers: [{'start', 'end', ...}] như trong tập đánh giá). n_rel = 1: chỉ lần trúng đầu tiên là True.
    """
    found, hits = False, []
    for doc_id, start, end in ranked_chunks:
        ok = not found and doc_id == gold_doc_id and any(
            min(end, a['end']) - max(start, a['start']) >= min_cover * (a['end'] - a['start']) for a in answers)
        hits.append(ok)
        found |= ok
    return hits


def mean_metrics(rows):
    """Trung bình từng chỉ số trên nhiều truy vấn; rows là các dict có đủ khóa METRIC_KEYS."""
    rows = list(rows)
    if not rows:
        raise ValueError('Không có truy vấn nào để lấy trung bình.')
    return {k: sum(r[k] for r in rows) / len(rows) for k in METRIC_KEYS}
