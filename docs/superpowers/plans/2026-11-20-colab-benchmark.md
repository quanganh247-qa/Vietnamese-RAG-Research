# Full Colab benchmark implementation plan

> **For agentic workers:** Use superpowers:executing-plans and test-driven development.

**Goal:** Benchmark C3–E3–R0 on all source query rows for retrieval and all frozen dev/test rows for answer generation and scoring, on Colab.

**Architecture:** Reuse the existing retrieval/generation/judge CLIs. `ragvi.benchmark` makes inputs and collects per-split metrics; `colab_run.sh benchmark` orchestrates a separate VM job and saves artifacts locally.

**Tech stack:** Existing `uv.lock`, Colab CLI 0.8, CUDA llama.cpp, pinned Qwen2.5-7B and Qwen3-8B GGUF.

**Spec:** Approved conversation scope: all source queries for retrieval; full frozen dev/test for generation and judging, no fine-tuning.

## Global constraints

- Keep original data and all frozen files unchanged; verify their SHA-256 hashes on the VM. Ignore retired Zalo reserve export.
- No ViQuAD upstream test quality metrics (no public gold). No fabricated Zalo train split. No model/quantization comparison against older results.
- GPU order G4 → A100 → L4 → T4; only recognized assignment errors trigger fallback. Start with the real pilot, then launch the benchmark when possible.
- Correctness, H_gold, H_ctx and RAH from uncalibrated judge are preliminary. Keep distinct denominators, pair oracle and RAG on jointly scorable answerable questions, report missing and invalid decisions.

## Tasks and checks

- [x] Reproduce allocation `POST /tun/m/assign` 503 and cover availability fallback without retrying authorization/application errors (shell CLI fake).
- [x] Test benchmark preparation (unlabeled source rows, frozen split and hash checks) and reports (null metrics, coverage, pairwise RAH). Verify actual 39,569 ViQuAD source rows, 788 Zalo source queries, 1,000 total frozen rows without rewriting the datasets.
- [x] Implement `bash colab_run.sh benchmark`, including separate sequential GGUF judge stage. Bash syntax and 67 local tests passed; verified frozen input hashes with `ragvi.benchmark prepare`.
- [x] Submit live Colab job. L4 allocated, uploaded to `content/`, dependencies installed, ViQuAD source retrieval started. Aggregate results: `reports/benchmark-colab-2026-11-20.md`. Per-run logs are not tracked.
- [ ] Verify the downloaded run summary and judge coverage after completion; do not report unmeasured scores.

Use the existing checkout. Record measured results in the research logs; keep raw artifacts, local paths and credentials out of Git.
