# Kế hoạch 30 ngày – nộp trước 12/12/2026

Từ thứ Năm 12/11 đến thứ Sáu 11/12/2026 có 30 ngày, khoảng 60 giờ nếu giữ 2 giờ mỗi ngày. Đề cương đầy đủ cần khoảng 16 tuần, nên kế hoạch này **thu hẹp phạm vi** để có sản phẩm của đề tài: một hệ thống RAG chạy được kèm demo, kết quả đánh giá thật, bảng khuyến nghị cấu hình và báo cáo; vẫn giữ được hai đóng góp chính (chỉ số RAH và ViStructChunk cho văn bản luật).

Kế hoạch này thay cho `Kế hoạch 14 ngày và mục lục bài báo.md` trong giai đoạn đến 11/12. `Kế hoạch 16 tuần.md` vẫn là tham chiếu cho phạm vi đầy đủ của khóa luận sau hạn này. Lịch theo từng ngày nằm trong `Kế hoạch chi tiết 30 ngày.md`. Các phương án thiết kế và mã pilot trong `Kế hoạch chi tiết từng ngày.md` (bản 14 ngày) được dùng lại.

## Việc đầu tiên: xác nhận với người hướng dẫn

Môn học yêu cầu sản phẩm thực tế. Kế hoạch giả định thứ phải nộp trước 12/12 gồm **demo chạy được, mã nguồn, kết quả đánh giá ở phạm vi thu hẹp, bảng khuyến nghị cấu hình và báo cáo đề tài**. Ngày 12/11 gửi người hướng dẫn ba câu hỏi:

1. Thứ phải nộp trước 12/12 là gì (bài báo, báo cáo tiến độ, hay khóa luận) và nộp ở đâu?
2. Phạm vi thu hẹp trong bảng dưới đây có chấp nhận được không?
3. Sản phẩm nộp theo hình thức nào: demo trực tiếp, video, hay chỉ báo cáo và mã nguồn?

Nếu thứ cần nộp là khóa luận đầy đủ theo đề cương thì 30 ngày không đủ; cần gia hạn hoặc thỏa thuận lại phạm vi.

## Phạm vi thu hẹp

| Hạng mục | Đề cương | Kế hoạch 30 ngày |
|---|---|---|
| Phân đoạn | C1–C6 | C1, C3, C4, C5 và C5 không gắn tiêu đề (bỏ C2, C6) |
| Truy xuất | E0–E5 | E0 (BM25), E3 (`BAAI/bge-m3`), E5 (hybrid) ở cả hai giai đoạn; E2 (`AITeamVN/Vietnamese_Embedding_v2`) và E4 (`intfloat/multilingual-e5-large`) chỉ ở Giai đoạn A |
| Reranking | R0–R3 | R0, R1 |
| Giai đoạn A | 144 cấu hình | 50 cấu hình trên Zalo (5 × 5 × 2), 30 trên ViQuAD (3 × 5 × 2), chỉ truy xuất; cần 15 + 9 = 24 lượt nhúng kho, trong đó 8 lượt `BAAI/bge-m3` chạy trước vì Giai đoạn B phụ thuộc vào chúng |
| Giai đoạn B | Khoảng 20 cấu hình × 1.000 câu × 2 bộ | 9 cấu hình trên Zalo, 7 trên ViQuAD, mỗi bộ 400 câu (280 trả lời được, 120 không); khoảng 6.400 lượt sinh |
| Chọn cấu hình B | 4 tổ hợp tốt nhất từ Giai đoạn A | Danh sách cố định trước, không chọn theo kết quả |
| Kho ViQuAD | Thêm khoảng 20.000 đoạn nhiễu | Chỉ các đoạn của ViQuAD; ghi thành hạn chế |
| Câu không trả lời được (Zalo) | Loại điều luật và viết tay | Chỉ loại điều luật khỏi kho |
| Nhãn người | 300 mẫu, hai người | 100 mẫu; hai người nếu có, một người thì ghi thành hạn chế |
| Hiệu chỉnh judge bằng ViHallu | 500 mẫu | Bỏ |
| Mô hình sinh thứ hai | 5 cấu hình | Bỏ |
| Thống kê | Bootstrap, hoán vị, Holm, hồi quy logistic | Bootstrap, hoán vị, Holm |
| Phân tích lỗi | 100 trường hợp | 30 trường hợp |
| Khuyến nghị | Pareto và điểm đa tiêu chí | Một bảng khuyến nghị có điều kiện theo miền, chỉ trong phạm vi các cấu hình đã thử |
| Công bố ViRAG-Hallu | Có | Sau hạn |
| Demo | Không nêu | Giao diện web một file: chọn cấu hình, xem câu trả lời và 5 đoạn căn cứ kèm nguồn; mặc định là cấu hình khuyến nghị |
| Hình thức báo cáo | Khóa luận và bài báo | Báo cáo đề tài, có mục mô tả hệ thống và demo |

**Cấu hình Giai đoạn B (cố định trước):**

| # | Zalo Legal | ViQuAD | Phục vụ |
|---|---|---|---|
| 1 | Closed-book | Closed-book | RAH, RQ4 |
| 2 | Oracle | Oracle | RAH, RQ4 |
| 3 | C3–E3–R0 (neo) | C3–E3–R0 (neo) | Mốc so sánh |
| 4 | C4–E3–R0 | C1–E3–R0 | RQ1 |
| 5 | C5–E3–R0 | – | RQ1, H1b |
| 6 | C5 không tiêu đề–E3–R0 | – | H1b |
| 7 | C3–E0–R0 | C3–E0–R0 | RQ2 |
| 8 | C3–E5–R0 | C3–E5–R0 | RQ2 |
| 9 | C3–E3–R1 | C3–E3–R1 | RQ3 |

Cấu hình 6 được thêm vì đề cương có một chỗ chưa nhất quán: C4 cắt theo Điều còn C5 cắt theo Khoản/Điểm, nên cặp C4–C5 không cùng ranh giới cắt như đề cương mô tả. So sánh 5 với 6 mới cô lập được tác động của việc gắn tiêu đề cha.

**Cỡ mẫu và sức mạnh thống kê:** với 280 câu trả lời được, khoảng tin cậy 95% của một tỷ lệ quanh 30% rộng khoảng ±5,4 điểm phần trăm; với 120 câu không trả lời được là khoảng ±8,2. Nghiên cứu chỉ phát hiện được khác biệt lớn; phải nói rõ điều này trong bài.

## Mức độ đạt mục tiêu đề cương

| Mục tiêu (mục 3.2) | Sau 30 ngày |
|---|---|
| 1. Pipeline mô-đun | Đạt, với tập con các thành phần; có demo chạy được |
| 2. Tập đánh giá có câu không trả lời được | Đạt, cỡ nhỏ hơn (400 thay vì 1.000 mỗi bộ) |
| 3. Bộ đo ảo giác và RAH | RAH đạt; hiệu chỉnh judge yếu hơn (100 nhãn) |
| 4. ViStructChunk | Đạt phần văn bản luật; chưa có phần văn bản thường |
| 5. Ablation và thống kê | Đạt một phần: ít mức hơn, không có hồi quy |
| 6. Khung khuyến nghị, công bố dữ liệu | Đạt ở mức hẹp: bảng khuyến nghị có điều kiện; chưa có Pareto, điểm theo kịch bản và công bố dữ liệu |

Câu hỏi nghiên cứu: RQ1 và RQ4 trả lời được ở phạm vi hẹp; RQ2 so được BM25, dense và hybrid ở cả tầng truy xuất lẫn câu trả lời; so sánh ba mô hình nhúng (E2 chuyên Việt, E3 và E4 đa ngôn ngữ) chỉ ở tầng truy xuất, nên chưa biết lợi thế có chuyển sang câu trả lời cuối hay không; RQ3 chỉ với một reranker; RQ5 chỉ trả lời bằng bảng khuyến nghị có điều kiện.

## Lịch

### Tuần 1 (12/11–18/11) – Thiết kế, dữ liệu, truy xuất

| Ngày | Việc | Xong khi |
|---|---|---|
| 12/11 | Gửi ba câu hỏi cho người hướng dẫn. Chạy lại notebook 01, lưu dữ liệu đã xử lý. Chốt D1–D9 bằng các phương án đề xuất sẵn có; ghi vào `reports/quyet-dinh-thiet-ke.md`. | Dữ liệu đã xử lý đọc được; file quyết định có đủ chín mục |
| 13/11 | `git init`; gói mã mỗi yếu tố một file; chuyển mã pilot (nạp dữ liệu, chỉ số, BM25) vào gói; chạy BM25 trên Zalo. | Có bốn chỉ số BM25 trên 788 truy vấn |
| 14/11 | Dense `BAAI/bge-m3` và hybrid; bộ nhớ đệm embedding theo (bộ dữ liệu, C, E). | Có bảng ba dòng trên Zalo |
| 15/11 | Phân đoạn C1, C3, C4 dùng tokenizer tham chiếu; một `assert` cho mỗi hàm trên điều luật mẫu. | Ba mức C sinh chunk cho cả hai kho |
| 16/11 | Tập đánh giá Zalo: tách dev/test theo điều luật vàng; loại điều luật để có 120 câu không trả lời được; 280 câu trả lời được; 100 câu dev. | File tập test Zalo, có seed và mã băm |
| 17/11 | Tập đánh giá ViQuAD từ train và validation: 280 + 120, tách dev/test theo `title`; kho là các đoạn ViQuAD. Đọc tay 30 câu không trả lời được mỗi bộ để kiểm tra. | Hai tập test đóng băng |
| 18/11 | Parser Điều → Khoản → Điểm (C5) và biến thể không tiêu đề; đối chiếu tay 30 điều luật; ghi tỷ lệ parse được. | C5 sinh chunk cho kho Zalo; có báo cáo tỷ lệ lỗi |

### Tuần 2 (19/11–25/11) – Sinh câu trả lời và judge

| Ngày | Việc | Xong khi |
|---|---|---|
| 19/11 | Chạy mô hình sinh cục bộ; prompt cố định; thử nhanh hai ứng viên trên 50 câu dev và chọn một theo tiêu chí ghi trước. | Đã chọn mô hình sinh |
| 20/11 | Điều kiện closed-book và oracle; quy tắc nhận diện câu từ chối; ghi kết quả từng câu ngay khi sinh để chạy tiếp được khi mất phiên. | Pipeline đầu-cuối chạy trên 50 câu |
| 21/11 | Reranker R1. Xếp hàng 24 lượt nhúng cho Giai đoạn A (chạy nền; 8 lượt `BAAI/bge-m3` trước, rồi E2 và E4). | Truy xuất có reranking chạy được |
| 22/11 | Prompt judge tiếng Việt, đầu ra JSON: H_ctx, H_gold, correctness. Chỉ số "nhầm điều luật" bằng biểu thức chính quy. | Judge chạy trên 20 câu, đầu ra hợp lệ |
| 23/11 | Sinh câu trả lời cấu hình neo, closed-book, oracle trên tập dev; bắt đầu gán nhãn tay 100 câu. | 50 câu đã gán nhãn |
| 24/11 | Gán nhãn xong 100 câu; tính κ giữa judge và người; sửa prompt một lần trên nửa đầu, kiểm tra trên nửa sau. | Có con số κ |
| 25/11 | **Cổng quyết định.** Gửi người hướng dẫn bản tóm tắt thiết kế một trang. Đóng băng prompt sinh, prompt judge, danh sách cấu hình B. | Xem mục "Cổng 25/11" |

### Tuần 3 (26/11–02/12) – Chạy thực nghiệm

| Ngày | Việc | Xong khi |
|---|---|---|
| 26/11 | Giai đoạn A: truy xuất và reranking trên mọi tổ hợp; bảng chỉ số kèm khoảng tin cậy. | Bảng Giai đoạn A |
| 27/11 | Giai đoạn B trên Zalo: sinh câu trả lời cho 9 cấu hình (chạy nền). Kiểm tra tay 20 câu của cấu hình đầu tiên. Trong lúc chờ: dựng demo thô (phần truy xuất). | Lượt sinh Zalo đang chạy, không lỗi định dạng; demo thô chạy được |
| 28/11 | Giai đoạn B trên ViQuAD: 7 cấu hình. | Đủ khoảng 6.400 câu trả lời |
| 29/11 | Chạy judge trên câu trả lời của các câu trả lời được (khoảng 4.480 lượt); chạy lại các đầu ra không hợp lệ. | Mọi câu trả lời cần chấm có điểm |
| 30/11 | Tính mọi chỉ số; dựng bảng một dòng cho mỗi cặp (cấu hình, câu hỏi). | Bảng kết quả đầy đủ |
| 01/12 | Đo độ trễ truy xuất và reranking; kích thước chỉ mục. | Bảng chi phí |
| 02/12 | Dự phòng cho tuần 3; nối mô hình sinh vào demo và thử 10 câu hỏi. | Demo trả lời được |

### Tuần 4 (03/12–09/12) – Phân tích và viết

| Ngày | Việc | Xong khi |
|---|---|---|
| 03/12 | Khoảng tin cậy bootstrap; kiểm định hoán vị ghép cặp so với cấu hình neo; hiệu chỉnh Holm; RAH theo cấu hình và theo miền. | Bảng kết quả chính kèm khoảng tin cậy |
| 04/12 | Gắn nhãn nguyên nhân 30 trường hợp ảo giác; dựng hình và bảng; lập bảng khuyến nghị có điều kiện; đặt cấu hình khuyến nghị làm mặc định của demo. | Hình, bảng, bảng khuyến nghị; demo dùng cấu hình khuyến nghị |
| 05/12 | Xác minh từ nguồn gốc các tài liệu sẽ trích (chỉ những tài liệu thực sự dùng). Viết phương pháp và thiết lập thực nghiệm. | Mục 3–4 |
| 06/12 | Viết kết quả và thảo luận theo từng câu hỏi nghiên cứu. | Mục 5–6 |
| 07/12 | Viết giới thiệu và công trình liên quan. | Mục 1–2 |
| 08/12 | Hạn chế, tóm tắt, kết luận; chạy danh sách kiểm tra nhất quán. | Bản thảo đầy đủ |
| 09/12 | README, video demo ngắn; gửi người hướng dẫn báo cáo, mã nguồn và demo. | Đã gửi |

### 10/12–11/12 – Hoàn thiện

Sửa theo phản hồi; kiểm tra tài liệu tham khảo, bảng, hình; nộp ngày 11/12. Người hướng dẫn chỉ có khoảng một ngày để đọc, nên bản tóm tắt thiết kế gửi ngày 25/11 là cơ hội chính để nhận góp ý về phương pháp.

## Cổng 25/11: tiếp tục hay chuyển phương án

Tiếp tục khi cả ba điều sau đúng:

- Pipeline đầu-cuối chạy được trên tập dev của cả hai bộ.
- Tập đánh giá đã đóng băng.
- κ giữa judge và người từ 0,6 trở lên (thấp hơn mục tiêu 0,7 của đề cương; ghi rõ trong bài).

Nếu không đạt, chuyển sang **phương án dự phòng**: bài protocol kèm kết quả truy xuất. Khi đó tuần 3 chỉ chạy Giai đoạn A trên cả hai bộ, và tuần 4 viết theo mục lục trong `Kế hoạch 14 ngày và mục lục bài báo.md`. Bài vẫn có số liệu thật về phân đoạn, truy xuất và reranking, nhưng không có kết quả ảo giác. Demo vẫn được dựng trong cả hai phương án, vì nó chỉ cần pipeline chạy được.

## Thang cắt khi trễ

Áp dụng theo thứ tự:

1. E2 và E4 chỉ chạy với C3 và C4; nếu vẫn không kịp thì bỏ hẳn khỏi Giai đoạn A.
2. Bỏ cấu hình 9 (reranker) khỏi Giai đoạn B; RQ3 chỉ trả lời ở tầng truy xuất.
3. Giảm còn 300 câu mỗi bộ (210 + 90).
4. Bỏ Giai đoạn B trên ViQuAD; chỉ còn miền pháp luật, mất so sánh giữa hai miền của RQ4.
5. Chuyển sang phương án dự phòng.

Không cắt: closed-book và oracle; đối chiếu judge với nhãn người; đóng băng tập đánh giá và danh sách cấu hình trước khi chạy Giai đoạn B; khoảng tin cậy.

## Rủi ro chính

| Rủi ro | Xử lý |
|---|---|
| 60 giờ không có dự phòng ngoài ngày 02/12 | Thêm giờ vào cuối tuần nếu được; nếu không, dùng thang cắt sớm, không đợi đến tuần 4 |
| Sinh 6.400 câu chậm trên GPU miễn phí | Đo thông lượng ngày 20/11; ghi kết quả từng câu để chạy tiếp; nếu ước lượng vượt 20 giờ GPU thì áp dụng bậc cắt 3 |
| Chỉ có một người gán nhãn | Ghi thành hạn chế (việc gán nhãn lại 30 câu đã bỏ để dành thời gian cho demo) |
| Parser C5 lỗi nhiều | Điều luật không parse được dùng chunk của C4; báo cáo tỷ lệ |
| Người hướng dẫn không chấp nhận phạm vi thu hẹp | Biết sớm nhờ câu hỏi ngày 12/11; khi đó cần gia hạn, không thể bù bằng lịch |
