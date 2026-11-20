# Kế hoạch 16 tuần để đạt mục tiêu đề cương

Kế hoạch này phủ cả sáu mục tiêu cụ thể ở mục 3.2 của đề cương v2. Hai tuần đầu chính là `Kế hoạch 14 ngày và mục lục bài báo.md` (chi tiết trong `Kế hoạch chi tiết từng ngày.md`); các tuần 3–16 đi theo lịch gốc ở mục 7 của đề cương.

## Giả định

- **Thời gian:** 2 giờ mỗi ngày, 14 giờ mỗi tuần, tổng khoảng 224 giờ. Các lượt chạy GPU dài chạy không cần người trông, ngoài 14 giờ này.
- **Mốc thời gian:** tuần 1 bắt đầu thứ Năm 12/11/2026; tuần 16 kết thúc thứ Tư 03/03/2027.
- **Tết Đinh Mùi rơi vào tuần 13** (mùng 1 là 06/02/2027). Tuần này chỉ xếp việc làm một mình, không phụ thuộc người khác; nếu nghỉ hẳn thì lịch lùi một tuần.
- **Người thứ hai:** đề cương cần hai người gán nhãn độc lập 300 câu trả lời và kiểm tra chéo câu hỏi. Phải có người này trước tuần 7; nếu không, mục tiêu 3 chỉ đạt một phần.
- **Tính toán:** Colab hoặc Kaggle cho embedding và reranker; GPU thuê theo giờ cho Giai đoạn B nếu cần. Các con số GPU và chi phí bên dưới là ước lượng, phải đo lại từ pilot ở tuần 2.

## Tổng quan

| Tuần | Ngày | Trọng tâm | Sản phẩm cuối tuần | Mục tiêu đề cương |
|---|---|---|---|---|
| 1–2 | 12/11–25/11 | Chốt thiết kế, pilot truy xuất, bản thảo protocol | Bản protocol; quyết định D1–D9; bảng pilot | Nền cho tất cả |
| 3 | 26/11–02/12 | Khung mã, phân đoạn C1–C4, truy xuất E0/E3 | Truy xuất chạy bằng cấu hình trên cả hai bộ | 1 |
| 4 | 03/12–09/12 | Sinh câu trả lời, chọn mô hình sinh, R1 | Pipeline đầu-cuối trên 100 câu | 1 |
| 5 | 10/12–16/12 | Tập đánh giá | Hai tập test và dev đã đóng băng | 2 |
| 6 | 17/12–23/12 | ViStructChunk, C6, các mức E/R còn lại | Đủ 6 × 6 × 4 thành phần chạy được | 1, 4 |
| 7 | 24/12–30/12 | Judge và nhãn người | Báo cáo κ | 3 |
| 8 | 31/12–06/01 | Giai đoạn A: lập chỉ mục và truy xuất | Kết quả truy xuất 36 tổ hợp C × E | 5 |
| 9 | 07/01–13/01 | Giai đoạn A: reranking, chọn cấu hình B | Bảng 144 cấu hình; danh sách cấu hình B | 5 |
| 10 | 14/01–20/01 | Giai đoạn B: sinh câu trả lời | Câu trả lời thô của mọi cấu hình | 5 |
| 11 | 21/01–27/01 | Giai đoạn B: chấm và tính chỉ số | Bảng chỉ số theo từng câu hỏi | 3, 5 |
| 12 | 28/01–03/02 | Độ bền, chi phí, chạy lại, dự phòng | Kết quả thô hoàn chỉnh | 5 |
| 13 | 04/02–10/02 | Phân tích thống kê, RAH (tuần Tết) | Bảng số liệu kèm khoảng tin cậy | 3, 5 |
| 14 | 11/02–17/02 | Phân tích lỗi, Pareto, khuyến nghị | Hình, bảng, bảng khuyến nghị | 6 |
| 15 | 18/02–24/02 | Viết báo cáo, đóng gói dữ liệu và mã | Bản thảo đầy đủ; ViRAG-Hallu | 6 |
| 16 | 25/02–03/03 | Phản biện thử, sửa, nộp | Khóa luận, bài báo, mã nguồn | Tất cả |

## Cổng kiểm tra và quy tắc cắt phạm vi

Mỗi cổng có một điều kiện đạt. Nếu không đạt, áp dụng bậc cắt tiếp theo trong thang bên dưới thay vì dồn việc sang tuần sau.

| Cuối tuần | Điều kiện đạt |
|---|---|
| 2 | D1–D9 đã chốt; có bảng pilot; người hướng dẫn đã trả lời về nơi nộp |
| 4 | Một lệnh chạy được từ câu hỏi đến câu trả lời trên 100 câu ViQuAD; đã chọn mô hình sinh |
| 6 | Tập đánh giá đóng băng; C5 parse được phần lớn kho luật, có báo cáo tỷ lệ lỗi |
| 7 | κ giữa judge và người đạt 0,7 trở lên, hoặc đã kích hoạt phương án dự phòng |
| 9 | Có bảng Giai đoạn A; danh sách cấu hình Giai đoạn B đóng băng |
| 12 | Mọi cấu hình B có đủ câu trả lời và điểm chấm |
| 14 | Mọi con số trong bài có khoảng tin cậy và truy được về file kết quả |

**Thang cắt phạm vi (theo thứ tự, cắt trên trước):**

1. Bỏ các phần đề cương đã ghi là tùy chọn: cổng từ chối dựa trên bằng chứng, `Qwen/Qwen3-Embedding-0.6B`.
2. Zalo không viết tay câu ngoài kho; chỉ dùng câu không trả lời được do loại điều luật (phương án A của D1).
3. Bỏ R3, lưới còn 6 × 6 × 3 = 108 cấu hình.
4. Bỏ C6 (phân đoạn ngữ nghĩa), lưới còn 5 × 6 × 3 = 90.
5. Giai đoạn B giảm còn 500 câu mỗi bộ (đề cương đã nêu phương án này).
6. Kiểm tra độ bền với mô hình sinh thứ hai giảm còn 3 cấu hình, hoặc chuyển thành hạn chế.

**Không cắt trong bất kỳ trường hợp nào:** hai điều kiện closed-book và oracle; hiệu chỉnh judge bằng nhãn người; đóng băng tập đánh giá và danh sách cấu hình B trước khi xem kết quả đầu-cuối; khoảng tin cậy và hiệu chỉnh nhiều phép so sánh. Thiếu các phần này thì RAH và các kết luận không bảo vệ được.

## Chi tiết từng tuần

### Tuần 1–2 – Thiết kế, pilot, bản protocol

Theo `Kế hoạch chi tiết từng ngày.md`. Ba thứ các tuần sau dùng lại: file quyết định D1–D9, notebook pilot (thành lõi của mô-đun truy xuất và đánh giá), và bản thảo protocol (thành khung bài báo ở tuần 15).

Việc thêm trong tuần 2: bắt đầu tìm người gán nhãn thứ hai; ghi lại tốc độ nhúng (số điều luật mỗi giây) từ pilot để ước lượng tuần 8.

### Tuần 3 – Khung mã, phân đoạn cơ bản, truy xuất

- `git init`, thêm file phụ thuộc có ghim phiên bản. Mã nằm trong một gói nhỏ, mỗi yếu tố một file: `chunking.py`, `retrieval.py`, `rerank.py`, `generate.py`, `judge.py`, `metrics.py`, `run.py`. Colab chỉ gọi gói này.
- Một lượt chạy được xác định bằng một dòng cấu hình (bộ dữ liệu, C, E, R, seed). Kết quả ghi thành một dòng cho mỗi cặp (cấu hình, câu hỏi); mọi phân tích về sau đọc từ bảng này.
- Bộ nhớ đệm theo khóa (bộ dữ liệu, C) cho chunk và (bộ dữ liệu, C, E) cho embedding, để tuần 8 không nhúng lại.
- Cài C1–C4 theo đặc tả ngày 3; chuyển BM25 và dense từ notebook pilot vào gói.
- Kiểm tra: mỗi hàm phân đoạn có một `assert` trên một điều luật mẫu; kết quả BM25 và dense của gói khớp bảng pilot.

**Sản phẩm:** một lệnh chạy truy xuất cho cấu hình bất kỳ trong C1–C4 × {E0, E3} trên cả hai bộ.

### Tuần 4 – Sinh câu trả lời, pipeline đầu-cuối

- Chạy mô hình sinh cục bộ (vLLM, hoặc transformers lượng tử hóa 4-bit); temperature 0, một prompt cố định, 5 đoạn ngữ cảnh.
- So sánh hai ứng viên của đề cương (`Qwen/Qwen3-8B`, `google/gemma-3-12b-it`) trên 100 câu ViQuAD, lấy từ phần sẽ thành tập dev. Tiêu chí chọn ghi trước khi chạy: tỷ lệ từ chối đúng trên câu không trả lời được, rồi đến độ đúng.
- Viết quy tắc nhận diện câu từ chối ("Không tìm thấy thông tin" và các biến thể); kiểm tra tay 50 câu trả lời.
- Thêm R1 (`BAAI/bge-reranker-v2-m3`), điều kiện closed-book và oracle.
- Đo thông lượng sinh (câu mỗi giây) để ước lượng tuần 10.

**Sản phẩm:** pipeline đầu-cuối trên 100 câu; mô hình sinh đã chọn kèm lý do; prompt đóng băng.

### Tuần 5 – Tập đánh giá

- **ViQuAD:** lấy mẫu phân tầng 700 + 300 từ train và validation, tách dev/test theo `title`. Dựng kho: các đoạn ViQuAD cộng khoảng 20.000 đoạn Wikipedia tiếng Việt cùng chủ đề; ghi rõ nguồn và ngày của bản Wikipedia, và quy tắc chọn "cùng chủ đề".
- **Zalo Legal:** tách dev/test theo điều luật vàng; chọn nhóm điều luật để loại khỏi kho, tạo câu không trả lời được (cỡ mẫu theo D1).
- **Kiểm tra tay:** 50 câu không trả lời được mỗi bộ, xem kho còn đoạn nào trả lời được không (D6); ghi tỷ lệ.
- Lưu cho mỗi câu hỏi: đáp án vàng (nếu có), đoạn/điều luật vàng, nhãn trả lời được hay không, lý do không trả lời được.
- Đóng băng: lưu file, ghi mã băm và seed; từ đây không sửa tập test.

**Sản phẩm:** hai tập test, hai tập dev, hai kho tài liệu, kèm bảng thống kê.

### Tuần 6 – ViStructChunk và các thành phần còn lại

- Parser Điều → Khoản → Điểm cho kho Zalo; mỗi chunk gắn tiêu đề cha. Quy tắc cho các trường hợp biên đã nêu ở ngày 3.
- Kiểm tra parser: 30 điều luật chọn ngẫu nhiên đối chiếu tay; báo cáo tỷ lệ điều luật parse được, số chunk rỗng, phân phối độ dài chunk. C4 và C5 phải có cùng ranh giới cắt ở mức so sánh đã thiết kế.
- ViStructChunk cho văn bản thường: không cắt giữa câu và giữa từ ghép.
- C6: phân đoạn ngữ nghĩa dùng một embedding nhỏ cố định.
- Thêm E1, E2, E4, E5 và R2, R3 (chủ yếu là đổi tên mô hình; E1 cần tách từ trước và kiểm tra giới hạn độ dài).

**Sản phẩm:** đủ 6 mức C, 6 mức E, 4 mức R; mỗi mức chạy thử được trên 50 câu.

### Tuần 7 – Judge và nhãn người

- Viết prompt judge tiếng Việt, đầu ra JSON: tách mệnh đề, gán nhãn hỗ trợ so với ngữ cảnh (H_ctx) và so với bằng chứng vàng (H_gold), chấm correctness 0/1/2.
- Chạy judge trên 500 mẫu ViHallu; báo cáo độ khớp với nhãn gốc.
- Sinh câu trả lời của cấu hình neo và vài cấu hình khác trên tập dev, lấy 300 câu (150 mỗi bộ) cho hai người gán nhãn độc lập. Ước lượng khoảng 10 giờ mỗi người; đây là phần lớn thời gian của tuần.
- Tính κ giữa hai người và giữa judge với nhãn đã phân xử. Nếu dưới 0,7: sửa prompt trên một nửa mẫu, kiểm tra lại trên nửa còn lại; nếu vẫn không đạt, thêm mô hình NLI theo phương án dự phòng của đề cương.
- Cài chỉ số "nhầm điều luật" bằng biểu thức chính quy; kiểm tra tay 30 trường hợp.

**Sản phẩm:** báo cáo κ; prompt judge đóng băng; 300 mẫu có nhãn người.

### Tuần 8–9 – Giai đoạn A

- **Tuần 8:** dựng chunk cho 6 mức C trên hai kho; nhúng bằng bốn mô hình dense (24 chỉ mục mỗi bộ) và dựng BM25 cho 6 mức C; chạy truy xuất top-20 cho 36 tổ hợp C × E trên dev và test. Các lượt nhúng xếp hàng chạy nền; trong lúc chờ, viết phần phương pháp cho bài.
- **Tuần 9:** reranking top-20 thành top-5 với R1–R3; tính Recall@5, Recall@20, MRR@10, nDCG@5; ghi độ trễ, kích thước chỉ mục, VRAM. Dựng bảng 144 cấu hình với khoảng tin cậy.
- Chọn 4 tổ hợp tốt nhất **chỉ dựa trên tập dev**; ghi tiêu chí chọn và đóng băng danh sách cấu hình Giai đoạn B trước khi sinh bất kỳ câu trả lời nào trên tập test.

**Sản phẩm:** bảng Giai đoạn A; danh sách khoảng 20 cấu hình Giai đoạn B.

### Tuần 10–12 – Giai đoạn B

- **Tuần 10:** sinh câu trả lời cho mọi cấu hình B trên hai tập test, gồm closed-book và oracle. Lưu nguyên văn prompt, ngữ cảnh và câu trả lời; kiểm tra tay 20 câu mỗi cấu hình đầu tiên để bắt lỗi định dạng sớm.
- **Tuần 11:** chạy judge trên toàn bộ câu trả lời; tính EM, token-F1 (ViQuAD), correctness, H_ctx, H_gold, fabrication, false refusal, nhầm điều luật. Kiểm tra tỷ lệ đầu ra judge không hợp lệ và chạy lại phần lỗi.
- **Tuần 12:** kiểm tra độ bền (5 cấu hình quan trọng nhất, mô hình sinh thứ hai, 300 câu); đo chi phí theo quy ước ngày 6; chạy lại các lượt hỏng. Phần còn lại của tuần là dự phòng cho tuần 8–11.

**Sản phẩm:** bảng kết quả một dòng cho mỗi cặp (cấu hình, câu hỏi), đủ mọi chỉ số.

### Tuần 13 – Phân tích thống kê (tuần Tết)

Chỉ cần máy tính và bảng kết quả, không cần GPU hay người khác.

- Khoảng tin cậy bootstrap (theo cụm `title` với ViQuAD); kiểm định hoán vị ghép cặp so với cấu hình neo; hiệu chỉnh Holm theo họ phép so sánh đã ghi trước.
- RAH cho từng cấu hình trên câu trả lời được, kèm khoảng tin cậy; tỷ lệ quy cho truy xuất, với ngưỡng không báo cáo khi H quá nhỏ; so sánh hai miền (RQ4).
- Hồi quy logistic xác suất ảo giác theo Recall@5, độ dài chunk, reranker.
- Điền bảng RQ đã lập ở ngày 2: mỗi giả thuyết được ủng hộ, bị bác bỏ, hay chưa kết luận được.

**Sản phẩm:** toàn bộ bảng số liệu cho RQ1–RQ4.

### Tuần 14 – Phân tích lỗi và khuyến nghị

- Gắn nhãn nguyên nhân cho 100 trường hợp ảo giác chọn ngẫu nhiên (năm loại nguyên nhân của đề cương); đối chiếu tỷ lệ "do truy xuất" với RAH.
- Biên Pareto theo độ đúng, tỷ lệ ảo giác, độ trễ cho từng bộ dữ liệu; điểm có trọng số cho ba kịch bản; phân tích độ nhạy ±0,1.
- Dựng hình và bảng cuối cùng; viết bảng khuyến nghị kèm điều kiện áp dụng (RQ5).

**Sản phẩm:** hình, bảng, bảng khuyến nghị.

### Tuần 15 – Viết và đóng gói

- Chuyển bản protocol thành bài báo kết quả: điền mục kết quả, viết lại tóm tắt, thảo luận, kết luận. Phần giới thiệu, công trình liên quan và phương pháp đã có từ tuần 2 và tuần 8.
- Đóng gói ViRAG-Hallu: câu hỏi kèm nhãn và đoạn vàng, 300 mẫu nhãn người, 100 trường hợp đã phân loại; viết thẻ dữ liệu; kiểm tra giấy phép của ViQuAD và Zalo Legal trước khi công bố lại bất kỳ phần nào.
- Script tái lập: một lệnh cho mỗi bảng trong bài.

**Sản phẩm:** bản thảo đầy đủ; gói dữ liệu; kho mã chạy lại được.

### Tuần 16 – Hoàn thiện và nộp

- Phản biện thử với người hướng dẫn hoặc đồng nghiệp; sửa theo phản hồi.
- Chạy lại danh sách kiểm tra nhất quán của ngày 13 trên bản cuối.
- Nộp khóa luận và bài báo; công bố mã và dữ liệu.

## Ước lượng tính toán và chi phí

Các con số dưới đây là ước lượng thô để lập kế hoạch; đo lại ở tuần 2 và tuần 4 rồi cập nhật.

| Hạng mục | Khối lượng | Ghi chú |
|---|---|---|
| Nhúng (tuần 8) | 6 mức C × 4 mô hình × 2 kho = 48 lượt | Kho Zalo chiếm phần lớn; số chunk ở C1 và C5 chưa biết cho đến tuần 6 |
| Reranking (tuần 9) | 36 tổ hợp × 3 reranker × 2 bộ, mỗi câu hỏi 20 cặp | Chạy được trên GPU 16 GB |
| Sinh (tuần 10) | Khoảng 20 cấu hình × tổng số câu test hai bộ | 40.000 lượt nếu giữ 1.000 câu mỗi bộ; khoảng 32.000 nếu Zalo còn 600 |
| Judge (tuần 11) | Một đến hai lượt gọi cho mỗi câu trả lời | Xem cảnh báo bên dưới |

**Cảnh báo về chi phí judge:** đề cương ước tính dưới 50 USD cho judge và kiểm tra độ bền. Mỗi lượt chấm faithfulness phải gửi cả 5 đoạn ngữ cảnh, tức khoảng 2.000–3.000 token đầu vào; với 32.000–40.000 câu trả lời là khoảng 80–100 triệu token đầu vào. Con số 50 USD chỉ đúng với mô hình judge giá rất thấp. Cần tính lại ở tuần 7 khi đã chọn judge; nếu vượt ngân sách thì dùng judge mã nguồn mở chạy cục bộ, hoặc cắt theo bậc 5 của thang cắt.

## Rủi ro chính

| Rủi ro | Phát hiện ở | Xử lý |
|---|---|---|
| Không có người gán nhãn thứ hai | Tuần 2–5 | Hỏi người hướng dẫn hoặc bạn cùng khóa ngay tuần 2; nếu không có, báo cáo độ nhất quán của một người gán nhãn hai lần cách nhau một tuần và ghi thành hạn chế |
| Parser C5 lỗi nhiều trên văn bản luật | Tuần 6 | Báo cáo tỷ lệ lỗi; điều luật không parse được dùng lại chunk của C4 |
| κ dưới 0,7 | Tuần 7 | Phương án dự phòng của đề cương; không chạy Giai đoạn B khi judge chưa đạt |
| Hết hạn mức GPU giữa Giai đoạn A | Tuần 8 | Bộ nhớ đệm embedding cho phép chạy tiếp; áp dụng bậc cắt 3–4 |
| Thời gian thực tế vượt 14 giờ mỗi tuần | Mọi cổng | Áp dụng thang cắt theo thứ tự; không bỏ các mục "không cắt" |
| Tuần Tết không làm được | Tuần 13 | Lịch lùi một tuần, nộp ngày 10/03/2027; báo trước cho người hướng dẫn |
