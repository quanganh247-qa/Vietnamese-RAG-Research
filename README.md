# Vietnamese RAG Research

Nghiên cứu ảnh hưởng của phân đoạn, truy xuất và xếp hạng lại đến độ đúng và ảo giác trên ViQuAD và Zalo Legal. Xem [quyết định thiết kế](reports/quyet-dinh-thiet-ke.md) cho phạm vi chính thức.

## Chạy Colab từ terminal

Cần Bash (dùng Git Bash trên Windows), [`uv`](https://docs.astral.sh/uv/getting-started/installation/) và tài khoản có quyền cấp Colab runtime. Không cần WSL, SSH, hay mở notebook trên website Colab. `uvx` tự lấy [Colab CLI](https://github.com/googlecolab/google-colab-cli) 0.8.0; lần đầu có thể cần xác thực tài khoản Google theo hướng dẫn CLI. Đã xác thực tài khoản và cấp được L4 từ Git Bash trên Windows; dự án Colab CLI chưa công bố hỗ trợ Windows.

```bash
# Smoke test RAG trên GPU; cần data/eval/viquad/{dev,corpus}.jsonl
bash colab_run.sh

# Benchmark cấu hình neo trên toàn bộ câu hỏi nguồn + dev/test đóng băng
bash colab_run.sh benchmark

# CPU EDA: chỉ truyền URL chia sẻ không chứa khóa/token; không lưu URL vào repo
RAGVI_DRIVE_URL='<URL thư mục Drive chia sẻ>' bash colab_run.sh eda
```

- `rag` và `benchmark` thử **G4 → A100 → L4 → T4** khi Google từ chối cấp máy hoặc endpoint cấp máy trả 502/503/504. Lỗi tài khoản, cài đặt hay mô hình dừng lượt chạy. Có thể tiêu compute units theo tài khoản.
- Trên Colab, `scripts/colab_job.sh` cài môi trường `uv` khóa bằng `uv.lock`, nhúng ViQuAD với BGE-M3, biên dịch llama.cpp CUDA và tải Qwen2.5-7B-Instruct GGUF Q4_K_M (hai tệp). Chạy `C3-E3-R0` và `closed_book` trên 10 câu dev (5 có/5 không có đáp án), `oracle` chỉ trên 5 câu có đáp án. Đây **không phải** lượt Phase B chính thức. Model, lượng tử hóa và cách chạy khác Transformers/NF4; không gộp kết quả.
- `benchmark` cần `data/processed/{viquad,zalo_legal}` và các file đóng băng trong `data/eval/`. Truy xuất C3–E3–R0 trên cả ba split nguồn ViQuAD và 788 truy vấn có nhãn duy nhất của Zalo; test nguồn ViQuAD chỉ chạy truy xuất, không chấm điểm. Sau đó chạy ba điều kiện trên toàn bộ dev/test đóng băng của cả hai bộ (oracle chỉ cho câu trả lời được), dùng Qwen3-8B GGUF Q4_K_M làm judge riêng. Không huấn luyện. Điểm judge chưa hiệu chỉnh; không dùng làm kết quả Phase B.
- Mỗi lượt tải JSONL/log hoặc `eda.ipynb` về thư mục mới dưới `results/colab/` và dừng runtime. Với `benchmark`, xem `summary.json` (điểm theo split, mẫu số, tỷ lệ từ chối, độ trễ, RAH ghép cặp) và `model.txt` (phiên bản). Với Zalo, test đóng băng dùng kho thu hẹp theo D1/D6; dev và truy xuất nguồn vẫn dùng kho đầy đủ. Lượt dài cần giữ terminal đang chạy để tải kết quả; nếu CLI không dừng được, làm theo lệnh `stop` in ra cuối lượt.

## Đọc dữ liệu và kiểm thử tại máy

[Notebook EDA](notebooks/06_eda_du_lieu.ipynb) có lưu kết quả đo từ dữ liệu thật; không cần GPU. Để chạy lại từ thư mục repo:

```bash
uv sync --locked --python 3.12 --extra eda
uv run --no-sync jupyter nbconvert --to notebook --execute \
  --output eda-output.ipynb --output-dir results/colab notebooks/06_eda_du_lieu.ipynb
uv run --locked --extra eda pytest -q
```

EDA đọc `data/` hoặc đường dẫn tuyệt đối `RAGVI_DATA_DIR`. Lần đầu cần tải tokenizer BGE-M3. Với mạng doanh nghiệp dùng CA riêng, có thể đặt `REQUESTS_CA_BUNDLE` đến CA bundle đã được tổ chức cấp; không tắt kiểm tra TLS.

## Kết quả benchmark

[Bảng truy xuất Colab L4](reports/benchmark-colab-2026-11-20.md) tách rõ split nguồn và tập đánh giá đóng băng. Không đưa dữ liệu câu hỏi hoặc log runtime lên Git.

## Chỉ số cần cải thiện

| Ưu tiên | Chỉ số | Dùng để quyết định gì? |
|---|---|---|
| Chính | **`H_gold` ↓, correctness ↑** | Câu trả lời ít mệnh đề thiếu bằng chứng vàng hơn và trả lời đúng hơn (judge 0/1/2, đối chiếu nhãn người). |
| Ràng buộc | **Fabrication ↓, false refusal ↓** | Không bịa khi kho thiếu bằng chứng, nhưng vẫn trả lời khi có bằng chứng. Báo cả hai, không tối ưu chỉ số ảo giác bằng cách từ chối nhiều hơn. |
| Chẩn đoán | **Recall@5 / nDCG@5 ↑**, Recall@20 | Kiểm tra bằng chứng có vào top-5 và đứng cao không; Recall@20 giúp phân biệt thiếu ứng viên với xếp hạng kém. Điểm truy xuất không phải điểm câu trả lời. |
| Phân tích | **RAH**, `H_ctx`, EM/F1, độ trễ | RAH so `H_gold` với oracle trên cùng câu trả lời được; EM/F1 bổ sung cho ViQuAD; theo dõi chi phí xếp hạng lại. |

Bước kế tiếp: hiệu chỉnh judge (mốc κ ≥ 0,6 cho `H_gold` theo phạm vi thu hẹp), sau đó đo liệu mức tăng Recall@5 của reranker Zalo dev **63% → 78%** có chuyển thành ít ảo giác hơn và độ đúng cao hơn không. So cùng tập câu hỏi/cùng backend, báo cáo hiệu số có khoảng tin cậy.
