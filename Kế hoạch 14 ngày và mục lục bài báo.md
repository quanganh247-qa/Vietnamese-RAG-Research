# Kế hoạch 14 ngày và mục lục bài báo

## Mục tiêu và phạm vi

**Thời lượng:** 14 ngày, khoảng 2 giờ mỗi ngày (tổng cộng khoảng 28 giờ).

**Đầu ra khả thi:** một bản thảo bài báo dạng đề xuất phương pháp/protocol nghiên cứu **kèm kết quả sơ bộ thật**, gồm (i) thống kê chất lượng dữ liệu đã có trong notebook và (ii) một pilot truy xuất nhỏ trên Zalo Legal. Bản thảo có câu hỏi nghiên cứu, phương pháp, thiết kế thực nghiệm, kế hoạch phân tích và hạn chế rõ ràng. Không trình bày kết quả dự kiến như kết quả đã đo.

Đây chưa phải bài báo kết quả thực nghiệm hoàn chỉnh. Dự án hiện có notebook khám phá và làm sạch dữ liệu; các kiểm định làm sạch đã có kết quả đạt trong notebook, nhưng bước lưu dữ liệu đã xử lý chưa được xác nhận là đã chạy. Chưa có pipeline RAG, kết quả đánh giá đầu-cuối hay nhãn người. Chỉ đưa các kết quả có thể kiểm chứng vào bài; nếu chưa chạy lại hoặc chưa truy cập được dữ liệu thì ghi rõ là công việc còn chờ.

**Vì sao thêm pilot:** phần lớn nội dung phương pháp đã có trong đề cương v2 (mục 5.1–5.9), nên việc đặc tả lại được nén còn 5 ngày. Các hội nghị dự kiến (VLSP, KSE, SoICT) thường không nhận bài thuần protocol không có số liệu; ba ngày tiết kiệm được dùng để có số liệu thật. Nếu pilot không chạy được, bản thảo vẫn là protocol với thống kê dữ liệu, và ghi rõ pilot là việc còn chờ.

**Vị trí trong lịch 16 tuần của đề cương:** 14 ngày này tương ứng tuần 3–4. Pilot truy xuất là phần đầu của pipeline cơ bản; phần sinh câu trả lời bị lùi sang sau 14 ngày.

**Người đọc:** người hướng dẫn, hội đồng và nhà nghiên cứu NLP/RAG.  
**Việc người đọc có thể làm sau khi đọc:** hiểu câu hỏi nghiên cứu, tái lập thiết kế dự kiến và đánh giá những gì cần hoàn thành trước khi bài báo có thể báo cáo kết quả đầy đủ.

## Các quyết định thiết kế phải chốt trong bản thảo

Đây là các điểm đề cương v2 chưa trả lời. Mỗi điểm phải có quyết định bằng văn bản, hoặc được ghi thành hạn chế/rủi ro, trước cổng kiểm tra cuối ngày 6.

| # | Vấn đề | Căn cứ | Chốt vào ngày |
|---|---|---|---|
| D1 | Zalo Legal không đủ 1.000 câu: chỉ có 788 truy vấn duy nhất có nhãn (818 dòng, 30 dòng trùng). Mục tiêu 700 + 300 cần ít nhất 212 câu viết tay, chưa kể tập dev. Chọn: giảm cỡ mẫu, viết thêm câu, hay bổ sung ALQAC. | Notebook mục 5 | 4 |
| D2 | Zalo Legal chỉ có qrels, không có đáp án vàng. EM, token-F1 và quy tắc "chunk chứa ≥ 80% đáp án vàng" không áp dụng được. Cần định nghĩa chunk đúng theo ID điều luật cha, và cách chấm độ đúng câu trả lời (judge so với điều luật vàng, hay tự viết đáp án tham chiếu). | Schema qrels | 5 |
| D3 | H(closed-book) chưa xác định: tỷ lệ ảo giác được định nghĩa qua faithfulness với ngữ cảnh, mà closed-book không có ngữ cảnh. | Đề cương 5.6 | 5 |
| D4 | RAH có thể đo thiếu: nếu truy xuất sai nhưng mô hình bám đúng ngữ cảnh sai, faithfulness = 1 và câu trả lời sai không bị tính là ảo giác. Cần quyết định H dựa trên faithfulness, trên độ đúng so với đáp án vàng, hay báo cáo cả hai. | Đề cương 5.6 | 5 |
| D5 | Oracle chưa xác định trên câu không trả lời được (đặc biệt câu tạo bằng cách loại điều luật vàng khỏi kho). Nêu rõ RAH tính trên tập con nào. | Đề cương 5.3, 5.4 | 5 |
| D6 | Câu không trả lời được của ViQuAD đối kháng với một đoạn cụ thể; khi thêm khoảng 20.000 đoạn nhiễu cùng chủ đề, đoạn khác có thể chứa đáp án. Cần quy trình kiểm tra hoặc ghi thành hạn chế. | Đề cương 5.4 | 4 |
| D7 | C và E không độc lập hoàn toàn: đếm token bằng tokenizer của từng mô hình nhúng làm tập chunk khác nhau theo E; BM25 không có tokenizer. Kiểm tra độ dài tối đa của từng mô hình (cần xác minh: `bkai vietnamese-bi-encoder` có thể giới hạn 256 token, khi đó C2 512 token bị cắt). | Đề cương 5.2 | 3 |
| D8 | Chọn 4 tổ hợp tốt nhất từ Giai đoạn A rồi đánh giá lại trên cùng bộ câu hỏi gây thiên lệch chọn lọc. Cần tập dev riêng; với Zalo điều này làm D1 khó hơn. | Đề cương 5.3 | 4 |
| D9 | Số lượt sinh không khớp trong đề cương: mục 5.3 ghi 40.000, mục 5.5 ghi 38.000. Theo thiết kế là 20 × 2 × 1.000 = 40.000; cập nhật lại sau khi chốt D1. | Đề cương 5.3, 5.5 | 6 |

## Mục lục đề xuất

### Tựa đề

Đánh giá ảnh hưởng của phân đoạn, truy xuất và xếp hạng lại đến độ chính xác và ảo giác trong RAG tiếng Việt: một thiết kế thực nghiệm có kiểm soát

### Tóm tắt

Trình bày vấn đề, khoảng trống, mục tiêu, thiết kế chính, dữ liệu, chỉ số và đóng góp. Ghi rõ đây là protocol kèm kết quả sơ bộ; chỉ nêu số liệu đã đo, không dùng ngôn ngữ khẳng định phát hiện thực nghiệm cho phần chưa chạy.

### 1. Giới thiệu

1.1 Bối cảnh RAG và ảo giác trong LLM  
1.2 Đặc thù tiếng Việt và văn bản pháp luật  
1.3 Khoảng trống nghiên cứu  
1.4 Mục tiêu, câu hỏi nghiên cứu và giả thuyết  
1.5 Đóng góp dự kiến và cấu trúc bài báo

### 2. Công trình liên quan

2.1 Truy xuất thông tin và embedding tiếng Việt  
2.2 Phân đoạn văn bản và truy xuất pháp luật  
2.3 Reranking tiếng Việt  
2.4 Đánh giá độ đúng và ảo giác trong RAG  
2.5 Vị trí của nghiên cứu này so với các công trình trước

### 3. Phương pháp

3.1 Kiến trúc pipeline RAG và nguyên tắc kiểm soát biến  
3.2 Các phương pháp phân đoạn C1–C6  
3.3 Các phương pháp truy xuất E0–E5  
3.4 Các phương pháp reranking R0–R3  
3.5 ViStructChunk  
3.6 Mô hình sinh, prompt và điều kiện tham chiếu closed-book/oracle  
3.7 Định nghĩa chỉ số RAH và các chỉ số đánh giá khác (gồm quyết định D2–D5)

### 4. Thiết lập thực nghiệm

4.1 Bộ dữ liệu, thống kê chất lượng dữ liệu và tiêu chí chọn mẫu  
4.2 Xây dựng tập câu hỏi trả lời được/không trả lời được  
4.3 Giai đoạn A: đánh giá truy xuất trên lưới cấu hình  
4.4 Giai đoạn B: đánh giá đầu-cuối trên tập cấu hình chọn lọc  
4.5 Hiệu chỉnh judge và gán nhãn người  
4.6 Thiết lập phần cứng, phần mềm và quy trình tái lập

### 5. Kế hoạch phân tích và báo cáo

5.1 Chỉ số truy xuất, độ đúng, ảo giác và chi phí  
5.2 Khoảng tin cậy, kiểm định và hiệu chỉnh nhiều phép so sánh  
5.3 Phân tích lỗi và khuyến nghị đa tiêu chí  
5.4 Kiểm tra độ bền và phân tích độ nhạy  
5.5 Các bảng/hình sẽ báo cáo và cách diễn giải theo từng câu hỏi nghiên cứu (bảng mẫu để trống, không điền số giả định)

### 6. Kết quả sơ bộ

6.1 Chất lượng dữ liệu sau làm sạch (số liệu từ notebook, chạy lại để xác nhận)  
6.2 Pilot truy xuất trên Zalo Legal: BM25, một mô hình dense và hybrid, phân đoạn theo Điều  
6.3 Những gì pilot chưa cho phép kết luận

Chỉ gồm số liệu đã đo. Nếu pilot không chạy được, mục này chỉ còn 6.1 và ghi rõ pilot là việc còn chờ.

### 7. Thảo luận

7.1 Ý nghĩa đối với hệ thống RAG tiếng Việt  
7.2 Hạn chế, đe dọa đến tính hợp lệ và khả năng khái quát  
7.3 Khả năng tái lập và phát hành dữ liệu/mã nguồn

### 8. Kết luận

Tóm tắt mục tiêu và đóng góp của thiết kế nghiên cứu; không kết luận về giả thuyết khi chưa có dữ liệu thực nghiệm.

### Tài liệu tham khảo và phụ lục

Danh mục tài liệu đã xác minh; prompt; quy tắc lấy mẫu; định nghĩa nhãn; cấu hình thí nghiệm; biểu mẫu gán nhãn; bảng kết quả trống.

## Lịch làm việc chi tiết

Mỗi ngày dành khoảng 2 giờ. Nếu cần trao đổi với người hướng dẫn hoặc chờ dữ liệu, ghi thành đầu việc có người phụ trách và ngày cần phản hồi; không tính phần chờ là tiến độ đã hoàn thành.

| Ngày | Việc cần làm trong 2 giờ | Đầu ra cuối ngày |
|---|---|---|
| 1 | 15 phút đầu: gửi người hướng dẫn câu hỏi về nơi dự định nộp và việc bài protocol kèm pilot có được chấp nhận không. 45 phút: kiểm tra quyền truy cập Drive, chạy lại notebook và lưu dữ liệu đã xử lý. 60 phút: xác minh từ nguồn gốc các tài liệu làm căn cứ cho "khoảng trống nghiên cứu" (ưu tiên các nguồn ghi năm 2025–2026). | Câu hỏi đã gửi; dữ liệu đã xử lý có trên Drive; danh sách nguồn đã/chưa xác minh. |
| 2 | 30 phút: hoàn tất xác minh nguồn còn lại cho khoảng trống. 30 phút: viết mục tiêu và khoảng trống, chỉ dựa trên nguồn đã xác minh. 60 phút: chốt RQ1–RQ5 và giả thuyết, nối mỗi giả thuyết với yếu tố, chỉ số và phép so sánh. | Bảng RQ – giả thuyết – biến – chỉ số. |
| 3 | 50 phút: rà soát C1–C6, so sánh C4/C5, cách xử lý chunk rỗng/quá dài/không parse được (kho Zalo có 357 dòng `text` rỗng và điều luật dài tới khoảng 250 nghìn ký tự). 40 phút: chốt D7 (tokenizer, độ dài tối đa từng mô hình). 30 phút: rà soát E0–E5, R0–R3, đầu vào/đầu ra và top-k. | Mô tả chunking, truy xuất, reranking có thể triển khai; quyết định D7. |
| 4 | 50 phút: chốt D1 và D8 (cỡ mẫu Zalo, tập dev, cách chọn cấu hình Giai đoạn B). 40 phút: cách tạo câu không trả lời được cho Zalo và chốt D6 cho ViQuAD. 30 phút: đánh dấu điều kiện cần quyền dữ liệu hoặc xác nhận giấy phép. | Quy trình dữ liệu, cỡ mẫu thực tế, danh sách rủi ro dữ liệu. |
| 5 | 50 phút: định nghĩa vận hành cho Recall/MRR/nDCG, EM/F1, correctness, faithfulness, fabrication, false refusal; chốt D2. 70 phút: đặc tả RAH và chốt D3–D5; ghi rõ RAH có thể âm, tỷ lệ RAH/H không ổn định khi H gần 0, báo cáo giá trị tuyệt đối kèm CI và không diễn giải nhân quả khi giả định chưa được chứng minh. | Bảng chỉ số có công thức/đơn vị/tập con áp dụng; định nghĩa RAH thận trọng. |
| 6 | 50 phút: chốt phân tích thống kê (đơn vị bootstrap, kiểm định hoán vị ghép cặp, hiệu chỉnh Holm, số phép so sánh). 40 phút: thiết kế hiệu chỉnh judge, nhãn người và quy tắc phân xử bất đồng. 30 phút: tiêu chí báo cáo độ trễ/VRAM; chốt D9. | Kế hoạch phân tích và quy trình judge; bảng D1–D9 đã có quyết định. |
| 7 | Pilot 1 (Colab): BM25 trên kho Zalo Legal, mỗi điều luật là một chunk, tách từ bằng underthesea (nếu quá chậm trên 61.425 điều thì dùng pyvi và ghi rõ). Tính Recall@5, Recall@20, MRR@10, nDCG@5 trên 788 truy vấn có nhãn. | Bảng chỉ số BM25; notebook pilot chạy lại được. |
| 8 | Pilot 2 (Colab, GPU): nhúng kho bằng `BAAI/bge-m3`, lập chỉ mục FAISS, tính cùng bộ chỉ số. Ghi lại cách cắt điều luật vượt độ dài tối đa và số điều bị cắt. | Bảng chỉ số dense; thời gian nhúng và kích thước chỉ mục. |
| 9 | 50 phút: hybrid BM25 + dense với α = 0,7. 40 phút: khoảng tin cậy bootstrap 95% cho ba cấu hình. 30 phút: ghi môi trường chạy và giới hạn của pilot. Đây cũng là ngày dự phòng nếu ngày 7–8 trễ; khi đó bỏ hybrid. | Bảng kết quả pilot kèm CI, hoặc ghi chú rõ phần chưa chạy. |
| 10 | 70 phút: viết nháp mục 3–5 theo nội dung đã chốt. 30 phút: sơ đồ pipeline và bảng cấu hình. 20 phút: gửi người hướng dẫn bản nháp phương pháp và bảng D1–D9 để có phản hồi trước ngày 14. | Bản nháp phương pháp đã gửi. |
| 11 | 60 phút: viết công trình liên quan theo nhóm chủ đề từ nguồn đã xác minh; kiểm tra mọi trích dẫn có mục tham khảo tương ứng. 60 phút: viết giới thiệu, động cơ và đóng góp. | Bản nháp mục 1–2. |
| 12 | 50 phút: viết mục 6 (thống kê dữ liệu và pilot). 40 phút: viết hạn chế/đe dọa tính hợp lệ (rò rỉ tri thức, judge, tính đại diện, khác biệt miền, các điểm D còn mở). 30 phút: bảng/hình mẫu chưa có số liệu cho mục 5.5. | Bản thảo đủ mục 3–7. |
| 13 | 30 phút: viết tóm tắt và kết luận. 60 phút: đọc liền mạch như người phản biện mới; kiểm tra thuật ngữ, ký hiệu, số cấu hình, cỡ mẫu và tổng lượt sinh nhất quán. 30 phút: sửa các điểm không khớp. | Bản thảo hoàn chỉnh vòng phản biện nội bộ. |
| 14 | 50 phút: tiếp nhận/sửa phản hồi của người hướng dẫn (nếu chưa có, ghi thành việc còn chờ). 40 phút: kiểm tra tài liệu tham khảo, bảng, hình, chú thích và rà soát lần cuối để không còn kết quả dự kiến trình bày như sự thật. 30 phút: xuất bản nộp và ghi rõ các bước thực nghiệm tiếp theo. | Bản thảo để xin phản hồi/duyệt; danh sách điều kiện trước khi chuyển thành bài báo kết quả. |

## Cổng kiểm tra tiến độ

- **Cuối ngày 2:** mọi câu hỏi nghiên cứu gắn được với phép đo và phép so sánh cụ thể; khẳng định về khoảng trống chỉ dựa trên nguồn đã xác minh.
- **Cuối ngày 6:** cả chín điểm D1–D9 có quyết định hoặc được ghi thành hạn chế; người khác có thể hiểu chính xác cách tính chỉ số và phân tích so sánh.
- **Cuối ngày 9:** có bảng pilot với số liệu thật, hoặc quyết định rõ ràng là bản thảo không có pilot.
- **Cuối ngày 10:** người hướng dẫn đã nhận bản nháp phương pháp.
- **Cuối ngày 13:** đủ bản thảo hoàn chỉnh; mọi bảng kết quả chưa có dữ liệu đều để trống/ghi là kế hoạch.
- **Cuối ngày 14:** có bản thảo sạch để người hướng dẫn phản biện, chưa gọi là bài báo thực nghiệm hoàn tất.

## Các việc nằm ngoài mục tiêu 14 ngày

Không cam kết hoàn tất trong 28 giờ: triển khai toàn bộ pipeline; chạy lưới truy xuất 144 cấu hình; sinh và chấm khoảng 40.000 câu trả lời; tạo nhãn người; xác nhận độ tin cậy của judge; và rút ra kết luận thực nghiệm. Đây là các điều kiện cần hoàn thành trước khi gửi một bài báo kết quả.

Pilot chỉ gồm ba cấu hình truy xuất trên một bộ dữ liệu, không có phân đoạn ngoài mức Điều, không reranking và không sinh câu trả lời. Pilot dùng toàn bộ truy vấn có nhãn để mô tả, không dùng để chọn cấu hình cho Giai đoạn B, và không đủ để trả lời bất kỳ câu hỏi nghiên cứu nào.

Nếu dữ liệu đã xử lý chưa có trên Drive, ưu tiên xác nhận/lưu dữ liệu trước mọi việc phụ thuộc dữ liệu. Nếu mục tiêu thực sự là bài báo có kết quả đầy đủ, cần gia hạn lịch hoặc thu hẹp phạm vi nghiên cứu với sự đồng ý của người hướng dẫn; không được bỏ qua kiểm định hoặc báo cáo kết quả chưa chạy để giữ hạn hai tuần.
