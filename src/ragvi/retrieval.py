"""Truy xuất BM25, dense và hybrid ở mức tài liệu: điều luật Zalo hoặc đoạn ViQuAD.

Chạy trên Colab, từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.retrieval <processed>/zalo_legal <thư mục đầu ra> --methods bm25,dense,hybrid
    PYTHONPATH=src python -m ragvi.retrieval <processed>/zalo_legal <thư mục đầu ra> --methods bm25 --tokenizer word
    PYTHONPATH=src python -m ragvi.retrieval <processed>/zalo_legal <thư mục đầu ra> --run zalo_test \\
        --questions <eval>/zalo/test.jsonl --removed <eval>/zalo/removed_doc_ids.json
    PYTHONPATH=src python -m ragvi.retrieval <eval>/viquad/corpus.jsonl <thư mục đầu ra> --run viquad_test \\
        --questions <eval>/viquad/test.jsonl
"""
import argparse
import json
import math
import random
import re
import time
from pathlib import Path

import numpy as np

from ragvi.metrics import METRIC_KEYS, mean_metrics, metrics, viquad_hits, zalo_hits

DEFAULT_MODEL = 'BAAI/bge-m3'
# alpha nhân với dense, min–max theo từng truy vấn trên cả kho: chốt 14/11 theo Nguyen & Quan
# (Findings of EACL 2026) và mã ViRE của họ; xem Nhật ký thay đổi trong reports/quyet-dinh-thiet-ke.md.
ALPHA = 0.7
TOP_K = 20


def model_prefixes(model_name):
    """Tiền tố (query_prefix, passage_prefix); dòng multilingual-e5 yêu cầu 'query: ' và 'passage: ' (D7)."""
    return ('query: ', 'passage: ') if 'e5' in model_name.lower() else ('', '')


def cached_chunks(docs, chunking, path, titles=None, tokenizer_name=DEFAULT_MODEL):
    """Dựng hoặc đọc đệm danh sách chunk [(chunk_id, doc_id, start, end, text)] tại `path`."""
    rows = read_rows(path)
    if rows and {r[1] for r in rows} == set(docs):
        return [tuple(r) for r in rows]
    if chunking == 'c5_nohead':
        c5_rows = read_rows(Path(path).with_name(Path(path).name.replace('__c5_nohead.', '__c5.')))
        if c5_rows and {r[1] for r in c5_rows} == set(docs):
            out = [(r[0], r[1], r[2], r[3], docs[r[1]][r[2]:r[3]]) for r in c5_rows]
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            Path(path).write_text(''.join(json.dumps(list(c), ensure_ascii=False) + '\n' for c in out), encoding='utf-8')
            return out

    from transformers import AutoTokenizer
    from ragvi.chunking import chunk_document, chunk_fixed, chunk_sentence, chunk_struct

    tok = None if chunking == 'c4' else AutoTokenizer.from_pretrained(tokenizer_name)
    out = []
    for d, text in docs.items():
        if chunking == 'c1':
            out += chunk_fixed(d, text, tok)
        elif chunking == 'c3':
            out += chunk_sentence(d, text, tok)
        elif chunking == 'c4':
            out += chunk_document(d, text)
        elif chunking in ('c5', 'c5_nohead'):
            title = titles[d] if titles else text.split('\n', 1)[0]
            body = text[len(title) + 1:] if text.startswith(title + '\n') else ''
            out += chunk_struct(d, title, body, tok, heading=(chunking == 'c5'))
        else:
            raise ValueError(f'Cách phân đoạn không hợp lệ: {chunking}')
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(''.join(json.dumps(list(c), ensure_ascii=False) + '\n' for c in out), encoding='utf-8')
    return out


# ---------- BM25 ----------

def tokenize_syllables(text):
    """Tách theo âm tiết: chữ thường, cắt ở khoảng trắng và dấu câu."""
    return re.findall(r'\w+', text.lower())


def tokenize_words(text):
    """Tách từ bằng underthesea: chữ thường, bỏ token chỉ có dấu câu, nối âm tiết trong một từ bằng '_'."""
    from underthesea import word_tokenize

    return [re.sub(r'\s+', '_', w.lower()) for w in word_tokenize(text) if re.search(r'\w', w)]


def cached_tokens(doc_ids, texts, path, tokenize=tokenize_words):
    """Token của từng tài liệu, đệm ra JSONL `[doc_id, "tok tok ..."]` theo doc_id.

    Ghi nối tiếp từng tài liệu: lượt chạy bị ngắt thì chạy lại chỉ tách phần còn thiếu;
    kho thu hẹp dùng lại đúng các dòng của kho đầy đủ.
    """
    cache = dict(read_rows(path))
    missing = [(d, t) for d, t in zip(doc_ids, texts) if d not in cache]
    if missing:
        start = time.perf_counter()
        with open_append(path) as f:
            if tokenize is tokenize_words and len(missing) >= 200:
                from concurrent.futures import ProcessPoolExecutor
                import os

                workers = min(os.cpu_count() or 2, 12)
                with ProcessPoolExecutor(max_workers=workers) as ex:
                    for (d, _), toks in zip(missing, ex.map(tokenize_words, [t for _, t in missing], chunksize=256)):
                        cache[d] = ' '.join(toks)
                        f.write(json.dumps([d, cache[d]], ensure_ascii=False) + '\n')
            else:
                for d, t in missing:
                    cache[d] = ' '.join(tokenize(t))
                    f.write(json.dumps([d, cache[d]], ensure_ascii=False) + '\n')
        print(f'Đã tách từ {len(missing)} tài liệu trong {time.perf_counter() - start:.1f} giây, đệm tại {path}')
    return [cache[d].split() for d in doc_ids]


class _FastBM25Okapi:
    """BM25Okapi dùng chỉ mục đảo nén cột (CSC) bằng NumPy thuần, khớp tuyệt đối với rank_bm25.BM25Okapi."""

    def __init__(self, corpus, k1=1.5, b=0.75, epsilon=0.25):
        from collections import Counter

        self.corpus_size = len(corpus)
        self.k1 = k1
        self.b = b
        self.epsilon = epsilon
        self.vocab = {}
        doc_len = np.zeros(self.corpus_size, dtype=np.float64)
        df = Counter()
        rows, cols, tfs = [], [], []
        for i, doc in enumerate(corpus):
            doc_len[i] = len(doc)
            if not doc:
                continue
            counts = Counter(doc)
            for term, freq in counts.items():
                cid = self.vocab.get(term)
                if cid is None:
                    cid = len(self.vocab)
                    self.vocab[term] = cid
                df[cid] += 1
                rows.append(i)
                cols.append(cid)
                tfs.append(freq)
        self.avgdl = float(doc_len.mean()) if self.corpus_size else 0.0
        n_terms = len(self.vocab)
        if n_terms == 0 or not rows:
            self.indptr = np.zeros(n_terms + 1, dtype=np.int64)
            self.indices = np.zeros(0, dtype=np.int32)
            self.data = np.zeros(0, dtype=np.float64)
            return
        idf = np.empty(n_terms, dtype=np.float64)
        neg_ids = []
        idf_sum = 0.0
        for cid, freq in df.items():
            val = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)
            idf[cid] = val
            idf_sum += val
            if val < 0:
                neg_ids.append(cid)
        avg_idf = idf_sum / n_terms
        if neg_ids:
            idf[neg_ids] = epsilon * avg_idf
        rows_arr = np.asarray(rows, dtype=np.int32)
        cols_arr = np.asarray(cols, dtype=np.int32)
        tfs_arr = np.asarray(tfs, dtype=np.float64)
        denom = tfs_arr + k1 * (1.0 - b + b * doc_len[rows_arr] / self.avgdl)
        weights = idf[cols_arr] * (tfs_arr * (k1 + 1.0) / denom)
        order = np.argsort(cols_arr, kind='stable')
        self.indices = rows_arr[order]
        self.data = weights[order]
        counts = np.bincount(cols_arr, minlength=n_terms)
        self.indptr = np.empty(n_terms + 1, dtype=np.int64)
        self.indptr[0] = 0
        np.cumsum(counts, out=self.indptr[1:])

    def get_scores(self, query):
        score = np.zeros(self.corpus_size, dtype=np.float64)
        for q in query:
            col = self.vocab.get(q)
            if col is not None:
                s, e = self.indptr[col], self.indptr[col + 1]
                score[self.indices[s:e]] += self.data[s:e]
        return score


def build_bm25(texts, tokenize=tokenize_syllables):
    """Dựng chỉ mục BM25Okapi ma trận thưa; đổi `tokenize` thành underthesea.word_tokenize để tách từ."""
    return _FastBM25Okapi([tokenize(t) for t in texts])


def bm25_scores(index, query, tokenize=tokenize_syllables):
    """Vector điểm BM25 của một truy vấn trên cả kho; `tokenize` phải trùng với lúc dựng chỉ mục."""
    return index.get_scores(tokenize(query))


def time_word_tokenize(texts, sample=500, seed=0, limit_minutes=30):
    """Đo underthesea.word_tokenize trên `sample` tài liệu ngẫu nhiên, ước lượng cho cả kho.

    Quy tắc của kế hoạch: dưới 30 phút thì E0 dùng underthesea, ngược lại dùng âm tiết.
    """
    from underthesea import word_tokenize

    picked = random.Random(seed).sample(list(texts), min(sample, len(texts)))
    start = time.perf_counter()
    for text in picked:
        word_tokenize(text)
    seconds = time.perf_counter() - start
    # Ước lượng theo số ký tự, vì độ dài điều luật lệch rất mạnh (có điều dài ~250 nghìn ký tự).
    minutes = seconds / max(sum(map(len, picked)), 1) * sum(map(len, texts)) / 60
    return {'sample_docs': len(picked), 'sample_seconds': seconds, 'docs_per_second': len(picked) / seconds,
            'estimated_minutes': minutes, 'use_underthesea': minutes < limit_minutes}


# ---------- Dense ----------

def embedding_cache_path(cache_dir, dataset, chunking, model_name=DEFAULT_MODEL):
    """Đường dẫn file đệm theo khóa (bộ dữ liệu, cách phân đoạn, mô hình)."""
    return Path(cache_dir) / f'{dataset}__{chunking}__{model_name.replace("/", "_")}.npy'


CHECKPOINT_EVERY = 20_000


def _auto_batch_size(batch_size):
    """Tự chọn batch_size và dtype (bf16 trên A100/L4, fp16 trên T4) theo VRAM GPU; nếu `batch_size > 0` thì giữ nguyên."""
    try:
        import torch
    except ImportError:
        return batch_size or 32, None
    if not torch.cuda.is_available():
        return batch_size or 32, None
    vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    if batch_size and batch_size > 0:
        return batch_size, dtype
    auto_bs = 512 if vram_gb >= 36 else 256 if vram_gb >= 20 else 64 if vram_gb >= 12 else 32
    return auto_bs, dtype


def _encode_with_oom_backoff(encode_fn, batch, batch_size):
    """Gọi `encode_fn(batch, batch_size)` và tự giảm nửa `batch_size` nếu gặp CUDA OutOfMemoryError."""
    bs = batch_size
    while True:
        try:
            return encode_fn(batch, bs)
        except RuntimeError as e:
            if 'out of memory' not in str(e).lower() or bs <= 8:
                raise
            bs = max(bs // 2, 8)
            try:
                import torch
                torch.cuda.empty_cache()
            except ImportError:
                pass
            print(f'Hết VRAM ở batch_size={bs * 2}, tự giảm xuống batch_size={bs} và chạy lại block...')


def embed(texts, cache_path=None, model_name=DEFAULT_MODEL, batch_size=0, prefix='',
          checkpoint_every=CHECKPOINT_EVERY, encode_fn=None):
    """Nhúng danh sách văn bản thành ma trận float32 chuẩn hóa L2; hỗ trợ checkpoint/resume theo block và fp16/bf16.

    - Nếu `cache_path` đã tồn tại: đọc trực tiếp (tương thích mọi file `.npy` đã lưu từ trước).
    - Nếu `cache_path` được truyền và `len(texts) > checkpoint_every`: lưu từng block `checkpoint_every` văn bản
      vào thư mục `<cache_path>.parts/` để có thể resume khi ngắt phiên hoặc đổi GPU (T4/L4/A100).
    - `batch_size=0` (mặc định): tự chọn theo VRAM GPU (T4=128, L4=256, A100=512).
    """
    cache_path = Path(cache_path) if cache_path is not None else None
    if cache_path is not None and cache_path.exists():
        cached = np.load(cache_path)
        if len(cached) != len(texts):
            raise ValueError(f'File đệm {cache_path} có {len(cached)} dòng nhưng kho có {len(texts)} văn bản; '
                             'hãy xóa file đệm hoặc đổi khóa.')
        return cached

    inputs = [prefix + t for t in texts] if prefix else list(texts)
    bs, dtype = _auto_batch_size(batch_size)

    def _get_encoder():
        if encode_fn is not None:
            return encode_fn
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(model_name)
        model.max_seq_length = 512
        if dtype is not None:
            model.to(dtype=dtype)
            print(f'Đang nhúng trên GPU với dtype={dtype}, batch_size={bs} ({model_name})')
        return lambda batch, cur_bs: model.encode(
            batch, batch_size=cur_bs, normalize_embeddings=True,
            convert_to_numpy=True, show_progress_bar=True).astype(np.float32)

    encoder = None
    start_t = time.perf_counter()

    if cache_path is not None and len(inputs) > checkpoint_every:
        part_dir = cache_path.with_suffix('.parts')
        part_dir.mkdir(parents=True, exist_ok=True)
        shards = []
        for i in range(0, len(inputs), checkpoint_every):
            end = min(i + checkpoint_every, len(inputs))
            shard = part_dir / f'{i:07d}_{end:07d}.npy'
            if shard.exists():
                arr = np.load(shard)
                if len(arr) == end - i:
                    shards.append(arr)
                    continue
            if encoder is None:
                encoder = _get_encoder()
            t0 = time.perf_counter()
            arr = _encode_with_oom_backoff(encoder, inputs[i:end], bs).astype(np.float32)
            tmp = shard.with_suffix('.tmp.npy')
            np.save(tmp, arr)
            tmp.replace(shard)
            shards.append(arr)
            dt = time.perf_counter() - t0
            print(f'[Checkpoint {end}/{len(inputs)}] Lưu {shard.name} ({(end - i) / max(dt, 1e-6):.1f} văn bản/giây)')
        vectors = np.concatenate(shards, axis=0)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_final = cache_path.with_suffix('.tmp.npy')
        np.save(tmp_final, vectors)
        tmp_final.replace(cache_path)
        for p in part_dir.glob('*.npy'):
            p.unlink(missing_ok=True)
        try:
            part_dir.rmdir()
        except OSError:
            pass
    else:
        encoder = _get_encoder()
        vectors = _encode_with_oom_backoff(encoder, inputs, bs).astype(np.float32)
        if cache_path is not None:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            tmp_final = cache_path.with_suffix('.tmp.npy')
            np.save(tmp_final, vectors)
            tmp_final.replace(cache_path)

    seconds = time.perf_counter() - start_t
    print(f'Đã nhúng {len(texts)} văn bản bằng {model_name} trong {seconds:.1f} giây '
          f'({len(texts) / max(seconds, 1e-6):.1f} tài liệu/giây).')
    return vectors


# ---------- Hybrid và xếp hạng ----------

def minmax(scores):
    """Chuẩn hóa min–max về [0, 1]; vector hằng thì trả về toàn 0."""
    scores = np.asarray(scores, dtype=np.float64)
    span = scores.max() - scores.min()
    return (scores - scores.min()) / span if span > 0 else np.zeros_like(scores)


def hybrid_scores(dense, bm25, alpha=ALPHA):
    """alpha * dense + (1 - alpha) * bm25, mỗi vector điểm được chuẩn hóa min–max trên cả kho."""
    return alpha * minmax(dense) + (1 - alpha) * minmax(bm25)


def top_k(scores, k=TOP_K):
    """Chỉ số của k điểm cao nhất, giảm dần; điểm bằng nhau thì giữ thứ tự trong kho."""
    return np.argsort(-np.asarray(scores), kind='stable')[:k]


# ---------- Bảng kết quả JSONL ----------

def read_rows(path):
    """Đọc các dòng JSONL đã có; bỏ qua dòng cuối bị cắt dở do lượt chạy trước bị ngắt."""
    rows = []
    if Path(path).exists():
        for line in Path(path).read_text(encoding='utf-8').splitlines():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def load_jsonl(path):
    """Đọc file JSONL đầu vào (tập đánh giá, kho ViQuAD); dòng hỏng thì báo lỗi chứ không bỏ qua."""
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]


def open_append(path):
    """Mở file để ghi nối tiếp; dòng cuối bị cắt dở thì xuống dòng trước để dòng mới không dính vào."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    dangling = False
    if path.exists() and path.stat().st_size > 0:
        with path.open('rb') as f:
            f.seek(-1, 2)
            dangling = f.read(1) != b'\n'
    f = path.open('a', encoding='utf-8')
    if dangling:
        f.write('\n')
    return f


def run_retrieval(scorers, questions, gold, doc_ids, out_path, k=TOP_K, hit_fn=None):
    """Ghi nối tiếp một dòng cho mỗi cặp (phương pháp, câu hỏi); cặp đã có trong file thì bỏ qua.

    scorers: {tên phương pháp: hàm qid -> vector điểm trên cả kho}. gold[qid] là None với câu không
    trả lời được: vẫn ghi `top` nhưng bốn chỉ số là null. Trả về số dòng mới ghi.
    """
    done = {(r['method'], r['qid']) for r in read_rows(out_path)}
    written = 0
    with open_append(out_path) as f:
        for method, score in scorers.items():
            for qid in questions:
                if (method, qid) in done:
                    continue
                top = [doc_ids[i] for i in top_k(score(qid), k)]
                if gold[qid] is None:
                    scores = dict.fromkeys(METRIC_KEYS)
                elif hit_fn is not None:
                    scores = hit_fn(qid, top)
                else:
                    scores = metrics(zalo_hits(top, gold[qid]), len(gold[qid]))
                row = {'method': method, 'qid': qid, **scores, 'top': top}
                f.write(json.dumps(row, ensure_ascii=False) + '\n')
                f.flush()
                written += 1
    return written


def summarize(out_path, methods):
    """Trả về {phương pháp: {'n': số câu có chỉ số, r5, r20, mrr10, ndcg5}}; dòng chỉ số null không tính."""
    rows = read_rows(out_path)
    table = {}
    for method in methods:
        own = [r for r in rows if r['method'] == method and r['r5'] is not None]
        if own:
            table[method] = {'n': len(own), **mean_metrics(own)}
    return table


def format_table(table):
    header = f'{"Phương pháp":<16}{"n":>6}' + ''.join(f'{name:>11}' for name in
                                                      ('Recall@5', 'Recall@20', 'MRR@10', 'nDCG@5'))
    lines = [f'{method:<16}{row["n"]:>6}' + ''.join(f'{row[k]:>11.4f}' for k in METRIC_KEYS)
             for method, row in table.items()]
    return '\n'.join([header, *lines])


# ---------- CLI ----------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('processed_dir', help='thư mục zalo_legal đã xử lý, hoặc corpus.jsonl của ViQuAD')
    parser.add_argument('out_dir')
    parser.add_argument('--methods', default='bm25,dense,hybrid')
    parser.add_argument('--alpha', type=float, default=ALPHA)
    parser.add_argument('--model', default=DEFAULT_MODEL)
    parser.add_argument('--batch-size', type=int, default=0,
                        help='0 = tự chọn theo VRAM GPU (T4=128, L4=256, A100=512)')
    parser.add_argument('--tokenizer', choices=['syllable', 'word'], default='syllable',
                        help='cách tách cho BM25: âm tiết, hoặc từ bằng underthesea (đệm trong <out_dir>/tokens)')
    parser.add_argument('--questions', help='test.jsonl hoặc dev.jsonl của tập đánh giá đã đóng băng')
    parser.add_argument('--removed', help='removed_doc_ids.json: các tài liệu loại khỏi kho trước khi truy xuất')
    parser.add_argument('--chunking', choices=['c1', 'c3', 'c4', 'c5', 'c5_nohead'],
                        help='chạy ở mức chunk (mặc định: mức tài liệu/đoạn)')
    parser.add_argument('--run', help='nhãn lượt chạy, kết quả ghi vào retrieval_<run>.jsonl (mặc định zalo)')
    parser.add_argument('--time-tokenizer', action='store_true',
                        help='đo tốc độ underthesea.word_tokenize trên 500 điều luật rồi thoát')
    args = parser.parse_args(argv)

    from ragvi.data import expand_zalo_doc_ids, load_zalo_corpus, load_zalo_queries

    if args.processed_dir.endswith('.jsonl'):
        # ponytail: đoạn ViQuAD chỉ lấy `text`, không ghép title (nhiều đoạn chung một title; vị trí đáp án tính trên text).
        corpus = {r['doc_id']: r['text'] for r in load_jsonl(args.processed_dir)}
        titles = None
        dataset, base_unit = 'viquad', 'passage'
        if args.chunking in ('c5', 'c5_nohead'):
            raise SystemExit('ViQuAD chỉ dùng c1, c3, c4.')
    else:
        corpus = load_zalo_corpus(args.processed_dir)
        titles = None
        if args.chunking in ('c5', 'c5_nohead') and (Path(args.processed_dir) / 'corpus').is_dir():
            from datasets import load_from_disk
            ds_corpus = load_from_disk(str(Path(args.processed_dir) / 'corpus')).select_columns(['id', 'title'])
            titles = {row['id']: row['title'] for row in ds_corpus}
        dataset, base_unit = 'zalo_legal', 'article'
    unit = args.chunking or base_unit
    doc_ids, texts = list(corpus), list(corpus.values())
    if args.time_tokenizer:
        print(json.dumps(time_word_tokenize(texts), ensure_ascii=False, indent=2))
        return

    methods = args.methods.split(',')
    unknown = set(methods) - {'bm25', 'dense', 'hybrid'}
    if unknown:
        raise SystemExit(f'Phương pháp không hợp lệ: {sorted(unknown)}')

    out = Path(args.out_dir)
    raw_removed = set(json.loads(Path(args.removed).read_text(encoding='utf-8'))) if args.removed else set()
    if raw_removed - set(corpus):
        raise SystemExit(f'{len(raw_removed - set(corpus))} doc_id trong {args.removed} không có trong kho.')
    removed = expand_zalo_doc_ids(raw_removed, corpus) if raw_removed else set()

    if args.chunking:
        chunks = cached_chunks(corpus, args.chunking, out / 'chunks' / f'{dataset}__{args.chunking}.jsonl',
                               titles=titles)
        unit_ids, unit_texts = [c[0] for c in chunks], [c[4] for c in chunks]
        parent_of = {c[0]: c[1] for c in chunks}
        span_of = {c[0]: (c[1], c[2], c[3]) for c in chunks}
        keep = [i for i, c in enumerate(chunks) if c[1] not in removed]
    else:
        unit_ids, unit_texts = doc_ids, texts
        parent_of = {d: d for d in doc_ids}
        span_of = {d: (d, 0, len(corpus[d])) for d in doc_ids}
        keep = [i for i, d in enumerate(doc_ids) if d not in removed]
    kept_ids, kept_texts = [unit_ids[i] for i in keep], [unit_texts[i] for i in keep]
    kept_docs = {parent_of[u] for u in kept_ids}

    answers_of = {}
    if args.questions:
        if args.run in (None, 'zalo'):
            raise SystemExit('Chạy trên tập đánh giá phải có --run khác "zalo" để không lẫn với retrieval_zalo.jsonl.')
        rows = load_jsonl(args.questions)
        questions = {q['qid']: q['question'] for q in rows}
        gold = {q['qid']: (set(q['gold_doc_ids']) if 'gold_doc_ids' in q else {q['gold_doc_id']})
                if q['answerable'] else None for q in rows}
        answers_of = {q['qid']: q.get('answers') or [] for q in rows}
        lost = set().union(*filter(None, gold.values())) - kept_docs
        if lost:
            raise SystemExit(f'{len(lost)} tài liệu vàng của câu trả lời được không có trong kho, ví dụ {sorted(lost)[:3]}.')
    elif dataset == 'viquad' or removed:
        raise SystemExit('Kho ViQuAD hoặc --removed cần đi kèm --questions.')
    else:
        questions, gold = load_zalo_queries(args.processed_dir)
    run = args.run or 'zalo'
    out_path = out / f'retrieval_{run}.jsonl'

    # Tham số khác mặc định thì đổi nhãn, để dòng cũ trong JSONL không bị coi là đã xong.
    chunk_tag = f'[{args.chunking}]' if args.chunking else ''
    model_tag = '' if args.model == DEFAULT_MODEL else f'[{args.model}]'
    word_tag = '[word]' if args.tokenizer == 'word' else ''
    labels = {'bm25': 'bm25' + chunk_tag + word_tag, 'dense': 'dense' + chunk_tag + model_tag,
              'hybrid': 'hybrid' + chunk_tag + word_tag + model_tag +
              ('' if args.alpha == ALPHA else f'[alpha={args.alpha:g}]')}
    done = {(r['method'], r['qid']) for r in read_rows(out_path)}
    pending = [m for m in methods if any((labels[m], q) not in done for q in questions)]

    tokenize = tokenize_words if args.tokenizer == 'word' else tokenize_syllables
    if {'bm25', 'hybrid'} & set(pending):
        if args.tokenizer == 'word':
            tok_path = out / 'tokens' / f'{dataset}__{unit}__underthesea.jsonl'
            base_tok_path = out / 'tokens' / f'{dataset}__{base_unit}__underthesea.jsonl'
            if args.chunking == 'c4' and not tok_path.exists() and base_tok_path.exists():
                tokens = cached_tokens([parent_of[u] for u in kept_ids], kept_texts, base_tok_path)
            else:
                tokens = cached_tokens(kept_ids, kept_texts, tok_path)
            index = build_bm25(tokens, tokenize=lambda t: t)
        else:
            index = build_bm25(kept_texts)
    if {'dense', 'hybrid'} & set(pending):
        cache = out / 'embeddings'
        q_pref, p_pref = model_prefixes(args.model)
        emb_path = embedding_cache_path(cache, dataset, unit, args.model)
        base_emb_path = embedding_cache_path(cache, dataset, base_unit, args.model)
        if args.chunking == 'c4' and not emb_path.exists() and base_emb_path.exists():
            emb_path = base_emb_path
        doc_vectors = embed(unit_texts, emb_path, args.model, args.batch_size, prefix=p_pref)
        if removed:
            doc_vectors = doc_vectors[keep]
        query_vectors = embed(list(questions.values()),
                              embedding_cache_path(cache, dataset, 'queries' if run == 'zalo' else f'queries_{run}',
                                                   args.model),
                              args.model, args.batch_size, prefix=q_pref)
        row_of = {qid: i for i, qid in enumerate(questions)}

    def bm25(qid):
        return bm25_scores(index, questions[qid], tokenize)

    def dense(qid):
        return doc_vectors @ query_vectors[row_of[qid]]

    def hybrid(qid):
        return hybrid_scores(dense(qid), bm25(qid), args.alpha)

    def hit_fn(qid, top):
        if dataset == 'viquad' and args.chunking:
            return metrics(viquad_hits([span_of[c] for c in top], next(iter(gold[qid])), answers_of[qid]), 1)
        return metrics(zalo_hits([parent_of[c] for c in top], gold[qid]), len(gold[qid]))

    scorers = {'bm25': bm25, 'dense': dense, 'hybrid': hybrid}
    written = run_retrieval({labels[m]: scorers[m] for m in pending}, questions, gold, kept_ids, out_path,
                            hit_fn=hit_fn if args.chunking else None)
    print(f'{len(kept_ids)} tài liệu, {len(questions)} truy vấn; ghi thêm {written} dòng vào {out_path}')
    print(format_table(summarize(out_path, [labels[m] for m in methods])))


if __name__ == '__main__':
    main()
