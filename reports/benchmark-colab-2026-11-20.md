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

## 2. Kết quả tầng sinh câu trả lời và LLM-as-a-Judge sơ bộ (`Qwen3.5-9B-GGUF:Q4_K_M`)

Toàn bộ **2.737 lượt sinh câu trả lời** và **2.211 lượt chấm điểm Judge** (`231` ViQuAD dev + `840` ViQuAD test + `300` Zalo dev + `840` Zalo test) hoàn tất với **0 câu thiếu (`n_judge_missing = 0`) và 0 lỗi định dạng JSON (`n_judge_errors = 0`, 100% hợp lệ)**.

> **Lưu ý:** Điểm Judge dưới đây là **điểm sơ bộ chưa hiệu chỉnh nhãn người** (`judge_calibrated: false`), dùng để kiểm tra toàn bộ luồng đầu-cuối trước khi đối chiếu 100 câu dev với nhãn người (Cohen's $\kappa$, Ngày 12–13).

### 2.1. Tập phát triển (`viquad_dev` & `zalo_dev`)

| Tập | Cấu hình | `n` (`n_ans`/`n_unans`) | `correct_refusal` | `fabrication` | `false_refusal` | `contains_gold` | `EM` | `F1` | `correctness` (0–2) | `H_gold` (`n`) | `H_ctx` (`n`) | `RAH` vs `oracle` (`n_pairs`) | Tốc độ (`q/min`) | Trung vị `p50` (s) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `viquad_dev` | `closed_book` | 100 (77/23) | 65,22% | 34,78% | 71,43% | 2,60% | 0,00% | 0,0531 | 0,1948 | 68,18% (22) | — | — | 54,00 | 0,713 |
| `viquad_dev` | `oracle` | 77 (77/0) | — | — | 7,79% | 59,74% | 0,00% | 0,4311 | 1,7532 | 14,08% (71) | 0,00% (71) | — | 30,71 | 1,695 |
| `viquad_dev` | `C3-E3-R0` | 100 (77/23) | 60,87% | 39,13% | 16,88% | 49,35% | 2,60% | 0,4012 | 1,5195 | 28,12% (64) | 4,69% (64) | **+11,11%** (63) | 16,33 | 3,096 |
| `zalo_dev` | `closed_book` | 100 (100/0) | — | — | 53,00% | — | — | — | 0,1100 | 95,74% (47) | — | — | 35,83 | 1,198 |
| `zalo_dev` | `oracle` | 100 (100/0) | — | — | 11,00% | — | — | — | 0,6800 | 61,80% (89) | 60,67% (89) | — | 16,89 | 3,119 |
| `zalo_dev` | `C3-E3-R0` | 100 (100/0) | — | — | 43,00% | — | — | — | 0,6400 | 54,39% (57) | 1,75% (57) | **+3,70%** (54) | 13,91 | 3,488 |

### 2.2. Tập kiểm tra đóng băng (`viquad_test` & `zalo_test`)

| Tập | Cấu hình | `n` (`n_ans`/`n_unans`) | `correct_refusal` | `fabrication` | `false_refusal` | `contains_gold` | `EM` | `F1` | `correctness` (0–2) | `H_gold` (`n`) | `H_ctx` (`n`) | `RAH` vs `oracle` (`n_pairs`) | Tốc độ (`q/min`) | Trung vị `p50` (s) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `viquad_test` | `closed_book` | 400 (280/120) | 88,33% | 11,67% | 75,00% | 3,93% | 0,36% | 0,0642 | 0,1964 | 77,14% (70) | — | — | 55,51 | 0,695 |
| `viquad_test` | `oracle` | 280 (280/0) | — | — | 12,50% | 57,14% | 0,71% | 0,4326 | 1,7000 | 10,20% (245) | 1,22% (245) | — | 28,64 | 2,002 |
| `viquad_test` | `C3-E3-R0` | 400 (280/120) | 64,17% | 35,83% | 15,71% | 52,14% | 2,86% | 0,3982 | 1,5643 | 19,07% (236) | 2,54% (236) | **+6,76%** (222) | 16,00 | 3,217 |
| `zalo_test` | `closed_book` | 400 (280/120) | 57,50% | 42,50% | 55,71% | — | — | — | 0,1000 | 92,74% (124) | — | — | 38,82 | 0,778 |
| `zalo_test` | `oracle` | 280 (280/0) | — | — | 14,29% | — | — | — | 1,1607 | 31,67% (240) | 31,67% (240) | — | 17,04 | 3,379 |
| `zalo_test` | `C3-E3-R0` | 400 (280/120) | 56,67% | 43,33% | 27,50% | — | — | — | 1,0679 | 34,48% (203) | 10,34% (203) | **+6,35%** (189) | 10,47 | 4,664 |

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

Chỉ lưu số liệu tổng hợp lên Git; log runtime và JSONL nằm trong thư mục `results/` và `data/retrieval_cache/` được bỏ qua theo `.gitignore`.
