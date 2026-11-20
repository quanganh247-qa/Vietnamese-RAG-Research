# Quyết định thiết kế D1–D9

**Ngày ghi:** 12/11/2026. **Trạng thái:** đề xuất, chờ người hướng dẫn xác nhận phạm vi. Đóng băng cùng prompt và danh sách cấu hình vào ngày 25/11 (thẻ `freeze-b`); sau ngày đó mọi thay đổi phải ghi thêm vào mục "Nhật ký thay đổi" ở cuối file, không sửa đè.

Phạm vi thu hẹp và danh sách cấu hình Giai đoạn B nằm trong `Kế hoạch 30 ngày (hạn 11-12).md`. File này ghi chín quyết định mà đề cương v2 chưa trả lời, kèm lý do và hạn chế phải nêu trong báo cáo.

## Tóm tắt

| # | Vấn đề | Quyết định |
|---|---|---|
| D1 | Cỡ mẫu và cách lấy mẫu tập đánh giá | Mỗi bộ: 280 câu trả lời được + 120 không trả lời được (test), 100 câu dev. Zalo lấy mẫu theo nhóm điều luật vàng |
| D2 | Tiêu chí chunk đúng; độ đúng trên Zalo | Zalo: theo điều luật cha. ViQuAD: phủ ít nhất 80% ký tự đáp án vàng. Độ đúng trên Zalo do judge chấm so với điều luật vàng |
| D3 | Tỷ lệ ảo giác ở closed-book | Dùng H_gold, xác định được ở mọi điều kiện |
| D4 | Truy xuất sai nhưng mô hình bám ngữ cảnh sai | Tách H_ctx và H_gold; H_gold là chỉ số chính |
| D5 | RAH và oracle trên câu không trả lời được | RAH chỉ tính trên câu trả lời được |
| D6 | Câu "không trả lời được" có thể vẫn trả lời được từ kho | Đọc tay 30 câu mỗi bộ, báo cáo tỷ lệ |
| D7 | Phân đoạn phụ thuộc tokenizer của mô hình nhúng | Một tokenizer tham chiếu (`BAAI/bge-m3`) cho mọi cấu hình |
| D8 | Chọn cấu hình Giai đoạn B theo kết quả gây thiên lệch | Danh sách cố định trước |
| D9 | Tổng số lượt sinh | (9 + 7) × 400 = 6.400 |

## D1 – Tập đánh giá

**Quyết định**

- **Zalo Legal:** tập test gồm 280 câu trả lời được và 120 câu không trả lời được; tập dev 100 câu trả lời được. Tổng 500 trong 788 truy vấn có nhãn; khoảng 288 truy vấn còn lại để dự trữ.
- **Đơn vị lấy mẫu là nhóm điều luật vàng.** Hai truy vấn thuộc cùng nhóm nếu chúng dùng chung ít nhất một điều luật vàng, trực tiếp hoặc qua truy vấn khác. Mỗi nhóm nằm trọn trong một phần (không trả lời được, dev, trả lời được).
- **Câu không trả lời được** tạo bằng cách loại toàn bộ điều luật vàng của 120 câu đó khỏi kho. Mọi cấu hình dùng chung một kho thu hẹp. Không viết tay câu hỏi ngoài kho.
- **Thứ tự phân nhóm:** xáo nhóm bằng seed 0, lần lượt đưa vào phần "không trả lời được", rồi "dev", rồi "trả lời được" cho đến khi đủ số câu. Cho phép lệch vài câu nếu kích thước nhóm không khớp đúng; ghi số thực tế.
- **Trước khi lấy mẫu:** bỏ 30 dòng truy vấn trùng (818 dòng, 788 mã duy nhất).
- **ViQuAD:** cùng cỡ mẫu. Lấy từ train và validation (split test không có đáp án). Tách dev/test theo `title`; mỗi đoạn tối đa một câu hỏi. Kho gồm các đoạn `context` duy nhất của cả ba split, mã tài liệu là mã băm nội dung đoạn. Khóa câu hỏi là (split, `id`) vì `id` lặp lại giữa các split.
- **Đóng băng:** lưu tập test, tập dev, danh sách điều luật bị loại, seed và mã băm SHA-256 của từng file.

**Lý do**

- 788 truy vấn không đủ cho mục tiêu 700 + 300 của đề cương nếu không viết tay hơn 212 câu.
- 793 cặp qrels chỉ trỏ tới 447 điều luật khác nhau, nên nhiều truy vấn dùng chung điều luật vàng. Loại điều luật theo từng truy vấn riêng lẻ sẽ vô tình làm các truy vấn khác thành không trả lời được, và tách dev/test theo truy vấn sẽ rò rỉ điều luật vàng giữa hai tập.

**Hạn chế phải nêu**

- Khoảng tin cậy 95% của một tỷ lệ quanh 30% rộng khoảng ±5,4 điểm phần trăm trên 280 câu và ±8,2 trên 120 câu. Chỉ phát hiện được khác biệt lớn.
- Câu không trả lời được của Zalo là nhân tạo: câu hỏi thật, nhưng kho bị bỏ bớt.
- Kho ViQuAD không có đoạn nhiễu ngoài như đề cương dự kiến, nên truy xuất dễ hơn thực tế.

## D2 – Chunk đúng và độ đúng câu trả lời

**Quyết định**

- **Zalo:** một chunk là đúng nếu điều luật cha của nó nằm trong qrels. Mỗi điều luật vàng chỉ tính một lần, ở lần xuất hiện đầu tiên trong danh sách xếp hạng.
- **ViQuAD:** một chunk là đúng nếu thuộc đúng đoạn gốc và phủ ít nhất 80% số ký tự của đáp án vàng.
- **Độ đúng câu trả lời:** ViQuAD dùng EM, token-F1 theo âm tiết và correctness 0/1/2 của judge. Zalo chỉ dùng correctness của judge, chấm so với điều luật vàng.
- **Chỉ số "nhầm điều luật" (cho H1b):** câu trả lời dẫn số Điều không khớp số điều của điều luật vàng (phần sau dấu `+` trong mã tài liệu); đo bằng biểu thức chính quy.

**Lý do:** Zalo chỉ có qrels, không có đáp án vàng, nên EM, F1 và quy tắc 80% của đề cương không áp dụng được.

**Hạn chế phải nêu:** tiêu chí của Zalo rộng hơn (đúng điều luật nhưng sai khoản vẫn được tính), nên không so trực tiếp con số truy xuất giữa hai miền. Token-F1 tính theo âm tiết, không tách từ như đề cương.

## D3 và D4 – Hai đại lượng ảo giác

**Quyết định**

| Đại lượng | Định nghĩa | Vai trò |
|---|---|---|
| H_gold | Tỷ lệ câu trả lời có ít nhất một mệnh đề không được bằng chứng vàng hỗ trợ | Chỉ số chính; dùng để tính RAH |
| H_ctx | Tỷ lệ câu trả lời có ít nhất một mệnh đề không được ngữ cảnh đã cung cấp hỗ trợ | Chỉ số phụ; không xác định ở closed-book |

Bằng chứng vàng là đoạn vàng và đáp án vàng (ViQuAD) hoặc điều luật vàng (Zalo). Câu từ chối không có mệnh đề nào; nó được tính vào false refusal, không tính vào H.

**Lý do:** định nghĩa của đề cương (faithfulness so với ngữ cảnh truy xuất) không xác định khi không có ngữ cảnh, và không bắt được trường hợp truy xuất sai mà mô hình bám đúng ngữ cảnh sai, tức đúng loại lỗi mà RAH muốn quy cho truy xuất.

**Hạn chế phải nêu:** H_gold phạt cả thông tin đúng nhưng nằm ngoài bằng chứng vàng (tri thức nền của mô hình). Vì vậy báo cáo cả hai đại lượng.

## D5 – RAH

**Quyết định**

- RAH(k) = H_gold(k) − H_gold(oracle), chỉ tính trên câu trả lời được.
- Tỷ lệ RAH(k) / H_gold(k) chỉ báo cáo khi H_gold(k) từ 10% trở lên.
- Câu không trả lời được: chỉ báo cáo fabrication rate (tỷ lệ không từ chối), đo bằng quy tắc nhận diện câu từ chối, không cần judge.
- Oracle chỉ đưa bằng chứng vàng, không kèm đoạn truy xuất. Điều luật vàng cắt ở 4.000 token tham chiếu.

**Lý do:** câu Zalo tạo bằng cách loại điều luật không còn đoạn vàng trong kho, nên oracle không xác định trên tập đó.

**Hạn chế phải nêu:** RAH có thể âm; luôn kèm khoảng tin cậy của hiệu số ghép cặp; RAH là hiệu số mô tả, chỉ diễn giải nhân quả với giả định rằng oracle chỉ khác cấu hình ở ngữ cảnh.

## D6 – Kiểm tra câu không trả lời được

**Quyết định:** với mỗi bộ, lấy 30 câu không trả lời được, xem 5 kết quả đầu của hybrid và đọc tay xem kho còn đoạn nào trả lời được không. Nếu tỷ lệ vẫn trả lời được trên 20% thì thay các câu đó trước khi đóng băng và ghi lại quy trình.

**Lý do:** sau khi loại điều luật, văn bản khác có thể chứa cùng nội dung (nghị định sửa đổi, thông tư hướng dẫn). Với ViQuAD, câu `is_impossible` chỉ đối kháng với một đoạn; đoạn khác trong kho có thể chứa đáp án.

## D7 – Tokenizer tham chiếu

**Quyết định:** ranh giới chunk và số token được tính bằng tokenizer của `BAAI/bge-m3` cho mọi cấu hình, kể cả BM25. Mô hình nhúng cắt ở 512 token; mỗi đoạn đưa vào prompt cắt ở 1.024 token tham chiếu. Báo cáo tỷ lệ bị cắt ở từng chỗ.

**Lý do:** đề cương đếm token bằng tokenizer của từng mô hình nhúng, khiến tập chunk thay đổi theo yếu tố E và hai yếu tố không còn độc lập.

**Cần xác minh ngày 21/11:** độ dài tối đa và yêu cầu tiền tố của E2 và E4 (`intfloat/multilingual-e5-large` cần tiền tố `query: ` và `passage: `).

## D8 – Cấu hình Giai đoạn B

**Quyết định:** 9 cấu hình trên Zalo và 7 trên ViQuAD, cố định trước (bảng trong kế hoạch 30 ngày). Giai đoạn A chỉ để mô tả, không dùng để chọn cấu hình. Tập dev chỉ dùng để chọn mô hình sinh, chỉnh prompt và judge.

**Lý do:** chọn "4 tổ hợp tốt nhất" rồi đánh giá trên cùng bộ câu hỏi gây thiên lệch chọn lọc; với cỡ mẫu nhỏ thì không đủ dữ liệu cho một tập chọn riêng.

**Ghi chú:** cặp C5 và "C5 không tiêu đề" thay cho cặp C4–C5 của đề cương khi kiểm định H1b, vì C4 (cắt theo Điều) và C5 (cắt theo Khoản/Điểm) không cùng ranh giới.

## D9 – Tổng lượt sinh

**Quyết định:** (9 + 7) cấu hình × 400 câu = 6.400 lượt sinh. Judge chỉ chấm câu trả lời của câu trả lời được: 16 × 280 = 4.480 lượt.

**Ghi chú:** đề cương ghi 40.000 ở mục 5.3 và 38.000 ở mục 5.5; cả hai con số không còn áp dụng cho phạm vi thu hẹp.

## Kế hoạch thống kê (ghi trước khi có số liệu)

- **Chỉ số chính:** H_gold và correctness. Các chỉ số khác là phụ.
- **Họ phép so sánh cho hiệu chỉnh Holm:** Zalo có 7 so sánh trên mỗi chỉ số chính (sáu cấu hình so với neo, và C5 so với C5 không tiêu đề); ViQuAD có 4. Mọi so sánh khác là khám phá.
- **Khoảng tin cậy:** bootstrap 1.000 lần, lấy mẫu lại theo cụm (`title` với ViQuAD, nhóm điều luật với Zalo).
- **Kiểm định:** hoán vị ghép cặp, đổi dấu hiệu số theo từng câu hỏi, 10.000 hoán vị.
- **Judge:** tiếp tục Giai đoạn B khi Cohen's κ giữa judge và người trên H_gold từ 0,6 trở lên (đề cương đặt 0,7; ghi rõ mức đạt được).

## Quyết định còn mở

| Hạn | Quyết định | Căn cứ |
|---|---|---|
| 16/11 | Xác nhận phạm vi và hình thức nộp | Trả lời của người hướng dẫn |
| 19/11 | Mô hình sinh | Thử trên 50 câu dev; tiêu chí: tỷ lệ từ chối đúng, rồi đến độ đúng |
| 20/11 | Giữ 400 hay giảm còn 300 câu mỗi bộ | Ước lượng giờ GPU (ngưỡng 20 giờ) |
| 22/11 | Mô hình judge | Ngân sách và độ ổn định JSON |

## Nhật ký thay đổi

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 14/11 | Chốt hybrid: s = α · minmax(dense) + (1 − α) · minmax(BM25), min–max theo từng truy vấn trên cả kho, α = 0,7 | Khớp thiết lập và mã nguồn công bố: Nguyen & Quan, "Which Works Best for Vietnamese? A Practical Study of Information Retrieval Methods across Domains", Findings of EACL 2026 (https://aclanthology.org/2026.findings-eacl.110); mã nguồn ViRE (https://github.com/longstnguyen/ViRE, `src/vi_retrieval_eval/runner.py`). Do agent tra cứu đối chiếu; cần tự kiểm lại trước khi trích dẫn |
| 14/11 | C5: khi khoản 1 nằm ngay sau tiêu đề Điều, dòng tiêu đề thành một chunk riêng (trước đó bị mất ở biến thể không tiêu đề) | Nếu không, so sánh C5 với C5 không tiêu đề (H1b) bị lẫn tác động của việc mất tên Điều |
| 14/11 | E0 dùng BM25 tách từ bằng underthesea (áp dụng quy tắc ghi trước) | Đo trên Colab: 500 điều luật mất 9,0 giây, ước lượng 19,2 phút cho cả kho, dưới ngưỡng 30 phút. BM25 tách từ chưa được cài vào lệnh chạy và chưa có số liệu |
| 15/11 | D2, làm rõ cho ViQuAD: chunk đúng khi thuộc đoạn gốc và phủ ít nhất 80% ký tự của ít nhất một đáp án vàng; `n_rel = 1`; chỉ lần trúng đầu tiên được tính | D2 chưa nói rõ khi có nhiều đáp án vàng. Trưởng nhóm chọn cách đơn giản nhất nhất quán với cách tính của Zalo; chủ đề tài có thể đổi trước khi chạy mức chunk (21/11) |
| 15/11 | Kho ViQuAD: văn bản của đoạn chỉ gồm `text`, không ghép `title` (Zalo vẫn ghép `title` và `text`) | Vị trí đáp án vàng tính trên `text`, và nhiều đoạn dùng chung một `title`. Phải chốt trước khi nhúng kho ViQuAD lần đầu |
| 15/11 | BM25 tách từ: chữ thường, bỏ token chỉ gồm dấu câu, âm tiết trong một từ nối bằng `_` | Tương ứng với cách tách âm tiết đang dùng (cũng chữ thường và bỏ dấu câu), để hai biến thể chỉ khác ở bước tách từ |
| 14/11 | C1: điểm cuối chunk bị chặn tại điểm đầu chunk kế tiếp | Tokenizer bge-m3 thật sinh vị trí trùng nhau, làm chunk chồng lấn một ký tự |
| 18/11 | D6: Kho thu hẹp Zalo tự động loại cả bản trùng mã `nd-cp` ↔ `nđ-cp` (`expand_zalo_doc_ids` trong `data.py`); đóng băng cả hai tập test | Kiểm tra 30 câu D6 trên Zalo phát hiện 8/30 câu (26,7%) trả lời được từ top-5 `hybrid[word]`, trong đó 2 câu do kho gốc có bản trùng Nghị định 24/2020/NĐ-CP dưới mã `24/2020/nd-cp+*` (chữ `d` không gạch). Sau khi loại bản trùng `nd-cp` ↔ `nđ-cp`, tỷ lệ còn 6/30 = 20,0% (≤ ngưỡng 20%); ViQuAD là 2/30 = 6,7% (≤ 20%) |
| 18/11 | Chủ đề tài xác nhận giữ nguyên 3 quyết định kỹ thuật ngày 15/11 (`viquad_hits` 80%, đoạn ViQuAD không ghép `title`, chuẩn hóa token BM25 tách từ) | Đảm bảo nhất quán trước khi chạy nhúng và truy xuất mức chunk ở Tuần 2 |
| 20/11 | Colab CLI + llama.cpp CUDA / Qwen2.5-7B-Instruct GGUF Q4_K_M là pilot riêng; thứ tự cấp máy G4 → A100 → L4 → T4; không đổi backend Phase B | Giảm thao tác tay, vẫn không trộn đầu ra GGUF với Transformers/NF4 khi so sánh C/E/R. Quota, CUDA và thời gian Colab chưa đo. |
| 20/11 | EDA dùng tokenizer BGE-M3 cố định và nhóm gần câu chữ trên dev bằng cosine TF-IDF ký tự ≥ 0,60 | Tìm trường hợp dễ truy xuất nhầm mà không đụng cách tạo nhóm vàng hoặc dùng câu test để chỉnh cấu hình. |
| 20/11 | Không xuất `reserve.jsonl` của Zalo; giữ các tập dev/test của cả hai bộ | `reserve` chứa 288 câu dư, không phải split nguồn và không dùng chấm điểm. Giữ nguyên truy vấn nguồn, seed, mã nhóm, câu dev/test và danh sách điều luật bị loại. |
| 20/11 | Benchmark vận hành riêng: cấu hình neo C3–E3–R0 trên toàn bộ truy vấn nguồn; sinh và chấm trên dev/test đóng băng với hai đối chứng | Không huấn luyện hoặc dò cấu hình bằng test. ViQuAD test nguồn không có nhãn; Zalo chỉ có một tập truy vấn nguồn có nhãn. Dùng GGUF cho cả generator và judge nên kết quả chưa hiệu chỉnh, không thay cho Phase B. RAH chỉ lấy câu có H_gold ở cả neo và oracle; báo mẫu số để thấy ảnh hưởng của từ chối/lỗi chấm. |
