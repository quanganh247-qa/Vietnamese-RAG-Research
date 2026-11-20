# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Master's-thesis research project: a controlled empirical study of how RAG design choices (chunking, embedding/retrieval, reranking) affect answer accuracy and hallucination for Vietnamese text. The authoritative spec is the proposal `Đề cương_ RAG tiếng Việt – độ chính xác & ảo giác (v2).md` — read it before designing any pipeline, dataset, or metric code; it fixes the factor levels, models, metrics, and experiment design.

The project is at the data-preparation stage (proposal weeks 3–6). Only dataset exploration/cleaning exists; there is no pipeline code, package, dependency manifest, test suite, or linter yet. The git repository was initialized on 2026-11-12 with no commits; `data/` and `CV/` are git-ignored.

The working scope until the 2026-12-11 deadline is the reduced one in `Kế hoạch 30 ngày (hạn 11-12).md` (day-by-day in `Kế hoạch chi tiết 30 ngày.md`), and the design decisions that deviate from the proposal are recorded in `reports/quyet-dinh-thiet-ke.md` (D1–D9). Where those conflict with the proposal-derived sections below, the decisions file wins.

Prose in the proposal, notebook markdown, and notebook error messages is Vietnamese; identifiers and code are English. Keep that convention.

## Cách làm việc (chủ đề tài yêu cầu ngày 14/11/2026)

- Làm theo nhóm agent: trưởng nhóm dùng Fable 5.2, thành viên dùng Opus 5.5 (`model: "opus"`). Mã viết theo kiểu ponytail: giải pháp ngắn nhất chạy được, không trừu tượng thừa.
- Chủ đề tài phải làm chủ được nghiên cứu, nên mỗi đợt làm việc phải lưu lại ba thứ: kết quả và trạng thái từng ngày trong `Checklist theo dõi 30 ngày.md` (cột Ghi chú và mục "Nhật ký thực hiện"); quyết định và lý do trong `reports/quyet-dinh-thiet-ke.md`; giải thích từng thành phần trong `reports/so-tay-nghien-cuu.md`.
- Chỉ đánh dấu `[x]` một mục tiêu ngày khi có kết quả trên dữ liệu thật. Không bao giờ ghi số liệu chưa đo.
- Mã chạy trên dữ liệu thật qua notebook sinh bởi `scripts/build_colab_notebook.py` từ `src/ragvi/` (hiện là `notebooks/03_tuan1_hoan_tat.ipynb`); chủ đề tài mở notebook cục bộ trong VS Code với kernel Colab, output lưu lại trong file `.ipynb`. Sinh lại notebook sẽ xóa output, nên notebook đã chạy (`02_tuan1_truy_xuat_phan_doan.ipynb`, lượt 14/11) được giữ nguyên làm bản ghi và bước mới đi vào notebook mới.

## Running things

- **Notebooks run on Google Colab, not locally.** `notebooks/01_dataset_exploration.ipynb` mounts Google Drive and hardcodes `PROJECT_DIR = /content/drive/MyDrive/Vietnamese-RAG-Research`. Datasets live on Drive under `data/raw/{viquad,zalo_legal}` and `data/processed/...`; the local `data/raw` and `data/processed` directories are empty, so notebook cells cannot be executed from this machine.
- Notebook cells are tagged in their markdown headers: `[TÁI SỬ DỤNG]` (reusable/idempotent), `[CHẠY MỘT LẦN / MỖI RUNTIME MỚI]` (per-runtime setup such as `%pip install`, Drive mount), `[CHẠY MỘT LẦN / KHI CẬP NHẬT]` (run once / on change). Cells are meant to run top to bottom; keep new cells tagged the same way.
- `python3 scripts/inspect_dataset.py` (run from repo root — it uses the relative path `data/raw`) lists files and peeks at `.json` files. Note it predates the current storage format: the datasets are now Hugging Face `save_to_disk` directories (Arrow), which it only lists by size.
- `CV/main.tex` is an unrelated LaTeX CV, built with `tectonic` on save via the VS Code LaTeX Workshop config in `.vscode/settings.json`.

## Data

- **UIT-ViQuAD 2.0** — `DatasetDict` with `train`/`validation`/`test`; columns `id, uit_id, title, context, question, answers, is_impossible, plausible_answers`. `is_impossible` marks the unanswerable questions the hallucination metrics depend on. The `test` split has no answers (`answers` is `None` for every row), so evaluation sets must be sampled from train/validation. `id` restarts per split (e.g. `0001-0001-0001` appears in each), so it is only unique within a split.
- **Zalo Legal Text Retrieval 2021** — BEIR-style: `corpus` (`id, title, text`; 61,425 law articles, id like `01/2009/tt-bnn+1` = document + article number, `title` is the `Điều N. ...` heading), `queries` (`id, text`), `qrels` (`query-id, corpus-id, score`). Known quirks: 30 duplicated query rows (818 rows, 788 unique ids), 357 corpus rows with empty `text`, and some extremely long articles (max ~250k chars).

### Cleaning invariants (notebook sections 6–8)

Normalization is deliberately conservative, because legal text and gold labels must survive intact:

- Allowed changes only: Unicode NFC, CRLF/CR → LF, stripping BOM/zero-width chars, replacing control chars and U+FFFD with a space, collapsing intra-line whitespace, at most one blank line between paragraphs.
- Never changed: diacritics, case, punctuation, Điều/Khoản/Điểm numbering, repeated legal content, any ID, and qrels (copied verbatim).
- `data/raw` is never modified; cleaned output goes to `data/processed`, and the save cell refuses to overwrite a non-empty output directory.
- Post-clean validation (`validate_cleaned_dataset`, `validate_ground_truth_after_cleaning`) asserts schema, row counts, IDs, non-text fields and qrels links are unchanged, and that the non-whitespace character signature of every text field is preserved. Any new cleaning step must still pass these checks.

## Planned architecture (from the proposal)

```
Documents → preprocess → chunk (C) → embed (E) → index (FAISS / BM25)
Query → retrieve top-20 → rerank (R) → top-5 → fixed prompt → fixed LLM → answer
Evaluate: retrieval · correctness · hallucination · cost
```

The pipeline must be modular so each factor can be swapped independently:

- **C – chunking (6):** C1 fixed 256 tokens; C2 fixed 512 / overlap 64; C3 sentence-based up to ~256; C4 document structure (Wikipedia paragraph / per-Điều); C5 **ViStructChunk** (proposed: Điều → Khoản → Điểm tree with parent headings prepended to every chunk; word-boundary-aware for plain text); C6 semantic chunking. Tokens are counted with the embedding model's own tokenizer. C4 and C5 share cut boundaries on purpose, differing only in the prepended heading.
- **E – retrieval (6):** E0 BM25 (underthesea word segmentation); E1 `bkai-foundation-models/vietnamese-bi-encoder`; E2 `AITeamVN/Vietnamese_Embedding_v2`; E3 `BAAI/bge-m3`; E4 `intfloat/multilingual-e5-large`; E5 hybrid E3 + BM25, α = 0.7.
- **R – reranking (4):** R0 none; R1 `BAAI/bge-reranker-v2-m3`; R2 `AITeamVN/Vietnamese_Reranker`; R3 `namdp-ptit/ViRanker` (or `itdainb/PhoRanker`).

Experiment design constraints that code must respect:

- **Phase A:** retrieval-only metrics over the full 6×6×4 = 144 grid (no LLM calls).
- **Phase B:** end-to-end on ~20 configs: anchor C3–E3–R0, one-factor-at-a-time variations, 4 best combinations from Phase A, plus **closed-book** (no context) and **oracle** (gold passage always supplied) reference conditions.
- Generator is held fixed: one local 8–12B model, temperature 0, a single prompt instructing it to answer only from context and otherwise reply `Không tìm thấy thông tin`, n = 5 context passages, fixed seed. Prompt tuning and fine-tuning embeddings/rerankers are out of scope.
- Evaluation sets: 1,000 questions per dataset, stratified 700 answerable / 300 unanswerable. Zalo Legal has no unanswerable questions, so they are created by removing the gold article from the corpus or hand-writing out-of-corpus questions. The ViQuAD corpus is padded with ~20k Vietnamese Wikipedia distractor passages.
- Metrics: Recall@5/@20, MRR@10, nDCG@5 (a chunk counts as correct if it contains ≥ 80% of the gold answer); EM / token-F1 / judge correctness (0/1/2); faithfulness, fabrication rate on unanswerable questions, false-refusal rate; and the proposed **RAH(k) = H(k) − H(oracle)** (retrieval-attributable hallucination), which is why the closed-book and oracle conditions must run on the same question set as every config.
- The judge is a different LLM from the generator, prompted in Vietnamese with JSON output, calibrated against human labels (target Cohen's κ ≥ 0.7) and ViHallu samples.
- Statistics: bootstrap 95% CIs over questions (1,000 resamples), paired permutation tests with Holm correction.

Planned stack: Python, `sentence-transformers`, `FlagEmbedding`, `rank_bm25`/Pyserini, FAISS, `underthesea` or `pyvi`, `vLLM` or `transformers`, with `ragas`/`deepeval` as a reference for the custom metrics.
