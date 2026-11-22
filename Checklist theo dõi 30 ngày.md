# Checklist theo dõi kế hoạch 30 ngày

Dùng cùng `Kế hoạch chi tiết 30 ngày.md`. Mục tiêu từng ngày được chép nguyên từ file đó.

## Cách dùng

- Cuối mỗi ngày (2 phút): đổi `[ ]` thành `[x]` nếu đạt mục tiêu, điền ngày đạt thực tế và số giờ đã làm. Chỉ đánh dấu khi mục tiêu đạt đủ, không đánh dấu khi "gần xong".
- Cuối mỗi tuần (10 phút): điền bảng đánh giá tuần và đánh dấu cổng kiểm tra.
- Ghi ở cột Ghi chú mọi thay đổi so với kế hoạch: bậc cắt đã áp dụng, quyết định đã chọn, lý do trễ.

## Quy tắc phản ứng khi trễ

| Tình trạng cuối ngày | Việc làm |
|---|---|
| Trễ 1 ngày | Bù trong cuối tuần gần nhất; không cắt phạm vi |
| Trễ 2 ngày trở lên | Áp dụng bậc cắt kế tiếp trong thang cắt của `Kế hoạch 30 ngày (hạn 11-12).md`, ghi vào Ghi chú |
| Trễ 2 ngày trở lên vào 25/11 | Chuyển sang phương án dự phòng (bài protocol kèm kết quả truy xuất) |
| Số giờ thực vượt 3 giờ mỗi ngày trong 3 ngày liền | Kế hoạch đang quá tải; cắt phạm vi thay vì tiếp tục thêm giờ |

## Tuần 1 (12/11–18/11) – Thiết kế, dữ liệu, truy xuất

| Xong | Ngày | Mục tiêu cuối ngày | Ngày đạt | Giờ | Ghi chú |
|---|---|---|---|---|---|
| [ ] | Thứ Năm 12/11 | Dữ liệu đã xử lý nằm trên Drive; chín quyết định D1–D9 được ghi thành văn bản; người hướng dẫn đã nhận ba câu hỏi về thứ phải nộp, phạm vi và hình thức nộp sản phẩm | | | |
| [x] | Thứ Sáu 13/11 | Có bốn chỉ số truy xuất (Recall@5, Recall@20, MRR@10, nDCG@5) của BM25 trên 788 truy vấn Zalo, tính bằng gói mã mới; đã chọn cách tách từ cho BM25 | 14/11 | | 788 truy vấn, kho đầy đủ: BM25 âm tiết 0,7005 / 0,8433 / 0,5160 / 0,5529; BM25 tách từ (`bm25[word]`, chạy 18/11) 0,7367 / 0,8909 / 0,5489 / 0,5855. underthesea ước lượng 19,2 phút cả kho (< 30 phút) nên E0 dùng tách từ |
| [x] | Thứ Bảy 14/11 | Có bảng so sánh BM25, dense và hybrid trên Zalo ở mức điều luật; biết tốc độ nhúng (tài liệu mỗi giây) | 14/11 | | Mức điều luật, 788 truy vấn, kho đầy đủ. Recall@5 / Recall@20 / MRR@10 / nDCG@5: BM25 âm tiết 0,7005 / 0,8433 / 0,5160 / 0,5529; BM25 tách từ 0,7367 / 0,8909 / 0,5489 / 0,5855; dense bge-m3 0,8147 / 0,9226 / 0,6525 / 0,6847; hybrid âm tiết 0,8763 / 0,9581 / 0,6986 / 0,7376; hybrid tách từ (`hybrid[word]`) 0,8839 / 0,9657 / 0,7000 / 0,7409. Nhúng kho Zalo 18,7 điều/giây (3.288,8s), kho ViQuAD 20,9 đoạn/giây (254,1s trên T4) |
| [x] | Chủ nhật 15/11 | Ba cách phân đoạn C1, C3, C4 sinh được chunk cho cả hai kho; có bảng số chunk và độ dài chunk | 15/11 | | Zalo (`03_tuan1_hoan_tat.ipynb` cell 13): C1 113.962 chunk (0,00% >512), C3 128.733 (0,00% >512), C4 61.425 (trung vị 223, p95 946, max 67.395, **17,45% >512**). ViQuAD 5.311 đoạn (cell 12): C1 6.481 (tb 175,3; trung vị 179,0; p95 256; max 257; 0,00% >512), C3 6.504 (tb 174,7; trung vị 179,5; p95 249; max 256; 0,00% >512), C4 5.311 (tb 213,9; trung vị 191,0; p95 370; max 2.091; 0,77% >512) |
| [x] | Thứ Hai 16/11 | Tập test Zalo (280 trả lời được + 120 không trả lời được), tập dev (100 câu) và kho thu hẹp đã lưu trên Drive kèm seed và mã băm | 14/11 | | Seed 0: 280 + 120 test, 100 dev, 288 dự trữ; 442 nhóm; 89 điều luật bị loại. Lưu ở `data/eval/zalo/` kèm manifest SHA-256. Từ 20/11 không xuất `reserve.jsonl`; 288 câu dư vẫn ở nguồn. Kho thu hẹp lưu dưới dạng danh sách điều luật bị loại (`removed_doc_ids.json`), không chép lại kho |
| [x] | Thứ Ba 17/11 | Tập test và dev ViQuAD đã đóng băng; biết tỷ lệ câu "không trả lời được" vẫn trả lời được từ kho ở cả hai bộ | 18/11 | | Đã dựng ViQuAD seed 0: 280 + 120 test, 100 dev (77 trả lời được, từ 3 bài), kho 5.311 đoạn, 0 câu mất đáp án. Đã chấm D6 (`reports/phieu/d6_*.md`): **ViQuAD 2/30 = 6,7%** (≤ 20%); **Zalo 8/30 = 26,7%**, loại thêm bản trùng mã `nd-cp` ↔ `nđ-cp` trong kho thu hẹp còn **6/30 = 20,0%** (≤ 20%). Cả hai tập test đã đóng băng |
| [x] | Thứ Tư 18/11 | C5 và biến thể không tiêu đề sinh được chunk cho toàn bộ kho Zalo; biết tỷ lệ điều luật parse được | 18/11 | | C5 và C5 không tiêu đề: 326.759 chunk mỗi loại (0,00% >512 ở cả hai); 84,7% điều luật có ít nhất một khoản. Token trung bình 91,7 so với 64,5; C5 max 717 (tiêu đề cha trung vị 23,0; p95 43; max 460 do một số thông tư đặt cả nội dung vào `title`, như `24/2019/tt-bgdđt+2`). Đã đối chiếu 30 điều luật (`reports/phieu/c5_review.md`): **30/30 đúng (100%)**, 0 khoản nhận nhầm, 0 bỏ sót |

**Cổng kiểm tra cuối giai đoạn:**

- [x] Hai tập test đã đóng băng
- [x] Năm cách phân đoạn trên Zalo và ba trên ViQuAD chạy được
- [x] BM25, dense, hybrid chạy được

**Đánh giá giai đoạn:**

| Chỉ số | Kế hoạch | Thực tế |
|---|---|---|
| Số mục tiêu đạt | 7 | |
| Số mục tiêu đạt đúng ngày | 7 | |
| Tổng số giờ | 14 | |
| Số ngày trễ tích lũy đến cuối giai đoạn | 0 | |
| Bậc cắt phạm vi đã áp dụng | Không | |
| Điều chỉnh cho giai đoạn sau | – | |

## Tuần 2 (19/11–25/11) – Sinh câu trả lời và judge

| Xong | Ngày | Mục tiêu cuối ngày | Ngày đạt | Giờ | Ghi chú |
|---|---|---|---|---|---|
| [x] | Thứ Năm 19/11 | Đã chọn một mô hình sinh, kèm số liệu so sánh trên 50 câu dev | 18/11 | | `04_tuan2_sinh_va_judge.ipynb` cell 28 (50 câu dev ViQuAD: 35 trả lời được + 15 không, oracle 4-bit): ban đầu chọn `Qwen2.5-7B-Instruct` (`correct_refusal 0,80` vs `0,533` của `Qwen3-8B`); ngày 20/11 chủ đề tài thống nhất nâng cấp cả mô hình sinh và judge lên **`Qwen/Qwen3.5-9B`** (`unsloth/Qwen3.5-9B-GGUF:Q4_K_M`, tắt thinking) |
| [x] | Thứ Sáu 20/11 | Một lệnh chạy được từ câu hỏi đến câu trả lời cho cấu hình neo, closed-book và oracle; có ước lượng số giờ GPU cho Giai đoạn B | 21/11 | | Đã chạy trọn bộ `C3-E3-R0`, `closed_book`, `oracle` trên **cả dev và test** của ViQuAD và Zalo bằng `bash colab_run.sh benchmark` với `unsloth/Qwen3.5-9B-GGUF:Q4_K_M` qua `llama.cpp` continuous batching (`--parallel 8` trên L4, `--parallel 12` trên A100). Tốc độ sinh `C3-E3-R0`: `16,0–16,3 câu/phút` (ViQuAD), `10,5–13,9 câu/phút` (Zalo) → ước lượng Giai đoạn B (6.400 lượt): **~6,5–10,2 giờ GPU** (< 20 giờ → giữ nguyên 400 câu mỗi bộ) |
| [ ] | Thứ Bảy 21/11 | Reranker R1 chạy được trên dev; 24 lượt nhúng cho Giai đoạn A đã khởi động (8 lượt `BAAI/bge-m3` xếp trước) và đang lưu đệm | | | Đã xác minh E2/E4 (`XLMRobertaTokenizer`, E2=8192, E4=512) và chạy xong R1 trên dev (Zalo dev Recall@5 tăng `0,6300 → 0,7800`, nDCG@5 `0,4712 → 0,6034`). Đã xong **6/8** lượt `BAAI/bge-m3` (ViQuAD c1/c3/c4, Zalo c1/c3/c4); còn `c5` và `c5_nohead` chuyển sang `05_tuan2_tiep_tuc.ipynb` với checkpoint mỗi 20.000 chunk + `bf16`/`fp16` |
| [x] | Chủ nhật 22/11 | Judge trả về JSON hợp lệ trên 20 câu dev; chỉ số "nhầm điều luật" chạy được | 21/11 | | `unsloth/Qwen3.5-9B-GGUF:Q4_K_M` (tắt thinking, `--parallel 12`) chấm xong toàn bộ **2.211/2.211 câu trả lời có đáp án** trên cả `viquad_{dev,test}` và `zalo_{dev,test}` với **100% JSON hợp lệ (`n_judge_errors = 0`, `n_judge_missing = 0`)**. Chỉ số "nhầm điều luật" (`wrong_article`) chạy trên toàn bộ Zalo dev/test ([bảng tổng hợp](reports/benchmark-colab-2026-11-20.md)) |
| [x] | Thứ Hai 23/11 | Có 100 câu trả lời dev đã xáo trộn để gán nhãn; 50 câu đầu đã có nhãn người | 22/11 | | Đã sinh 2 phiếu gán nhãn ẩn danh (`seed=0`, mã hóa cấu hình bằng `blind_id`) gồm 50 mẫu ViQuAD dev (`reports/phieu/human_dev_viquad.md`) và 50 mẫu Zalo dev (`reports/phieu/human_dev_zalo.md`); 50 mẫu đầu (ViQuAD dev) đã chấm độc lập xong (`Correctness`: 39 mẫu `2`, 4 mẫu `1`, 7 mẫu `0`; `H_gold=1`: 9/50) |
| [x] | Thứ Ba 24/11 | 100 câu có đủ nhãn người; có Cohen's κ giữa judge và người cho H_gold, H_ctx và correctness | 22/11 | | Đã chấm độc lập đủ 100/100 mẫu dev. Phát hiện `JUDGE_MAX_CHARS = 3000` cắt mất Khoản 3–10 của điều luật dài trên Zalo; sau khi nâng `JUDGE_MAX_CHARS = 15000` (khớp trần 4.000 token của `oracle`) và chấm lại các câu điều luật dài, **Cohen's κ trên 100 mẫu dev đạt: `κ(H_gold) = 0,8163`, `κ(correctness_linear) = 0,8519`, `κ(H_ctx) = 0,3871` (tỷ lệ đồng thuận tuyệt đối `H_ctx` đạt `72/76 = 94,74%`)**. Riêng ViQuAD dev (50 mẫu): `κ(H_gold) = 0,7216`, `κ(correctness) = 0,8623`; riêng Zalo dev (50 mẫu): `κ(H_gold) = 0,8764`, `κ(correctness) = 0,8324`, `κ(H_ctx) = 0,4776` |
| [ ] | Thứ Tư 25/11 | Có quyết định tiếp tục hay chuyển phương án dự phòng; prompt, cấu hình và tập test đã đóng băng (thẻ `freeze-b`); người hướng dẫn đã nhận bản tóm tắt thiết kế | | | |

**Cổng kiểm tra cuối giai đoạn:**

- [x] Pipeline đầu-cuối chạy được trên dev của cả hai bộ
- [ ] Tập test, prompt và danh sách cấu hình đã đóng băng
- [x] κ của H_gold từ 0,6 trở lên

**Đánh giá giai đoạn:**

| Chỉ số | Kế hoạch | Thực tế |
|---|---|---|
| Số mục tiêu đạt | 7 | |
| Số mục tiêu đạt đúng ngày | 7 | |
| Tổng số giờ | 14 | |
| Số ngày trễ tích lũy đến cuối giai đoạn | 0 | |
| Bậc cắt phạm vi đã áp dụng | Không | |
| Điều chỉnh cho giai đoạn sau | – | |

## Tuần 3 (26/11–02/12) – Chạy thực nghiệm

| Xong | Ngày | Mục tiêu cuối ngày | Ngày đạt | Giờ | Ghi chú |
|---|---|---|---|---|---|
| [ ] | Thứ Năm 26/11 | Có bảng Giai đoạn A kèm khoảng tin cậy cho mọi cấu hình dùng BM25, `BAAI/bge-m3` và hybrid (30 trên Zalo, 18 trên ViQuAD); các cấu hình E2 và E4 (20 + 12) có trong bảng hoặc có ngày hoàn thành không muộn hơn 02/12 | | | |
| [ ] | Thứ Sáu 27/11 | 3.600 lượt sinh trên Zalo đã chạy xong hoặc đang chạy mà không có lỗi định dạng; demo thô chạy được ở phần truy xuất (chọn cấu hình, hiển thị 5 đoạn căn cứ) | | | |
| [ ] | Thứ Bảy 28/11 | Đủ 6.400 câu trả lời, không thiếu, không trùng; có fabrication rate và false refusal sơ bộ | | | |
| [ ] | Chủ nhật 29/11 | Khoảng 4.480 câu trả lời cần chấm đều có điểm judge, hoặc được ghi rõ là lỗi | | | |
| [ ] | Thứ Hai 30/11 | Bảng kết quả một dòng cho mỗi cặp (cấu hình, câu hỏi) có đủ mọi chỉ số và qua được các kiểm tra hợp lý | | | |
| [ ] | Thứ Ba 01/12 | Có bảng chi phí: độ trễ (trung vị, phân vị 95), kích thước chỉ mục, môi trường chạy | | | |
| [ ] | Thứ Tư 02/12 | Không còn việc tồn của tuần 3; demo đã nối mô hình sinh và trả lời được 10 câu hỏi thử | | | |

**Cổng kiểm tra cuối giai đoạn:**

- [ ] Bảng Giai đoạn A đầy đủ
- [ ] Bảng kết quả Giai đoạn B đầy đủ, qua kiểm tra hợp lý
- [ ] Bảng chi phí
- [ ] Demo chạy được từ câu hỏi đến câu trả lời kèm căn cứ

**Đánh giá giai đoạn:**

| Chỉ số | Kế hoạch | Thực tế |
|---|---|---|
| Số mục tiêu đạt | 7 | |
| Số mục tiêu đạt đúng ngày | 7 | |
| Tổng số giờ | 14 | |
| Số ngày trễ tích lũy đến cuối giai đoạn | 0 | |
| Bậc cắt phạm vi đã áp dụng | Không | |
| Điều chỉnh cho giai đoạn sau | – | |

## Tuần 4 và nộp (03/12–11/12) – Phân tích và viết

| Xong | Ngày | Mục tiêu cuối ngày | Ngày đạt | Giờ | Ghi chú |
|---|---|---|---|---|---|
| [ ] | Thứ Năm 03/12 | Mọi chỉ số có khoảng tin cậy 95%; mọi so sánh trong họ đã ghi trước có giá trị p hiệu chỉnh Holm; có RAH cho từng cấu hình và từng miền | | | |
| [ ] | Thứ Sáu 04/12 | 30 trường hợp ảo giác đã gắn nguyên nhân; có ba hình, các bảng cuối cùng và bảng khuyến nghị có điều kiện theo miền; demo chạy mặc định bằng cấu hình khuyến nghị | | | |
| [ ] | Thứ Bảy 05/12 | Mọi tài liệu sẽ trích đã được xác minh từ nguồn gốc; có bản nháp mục phương pháp và thiết lập thực nghiệm | | | |
| [ ] | Chủ nhật 06/12 | Có bản nháp mục kết quả và thảo luận; mỗi câu hỏi RQ1–RQ4 có một kết luận kèm số liệu | | | |
| [ ] | Thứ Hai 07/12 | Có bản nháp mục giới thiệu và công trình liên quan | | | |
| [ ] | Thứ Ba 08/12 | Bản thảo đủ mọi mục, kể cả tóm tắt và hạn chế, và qua được danh sách kiểm tra nhất quán | | | |
| [ ] | Thứ Tư 09/12 | Người hướng dẫn đã nhận báo cáo hoàn chỉnh và demo; kho mã có README (cách chạy demo, cách tái lập từng bảng), video demo ngắn và thẻ phiên bản | | | |
| [ ] | Thứ Năm 10/12 | Mọi phản hồi ảnh hưởng đến kết luận đã được xử lý; nếu chưa có phản hồi, mọi con số trong mục kết quả đã được đối chiếu lại với bảng | | | |
| [ ] | Thứ Sáu 11/12 | Bài đã nộp; có danh sách việc còn lại cho khóa luận | | | |

**Cổng kiểm tra cuối giai đoạn:**

- [ ] Mọi con số trong bài có khoảng tin cậy và truy được về bảng kết quả
- [ ] Người hướng dẫn nhận báo cáo và demo trước hết ngày 09/12
- [ ] Đã nộp trước 12/12

**Đánh giá giai đoạn:**

| Chỉ số | Kế hoạch | Thực tế |
|---|---|---|
| Số mục tiêu đạt | 9 | |
| Số mục tiêu đạt đúng ngày | 9 | |
| Tổng số giờ | 18 | |
| Số ngày trễ tích lũy đến cuối giai đoạn | 0 | |
| Bậc cắt phạm vi đã áp dụng | Không | |
| Điều chỉnh cho giai đoạn sau | – | |

## Các điểm quyết định

| Xong | Ngày | Quyết định | Đã chọn | Lý do |
|---|---|---|---|---|
| [x] | 13/11 | BM25 tách từ hay theo âm tiết | Tách từ bằng underthesea | Quy tắc ghi trước: ước lượng 19,2 phút cho cả kho, dưới ngưỡng 30 phút (đo 14/11) |
| [x] | 17/11 | Có thay câu không trả lời được không | Không thay câu; loại thêm bản trùng mã `nd-cp` ↔ `nđ-cp` trong kho thu hẹp Zalo | ViQuAD 2/30 = 6,7% (≤ 20%). Zalo 8/30 = 26,7%, trong đó 2 câu do bản trùng `24/2020/nd-cp+*`; loại bản trùng còn 6/30 = 20,0% (≤ 20%), giữ nguyên 400 câu test (chốt 18/11) |
| [x] | 19/11 | Mô hình sinh | `Qwen/Qwen3.5-9B` (`unsloth/Qwen3.5-9B-GGUF:Q4_K_M`, tắt thinking) | Ngày 18/11 thử nghiệm ban đầu với `Qwen2.5-7B-Instruct`; ngày 20/11 chủ đề tài chốt nâng cấp lên `Qwen3.5-9B` kèm continuous batching qua `llama.cpp` |
| [x] | 20/11 | Giữ 400 hay giảm còn 300 câu mỗi bộ | Giữ nguyên 400 câu mỗi bộ | Tốc độ sinh `C3-E3-R0` đo thật 10,5–16,3 câu/phút (55,5 câu/phút ở `closed_book`) → ước lượng ~6,5–10,2 giờ GPU cho 6.400 lượt, dưới ngưỡng 20 giờ |
| [x] | 22/11 | Mô hình judge | `Qwen/Qwen3.5-9B` (`unsloth/Qwen3.5-9B-GGUF:Q4_K_M`, tắt thinking) | Chủ đề tài chốt dùng thống nhất `Qwen3.5-9B` cho cả sinh và judge (100% JSON hợp lệ trên 2.211/2.211 lượt chấm) |
| [ ] | 25/11 | Tiếp tục hay chuyển phương án dự phòng | | |

## Việc chờ người khác

| Xong | Việc | Gửi ngày | Hạn phản hồi | Nhận ngày |
|---|---|---|---|---|
| [ ] | Người hướng dẫn trả lời: thứ phải nộp, phạm vi thu hẹp, hình thức nộp sản phẩm | 12/11 | 16/11 | |
| [ ] | Người gán nhãn thứ hai nhận 100 câu (nếu có) | 23/11 | 26/11 | |
| [ ] | Người hướng dẫn góp ý bản tóm tắt thiết kế | 25/11 | 30/11 | |
| [ ] | Người hướng dẫn góp ý bản thảo | 09/12 | 10/12 | |

## Tổng kết sau khi nộp

| Chỉ số | Kế hoạch | Thực tế |
|---|---|---|
| Số mục tiêu ngày đạt | 30 | |
| Số mục tiêu đạt đúng ngày | 30 | |
| Tổng số giờ | 60 | |
| Số cổng kiểm tra đạt | 13 | |
| Bậc cắt phạm vi cao nhất đã dùng | Không | |
| Sản phẩm đã nộp | Demo, mã nguồn, kết quả đánh giá, bảng khuyến nghị, báo cáo | |

Ba việc tốn thời gian hơn dự kiến nhất (dùng để ước lượng lại `Kế hoạch 16 tuần.md`):

1. 
2. 
3. 

## Nhật ký thực hiện

### 20–21/11 – Colab CLI, hoàn tất baseline `Qwen3.5-9B` với continuous batching và khám phá dữ liệu bổ sung

- `colab_run.sh` điều phối G4 → A100 → L4 → T4. CLI đã xác thực và hoàn tất toàn bộ lượt `benchmark` trên L4 (23 GB) và A100 (40 GB) với **`unsloth/Qwen3.5-9B-GGUF:Q4_K_M`** (revision `1daf391c47cef14242f238b819fbe6fd500d624b`) qua `llama-server` (`--parallel 8/12 --cont-batching`, cổng `18080` để tránh trùng cổng `8080` nội bộ của Colab) và `ThreadPoolExecutor` trong `generate.py`/`judge.py`.
- Kết quả đầy đủ 6 tập truy xuất (`C3–E3–R0`), 2.737 câu trả lời (`closed_book`, `oracle`, `C3-E3-R0` trên `viquad_{dev,test}` và `zalo_{dev,test}`) và 2.211 lượt chấm Judge đã hiệu chỉnh (`JUDGE_MAX_CHARS = 15000`, **0 lỗi JSON, 0 câu thiếu**, Cohen's $\kappa(H_{\text{gold}}) = 0,8163$ và $\kappa(\text{correctness}) = 0,8519$ trên 100 mẫu dev) được ghi tại [bảng tổng hợp](reports/benchmark-colab-2026-11-20.md):
  - `viquad_test` (400 câu): `C3-E3-R0` đạt `F1 = 0,3982`, `contains_gold = 52,14%`, `correctness = 1,5643/2`, `H_gold = 19,07%`, `H_ctx = 2,54%`, `RAH = +6,76%` so với `oracle` (`H_gold = 10,20%`, `F1 = 0,4326`).
  - `zalo_test` (400 câu): `C3-E3-R0` đạt `correctness = 1,1821/2`, `false_refusal = 27,50%` (giảm từ `55,71%` ở `closed_book`), `H_gold = 25,12%`, `H_ctx = 7,39%`, `RAH = +17,46%` so với `oracle` (`H_gold = 4,58%`, `correctness = 1,6214/2`).
- Chạy `notebooks/06_eda_du_lieu.ipynb` trên bản dữ liệu thật đã tải về. BGE-M3 đếm 1.135.938 token trên 5.311 đoạn ViQuAD và 21.075.880 token trên 61.425 điều Zalo (tiêu đề + thân). Tỷ lệ dài hơn 512 token lần lượt 0,77% và 17,45%. Cụm gần câu chữ dev: ViQuAD 2/100 câu, Zalo 24/100 câu.
- Bỏ file dự trữ riêng của Zalo khỏi dữ liệu local và trình sinh tập eval; dữ liệu thô, tập đánh giá dev/test và các đầu ra notebook lịch sử giữ nguyên.

### 14/11 – Viết mã Tuần 1 (chưa có số liệu thực nghiệm)

Mã cho các ngày 13–18/11 đã viết xong ở máy và qua 26 test trên dữ liệu giả (`PYTHONPATH=src .venv/bin/python -m pytest -q tests`). Không mục tiêu ngày nào được đánh dấu, vì mục tiêu nào cũng đòi kết quả trên dữ liệu thật, mà dữ liệu chỉ có trên Drive. Chưa lần nào chạy thật: `load_from_disk`, mô hình `BAAI/bge-m3`, tokenizer bge-m3, `underthesea`.

| File | Nội dung | Ngày kế hoạch |
|---|---|---|
| `src/ragvi/metrics.py` | Recall@5, Recall@20, MRR@10, nDCG@5; mỗi điều luật vàng tính một lần | 13/11 |
| `src/ragvi/retrieval.py` | BM25 âm tiết, dense (đệm `.npy`), hybrid min–max α = 0,7, đo tốc độ underthesea, ghi JSONL nối tiếp | 13–14/11 |
| `src/ragvi/chunking.py` | C1, C3, C4, C5 và C5 không tiêu đề; thống kê số chunk, độ dài, tỷ lệ có khoản | 15/11, 18/11 |
| `src/ragvi/data.py` | Nạp kho Zalo (kể cả kho thu hẹp), tập đánh giá Zalo và ViQuAD kèm seed, SHA-256 | 16–17/11 |

Lệnh cần chạy trên Colab để lấy số liệu (`P` = thư mục `data/processed`, `O` = thư mục kết quả trên Drive):

```
PYTHONPATH=src python -m ragvi.retrieval $P/zalo_legal $O/retrieval --time-tokenizer
PYTHONPATH=src python -m ragvi.retrieval $P/zalo_legal $O/retrieval --methods bm25,dense,hybrid
PYTHONPATH=src python -m ragvi.chunking  $P/zalo_legal --methods c1,c3,c4,c5,c5_nohead
PYTHONPATH=src python -m ragvi.data zalo   $P/zalo_legal $O/eval_zalo   --seed 0
PYTHONPATH=src python -m ragvi.data viquad $P/viquad     $O/eval_viquad --seed 0
```

Điểm cần quyết định hoặc kiểm tra khi chạy thật:

- ViQuAD: bước làm sạch có thể làm lệch `answer_start`; mã định vị lại đáp án và loại câu không còn đáp án. Xem `labeled_rows − usable_questions` trong manifest.
- ViQuAD: dev đang trộn câu trả lời được và `is_impossible` (khác dev Zalo theo D1), và chưa có phần dự trữ để thay câu theo D6.
- C5: regex khoản `^\d+\.\s` có thể nhận nhầm danh sách đánh số nằm trong một điểm; chờ đối chiếu tay 30 điều.
- Lệnh `python -m ragvi.data` nay cần đối số đầu `zalo` hoặc `viquad`.

### 14/11 (đợt 2) – Rà soát, notebook Colab, sổ tay, chốt hybrid

Nhóm bốn agent Opus 5.5, trưởng nhóm Fable 5.2. Vẫn chưa có số liệu thực nghiệm; chưa mục tiêu ngày nào được đánh dấu.

| Việc | Kết quả | Ở đâu |
|---|---|---|
| Rà soát mã bằng thư viện thật (`datasets`, tokenizer `BAAI/bge-m3`, `underthesea`) trên dữ liệu tổng hợp đúng lược đồ | Sửa 2 lỗi trong phân đoạn (C1 chồng lấn một ký tự; C5 mất dòng tiêu đề Điều); 28 test qua. Ba CLI chạy được từ đầu đến cuối trên dữ liệu tổng hợp | `src/ragvi/chunking.py`, `tests/test_chunking.py` |
| Notebook chạy Tuần 1 trên Colab | 17 bước, chưa chạy lần nào | `notebooks/02_tuan1_truy_xuat_phan_doan.ipynb`, sinh bằng `scripts/build_colab_notebook.py` |
| Sổ tay giải thích từng thành phần | Có ví dụ tính tay, câu hỏi hội đồng, bảng kết quả trống chờ số liệu | `reports/so-tay-nghien-cuu.md` |
| Chốt công thức hybrid | α · dense + (1 − α) · BM25, min–max trên cả kho, α = 0,7 | `reports/quyet-dinh-thiet-ke.md`, Nhật ký thay đổi |

Việc tiếp theo của chủ đề tài: mở notebook 02 trong VS Code với kernel Colab, chạy từ trên xuống rồi lưu file; cell dense và hybrid cần runtime GPU. Trưởng nhóm đọc output trong file `.ipynb` để điền bảng kết quả và đánh dấu mục tiêu.

Vẫn chưa kiểm được: nhánh dense (`sentence_transformers` + trọng số bge-m3), lược đồ và kiểu dữ liệu thật trên Drive (ví dụ `query-id` trong qrels là chuỗi hay số), thời gian phân đoạn trên cả 61.425 điều luật.

Khoảng trống thiết kế cần quyết trước Giai đoạn A (26/11), xếp theo mức ảnh hưởng tới số liệu:

1. Tiêu chí chunk đúng của ViQuAD (phủ ít nhất 80% ký tự đáp án) chưa được cài đặt, và chưa rõ khi có nhiều đáp án vàng thì tính theo đáp án nào.
2. `ragvi.retrieval` mới chạy ở mức điều luật trên kho đầy đủ; chưa chạy ở mức chunk, chưa dùng kho thu hẹp, chưa lọc câu không trả lời được.
3. Dense cắt ở 512 token nhưng mã chưa báo tỷ lệ bị cắt (D7 yêu cầu). Ở mức điều luật, dense chỉ thấy phần đầu điều luật dài còn BM25 thấy toàn bộ.
4. Recall@k đếm theo chunk: với C5, 20 chunk đầu chứa ít điều luật khác nhau hơn C4, nên so Recall giữa các cách phân đoạn không cùng thước đo. Phải nêu rõ khi báo cáo.
5. "Không trả lời được" ở Zalo là điều luật vàng bị loại khỏi kho, còn ở ViQuAD đoạn gốc vẫn trong kho; fabrication rate của hai miền vì thế không so trực tiếp được.
6. ViQuAD: dev trộn cả câu `is_impossible` và chưa có phần dự trữ (lệch D1, D6); `ragvi.chunking` chưa có lệnh cho ViQuAD.

### 14/11 (đợt 3) – Lượt chạy đầu tiên trên dữ liệu thật

Chủ đề tài chạy `notebooks/02_tuan1_truy_xuat_phan_doan.ipynb` trên Colab. Dữ liệu đọc được và khớp số dòng mong đợi (61.425 điều luật, 818 dòng truy vấn, 788 mã duy nhất, 793 dòng qrels; ViQuAD 28.454 / 3.814 / 7.301). Đánh dấu đạt bốn mục tiêu: 13/11, 14/11, 16/11, 18/11 (mục 14/11 bổ sung sau khi notebook lưu lại lúc 11:35 có đủ output dense và hybrid). Số liệu đầy đủ nằm ở mục "Kết quả" của `reports/so-tay-nghien-cuu.md`.

Chưa xong:

- C1, C3, C4 trên ViQuAD (15/11): chưa có lệnh.
- Đọc tay 30 câu không trả lời được mỗi bộ (17/11) và đối chiếu tay 30 điều luật của C5 (18/11).
- BM25 tách từ bằng underthesea: đã chọn theo quy tắc nhưng chưa cài vào lệnh chạy.

Điều rút ra từ số liệu:

1. C4 (nguyên điều luật) có trung vị 223 token nhưng p95 là 946 và lớn nhất 67.395. Mô hình nhúng cắt ở 512 token, nên một phần đáng kể điều luật chỉ được nhúng phần đầu; tỷ lệ chính xác chưa đo.
2. Tiêu đề cha của C5 chiếm trung bình khoảng 27 token trên chunk có nội dung trung vị 47 token. Khi so C5 với C5 không tiêu đề, phần văn bản thêm vào là lớn so với nội dung.
3. C5 có chunk dài tới 717 token trong khi C5 không tiêu đề tối đa 257, tức có tiêu đề cha dài khoảng 460 token. Cần xem điều luật đó: nhiều khả năng trường `title` của nó chứa cả nội dung.
4. Nhúng mức điều luật đạt 18,7 điều luật/giây, tức 55 phút cho một lượt. C5 có 326.759 chunk, gấp 5,3 lần số văn bản; cần đo tốc độ trên chunk ngắn trước khi ước lượng 24 lượt nhúng của Giai đoạn A.
5. Tập dev ViQuAD chỉ gồm 3 bài Wikipedia (đúng cách lấy mẫu trong kế hoạch), nên hẹp về chủ đề khi dùng để chọn mô hình sinh.
6. Ở mức điều luật, hybrid cao hơn dense và dense cao hơn BM25 ở cả bốn chỉ số (Recall@5: 0,876 / 0,815 / 0,701). Đây là một lượt chạy trên 788 truy vấn, chưa có khoảng tin cậy hay kiểm định, nên chưa kết luận được về ý nghĩa thống kê.

### 15/11 – Mã cho phần còn lại của Tuần 1 (chưa chạy trên dữ liệu thật)

Ba agent Opus 5.5, trưởng nhóm Fable 5.2. 39 test qua; các lệnh mới đã chạy thử trên dữ liệu tổng hợp (BM25 và tách từ bằng underthesea thật; dense chưa chạy vì máy không có torch). Chưa có số liệu mới, chưa đánh dấu thêm mục tiêu nào.

| Việc | Phục vụ | Ở đâu |
|---|---|---|
| BM25 tách từ bằng underthesea, có đệm kho đã tách | Quyết định E0 (13/11) | `src/ragvi/retrieval.py`, tùy chọn `--tokenizer word` |
| Truy xuất trên tập test đã đóng băng với kho thu hẹp; câu không trả lời được vẫn có 20 kết quả đầu, chỉ số để trống | 16–17/11, chuẩn bị Giai đoạn A | `--run`, `--questions`, `--removed` |
| Truy xuất ViQuAD ở mức đoạn | 17/11 | đối số đầu là `corpus.jsonl` |
| Tiêu chí chunk đúng 80% của ViQuAD (chưa nối vào lệnh chạy) | D2 | `viquad_hits` trong `src/ragvi/metrics.py` |
| C1, C3, C4 trên ViQuAD; cột tỷ lệ chunk dài hơn 512 token; chẩn đoán tiêu đề cha dài nhất | 15/11, D7 | `src/ragvi/chunking.py` |
| Phiếu đối chiếu tay 30 điều luật của C5 | 18/11 | `python -m ragvi.chunking ... --review` |
| Phiếu đọc tay 30 câu không trả lời được mỗi bộ và lệnh đếm kết quả | 17/11, D6 | `src/ragvi/review.py` |
| Notebook chạy các bước trên | – | `notebooks/03_tuan1_hoan_tat.ipynb` (notebook 02 giữ nguyên làm bản ghi lượt 14/11) |

Việc tiếp theo của chủ đề tài: chạy notebook 03 từ trên xuống rồi lưu file. Cell tách từ cả kho mất khoảng 19 phút; cell ViQuAD cần GPU. Sau đó trưởng nhóm tách ba phiếu ra `reports/phieu/` để chủ đề tài đọc và chấm (30 điều luật C5, 30 câu Zalo, 30 câu ViQuAD).

Ba quyết định trưởng nhóm đã tự chốt, chủ đề tài cần xem lại (ghi ở Nhật ký thay đổi của `reports/quyet-dinh-thiet-ke.md`): cách tính chunk đúng của ViQuAD khi có nhiều đáp án; đoạn ViQuAD không ghép `title`; cách chuẩn hóa token của BM25 tách từ.

### 18/11 – Hoàn tất chạy `03_tuan1_hoan_tat.ipynb` trên T4 GPU và chấm 3 phiếu kiểm tra

Chủ đề tài chạy hoàn tất `notebooks/03_tuan1_hoan_tat.ipynb` trên Colab T4 GPU. Toàn bộ bảng kết quả truy xuất (`bm25`, `bm25[word]`, `dense`, `hybrid`, `hybrid[word]`) trên Zalo đầy đủ (788 câu), Zalo test kho thu hẹp (280/400 câu) và ViQuAD test mức đoạn (280/400 câu) cùng bảng phân đoạn hai kho đã được cập nhật vào `reports/so-tay-nghien-cuu.md`. Ba phiếu kiểm tra đã được trích ra `reports/phieu/` và chấm xong:

1. **Đối chiếu 30 điều luật C5 (`reports/phieu/c5_review.md`):** **30/30 điều luật parse đúng (100%)**, 0 khoản nhận nhầm, 0 bỏ sót khoản/điểm (gồm 3 điều không có khoản giữ nguyên 1 chunk, 3 điều có câu dẫn trước khoản 1 tách riêng `#0`, 5 điều có khoản >256 token tách chính xác xuống mức Điểm và câu).
2. **Đọc tay 30 câu không trả lời được của ViQuAD (`reports/phieu/d6_viquad.md`):** **2/30 câu (6,7%)** vẫn trả lời được từ top-5 `hybrid[word]` (`validation:0004-0047-0008` và `train:0106-0047-0008`, cả hai do đoạn gốc vẫn chứa thông tin trả lời khi hiểu theo ngữ nghĩa tự nhiên). Tỷ lệ 6,7% **không vượt ngưỡng 20%**, nên tập test ViQuAD chính thức đóng băng.
3. **Đọc tay 30 câu không trả lời được của Zalo (`reports/phieu/d6_zalo.md`):** **8/30 câu (26,7%)** vẫn trả lời được từ top-5 `hybrid[word]`, **vượt ngưỡng 20%**:
   - **2 câu (`b2b5d0355d1d8ffa676851892774378c`, `1d4d97918d405787a4183231832dc6ac`):** do kho Zalo có bản trùng mã của Nghị định 24/2020/NĐ-CP viết bằng chữ `d` không dấu (`24/2020/nd-cp+14` và `24/2020/nd-cp+12`), nên khi loại `24/2020/nđ-cp+*` thì bản trùng `nd-cp` vẫn còn trong kho.
   - **6 câu còn lại:** do trong kho vẫn còn luật cũ/mới hoặc nghị định/thông tư hướng dẫn quy định cùng nội dung (`53/2010/qh12+159`, `68/2020/qh14+29`, `63/2018/nđ-cp+67`, `91/2015/qh13+140`, `168/2011/tt-btc+3`, `162/2017/nđ-cp+4`).
   - **Lưu ý quan trọng cho quyết định D6 (17/11):** Nếu loại thêm các bản trùng mã `nd-cp` ↔ `nđ-cp` trong kho thu hẹp, số câu vẫn trả lời được trong mẫu 30 câu giảm từ 8/30 xuống **6/30 = 20,0%** (không vượt ngưỡng `> 20%`). Chủ đề tài đã chốt phương án này (`expand_zalo_doc_ids` trong `src/ragvi/data.py`), chính thức đóng băng cả hai tập test và đạt đủ 3 cổng kiểm tra Tuần 1.

### 18/11 (đợt 2) – Viết mã Tuần 2 và sinh `notebooks/04_tuan2_sinh_va_judge.ipynb`

Đã viết xong toàn bộ mã nguồn và test cho Tuần 2 (19/11–25/11), qua **48 test** (`PYTHONPATH=src .venv/bin/python -m pytest -q tests`):

| File | Nội dung | Ngày kế hoạch |
|---|---|---|
| `src/ragvi/data.py`, `src/ragvi/retrieval.py` | Tự động loại bản trùng mã `nd-cp` ↔ `nđ-cp` trong kho thu hẹp Zalo (D6); bổ sung `--chunking c1\|c3\|c4\|c5\|c5_nohead` (lưu đệm chunk JSONL), nối `viquad_hits` 80% và tiền tố `query: ` / `passage: ` cho dòng E5 | 17/11, 21/11 |
| `src/ragvi/metrics.py` | Bổ sung `normalize_answer` và `em_f1` (Exact Match, token-F1 theo âm tiết cho ViQuAD; D2) | 19–20/11 |
| `src/ragvi/rerank.py` | Reranker R1 (`BAAI/bge-reranker-v2-m3`) trên top-20 ứng viên, giữ bất biến Recall@20, ghi nối tiếp JSONL | 21/11 |
| `src/ragvi/generate.py` | Sinh câu trả lời 4-bit NF4 (`do_sample=False`, tắt `<think>`), prompt cố định cho RAG / `closed_book` / `oracle`, cắt đoạn ở 1.024 / 4.000 token tham chiếu, nhận diện câu từ chối, ước lượng giờ GPU cho 6.400 lượt | 19–20/11, 23/11 |
| `src/ragvi/judge.py` | LLM-as-judge đầu ra JSON tiếng Việt (`claims`, `correctness`, `h_gold`, `h_ctx`), chỉ số "nhầm điều luật" bằng regex (H1b), xuất phiếu gán nhãn tay 100 câu dev ẩn cấu hình và tính Cohen's κ | 22–24/11 |
| `notebooks/04_tuan2_sinh_va_judge.ipynb` | Notebook Colab 41 cell cho toàn bộ các bước thực nghiệm Tuần 2 | 19–25/11 |
