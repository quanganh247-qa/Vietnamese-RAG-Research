"""API hợp nhất nối truy xuất, xếp hạng lại và sinh câu trả lời cho ứng dụng Demo (Tuần 3–4: Ngày 16, 21, 23).

Hỗ trợ hai chế độ:
1. Tra cứu trực tiếp từ bộ nhớ đệm thực nghiệm (`data/retrieval_cache/`) khi câu hỏi thuộc tập đánh giá (phản hồi < 10 ms trên CPU).
2. Chạy truy xuất BM25/Dense/Hybrid + Reranker R1 + mô hình sinh (`llama-server` hoặc Transformers) cho câu hỏi tự do bất kỳ.
"""
from dataclasses import dataclass
import json
from pathlib import Path
import re

from ragvi.generate import CTX_LIMIT, build_prompt, clean_generation, load_generator, load_llamacpp, subset_chunks
from ragvi.metrics import normalize_answer
from ragvi.rerank import DEFAULT_RERANKER, load_reranker, load_units
from ragvi.retrieval import (ALPHA, DEFAULT_MODEL, TOP_K, bm25_scores, cached_chunks, cached_tokens, embed,
                             hybrid_scores, load_jsonl, read_rows, tokenize_words, top_k)

RECOMMENDED_DEFAULTS = {
    'zalo': {'c': 'C5', 'e': 'E5', 'rerank': True},
    'viquad': {'c': 'C3', 'e': 'E3', 'rerank': True},
}

METHOD_MAP = {
    ('E0', 'R0'): lambda c: f'bm25[{c}][word]',
    ('E3', 'R0'): lambda c: f'dense[{c}]',
    ('E5', 'R0'): lambda c: f'hybrid[{c}][word]',
    ('E0', 'R1'): lambda c: f'bm25[{c}][word]+r1',
    ('E3', 'R1'): lambda c: f'dense[{c}]+r1',
    ('E5', 'R1'): lambda c: f'hybrid[{c}][word]+r1',
}


@dataclass
class Passage:
    chunk_id: str
    source: str
    score: float
    text: str


def method_name(c, e, r='R0'):
    """Ánh xạ (C, E, R) sang nhãn phương pháp trong file `retrieval_*_phase_a.jsonl`."""
    c_low = c.lower()
    if c_low == 'c5 không tiêu đề':
        c_low = 'c5_nohead'
    fn = METHOD_MAP.get((e.upper(), r.upper()))
    if fn is None:
        raise ValueError(f'Tổ hợp (E={e}, R={r}) không được hỗ trợ trong demo.')
    return fn(c_low)


def config_name(c, e, r='R0'):
    """Nhãn cấu hình Giai đoạn B chuẩn (ví dụ 'C5-E3-R0', 'C3-E3-R1')."""
    c_up = 'C5_nohead' if c.lower() in ('c5_nohead', 'c5 không tiêu đề') else c.upper()
    return f'{c_up}-{e.upper()}-{r.upper()}'


def format_source(dataset, chunk_id, text='', titles=None):
    """Định dạng nguồn dẫn chiếu: số hiệu văn bản + Điều + Khoản với Zalo; tên bài Wikipedia với ViQuAD."""
    doc_id = chunk_id.rsplit('#', 1)[0]
    part = chunk_id.rsplit('#', 1)[1] if '#' in chunk_id else '0'
    if dataset == 'zalo' and '+' in doc_id:
        code, art = doc_id.rsplit('+', 1)
        m_clause = re.search(r'Khoản\s+(\d+)', (text or '').split('\n', 1)[0])
        clause_str = f', Khoản {m_clause.group(1)}' if m_clause else f' (đoạn #{part})'
        return f'Văn bản {code.upper()}, Điều {art}{clause_str}'
    title = (titles or {}).get(doc_id)
    return f'Wikipedia: {title} ({chunk_id})' if title else f'ViQuAD ({chunk_id})'


_CACHE_STATE = {}


def _load_cache_state(cache_dir='data/retrieval_cache', results_dir='results/colab/benchmark-Pa3Gy3aM'):
    key = (str(cache_dir), str(results_dir))
    if key in _CACHE_STATE:
        return _CACHE_STATE[key]
    cdir, rdir = Path(cache_dir), Path(results_dir)
    state = {'questions': {'zalo': {}, 'viquad': {}}, 'titles': {}, 'chunks': {'zalo': {}, 'viquad': {}}}
    for ds, fn in [('viquad', 'viquad_source.jsonl'), ('zalo', 'zalo_source.jsonl')]:
        p = rdir / fn
        if p.exists():
            for line in p.open(encoding='utf-8'):
                r = json.loads(line)
                state['questions'][ds][normalize_answer(r['question'])] = r
                if ds == 'viquad' and r.get('gold_doc_id') and r.get('title'):
                    state['titles'][r['gold_doc_id']] = r['title']
    for ds, fn in [('viquad', 'chunks/viquad__c3.jsonl'), ('zalo', 'chunks/zalo_legal__c3.jsonl')]:
        p = cdir / fn
        if p.exists():
            text_of, _, _ = load_units(p)
            state['chunks'][ds]['c3'] = text_of
    _CACHE_STATE[key] = state
    return state


def retrieve(dataset, c, e, r='R0', question='', top_n=5, cache_dir='data/retrieval_cache',
             data_dir='data', results_dir='results/colab/benchmark-Pa3Gy3aM'):
    """Trả về `top_n` đối tượng `Passage(chunk_id, source, score, text)` cho `(dataset, c, e, r, question)`."""
    dataset = dataset.lower()
    c_low = 'c5_nohead' if c.lower() in ('c5_nohead', 'c5 không tiêu đề') else c.lower()
    if dataset == 'viquad' and c_low in ('c5', 'c5_nohead'):
        c_low = 'c3'  # C5 chỉ dành cho văn bản luật
    m_name = method_name(c_low, e, r)
    state = _load_cache_state(cache_dir, results_dir)
    q_norm = normalize_answer(question)
    q_info = state['questions'].get(dataset, {}).get(q_norm)

    cdir = Path(cache_dir)
    ret_path = cdir / f'retrieval_{dataset}_phase_a.jsonl'
    top_cids = None
    if q_info and ret_path.exists():
        qid = q_info['qid']
        for row in read_rows(ret_path):
            if row.get('qid') == qid and row.get('method') == m_name and 'top' in row:
                top_cids = row['top'][:top_n]
                break

    if top_cids is not None:
        chunk_map = state['chunks'][dataset].get(c_low)
        if chunk_map is None:
            # Nếu chưa có file chunk của c_low, tái tạo từ các chunk C3 đã lưu đệm của cùng doc_id
            c3_map = state['chunks'][dataset].get('c3', {})
            needed_docs = {cid.rsplit('#', 1)[0] for cid in top_cids}
            doc_texts = {}
            for cid, txt in c3_map.items():
                did = cid.rsplit('#', 1)[0]
                if did in needed_docs:
                    doc_texts.setdefault(did, []).append((int(cid.rsplit('#', 1)[1]), txt))
            corpus_sub = {did: '\n'.join(t for _, t in sorted(parts)) for did, parts in doc_texts.items()}
            chunk_map = subset_chunks(corpus_sub, c_low, list(needed_docs))
        out = []
        for rank, cid in enumerate(top_cids, 1):
            txt = chunk_map.get(cid, state['chunks'][dataset].get('c3', {}).get(cid, ''))
            score = round(1.0 / rank, 3)
            out.append(Passage(cid, format_source(dataset, cid, txt, state['titles']), score, txt))
        return out

    # Nhánh chạy trực tiếp trên kho dữ liệu khi câu hỏi mới không nằm trong bộ nhớ đệm
    ddir = Path(data_dir)
    units_path = ddir / 'eval/viquad/corpus.jsonl' if dataset == 'viquad' else ddir / 'processed/zalo_legal'
    if not units_path.exists():
        c3_map = state['chunks'][dataset].get('c3', {})
        if not c3_map:
            return []
        from rank_bm25 import BM25Okapi
        cids = list(c3_map.keys())
        texts = [c3_map[k] for k in cids]
        q_toks = re.findall(r'\w+', question.lower())
        bm25 = BM25Okapi([re.findall(r'\w+', t.lower()) for t in texts])
        scores = bm25.get_scores(q_toks)
        best = top_k(scores, top_n)
        return [Passage(cids[i], format_source(dataset, cids[i], texts[i], state['titles']),
                        round(float(scores[i]), 3), texts[i]) for i in best]

    docs, _, _ = load_units(units_path)
    chunks = cached_chunks(docs, c_low, cdir / f'chunks/{dataset}__{c_low}.jsonl')
    cids = [row[0] for row in chunks]
    texts = [row[4] for row in chunks]
    text_of = dict(zip(cids, texts))
    e_up = e.upper()
    s_bm25 = s_dense = None
    if e_up in ('E0', 'E5'):
        from rank_bm25 import BM25Okapi
        tok_lists = cached_tokens(cids, texts, cdir / f'tokens/{dataset}__{c_low}__underthesea.jsonl', tokenize=tokenize_words)
        bm25 = BM25Okapi(tok_lists)
        s_bm25 = bm25_scores(bm25, question, tokenize=tokenize_words)
    if e_up in ('E3', 'E5'):
        d_vecs = embed(texts, cdir / f'embeddings/{dataset}__{c_low}__BAAI_bge-m3.npy', model_name=DEFAULT_MODEL)
        q_vec = embed([question], None, model_name=DEFAULT_MODEL)
        s_dense = (q_vec @ d_vecs.T)[0]
    scores = s_bm25 if e_up == 'E0' else (s_dense if e_up == 'E3' else hybrid_scores(s_dense, s_bm25, alpha=ALPHA))
    cand_idx = top_k(scores, TOP_K if r.upper() == 'R1' else top_n)
    cand_ids = [cids[i] for i in cand_idx]
    cand_scores = [float(scores[i]) for i in cand_idx]
    if r.upper() == 'R1':
        scorer = load_reranker(DEFAULT_RERANKER)
        r_scores = [float(s) for s in scorer(question, [text_of[cid] for cid in cand_ids])]
        order = top_k(r_scores, top_n)
        cand_ids = [cand_ids[i] for i in order]
        cand_scores = [r_scores[i] for i in order]
    return [Passage(cid, format_source(dataset, cid, text_of[cid], state['titles']),
                    round(sc, 3), text_of[cid]) for cid, sc in zip(cand_ids[:top_n], cand_scores[:top_n])]


def generate(question, passages, dataset=None, c=None, e=None, r='R0',
             cache_dir='data/retrieval_cache', results_dir='results/colab/benchmark-Pa3Gy3aM',
             llama_url=None, model_name='Qwen/Qwen3.5-9B', generator_fn=None):
    """Sinh câu trả lời từ `question` và danh sách `passages` (ưu tiên đọc câu trả lời đã lưu đệm nếu khớp cấu hình)."""
    if dataset and c and e:
        state = _load_cache_state(cache_dir, results_dir)
        q_info = state['questions'].get(dataset.lower(), {}).get(normalize_answer(question))
        ans_path = Path(cache_dir) / f'answers_{dataset.lower()}_test.jsonl'
        if q_info and ans_path.exists():
            qid = q_info['qid']
            cfg = config_name(c, e, r)
            want_cids = [p.chunk_id for p in (passages or [])]
            for row in read_rows(ans_path):
                if row.get('qid') == qid and (row.get('config') == cfg or (want_cids and row.get('context_ids') == want_cids)):
                    return row['answer']

    texts = [p.text if hasattr(p, 'text') else str(p) for p in (passages or [])]
    prompt, _ = build_prompt(question, texts if texts else None, limit=CTX_LIMIT)
    if generator_fn is not None:
        return clean_generation(generator_fn(prompt))
    if llama_url:
        fn = load_llamacpp(llama_url, model_name)
        return clean_generation(fn(prompt))
    try:
        fn = load_generator(model_name)
        return clean_generation(fn(prompt))
    except Exception:
        return ('[Chế độ chỉ truy xuất trên CPU] Đã hiển thị 5 đoạn căn cứ ở bảng bên dưới. '
                'Để sinh câu trả lời cho câu hỏi mới ngoài tập đánh giá, hãy kết nối --llama-url hoặc GPU runtime.')
