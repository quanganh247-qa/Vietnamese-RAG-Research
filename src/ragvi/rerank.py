"""Xếp hạng lại (reranking R1: BAAI/bge-reranker-v2-m3) trên top-20 ứng viên truy xuất.

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.rerank <retrieval.jsonl> <questions.jsonl> <kho_hoặc_chunks> <out.jsonl> [--method hybrid[word]]
"""
import argparse
import json
import time
from pathlib import Path

from ragvi.metrics import METRIC_KEYS, mean_metrics, metrics, viquad_hits, zalo_hits
from ragvi.retrieval import format_table, load_jsonl, open_append, read_rows, summarize, top_k

DEFAULT_RERANKER = 'BAAI/bge-reranker-v2-m3'


def rerank_top(query, candidate_ids, text_of, scorer):
    """Chấm điểm lại danh sách `candidate_ids` bằng `scorer(query, passages)`, giữ nguyên tập ứng viên (Recall@20 bất biến)."""
    if not candidate_ids:
        return []
    passages = [text_of[cid] for cid in candidate_ids]
    scores = scorer(query, passages)
    return [candidate_ids[i] for i in top_k(scores, len(candidate_ids))]


def load_reranker(model_name=DEFAULT_RERANKER, max_length=512, batch_size=0):
    """Nạp CrossEncoder (tự bật bf16/fp16 trên GPU) và trả về hàm `scorer(query, passages) -> danh sách điểm`."""
    from sentence_transformers import CrossEncoder
    from ragvi.retrieval import _auto_batch_size

    bs, dtype = _auto_batch_size(batch_size)
    model = CrossEncoder(model_name, max_length=max_length)
    if dtype is not None and hasattr(model, 'model'):
        model.model.to(dtype=dtype)
    return lambda query, passages: model.predict(
        [(query, p) for p in passages], batch_size=bs, show_progress_bar=False)


def run_rerank(retrieval_rows, questions, gold, text_of, out_path, scorer, method, out_method=None, hit_fn=None):
    """Xếp hạng lại kết quả của `method` trong `retrieval_rows`, ghi nối tiếp vào `out_path`."""
    out_method = out_method or f'{method}+r1'
    candidates = {r['qid']: r['top'] for r in retrieval_rows if r.get('method') == method and 'top' in r}
    done = {(r['method'], r['qid']) for r in read_rows(out_path)}
    written = 0
    with open_append(out_path) as f:
        for qid, question in questions.items():
            if (out_method, qid) in done or qid not in candidates:
                continue
            t0 = time.perf_counter()
            top = rerank_top(question, candidates[qid], text_of, scorer)
            elapsed = time.perf_counter() - t0
            if gold[qid] is None:
                scores = dict.fromkeys(METRIC_KEYS)
            elif hit_fn is not None:
                scores = hit_fn(qid, top)
            else:
                scores = metrics(zalo_hits(top, gold[qid]), len(gold[qid]))
            row = {'method': out_method, 'qid': qid, **scores, 'top': top, 'seconds': round(elapsed, 4)}
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
            f.flush()
            written += 1
    return written


def load_units(path):
    """Đọc văn bản và ánh xạ (parent_of, span_of) từ kho Zalo, corpus.jsonl ViQuAD, hoặc file đệm chunks/*.jsonl."""
    p = Path(path)
    if p.is_file() and p.name.endswith('.jsonl'):
        rows = load_jsonl(p)
        if rows and isinstance(rows[0], list):  # [chunk_id, doc_id, start, end, text]
            return ({r[0]: r[4] for r in rows},
                    {r[0]: r[1] for r in rows},
                    {r[0]: (r[1], r[2], r[3]) for r in rows})
        return ({r['doc_id']: r['text'] for r in rows},
                {r['doc_id']: r['doc_id'] for r in rows},
                {r['doc_id']: (r['doc_id'], 0, len(r['text'])) for r in rows})
    from ragvi.data import load_zalo_corpus

    corpus = load_zalo_corpus(p)
    return corpus, {d: d for d in corpus}, {d: (d, 0, len(t)) for d, t in corpus.items()}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('retrieval_path', help='file retrieval_*.jsonl chứa top-20 ứng viên')
    parser.add_argument('questions_path', help='dev.jsonl hoặc test.jsonl')
    parser.add_argument('units_path', help='thư mục zalo_legal, corpus.jsonl ViQuAD, hoặc chunks/*.jsonl')
    parser.add_argument('out_path', help='file JSONL đầu ra (có thể trùng retrieval_path)')
    parser.add_argument('--method', default='dense', help='nhãn phương pháp đầu vào (có thể phân tách bằng dấu phẩy)')
    parser.add_argument('--out-method', help='nhãn phương pháp đầu ra (mặc định: <method>+r1)')
    parser.add_argument('--model', default=DEFAULT_RERANKER)
    parser.add_argument('--batch-size', type=int, default=0)
    args = parser.parse_args(argv)

    q_rows = load_jsonl(args.questions_path)
    questions = {q['qid']: q['question'] for q in q_rows}
    is_viquad = any('gold_doc_id' in q for q in q_rows)
    gold = {q['qid']: (set(q['gold_doc_ids']) if 'gold_doc_ids' in q else {q['gold_doc_id']})
            if q['answerable'] else None for q in q_rows}
    answers_of = {q['qid']: q.get('answers') or [] for q in q_rows}
    text_of, parent_of, span_of = load_units(args.units_path)
    ret_rows = read_rows(args.retrieval_path)

    methods = [m.strip() for m in args.method.split(',') if m.strip()]
    out_methods = [args.out_method if (args.out_method and len(methods) == 1) else f'{m}+r1' for m in methods]
    done = {(r['method'], r['qid']) for r in read_rows(args.out_path)}
    need = any((om, q) not in done for om in out_methods for q in questions)
    scorer = load_reranker(args.model, batch_size=args.batch_size) if need else (lambda q, ps: [])

    def hit_fn(qid, top):
        if is_viquad:
            return metrics(viquad_hits([span_of[c] for c in top], next(iter(gold[qid])), answers_of[qid]), 1)
        return metrics(zalo_hits([parent_of[c] for c in top], gold[qid]), len(gold[qid]))

    for m, om in zip(methods, out_methods):
        written = run_rerank(ret_rows, questions, gold, text_of, args.out_path, scorer,
                             m, out_method=om, hit_fn=hit_fn)
        print(f'Ghi thêm {written} dòng ({om}) vào {args.out_path}')
    base_table = summarize(args.retrieval_path, methods)
    rerank_table = summarize(args.out_path, out_methods)
    print(format_table({**base_table, **rerank_table}))


if __name__ == '__main__':
    main()
