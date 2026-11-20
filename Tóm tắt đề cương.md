# Tóm tắt đề cương nghiên cứu

## Tên đề tài

**Đánh giá thực nghiệm ảnh hưởng của các lựa chọn thiết kế đến độ chính xác và hiện tượng ảo giác trong hệ thống tạo sinh tăng cường truy xuất (RAG) cho văn bản tiếng Việt.**

## Bối cảnh và khoảng trống

RAG có thể giảm hiện tượng mô hình ngôn ngữ lớn (LLM) tạo thông tin sai bằng cách cung cấp tài liệu làm căn cứ trả lời. Tuy nhiên, hiệu quả phụ thuộc vào cách chia đoạn, mô hình truy xuất và xếp hạng lại. Những lựa chọn này chưa được đánh giá có hệ thống trong bối cảnh tiếng Việt, đặc biệt là văn bản pháp luật có cấu trúc Điều/Khoản/Điểm.

Các nghiên cứu hiện có thường đo chất lượng truy xuất hoặc phát hiện ảo giác riêng rẽ. Đề tài kết nối hai khâu để tìm hiểu chất lượng truy xuất ảnh hưởng thế nào đến độ đúng và ảo giác trong câu trả lời cuối cùng.

## Mục tiêu

- Xây dựng pipeline RAG tiếng Việt có thể tái lập và hoán đổi độc lập các thành phần.
- So sánh tác động của chiến lược phân đoạn, mô hình nhúng/truy xuất và xếp hạng lại.
- Đánh giá cả câu hỏi trả lời được và không trả lời được.
- Đề xuất cách đo phần ảo giác quy cho truy xuất (RAH), bên cạnh các chỉ số độ đúng và ảo giác thông thường.
- Xây dựng chiến lược phân đoạn **ViStructChunk** cho văn bản pháp luật Việt Nam.
- Đưa ra khuyến nghị cấu hình theo miền và kịch bản sử dụng, có cân nhắc độ đúng, ảo giác và chi phí.

## Câu hỏi nghiên cứu

1. Chiến lược phân đoạn ảnh hưởng thế nào đến truy xuất và ảo giác?
2. Mô hình nhúng chuyên tiếng Việt có ưu thế so với mô hình đa ngôn ngữ không, và ưu thế đó có cải thiện câu trả lời cuối không?
3. Xếp hạng lại cải thiện độ đúng/giảm ảo giác ra sao so với chi phí độ trễ?
4. Bao nhiêu phần ảo giác có thể quy cho tầng truy xuất?
5. Cấu hình nào phù hợp nhất với từng miền và kịch bản sử dụng?

## Thiết kế hệ thống và các yếu tố

Pipeline dự kiến: tài liệu → tiền xử lý → phân đoạn → nhúng và lập chỉ mục → truy xuất top-20 → xếp hạng lại → lấy top-5 → sinh câu trả lời → đánh giá.

- **Phân đoạn (6 mức):** cố định 256 token; cố định 512 token với overlap 64; theo câu; theo cấu trúc tài liệu; ViStructChunk; phân đoạn ngữ nghĩa.
- **Truy xuất/embedding (6 mức):** BM25; Vietnamese Bi-Encoder; Vietnamese Embedding v2; BGE-M3; multilingual-e5-large; hybrid BGE-M3 và BM25 với α = 0,7.
- **Reranking (4 mức):** không rerank; BGE reranker đa ngôn ngữ; Vietnamese Reranker; ViRanker hoặc PhoRanker.

ViStructChunk phân đoạn văn bản luật theo cây Điều → Khoản → Điểm và thêm tiêu đề cha vào từng đoạn. So sánh C4–C5 được thiết kế để chủ yếu đo tác động của việc bổ sung tiêu đề, với cùng ranh giới cắt.

## Dữ liệu và thực nghiệm

Dùng hai bộ dữ liệu đại diện cho hai miền:

- **UIT-ViQuAD 2.0:** văn bản Wikipedia, có câu hỏi trả lời được và không trả lời được; dự kiến bổ sung khoảng 20.000 đoạn gây nhiễu.
- **Zalo Legal Text Retrieval 2021:** truy vấn và văn bản pháp luật; câu hỏi không trả lời được được tạo bằng cách loại tài liệu vàng khỏi kho hoặc viết câu hỏi ngoài kho và kiểm tra chéo.

Dự kiến lấy mẫu 1.000 câu hỏi cho mỗi bộ dữ liệu, gồm 700 câu trả lời được và 300 câu không trả lời được.

Thực nghiệm chia thành hai giai đoạn:

1. **Giai đoạn A:** đánh giá truy xuất trên toàn bộ 6 × 6 × 4 = 144 cấu hình, không gọi LLM.
2. **Giai đoạn B:** đánh giá đầu-cuối trên khoảng 20 cấu hình, gồm cấu hình neo, các biến thể thay từng yếu tố, một số tổ hợp tốt nhất, cùng hai điều kiện tham chiếu: **closed-book** (không cung cấp ngữ cảnh) và **oracle** (cung cấp đoạn vàng).

Mô hình sinh, prompt, số đoạn ngữ cảnh (5), nhiệt độ (0) và seed được giữ cố định để cô lập ảnh hưởng của các thành phần truy xuất. Dự kiến kiểm tra độ bền với mô hình sinh thứ hai trên một tập con.

## Chỉ số đánh giá

- **Truy xuất:** Recall@5, Recall@20, MRR@10 và nDCG@5.
- **Độ đúng:** Exact Match, token-F1 và điểm correctness của LLM-as-judge theo thang 0–2.
- **Ảo giác:** faithfulness với ngữ cảnh, fabrication rate trên câu hỏi không trả lời được, false refusal trên câu hỏi trả lời được; đồng thời phân loại ảo giác nội tại và ngoại lai.
- **Chi phí:** độ trễ truy xuất/reranking, kích thước chỉ mục và VRAM.

### Chỉ số RAH

Gọi H(k) là tỷ lệ ảo giác của cấu hình RAG k và H(oracle) là tỷ lệ ảo giác khi cung cấp đoạn vàng. Đề cương định nghĩa:

**RAH(k) = H(k) − H(oracle)**

RAH ước lượng phần ảo giác tăng thêm so với điều kiện truy xuất lý tưởng. Tỷ lệ RAH(k)/H(k) được dùng để biểu thị tỷ trọng ảo giác quy cho truy xuất. H(cb), tỷ lệ ảo giác trong điều kiện closed-book, là một mốc tham chiếu khác.

## Kiểm chứng và phân tích

- Dùng judge là LLM khác với mô hình sinh, prompt tiếng Việt và đầu ra JSON.
- Hai người gán nhãn độc lập 300 câu trả lời; đo Cohen’s κ giữa người với người và giữa judge với người, mục tiêu κ ≥ 0,7.
- Dùng bootstrap 1.000 lần để tính khoảng tin cậy 95%, kiểm định hoán vị theo cặp và hiệu chỉnh Holm.
- Phân tích hồi quy logistic và phân tích định tính 100 trường hợp ảo giác để khảo sát nguyên nhân.
- Xếp hạng cấu hình bằng biên Pareto và điểm đa tiêu chí cho các kịch bản pháp luật/y tế, tra cứu nhanh và cân bằng.

## Sản phẩm dự kiến

- Pipeline RAG tiếng Việt mô-đun cùng mã nguồn/script tái lập.
- Bộ dữ liệu **ViRAG-Hallu** gồm câu hỏi có nhãn trả lời được/không, đoạn vàng, mẫu gán nhãn người và trường hợp ảo giác đã phân loại.
- Bảng khuyến nghị cấu hình theo miền và kịch bản.
- Khóa luận và một bài báo gửi hội nghị trong nước hoặc workshop quốc tế.

## Tiến độ dự kiến

Kế hoạch kéo dài **16 tuần**: hoàn thiện tài liệu và xin dữ liệu (tuần 1–2); xây pipeline và tập đánh giá (tuần 3–6); hiệu chỉnh judge (tuần 7); chạy đánh giá truy xuất (tuần 8–9); chạy đánh giá đầu-cuối (tuần 10–12); phân tích thống kê và tổng hợp khuyến nghị (tuần 13); viết, chỉnh sửa và nộp báo cáo (tuần 14–16).

## Rủi ro và phương án dự phòng

- Nếu không xin được Zalo Legal, cân nhắc ALQAC hoặc bộ luật thay thế.
- Nếu judge chưa đạt κ mục tiêu, hiệu chỉnh prompt, kết hợp mô hình NLI hoặc tăng nhãn người.
- Nếu thiếu GPU, giảm số câu hỏi hoặc dùng LLM nhỏ hơn/thuê GPU.
- Nếu khác biệt giữa cấu hình không có ý nghĩa thống kê, báo cáo đó như một kết quả và tập trung phân tích miền khó.
- Với nguy cơ LLM đã biết đáp án Wikipedia từ dữ liệu huấn luyện, dùng closed-book làm mốc và báo cáo rõ ảnh hưởng này.
