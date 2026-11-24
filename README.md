# Vietnamese RAG Research

Nghiên cứu thực nghiệm có kiểm soát về ảnh hưởng của **phân đoạn (chunking)**, **truy xuất (BM25 / Dense / Hybrid)** và **xếp hạng lại (reranking)** đến **độ chính xác** và **ảo giác (`H_gold`, `H_ctx`, `RAH`, nhầm điều luật)** trên tiếng Việt.

## Kết quả chính (Full Datasets — `6.910` câu hỏi thực)

Đánh giá hoàn chỉnh trên toàn bộ **UIT-ViQuAD 2.0 validation (`3.814` câu)** và **Zalo Legal 2021 full (`3.096` câu trên `61.425` điều luật)** với `60` cấu hình truy xuất (Giai đoạn A) và `18` cấu hình đầu cuối (`59.382` câu trả lời, `42.887` lượt chấm Judge hợp lệ `99,98%` ở Giai đoạn B):

| Miền | Cấu hình tốt nhất | `Recall@5` | `nDCG@5` | `Correctness` (0–2) | `H_gold` | `RAH / H_gold` | Nhầm điều luật |
|---|---|---:|---:|---:|---:|---:|---:|
| **Zalo Legal Full** (`n = 2.167`) | **`C5-E5-R1`** *(ViStructChunk + Hybrid + R1)* | **90,50%** | **0,8355** | **1,5265** *(92,1% oracle)* | 18,57% | **88,9%** | **3,27%** *(C5-E3: 3,21%)* |
| **UIT-ViQuAD 2.0 Full** (`n = 2.653`) | **`C4-E5-R1`** *(Para + Hybrid + R1)* | **96,49%** | **0,9233** | **1,5973** *(94,6% oracle)* | 22,24% | **50,5%** | — |

- **Ablation `ViStructChunk (C5)` vs `C5_nohead` (Zalo Full):** Gắn tiêu đề phân cấp *Văn bản / Điều* tăng **`+0,0943`** `nDCG@5` ở Hybrid+R1 ($p_{\text{Holm}} = 0,0007$), tăng **`+0,2073`** `Correctness` ($p_{\text{Holm}} = 0,0008$), và giảm một nửa lỗi nhầm điều luật so với `C4` nguyên điều (`3,21%` vs `6,35%`).
- **Phân rã `RAH` theo miền (H4):** Trên văn bản pháp luật (Zalo), **`88,2% – 90,6%`** ảo giác bắt nguồn từ tầng truy xuất (`oracle` chỉ `2,06%`); trên Wikipedia (ViQuAD), tỷ phần này chỉ chiếm **`38,6% – 50,5%`** (`oracle = 11,01%`).

## Tài liệu & Báo cáo

- **[Bản thảo báo cáo hoàn chỉnh](reports/ban-thao.md)** — Tổng hợp đầy đủ phương pháp, kết quả Full Datasets (`6.910` câu), kiểm định thống kê Holm–Bonferroni, phân tích lỗi và khuyến nghị cấu hình.
- **[Báo cáo chi tiết thực nghiệm & số liệu](reports/benchmark-colab-2026-11-20.md)** — Bao gồm cả phạm vi đóng băng `400` câu/bộ (Mục 1–9) và mở rộng Full Datasets (Mục 10).
- **[Phiếu phân tích định tính 30 ca ảo giác](reports/phieu/hallucination_30_cases.md)** — Phân loại 5 nhóm nguyên nhân và đối chiếu chéo với `RAH`.
- **Số liệu JSON:** [full_phase_a_summary.json](reports/full_phase_a_summary.json), [full_phase_b_summary.json](reports/full_phase_b_summary.json), [phase_a_summary.json](reports/phase_a_summary.json), [phase_b_summary.json](reports/phase_b_summary.json), [cost_summary.json](reports/cost_summary.json).
- **Biểu đồ SVG (`reports/figures/`):** [fig1_full_phase_a_heatmap.svg](reports/figures/fig1_full_phase_a_heatmap.svg), [fig2_full_phase_b_h_gold_ci.svg](reports/figures/fig2_full_phase_b_h_gold_ci.svg), [fig3_full_rah_by_domain.svg](reports/figures/fig3_full_rah_by_domain.svg).

## Chạy Demo Gradio & Kiểm thử cục bộ

```bash
# Cài đặt môi trường & chạy 70 unit tests
uv sync --locked --python 3.12 --extra eda
PYTHONPATH=src .venv/bin/python -m pytest -q tests --ignore=tests/test_llamacpp.py

# Chạy giao diện Demo hỏi đáp RAG (mặc định C5 cho pháp luật, C3 cho Wikipedia)
PYTHONPATH=src .venv/bin/python -m ragvi.app

# Tổng hợp lại toàn bộ bảng thống kê & 3 hình SVG Full Dataset (chỉ dùng CPU)
PYTHONPATH=src .venv/bin/python scripts/build_full_reports.py
```

## Tái lập Thực nghiệm trên Google Colab từ Terminal

Yêu cầu Bash, [`uv`](https://docs.astral.sh/uv/getting-started/installation/) và tài khoản Google Colab (`google-colab-cli==0.8.0`):

```bash
# Giai đoạn A Full (tách riêng 2 phiên song song)
bash colab_run.sh full_phase_a_viquad "<URL thư mục Drive dữ liệu>"
bash colab_run.sh full_phase_a_zalo   "<URL thư mục Drive dữ liệu>"

# Giai đoạn B Full (Generation & Judge với KV cache q8_0 + pre-dedup theo qid)
bash colab_run.sh full_viquad_b_gen   "<URL thư mục Drive dữ liệu>"
bash colab_run.sh full_viquad_b_judge "<URL thư mục Drive dữ liệu>"
bash colab_run.sh full_zalo_b_gen     "<URL thư mục Drive dữ liệu>"
bash colab_run.sh full_zalo_b_judge   "<URL thư mục Drive dữ liệu>"
```
