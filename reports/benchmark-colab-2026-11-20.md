# Benchmark Baseline trên Colab (L4 & A100) — 20–21/11/2026

**Cấu hình:** `C3–E3–R0` (phân đoạn theo câu C3, `BAAI/bge-m3` dense, không reranker), `closed_book` và `oracle`.
- **Mô hình sinh & giám khảo (Judge):** `unsloth/Qwen3.5-9B-GGUF:Q4_K_M` (`Qwen3.5-9B-Q4_K_M.gguf`, revision `1daf391c47cef14242f238b819fbe6fd500d624b`), tắt chế độ suy luận (`enable_thinking=false`), chạy qua `llama.cpp` (`llama-server` commit `3837bf0bc02ea5d08f8ee3585fc8c7784a81bce8`) với **continuous batching** (`--parallel 8` trên NVIDIA L4 23 GB và `--parallel 12` trên NVIDIA A100 40 GB, `--cont-batching --batch-size 2048 --ubatch-size 512`).
- **Lệnh thực thi:** `bash colab_run.sh benchmark https://drive.google.com/drive/folders/1unFYNOZA0ytJKYZkI0X4ZIy802GcOyjZ`.

---

## 1. Kết quả tầng truy xuất (`C3–E3–R0`, top-20)

Sáu lượt truy xuất ban đầu trên NVIDIA L4 mất tổng cộng khoảng **15 phút 3 giây** (nhúng BGE-M3 `bf16` đạt `143,8–251,8 docs/s`); các lượt chạy tiếp theo nạp từ `data/retrieval_cache/` trong **< 2 phút**.

| Tập | Đã truy xuất | Có điểm | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---:|---:|---:|---:|---:|---:|
| ViQuAD nguồn train | 28.454 | 19.238 | 87,44% | 94,90% | 0,7568 | 0,7820 |
| ViQuAD nguồn validation | 3.814 | 2.653 | 87,03% | 94,42% | 0,7475 | 0,7741 |
| ViQuAD nguồn test | 7.301 | 0 | — | — | — | — |
| ViQuAD dev đóng băng | 100 | 77 | 84,42% | 93,51% | 0,7379 | 0,7588 |
| ViQuAD test đóng băng | 400 | 280 | 88,93% | 95,71% | 0,7609 | 0,7894 |
| Zalo nguồn | 788 | 788 | 80,96% | 92,64% | 0,6567 | 0,6870 |
| Zalo dev đóng băng | 100 | 100 | 51,00% | 81,00% | 0,3740 | 0,3883 |
| Zalo test đóng băng | 400 | 280 | 81,43% | 92,68% | 0,6229 | 0,6642 |

- “Có điểm” chỉ gồm câu có đáp án/bằng chứng vàng. Test nguồn ViQuAD không có nhãn công khai trong bản dữ liệu này; không đồng nhất với test đóng băng. Zalo test đóng băng dùng kho thu hẹp đã loại điều luật theo D1/D6 (kể cả bản trùng mã `nd-cp` ↔ `nđ-cp`).
- Zalo dev có khoảng cách 30 điểm phần trăm giữa Recall@20 (`81,00%`) và Recall@5 (`51,00%`), tạo dư địa rõ rệt để đánh giá tác động của reranker R1.

---

## 2. Kết quả tầng sinh câu trả lời và LLM-as-a-Judge đã hiệu chỉnh (`Qwen3.5-9B-GGUF:Q4_K_M`, `JUDGE_MAX_CHARS = 15000`)

Toàn bộ **2.737 lượt sinh câu trả lời** và **2.211 lượt chấm điểm Judge** (`231` ViQuAD dev + `840` ViQuAD test + `300` Zalo dev + `840` Zalo test) hoàn tất với **0 câu thiếu (`n_judge_missing = 0`) và 0 lỗi định dạng JSON (`n_judge_errors = 0`, 100% hợp lệ)**.

> **Hiệu chỉnh Judge với nhãn người (Ngày 12–13):** Đối chiếu mù (blind grading) trên 100 mẫu dev (`reports/phieu/human_dev_viquad.md` và `reports/phieu/human_dev_zalo.md`) giúp phát hiện `JUDGE_MAX_CHARS = 3000` ban đầu cắt mất Khoản 3–10 của các điều luật dài trên Zalo. Sau khi nâng `JUDGE_MAX_CHARS = 15000` (khớp trần `4.000 token` của `oracle`), hệ số đồng thuận **Cohen's $\kappa$ trên 100 mẫu dev đạt $\kappa(H_{\text{gold}}) = 0,8163$ và $\kappa(\text{correctness}) = 0,8519$** (riêng ViQuAD dev: $\kappa(H_{\text{gold}}) = 0,7216$, $\kappa(\text{correctness}) = 0,8623$; riêng Zalo dev: $\kappa(H_{\text{gold}}) = 0,8764$, $\kappa(\text{correctness}) = 0,8324$), vượt xa ngưỡng cổng kiểm tra $\kappa \ge 0,60$.

### 2.1. Tập phát triển (`viquad_dev` & `zalo_dev`)

| Tập | Cấu hình | `n` (`n_ans`/`n_unans`) | `correct_refusal` | `fabrication` | `false_refusal` | `contains_gold` | `EM` | `F1` | `correctness` (0–2) | `H_gold` (`n`) | `H_ctx` (`n`) | `RAH` vs `oracle` (`n_pairs`) | Tốc độ (`q/min`) | Trung vị `p50` (s) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `viquad_dev` | `closed_book` | 100 (77/23) | 65,22% | 34,78% | 71,43% | 2,60% | 0,00% | 0,0531 | 0,1948 | 68,18% (22) | — | — | 54,00 | 0,713 |
| `viquad_dev` | `oracle` | 77 (77/0) | — | — | 7,79% | 59,74% | 0,00% | 0,4311 | 1,7532 | 14,08% (71) | 0,00% (71) | — | 30,71 | 1,695 |
| `viquad_dev` | `C3-E3-R0` | 100 (77/23) | 60,87% | 39,13% | 16,88% | 49,35% | 2,60% | 0,4012 | 1,5195 | 28,12% (64) | 4,69% (64) | **+11,11%** (63) | 16,33 | 3,096 |
| `zalo_dev` | `closed_book` | 100 (100/0) | — | — | 53,00% | — | — | — | 0,1800 | 89,36% (47) | — | — | 35,83 | 1,198 |
| `zalo_dev` | `oracle` | 100 (100/0) | — | — | 11,00% | — | — | — | 1,7300 | 2,25% (89) | 1,12% (89) | — | 16,89 | 3,119 |
| `zalo_dev` | `C3-E3-R0` | 100 (100/0) | — | — | 43,00% | — | — | — | 0,7900 | 31,58% (57) | 3,51% (57) | **+31,48%** (54) | 13,91 | 3,488 |

### 2.2. Tập kiểm tra đóng băng (`viquad_test` & `zalo_test`)

| Tập | Cấu hình | `n` (`n_ans`/`n_unans`) | `correct_refusal` | `fabrication` | `false_refusal` | `contains_gold` | `EM` | `F1` | `correctness` (0–2) | `H_gold` (`n`) | `H_ctx` (`n`) | `RAH` vs `oracle` (`n_pairs`) | Tốc độ (`q/min`) | Trung vị `p50` (s) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `viquad_test` | `closed_book` | 400 (280/120) | 88,33% | 11,67% | 75,00% | 3,93% | 0,36% | 0,0642 | 0,1964 | 77,14% (70) | — | — | 55,51 | 0,695 |
| `viquad_test` | `oracle` | 280 (280/0) | — | — | 12,50% | 57,14% | 0,71% | 0,4326 | 1,7000 | 10,20% (245) | 1,22% (245) | — | 28,64 | 2,002 |
| `viquad_test` | `C3-E3-R0` | 400 (280/120) | 64,17% | 35,83% | 15,71% | 52,14% | 2,86% | 0,3982 | 1,5643 | 19,07% (236) | 2,54% (236) | **+6,76%** (222) | 16,00 | 3,217 |
| `zalo_test` | `closed_book` | 400 (280/120) | 57,50% | 42,50% | 55,71% | — | — | — | 0,1429 | 91,94% (124) | — | — | 38,82 | 0,778 |
| `zalo_test` | `oracle` | 280 (280/0) | — | — | 14,29% | — | — | — | 1,6214 | 4,58% (240) | 4,58% (240) | — | 17,04 | 3,379 |
| `zalo_test` | `C3-E3-R0` | 400 (280/120) | 56,67% | 43,33% | 27,50% | — | — | — | 1,1821 | 25,12% (203) | 7,39% (203) | **+17,46%** (189) | 10,47 | 4,664 |

### 2.3. Chỉ số "nhầm điều luật" (`wrong_article`, phục vụ H1b) trên Zalo

| Tập | Cấu hình | Câu không từ chối (`non_refused`) | Câu có viện dẫn `Điều N` (`cited`) | Câu viện dẫn sai số Điều (`wrong_article`) | Tỷ lệ trên câu không từ chối | Tỷ lệ trên câu có viện dẫn |
|---|---|---:|---:|---:|---:|---:|
| `zalo_dev` | `closed_book` | 47 | 16 | 16 | 34,04% | 100,00% |
| `zalo_dev` | `oracle` | 89 | 4 | 0 | 0,00% | 0,00% |
| `zalo_dev` | `C3-E3-R0` | 57 | 2 | 1 | 1,75% | 50,00% |
| `zalo_test` | `closed_book` | 124 | 34 | 34 | 27,42% | 100,00% |
| `zalo_test` | `oracle` | 240 | 18 | 7 | 2,92% | 38,89% |
| `zalo_test` | `C3-E3-R0` | 203 | 17 | 7 | 3,45% | 41,18% |

*(Lưu ý: Trên `zalo_test` `oracle` và `C3-E3-R0`, các trường hợp `wrong_article` trong điều kiện có ngữ cảnh chủ yếu do văn bản điều luật vàng có dẫn chiếu chéo tới điều luật khác trong cùng nghị định/luật và mô hình nhắc lại số điều được dẫn chiếu đó; sẽ phân tích chi tiết khi so sánh `C4`, `C5` và `C5_nohead` ở Giai đoạn B.)*

---

## 3. Ma trận Giai đoạn A — Truy xuất và Xếp hạng lại (`bash colab_run.sh phase_a` trên NVIDIA A100 40 GB, 22/11/2026)

- **Lệnh thực thi:** `bash colab_run.sh phase_a https://drive.google.com/drive/folders/1unFYNOZA0ytJKYZkI0X4ZIy802GcOyjZ` (gói kết quả tại `results/colab/phase_a-Cq9WWQSy/`, đã đồng bộ vào `data/retrieval_cache/retrieval_{viquad,zalo}_{dev,phase_a}.jsonl`).
- **Tối ưu hiệu năng triển khai:**
  - Tách từ `underthesea` song song bằng `ProcessPoolExecutor` (12 luồng CPU trên A100): 326.067 chunk `c5` / `c5_nohead` tách từ trong `148,3–166,9 giây`.
  - Nhúng `BAAI/bge-m3` với `torch.bfloat16`, `batch_size=512`, checkpoint mỗi 20.000 chunk: 326.603 chunk `c5` / `c5_nohead` nhúng trong **`169,3–169,6 giây` (`1.925,5–1.928,7 chunk/giây`)**.
  - `CrossEncoder('BAAI/bge-reranker-v2-m3')` (`R1`) chạy với `bfloat16` và gộp tất cả phương pháp của cùng một cách phân đoạn vào một lượt nạp mô hình (~1 phút cho 3–5 phương pháp × 400 truy vấn × top-20).

### 3.1. Xếp hạng lại `R1` trên tập phát triển (`viquad_dev` & `zalo_dev`, cấu hình neo `C3–E3`)

| Tập | Cấu hình | `n` | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---:|---:|---:|---:|---:|
| `viquad_dev` | `dense[c3]` (`C3–E3–R0`) | 77 | 84,42% | 93,51% | 0,7379 | 0,7588 |
| `viquad_dev` | `dense[c3]+r1` (`C3–E3–R1`) | 77 | **92,21%** (+7,79 điểm %) | 93,51% | **0,8723** (+0,1344) | **0,8834** (+0,1246) |
| `zalo_dev` | `dense[c3]` (`C3–E3–R0`) | 100 | 51,00% | 81,00% | 0,3740 | 0,3883 |
| `zalo_dev` | `dense[c3]+r1` (`C3–E3–R1`) | 100 | **69,00%** (+18,00 điểm %) | 81,00% | **0,4828** (+0,1088) | **0,5271** (+0,1388) |

### 3.2. Toàn bộ 30/30 cấu hình Giai đoạn A trên `viquad_test` (`n = 280` câu trả lời được / 400 câu test)

| Phân đoạn (`C`) | Truy xuất (`E`) | Xếp hạng (`R`) | Mã phương pháp trong cache | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---:|---:|---:|---:|
| `C1` (cửa sổ 256) | `E0` (BM25 tách từ) | `R0` | `bm25[c1][word]` | 78,21% | 85,00% | 0,6999 | 0,7162 |
| `C1` | `E2` (`Vietnamese_Embedding_v2`) | `R0` | `dense[c1][AITeamVN/Vietnamese_Embedding_v2]` | 87,14% | 93,93% | 0,7445 | 0,7728 |
| `C1` | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c1]` | 86,07% | 94,29% | 0,7401 | 0,7650 |
| `C1` | `E4` (`multilingual-e5-large`) | `R0` | `dense[c1][intfloat/multilingual-e5-large]` | 87,86% | 95,00% | 0,7921 | 0,8092 |
| `C1` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c1][word]` | 91,79% | 94,64% | 0,8331 | 0,8523 |
| `C1` | `E0` (BM25 tách từ) | `R1` | `bm25[c1][word]+r1` | 83,93% | 85,00% | 0,8123 | 0,8181 |
| `C1` | `E2` (`Vietnamese_Embedding_v2`) | `R1` | `dense[c1][AITeamVN/Vietnamese_Embedding_v2]+r1` | 92,14% | 93,93% | 0,8787 | 0,8881 |
| `C1` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c1]+r1` | 92,86% | 94,29% | 0,8855 | 0,8946 |
| `C1` | `E4` (`multilingual-e5-large`) | `R1` | `dense[c1][intfloat/multilingual-e5-large]+r1` | 93,21% | 95,00% | 0,8876 | 0,8971 |
| `C1` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c1][word]+r1` | 93,21% | 94,64% | 0,8923 | 0,9010 |
| `C3` (câu ≤ 256) | `E0` (BM25 tách từ) | `R0` | `bm25[c3][word]` | 79,64% | 86,43% | 0,7118 | 0,7289 |
| `C3` | `E2` (`Vietnamese_Embedding_v2`) | `R0` | `dense[c3][AITeamVN/Vietnamese_Embedding_v2]` | 88,93% | 94,64% | 0,7608 | 0,7893 |
| `C3` | `E3` (`BAAI/bge-m3`, **Neo**) | `R0` | `dense[c3]` | 88,93% | 95,71% | 0,7609 | 0,7894 |
| `C3` | `E4` (`multilingual-e5-large`) | `R0` | `dense[c3][intfloat/multilingual-e5-large]` | 89,29% | 96,79% | 0,8049 | 0,8227 |
| `C3` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c3][word]` | 92,86% | 96,07% | 0,8574 | 0,8727 |
| `C3` | `E0` (BM25 tách từ) | `R1` | `bm25[c3][word]+r1` | 86,07% | 86,43% | 0,8329 | 0,8397 |
| `C3` | `E2` (`Vietnamese_Embedding_v2`) | `R1` | `dense[c3][AITeamVN/Vietnamese_Embedding_v2]+r1` | 93,21% | 94,64% | 0,8908 | 0,9000 |
| `C3` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c3]+r1` | 94,64% | 95,71% | 0,8995 | 0,9100 |
| `C3` | `E4` (`multilingual-e5-large`) | `R1` | `dense[c3][intfloat/multilingual-e5-large]+r1` | 95,00% | **96,79%** | 0,9029 | 0,9131 |
| `C3` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c3][word]+r1` | 95,00% | 96,07% | 0,9058 | 0,9158 |
| `C4` (đoạn gốc) | `E0` (BM25 tách từ) | `R0` | `bm25[c4][word]` | 79,29% | 86,43% | 0,7072 | 0,7253 |
| `C4` | `E2` (`Vietnamese_Embedding_v2`) | `R0` | `dense[c4][AITeamVN/Vietnamese_Embedding_v2]` | 88,57% | 93,93% | 0,7513 | 0,7827 |
| `C4` | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c4]` | 86,79% | 95,36% | 0,7557 | 0,7794 |
| `C4` | `E4` (`multilingual-e5-large`) | `R0` | `dense[c4][intfloat/multilingual-e5-large]` | 89,64% | 95,36% | 0,7986 | 0,8195 |
| `C4` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c4][word]` | 92,14% | 96,43% | 0,8371 | 0,8556 |
| `C4` | `E0` (BM25 tách từ) | `R1` | `bm25[c4][word]+r1` | 86,07% | 86,43% | 0,8276 | 0,8357 |
| `C4` | `E2` (`Vietnamese_Embedding_v2`) | `R1` | `dense[c4][AITeamVN/Vietnamese_Embedding_v2]+r1` | 92,86% | 93,93% | 0,8882 | 0,8975 |
| `C4` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c4]+r1` | 94,29% | 95,36% | 0,9022 | 0,9110 |
| `C4` | `E4` (`multilingual-e5-large`) | `R1` | `dense[c4][intfloat/multilingual-e5-large]+r1` | 94,29% | 95,36% | 0,8998 | 0,9097 |
| `C4` | `E5` (Hybrid BM25+BGE-M3) | `R1` | **`hybrid[c4][word]+r1`** | **95,71%** | 96,43% | **0,9153** | **0,9253** |

### 3.3. Toàn bộ 30/30 cấu hình chính Giai đoạn A trên `zalo_test` (`n = 280` câu trả lời được / 400 câu test, kho thu hẹp 61.334 điều luật)

| Phân đoạn (`C`) | Truy xuất (`E`) | Xếp hạng (`R`) | Mã phương pháp trong cache | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---:|---:|---:|---:|
| `C1` (cửa sổ 256) | `E0` (BM25 tách từ) | `R0` | `bm25[c1][word]` | 76,43% | 87,50% | 0,6289 | 0,6573 |
| `C1` | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c1]` | 81,07% | 93,04% | 0,6457 | 0,6795 |
| `C1` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c1][word]` | 85,36% | 95,54% | 0,7045 | 0,7354 |
| `C1` | `E0` (BM25 tách từ) | `R1` | `bm25[c1][word]+r1` | 82,14% | 87,50% | 0,6634 | 0,7000 |
| `C1` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c1]+r1` | 87,32% | 93,04% | 0,7111 | 0,7484 |
| `C1` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c1][word]+r1` | 89,46% | 95,54% | 0,7207 | 0,7597 |
| `C3` (câu ≤ 256) | `E0` (BM25 tách từ) | `R0` | `bm25[c3][word]` | 76,43% | 89,64% | 0,6262 | 0,6539 |
| `C3` | `E3` (`BAAI/bge-m3`, **Neo**) | `R0` | `dense[c3]` | 81,43% | 92,68% | 0,6229 | 0,6642 |
| `C3` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c3][word]` | 85,36% | 95,54% | 0,6939 | 0,7276 |
| `C3` | `E0` (BM25 tách từ) | `R1` | `bm25[c3][word]+r1` | 83,21% | 89,64% | 0,6720 | 0,7086 |
| `C3` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c3]+r1` | 87,68% | 92,68% | 0,6977 | 0,7401 |
| `C3` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c3][word]+r1` | 88,39% | 95,54% | 0,7077 | 0,7486 |
| `C4` (nguyên điều luật) | `E0` (BM25 tách từ) | `R0` | `bm25[c4][word]` | 73,93% | 88,04% | 0,5779 | 0,6096 |
| `C4` | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c4]` | 80,54% | 93,04% | 0,6458 | 0,6745 |
| `C4` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c4][word]` | 87,86% | **96,25%** | 0,7159 | 0,7502 |
| `C4` | `E0` (BM25 tách từ) | `R1` | `bm25[c4][word]+r1` | 84,46% | 88,04% | 0,6922 | 0,7276 |
| `C4` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c4]+r1` | 86,96% | 93,04% | 0,7111 | 0,7463 |
| `C4` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c4][word]+r1` | 87,68% | **96,25%** | 0,7124 | 0,7468 |
| **`C5` (ViStructChunk)** | `E0` (BM25 tách từ) | `R0` | `bm25[c5][word]` | 79,64% | 91,96% | 0,7242 | 0,7359 |
| **`C5` (ViStructChunk)** | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c5]` | 86,07% | 94,11% | 0,7455 | 0,7695 |
| **`C5` (ViStructChunk)** | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c5][word]` | 89,82% | 95,89% | **0,8188** | 0,8352 |
| **`C5` (ViStructChunk)** | `E0` (BM25 tách từ) | `R1` | `bm25[c5][word]+r1` | 88,39% | 91,96% | 0,7820 | 0,8054 |
| **`C5` (ViStructChunk)** | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c5]+r1` | 90,54% | 94,11% | 0,7998 | 0,8245 |
| **`C5` (ViStructChunk)** | `E5` (Hybrid BM25+BGE-M3) | `R1` | **`hybrid[c5][word]+r1`** | **91,61%** | 95,89% | 0,8132 | **0,8369** |
| `C5_nohead` (bỏ tiêu đề) | `E0` (BM25 tách từ) | `R0` | `bm25[c5_nohead][word]` | 76,25% | 90,54% | 0,6241 | 0,6515 |
| `C5_nohead` | `E3` (`BAAI/bge-m3`) | `R0` | `dense[c5_nohead]` | 78,75% | 91,96% | 0,5873 | 0,6297 |
| `C5_nohead` | `E5` (Hybrid BM25+BGE-M3) | `R0` | `hybrid[c5_nohead][word]` | 83,39% | 95,18% | 0,6870 | 0,7167 |
| `C5_nohead` | `E0` (BM25 tách từ) | `R1` | `bm25[c5_nohead][word]+r1` | 81,96% | 90,54% | 0,6220 | 0,6657 |
| `C5_nohead` | `E3` (`BAAI/bge-m3`) | `R1` | `dense[c5_nohead]+r1` | 79,11% | 91,96% | 0,6323 | 0,6633 |
| `C5_nohead` | `E5` (Hybrid BM25+BGE-M3) | `R1` | `hybrid[c5_nohead][word]+r1` | 78,75% | 95,18% | 0,6336 | 0,6629 |

### 3.4. Phát hiện chính từ Giai đoạn A (RQ1, RQ2, RQ3)

1. **Đột phá của `ViStructChunk (C5)` và phép khử tiêu đề (`C5` vs `C5_nohead`) trên miền pháp luật (`RQ1 / H1a`):**
   - Trên `zalo_test`, `C5` vượt xa `C1`, `C3` và `C4` trên mọi phương pháp truy xuất: với `dense` (`BAAI/bge-m3`, `R0`), `C5` đạt **Recall@5 = `86,07%`, nDCG@5 = `0,7695`** so với `C3` (`Recall@5 = 81,43%`, `nDCG@5 = 0,6642`, **+10,53 điểm nDCG@5**) và `C4` (`Recall@5 = 80,54%`, `nDCG@5 = 0,6745`, **+9,50 điểm nDCG@5**).
   - **Phép thử khử tiêu đề (`C5` vs `C5_nohead`):** Khi giữ nguyên ranh giới cắt theo Khoản/Điểm nhưng **bỏ tiêu đề phân cấp** (`[Văn bản | Chương | Mục | Điều | Khoản]`), hiệu năng của `C5_nohead` tụt mạnh xuống `Recall@5 = 78,75%`, `nDCG@5 = 0,6297` ở `dense` (thấp hơn `C5` tới **13,98 điểm nDCG@5** và thấp hơn cả `C3`) và ở `hybrid+r1` tụt từ **`0,8369` (`C5`) xuống `0,6629` (`C5_nohead`, -17,40 điểm nDCG@5)**! Nguyên nhân: một Khoản/Điểm đứng rời rạc thường chỉ chứa quy định chi tiết (*"Phạt tiền từ 800.000 đồng đến 1.000.000 đồng đối với hành vi..."*) mà mất tên văn bản và tiêu đề Điều luật; cả Bi-Encoder lẫn Cross-Encoder (`R1`) đều cần tiêu đề phân cấp để khớp chủ đề pháp lý của truy vấn.
2. **Hiệu quả của Truy xuất lai (`E5 = Hybrid[word]`) và so sánh các mô hình nhúng (`RQ2`):**
   - Trên cả hai miền, `E5 (Hybrid BM25 tách từ + BGE-M3)` luôn vượt mọi mô hình đơn lẻ (`E0, E2, E3, E4`) ở `R0`.
   - Trên `viquad_test` (`R0`), `E4 (multilingual-e5-large)` nhỉnh hơn `E3 (BAAI/bge-m3)` và `E2 (Vietnamese_Embedding_v2)` khoảng `+2,9–4,4` điểm nDCG@5, nhưng sau khi qua reranker `R1`, khoảng cách giữa `E3+R1` (`nDCG@5 = 0,9100` ở `C3`) và `E4+R1` (`0,9131`) thu hẹp còn `0,0031`.
3. **Tác động của Xếp hạng lại (`R1 = bge-reranker-v2-m3`, `RQ3`):**
   - Trên `viquad_test`, `R1` nâng nDCG@5 của mọi phương pháp thêm `+4,3` đến `+12,1` điểm (đỉnh cao là `hybrid[c4][word]+r1` với **Recall@5 = `95,71%`, nDCG@5 = `0,9253`** và `hybrid[c3][word]+r1` với **Recall@5 = `95,00%`, nDCG@5 = `0,9158`**).
   - Trên `zalo_test`, `R1` phát huy hiệu quả mạnh nhất khi chunk mang đầy đủ ngữ cảnh phân cấp (`C5`), đưa `dense[c5]+r1` lên **Recall@5 = `90,54%`, nDCG@5 = `0,8245`** và `hybrid[c5][word]+r1` lên **Recall@5 = `91,61%`, nDCG@5 = `0,8369`**.

Chỉ lưu số liệu tổng hợp lên Git; log runtime và JSONL nằm trong thư mục `results/` và `data/retrieval_cache/` được bỏ qua theo `.gitignore`.
