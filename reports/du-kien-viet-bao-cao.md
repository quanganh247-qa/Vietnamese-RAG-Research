# Tổng hợp Dữ kiện & Số liệu Chuẩn để Viết Báo cáo (Source of Truth)

> Tài liệu này gom toàn bộ thông tin quan trọng, số liệu thực đo đã xác minh (`0` số ước lượng/bịa), kết quả kiểm định thống kê, phân tích lỗi và chi tiết kỹ thuật của đề tài **Vietnamese RAG Research** để tra cứu trực tiếp khi viết khóa luận / bài báo / slide bảo vệ.

---

## 1. Thông tin tổng quan đề tài & Phạm vi thực nghiệm

- **Tên đề tài:** *Ảnh hưởng của chiến lược phân đoạn, truy xuất và xếp hạng lại đến độ chính xác và ảo giác trong hệ thống RAG tiếng Việt*.
- **Kho mã nguồn:** `https://github.com/quanganh247-qa/Vietnamese-RAG-Research`
- **Hai đóng góp chính:**
  1. **`ViStructChunk (C5)`:** Chiến lược phân đoạn nhận biết cấu trúc pháp lý Việt Nam (*Điều / Khoản / Điểm*, ≤ 256 token) kèm gắn tiêu đề phân cấp cha (*Tên văn bản + Số & Tiêu đề Điều*), được kiểm chứng bằng biến thể ablation **`C5_nohead`** (giữ nguyên ranh giới cắt, chỉ bỏ tiêu đề cha).
  2. **Chỉ số `RAH` (Retrieval-Attributable Hallucination):** $\text{RAH}(k) = H_{\text{gold}}(k) - H_{\text{gold}}(\text{oracle})$ dùng bộ ba điều kiện `closed_book / cấu hình / oracle` để tách phần ảo giác do truy xuất khỏi sàn ảo giác nội tại của LLM.
- **Hai quy mô thực nghiệm đã hoàn thành 100%:**
  - **Phạm vi 30 ngày (đóng băng `400` câu/bộ):** `60` cấu hình Phase A + `16` cấu hình Phase B (`9` Zalo + `7` ViQuAD = `6.160` câu trả lời, `4.480` lượt Judge hợp lệ, `0` lỗi JSON).
  - **Mở rộng Toàn bộ Dữ liệu — Full Datasets (`6.910` câu hỏi thực, gấp `3,5×` đề cương gốc `2.000` câu):** `60` cấu hình Phase A (`207.300` dòng truy xuất) + `18` cấu hình Phase B (`8` ViQuAD + `10` Zalo = **`59.382` câu trả lời**, **`42.887` lượt Judge hợp lệ `99,98%`**).

---

## 2. Dữ liệu & Kiểm soát rò rỉ (Data Hygiene)

| Bộ dữ liệu | Nguồn gốc | Kho tài liệu | Tập `dev` (hiệu chỉnh) | Tập `Full Test` | Tỷ lệ Có / Không đáp án | Số cụm Cluster Bootstrap | Trùng lặp `dev ∩ test` |
|---|---|---:|---:|---:|---|---:|---:|
| **UIT-ViQuAD 2.0** | Split `validation` đầy đủ | `5.311` đoạn | `100` câu | **`3.814` câu** | `2.653` (69,6%) / `1.161` (30,4%) | `19` bài Wikipedia (`title`) | **`0`** |
| **Zalo Legal 2021** | `train_question_answer.json` (`3.196` câu gốc − `100` dev) | `61.425` điều (`699` điều loại bỏ để tạo câu không đáp án) | `100` câu | **`3.096` câu** | `2.167` (70,0%) / `929` (30,0%) | `2.117` nhóm liên thông (`gold_group`) | **`0`** |

---

## 3. Cấu hình Phần cứng, Mô hình & Hiệu chỉnh Judge

- **Mô hình nhúng (Embeddings):**
  - `E0`: `BM25Okapi` tách từ `underthesea` (triển khai chỉ mục đảo nén cột CSC bằng NumPy thuần khớp `< 1e-12` với `rank_bm25`, tăng tốc `8,1×` cho kho `320.841` đoạn).
  - `E2`: `AITeamVN/Vietnamese_Embedding_v2` (chỉ Phase A ViQuAD).
  - `E3`: `BAAI/bge-m3` (`1024-d`, `max_seq_length = 512`, `bf16`).
  - `E4`: `intfloat/multilingual-e5-large` (chỉ Phase A ViQuAD).
  - `E5`: `Hybrid` (`0,5 × minmax(Dense E3) + 0,5 × minmax(BM25[word])`).
- **Xếp hạng lại (Reranker):** `R0` (không rerank) vs `R1` (`BAAI/bge-reranker-v2-m3`, top-20 $\rightarrow$ top-5).
- **Mô hình sinh & LLM-as-Judge:** `unsloth/Qwen3.5-9B-GGUF:Q4_K_M` chạy qua `llama.cpp` (`llama-server`, `temperature = 0`, `seed = 0`, `--flash-attn on`, `--cache-type-k q8_0 --cache-type-v q8_0`, `top-k = 5`, trần `CTX_LIMIT = 1.024` token/đoạn).
- **Hiệu chỉnh Judge với nhãn người (Blind Human Grading trên `100` mẫu `dev`):**
  - Ban đầu `JUDGE_MAX_CHARS = 3000` cắt mất Khoản 3–10 của điều luật dài trên Zalo $\rightarrow$ đã nâng lên `JUDGE_MAX_CHARS = 15000` (khớp trần `4.000` token của `oracle`).
  - **Kết quả Cohen's $\kappa$ trên `100` mẫu `dev`** (vượt xa ngưỡng cổng $\kappa \ge 0,60$):
    - **Tổng hợp (`n = 100`):** $\kappa(H_{\text{gold}}) = \mathbf{0,8163}$, $\kappa(\text{Correctness}) = \mathbf{0,8519}$.
    - **ViQuAD dev (`n = 50`):** $\kappa(H_{\text{gold}}) = 0,7216$, $\kappa(\text{Correctness}) = 0,8623$.
    - **Zalo dev (`n = 50`):** $\kappa(H_{\text{gold}}) = 0,8764$, $\kappa(\text{Correctness}) = 0,8324$.
- **Phần cứng thực nghiệm:** Google Colab `NVIDIA A100-SXM4-40GB` và `NVIDIA L4 (23 GB)`.

---

## 4. Số liệu Giai đoạn A — Truy xuất (`60` cấu hình, Full Datasets)

*(Nguồn: [reports/full_phase_a_summary.json](full_phase_a_summary.json), Hình: [fig1_full_phase_a_heatmap.svg](figures/fig1_full_phase_a_heatmap.svg))*

### 4.1. Các mốc tốt nhất & Ablation chính
- **UIT-ViQuAD 2.0 Full (`n = 2.653` câu có đáp án):**
  - Tốt nhất: **`hybrid[c4][word]+r1`** — `Recall@5 = 96,49%`, `Recall@20 = 97,63%`, `MRR@10 = 0,9102`, **`nDCG@5 = 0,9233`**.
  - `hybrid[c3][word]+r1`: `Recall@5 = 96,19%`, `nDCG@5 = 0,9195` (`C4 − C3 = +0,0039 [+0,0018, +0,0060]`, $p_{\text{Holm}} = 0,0368$).
  - `Hybrid vs BM25 (C3)`: `0,8545` vs `0,7292` (**`+0,1253 [+0,0884, +0,1612]`**, $p_{\text{Holm}} = 0,0004$).
  - `R1 vs R0 (C3 Dense)`: `0,8952` vs `0,7742` (**`+0,1210 [+0,0998, +0,1410]`**, $p_{\text{Holm}} = 0,0004$).
- **Zalo Legal Full (`n = 2.167` câu có đáp án):**
  - Tốt nhất: **`dense[c5]+r1`** (`nDCG@5 = 0,8369`, `Recall@5 = 90,13%`, `Recall@20 = 93,98%`, `MRR@10 = 0,8234`) và **`hybrid[c5][word]+r1`** (`nDCG@5 = 0,8355`, **`Recall@5 = 90,50%`**, **`Recall@20 = 94,34%`**, `MRR@10 = 0,8199`).
  - So với các chiến lược cắt khác (ở `hybrid + r1`): `c1 = 0,8113`, `c3 = 0,8056`, `c4 = 0,7752`, `c5_nohead = 0,7412`.
  - **Ablation H1b (`c5` vs `c5_nohead` trên `n = 2.167`):**
    - `Dense R0`: `0,7811` vs `0,7179` $\rightarrow$ **`+0,0632 [+0,0455, +0,0832]`**, $p_{\text{Holm}} = \mathbf{0,0007}$.
    - `Dense R1`: `0,8369` vs `0,7429` $\rightarrow$ **`+0,0941 [+0,0739, +0,1193]`**, $p_{\text{Holm}} = \mathbf{0,0007}$.
    - `Hybrid R1`: `0,8355` vs `0,7412` $\rightarrow$ **`+0,0943 [+0,0742, +0,1186]`**, $p_{\text{Holm}} = \mathbf{0,0007}$.
  - **H1 (`c5` vs `c3`):** `Dense R0`: `+0,0606 [+0,0440, +0,0783]`, $p_{\text{Holm}} = 0,0007$; `Hybrid R1`: `+0,0299 [+0,0131, +0,0513]`, $p_{\text{Holm}} = 0,0007$.

---

## 5. Số liệu Giai đoạn B — Độ chính xác, Ảo giác & `RAH` (`18` cấu hình, Full Datasets)

*(Nguồn: [reports/full_phase_b_summary.json](full_phase_b_summary.json), Hình: [fig2_full_phase_b_h_gold_ci.svg](figures/fig2_full_phase_b_h_gold_ci.svg), [fig3_full_rah_by_domain.svg](figures/fig3_full_rah_by_domain.svg))*

### 5.1. UIT-ViQuAD 2.0 Full (`3.814` câu; `2.653` có đáp án; `21.218 / 21.224` Judge hợp lệ)

| Cấu hình | `Correctness` (95% CI) | `F1` | `Contains Gold` | `H_gold` (95% CI) | `H_ctx` | `False Refusal` | `Correct Refusal` | `RAH` ghép cặp (95% CI) | `RAH / H_gold` | `p50` (s) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `closed_book` | `0,1870 [0,1416, 0,2407]` | 0,0644 | 4,03% | `75,04% [69,62%, 79,29%]` | — | 74,59% | 87,60% | — | — | 1,35 |
| `C3-E0-R0` | `1,4054 [1,2790, 1,5372]` | 0,3781 | 54,50% | `17,93% [14,75%, 20,95%]` | 2,09% | 24,09% | 75,28% | `+5,77% [+3,97%, +7,41%]` | 38,6% | 5,64 |
| `C1-E3-R0` | `1,4685 [1,3938, 1,5513]` | 0,3854 | 56,01% | `20,11% [16,09%, 23,79%]` | 1,80% | 20,35% | 73,82% | `+7,63% [+5,12%, +9,86%]` | 45,3% | 6,01 |
| `C3-E3-R0` *(neo)* | `1,4955 [1,4284, 1,5675]` | 0,3906 | 56,88% | `20,68% [17,15%, 23,83%]` | 1,76% | 18,66% | 72,18% | `+7,97% [+6,01%, +9,64%]` | 46,8% | 6,05 |
| `C3-E5-R0` | `1,5586 [1,4760, 1,6474]` | 0,4116 | 59,56% | `21,11% [17,50%, 24,76%]` | 2,05% | 15,53% | 70,97% | `+8,85% [+6,45%, +11,43%]` | 47,9% | 6,10 |
| `C3-E3-R1` | `1,5633 [1,4794, 1,6482]` | 0,4139 | 59,74% | `21,84% [17,55%, 25,94%]` | 2,08% | 14,89% | 69,08% | `+9,54% [+6,69%, +12,17%]` | 49,6% | 6,17 |
| **`C4-E5-R1`** | **`1,5973 [1,5099, 1,6867]`** | **0,4222** | **61,48%** | `22,24% [17,68%, 26,44%]` | 2,30% | **13,00%** | 69,60% | `+9,83% [+6,90%, +12,49%]` | 50,5% | 6,96 |
| `oracle` | `1,6882 [1,6125, 1,7600]` | 0,4595 | 65,70% | `11,01% [9,36%, 12,63%]` | 1,08% | 12,63% | — | — | — | 3,31 |

### 5.2. Zalo Legal Full (`3.096` câu; `2.167` có đáp án; `21.669 / 21.670` Judge hợp lệ)

| Cấu hình | `Correctness` (95% CI) | `H_gold` (95% CI) | `H_ctx` | `False Refusal` | `Correct Refusal` | Nhầm điều luật | `RAH` ghép cặp (95% CI) | `RAH / H_gold` | `p50` (s) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `closed_book` | `0,2164 [0,1919, 0,2429]` | `84,12% [81,45%, 86,47%]` | — | 58,14% | 57,16% | 17,75% | — | — | 1,65 |
| `C5_nohead-E3-R0` | `1,2381 [1,1526, 1,3095]` | `22,00% [19,29%, 24,93%]` | 2,84% | 27,00% | 59,42% | 3,35% | `+18,30% [+15,65%, +21,22%]` | **90,6%** | 6,95 |
| `C3-E0-R0` | `1,3069 [1,2487, 1,3653]` | `18,62% [15,91%, 21,61%]` | 3,94% | 26,17% | 59,85% | 4,81% | `+15,46% [+12,65%, +18,42%]` | **88,9%** | 10,20 |
| `C3-E3-R0` *(neo)* | `1,4338 [1,3640, 1,4935]` | `17,58% [15,18%, 20,10%]` | 3,64% | 20,21% | 57,05% | 4,11% | `+13,76% [+11,30%, +16,32%]` | **88,3%** | 10,81 |
| `C4-E3-R0` | `1,4476 [1,3430, 1,5336]` | `17,62% [15,15%, 20,24%]` | 4,33% | 20,12% | 57,05% | 6,35% | `+13,38% [+11,05%, +15,83%]` | **88,3%** | 16,71 |
| `C5-E3-R0` | `1,4451 [1,3770, 1,5080]` | `20,43% [17,95%, 23,34%]` | 3,83% | 17,95% | 54,47% | **3,21%** | `+17,02% [+14,29%, +19,85%]` | **89,9%** | 9,19 |
| `C3-E5-R0` | `1,4707 [1,4049, 1,5284]` | **17,49%** `[15,25%, 19,76%]` | 3,44% | 18,23% | 55,76% | 4,23% | `+14,09% [+11,77%, +16,66%]` | **88,2%** | 10,52 |
| `C3-E3-R1` | `1,5242 [1,4466, 1,5877]` | `18,07% [15,56%, 20,72%]` | 3,55% | 15,46% | 52,96% | 3,77% | `+14,67% [+12,19%, +17,70%]` | **88,6%** | 10,68 |
| **`C5-E5-R1`** | **`1,5265 [1,4554, 1,5881]`** | `18,57% [16,12%, 21,16%]` | **3,38%** | **15,27%** | 51,78% | **3,27%** | `+15,64% [+13,33%, +18,14%]` | **88,9%** | 9,27 |
| `oracle` | `1,6567 [1,6172, 1,6906]` | `2,06% [1,23%, 2,98%]` | 5,15% | 14,95% | — | 1,95% | — | — | 9,12 |

---

## 6. Bảng Tổng kết Kiểm định 4 Giả thuyết (`H1–H4`, `10.000` hoán vị, Holm–Bonferroni)

| Giả thuyết | Cặp kiểm định chính | Kết quả thực đo (`Full Datasets`) | $p_{\text{Holm}}$ | Trạng thái |
|---|---|---|---:|---|
| **H1 (Chunking)** | ViQuAD: `C3-E3-R0` vs `C1-E3-R0`<br>Zalo (Phase A): `C5` vs `C3` (`Dense R0` / `Hybrid R1`) | ViQuAD `Correctness`: `+0,0264 [+0,0007, +0,0480]`<br>Zalo `nDCG@5`: `+0,0606` (`R0`) / `+0,0299` (`R1`) | `0,0019`<br>`0,0007` | **Xác nhận** |
| **H1b (Tiêu đề cha `ViStructChunk`)** | Zalo: `C5-E3-R0` vs `C5_nohead-E3-R0`<br>Zalo: `WrongArt` `C5-E3-R0` vs `C4-E3-R0` | `Correctness`: **`+0,2073 [+0,1693, +0,2456]`**<br>`nDCG@5 (Hybrid+R1)`: **`+0,0943`**<br>Nhầm điều luật: **`3,21%`** vs `6,35%` (giảm 50%) | **`0,0008`**<br>**`0,0007`** | **Xác nhận rất mạnh** |
| **H2 (Retriever)** | `Dense` vs `BM25` và `Hybrid` vs `Dense` (cả 2 miền) | ViQuAD: `+0,0902` (`E3>E0`), `+0,0630` (`E5>E3`)<br>Zalo: `+0,1269` (`E3>E0`), `+0,0369` (`E5>E3`) | `0,0006`<br>`0,0008 / 0,0270` | **Xác nhận trên cả 2 miền** |
| **H3 (Reranker R1)** | `C3-E3-R1` vs `C3-E3-R0` (cả 2 miền) | ViQuAD: **`+0,0687 [+0,0363, +0,0994]`**<br>Zalo: **`+0,0904 [+0,0629, +0,1184]`** | **`0,0006`**<br>**`0,0008`** | **Xác nhận trên cả 2 miền** |
| **H4 (RAH liên miền)** | Tỷ phần `RAH / H_gold` giữa Zalo Legal và ViQuAD | **Zalo: `88,2% – 90,6%`** (`oracle = 2,06%`)<br>**ViQuAD: `38,6% – 50,5%`** (`oracle = 11,01%`) | CI 95% dương chặt trên mọi cấu hình | **Xác nhận nổi bật** |
| **Best vs Anchor** | `C4-E5-R1` (ViQuAD) & `C5-E5-R1` (Zalo) vs `C3-E3-R0` | ViQuAD: **`+0,1018`** (`94,6%` oracle)<br>Zalo: **`+0,0928`** (`92,1%` oracle) | **`0,0006`**<br>**`0,0008`** | **Vượt trội có ý nghĩa** |

---

## 7. Phân tích Định tính 30 ca Ảo giác (`H_gold = 1`) & Chi phí Hệ thống

- **Phân bố 30 ca mẫu (`15` ViQuAD + `15` Zalo, `seed = 0`, [reports/phieu/hallucination_30_cases.md](phieu/hallucination_30_cases.md)):**
  - **Zalo Legal (`n = 15`):** `13/15` (**`86,7%`**) quy cho truy xuất/phân đoạn — trong đó **`4. Nhầm điều luật` chiếm `7/15` (`46,7%`)** (điển hình là Nghị định `100/2019/NĐ-CP`: chunk `C3` mất tiêu đề Điều 5/6/7/8 khiến LLM lấy mức phạt xe máy/xe đạp trả lời cho xe ô tô), `1. Truy xuất sai` (`3/15`), `2. Chunk cắt mất khoản` (`2/15`), `3. Nhiễu đoạn khác` (`1/15`), `5. Lỗi tầng sinh` (`2/15`).
  - **ViQuAD (`n = 15`):** `6/15` (`40,0%`) là lỗi nội tại tầng sinh/judge (`8/15 = 53,3%` xuất hiện cả ở `oracle`), `5/15` (`33,3%`) nhiễu đoạn cùng bài, `3/15` truy xuất sai, `1/15` chunk cắt mất thông tin, `0/15` nhầm điều luật.
- **Chi phí chỉ mục & độ trễ ([reports/cost_summary.json](cost_summary.json)):**
  - `Zalo C5 (ViStructChunk)`: `326.759` chunks, độ dài TB **`91,7` token** (`0,00% > 512`), chỉ mục FP32 `1.276 MB`, tốc độ nhúng `1.507,7` chunk/s trên A100, độ trễ sinh `p50 = 9,19–9,27 s` trên L4 (`16 slots`) — **nhanh gần gấp `2×` so với `C4` nguyên điều (`p50 = 16,71 s`, `17,45%` điều luật vượt `512` token, `1.660` đoạn bị cắt ở `1.024` token)**.
  - Cross-Encoder `R1` (`bge-reranker-v2-m3`) trên A100 chỉ tốn thêm **`~38–39 ms/truy vấn`** (`p50`).

---

## 8. Khung Khuyến nghị Đa tiêu chí (Biên Pareto + MCDM + Độ nhạy `±0,1`, Mục 5.9) & Hồi quy Logistic (Mục 5.8)

*(Nguồn: [reports/pareto_mcdm_summary.json](pareto_mcdm_summary.json), [reports/logistic_summary.json](logistic_summary.json), Hình: [fig4_pareto_mcdm.svg](figures/fig4_pareto_mcdm.svg))*

### 8.1. Biên Pareto & Điểm có trọng số 3 kịch bản (Full Datasets)
- **Zalo Legal Full (`8` cấu hình RAG):**
  - **3 cấu hình bị trội (loại khỏi khuyến nghị):** `C3-E0-R0` (bị trội hoàn toàn bởi **`C5-E5-R1`** trên cả 3 tiêu chí), `C3-E3-R0` và `C4-E3-R0` nguyên điều (cả hai bị trội bởi `C3-E5-R0`).
  - **5 cấu hình Biên Pareto:** `C5-E5-R1`, `C3-E5-R0`, `C3-E3-R1`, `C5-E3-R0`, `C5_nohead-E3-R0`.
  - **Kết quả 3 kịch bản & Phân tích độ nhạy (dao động trọng số `±0,10`):**
    - *Cân bằng (`0,34 / 0,33 / 0,33`):* **`C5-E5-R1`** hạng `#1` (`score = 0,7136`, **độ ổn định `100,0%` — `27/27` điểm lưới**).
    - *Tra cứu nhanh (`0,20 / 0,30 / 0,50`):* **`C5-E5-R1`** hạng `#1` (`score = 0,6416`, **độ ổn định `88,9%` — `24/27` điểm lưới**, vì chunk `C5` ngắn nên `p50 = 9,27 s` nhanh hơn cả `C3` và `C4`).
    - *Pháp luật / Y tế (`0,60 / 0,30 / 0,10`):* **`C3-E5-R0`** hạng `#1` (`score = 0,8463`, độ ổn định `77,8%` — `14/18` điểm lưới; `C5-E5-R1` thắng ở `3/18` điểm lưới và có lỗi nhầm điều luật thấp hơn `3,27%` vs `4,23%`).
- **UIT-ViQuAD 2.0 Full (`6` cấu hình RAG):**
  - Cả `6/6` cấu hình đều nằm trên Biên Pareto. Trong không gian 3 tiêu chí `(H_gold, Correctness, Latency)`, `C3-E0-R0` đạt điểm MCDM `#1` (`stability = 81,5%–100%`) chủ yếu vì có `H_gold` danh nghĩa thấp nhất (`17,93%`) và độ trễ thấp nhất (`5,64 s`), **nhưng phải trả giá bằng tỷ lệ từ chối sai rất cao (`false_refusal = 24,09%` vs `13,00%` của `C4-E5-R1`)**. Khi đặt ràng buộc `false_refusal ≤ 16%`, cấu hình khuyến nghị tối ưu là **`C4-E5-R1`** (độ đúng cao nhất) hoặc **`C3-E5-R0`** (cân bằng, không cần Reranker).

### 8.2. Hồi quy Logistic (`H_gold ~ Recall@5 + Reranker + Hybrid + Chunking`, Mục 5.8)
- **Zalo Legal Full (`n = 13.859` quan sát, `McFadden R² = 0,1128`):**
  - **`Recall@5`:** $\beta = -2,8754$ ($z = -35,66$, $p < 10^{-10}$, **Odds Ratio = `0,056`**) $\rightarrow$ Truy xuất trúng điều luật vàng vào Top-5 làm **giảm `94,4%` odds bị ảo giác** (giảm `18` lần).
  - Sau khi kiểm soát `Recall@5`, `has_reranker` ($p = 0,4238$) và `is_hybrid` ($p = 0,7481$) **không còn tác động trực tiếp** $\Rightarrow$ lợi ích giảm ảo giác của Hybrid và Reranker đi **hoàn toàn gián tiếp qua `Recall@5`**.
  - **`is_c5_nohead`:** $\beta = +0,3220$ ($z = +4,23$, $p < 0,0001$, **`OR = 1,380`**) $\rightarrow$ Bỏ tiêu đề phân cấp làm **tăng trực tiếp `+38%` odds ảo giác ngay cả khi `Recall@5` không đổi**.
- **UIT-ViQuAD 2.0 Full (`n = 13.088` quan sát, `McFadden R² = 0,0558`):**
  - **`Recall@5`:** $\beta = -2,8660$ ($z = -23,58$, $p < 10^{-10}$, **Odds Ratio = `0,057`**) $\rightarrow$ Truy xuất trúng đoạn vàng làm **giảm `94,3%` odds bị ảo giác**.

---

## 9. Điểm nhấn Kỹ thuật & Tối ưu hoá Triển khai (cho mục Thiết kế Hệ thống)

1. **BM25 ma trận thưa CSC (`_FastBM25Okapi` trong [src/ragvi/retrieval.py](../src/ragvi/retrieval.py)):** Cài đặt chỉ mục đảo nén cột bằng NumPy thuần, khớp tuyệt đối `< 1e-12` với `rank_bm25.BM25Okapi`, giảm thời gian chấm điểm `c5_nohead` (`320.841` đoạn × `3.096` câu) từ `176 phút` xuống `21,7 phút` (**`8,1×`**).
2. **Tối ưu suy luận LLM trên Colab ([scripts/colab_job.sh](../scripts/colab_job.sh), [src/ragvi/judge.py](../src/ragvi/judge.py)):**
   - Nén KV cache `--cache-type-k q8_0 --cache-type-v q8_0` kết hợp `--flash-attn on --batch-size 4096`, nâng song song lên `16 slots` (`L4`) / `20–24 slots` (`A100`).
   - Pre-deduplication prompt trước `ThreadPoolExecutor` + sắp xếp theo `(qid, độ dài prompt)` để tối đa hoá LCP KV-prefix cache của `llama-server` (đạt `99,4–219,7 dòng/phút` trên A100).
3. **Ứng dụng Demo Gradio ([src/ragvi/app.py](../src/ragvi/app.py)):** Hỗ trợ tra cứu trực tiếp theo miền (mặc định `C5` cho pháp luật, `C3` cho Wikipedia), hiển thị top-5 đoạn căn cứ kèm trích dẫn nguồn; kiểm thử tự động **`70 passed, 1 skipped`**.

---

## 10. Danh mục File & Biểu đồ sẵn sàng chèn vào Báo cáo

| Thành phần | Đường dẫn | Nội dung |
|---|---|---|
| Bản thảo báo cáo đầy đủ | `reports/ban-thao.md` | Khung bài báo/báo cáo hoàn chỉnh |
| Báo cáo chi tiết thực nghiệm | `reports/benchmark-colab-2026-11-20.md` | Mục 1–9 (`400` câu) + Mục 10 (`6.910` câu) |
| Số liệu JSON Full Phase A | `reports/full_phase_a_summary.json` | 60 cấu hình + 95% CI + kiểm định Holm |
| Số liệu JSON Full Phase B | `reports/full_phase_b_summary.json` | 18 cấu hình + 95% CI + RAH + kiểm định Holm |
| Số liệu Pareto & MCDM | `reports/pareto_mcdm_summary.json` | Biên Pareto, điểm 3 kịch bản & độ nhạy ±0,1 |
| Số liệu Hồi quy Logistic | `reports/logistic_summary.json` | Hồi quy `H_gold ~ Recall@5 + ...` (`n = 26.947`) |
| Số liệu chi phí & độ trễ | `reports/cost_summary.json` | Kích thước chỉ mục, thông lượng, `p50/p95` |
| Phiếu phân tích 30 ca lỗi | `reports/phieu/hallucination_30_cases.md` | 30 ca `H_gold = 1` gán nhãn 5 nguyên nhân |
| Hình 1 (Full Phase A) | `reports/figures/fig1_full_phase_a_heatmap.svg` | Bản đồ nhiệt `nDCG@5` (60 cấu hình) |
| Hình 2 (Full Phase B) | `reports/figures/fig2_full_phase_b_h_gold_ci.svg` | `Correctness` & `H_gold` kèm 95% CI (18 cấu hình) |
| Hình 3 (Full RAH) | `reports/figures/fig3_full_rah_by_domain.svg` | Phân rã `RAH` vs `Oracle` giữa 2 miền |
| Hình 4 (Biên Pareto) | `reports/figures/fig4_pareto_mcdm.svg` | Biên Pareto 3 tiêu chí trên cả 2 miền |
