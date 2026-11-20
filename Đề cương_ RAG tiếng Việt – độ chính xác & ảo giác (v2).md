# ĐỀ CƯƠNG NGHIÊN CỨU

## Đánh giá thực nghiệm ảnh hưởng của các lựa chọn thiết kế đến độ chính xác và hiện tượng ảo giác trong hệ thống tạo sinh tăng cường truy xuất (RAG) cho văn bản tiếng Việt

---

## 1. Đặt vấn đề và tính cấp thiết

Các mô hình ngôn ngữ lớn (LLM) trả lời trôi chảy nhưng thường "bịa" thông tin (ảo giác – hallucination), đặc biệt với tri thức chuyên ngành hoặc tri thức mới. RAG giảm thiểu vấn đề này bằng cách truy xuất tài liệu liên quan và buộc mô hình trả lời dựa trên bằng chứng. Tuy nhiên, chất lượng của một hệ thống RAG phụ thuộc mạnh vào các quyết định kỹ thuật tưởng như "nhỏ": cắt tài liệu thế nào, dùng mô hình nhúng nào, có xếp hạng lại hay không. Phần lớn khuyến nghị hiện có được rút ra từ tiếng Anh.

Tiếng Việt có những đặc thù khiến các khuyến nghị này không chắc còn đúng:

- **Đơn vị từ không trùng với khoảng trắng** (từ ghép, từ láy), ảnh hưởng đến cả tách từ cho BM25 lẫn số token khi phân đoạn.
- **Văn bản hành chính – pháp luật có cấu trúc riêng** (Điều/Khoản/Điểm) mà phân đoạn theo độ dài cố định dễ cắt đứt ngữ cảnh.
- **Truy vấn thực tế nhiều nhiễu**: viết tắt, thiếu dấu, teencode, trộn tiếng Anh.
- **Tài nguyên đánh giá còn mỏng**: các benchmark truy xuất và phát hiện ảo giác cho tiếng Việt chỉ mới xuất hiện trong 1–2 năm gần đây.

Hơn nữa, các nghiên cứu Việt ngữ hiện có chủ yếu đo **chất lượng truy xuất** (Recall, MRR) hoặc **phát hiện ảo giác** một cách tách rời. Chưa có nghiên cứu nào nối hai đầu lại: *thay đổi cấu hình retrieval thì tỷ lệ ảo giác của câu trả lời cuối cùng thay đổi ra sao?* Đây chính là khoảng trống đề tài hướng tới.

## 2. Tổng quan nghiên cứu liên quan

**Truy xuất tiếng Việt.** Nghiên cứu gần đây nhất và sát đề tài nhất là của Nguyen & Quan (EACL 2026), xây dựng benchmark truy xuất đa miền cho tiếng Việt gồm 10 bộ dữ liệu trên 6 lĩnh vực và so sánh các mô hình lexical, dense, hybrid. Các kết luận chính: (i) kết hợp BM25 với dense theo nội suy tuyến tính (α ≈ 0,6–0,8) là chiến lược ổn định nhất; (ii) các mô hình đa ngôn ngữ như multilingual-e5-large và bge-m3 bền vững nhất giữa các miền, trong khi mô hình chuyên Việt (Vietnamese_Embedding_v2) mạnh ở văn bản chính thống/pháp luật nhưng yếu hơn ở miền hội thoại; (iii) kích thước mô hình không dự báo được chất lượng truy xuất. Nghiên cứu này **không** đánh giá phân đoạn, xếp hạng lại, hay ảnh hưởng đến câu trả lời sinh ra – là ba điểm đề tài sẽ bổ sung.

Về benchmark nhúng, VN-MTEB (Pham et al., 2025) cung cấp 41 bộ dữ liệu dịch từ MTEB cho 6 nhiệm vụ, còn Vietnamese Context Search (Nguyen et al., 2024) tập trung riêng vào truy xuất và xếp hạng lại.

**Xếp hạng lại tiếng Việt.** Hiện có ba cross-encoder công khai đáng chú ý: PhoRanker (2024), ViRanker (Dang et al., 2026 – nền BGE-M3, đánh giá trên MMARCO-VI) và AITeamVN/Vietnamese_Reranker (tinh chỉnh từ bge-reranker-v2-m3 với \~1,1 triệu bộ ba, hỗ trợ đoạn văn tới 2048 token). Chưa có nghiên cứu nào đo đóng góp của reranking đối với ảo giác đầu cuối.

**Ảo giác tiếng Việt.** Hai tài nguyên mới: ViHallu (cuộc thi DSC 2025, UIT) với 10.000 bộ ba (ngữ cảnh, câu hỏi, câu trả lời) gán nhãn không ảo giác / ảo giác nội tại / ảo giác ngoại lai, độ dài đoạn 88–1500 token được chọn chủ ý để giống ngữ cảnh RAG; và VietPS-Hallu (2026) cho lĩnh vực dịch vụ công. Cả hai phục vụ bài toán *phát hiện* ảo giác; đề tài sẽ tận dụng chúng để **hiệu chỉnh bộ chấm điểm** (judge) chứ không phải mục tiêu chính.

**Đánh giá RAG nói chung.** RAGTruth, RAGBench và các framework như RAGAS định nghĩa các chỉ số faithfulness, answer relevance, context precision. Các nghiên cứu benchmark bộ phát hiện ảo giác cho thấy LLM-as-judge có hiệu quả nhưng cần kiểm chứng với nhãn người.

**Khoảng trống:** chưa có nghiên cứu có kiểm soát nào cho tiếng Việt đo đồng thời (a) chất lượng truy xuất, (b) độ đúng câu trả lời, (c) mức độ ảo giác, dưới tác động của ba yếu tố thiết kế chunking – embedding – reranking. Ngoài ra, các nghiên cứu hiện có chỉ báo cáo một con số ảo giác tổng, chưa tách được phần ảo giác mà tầng truy xuất *có thể sửa* khỏi phần do bản thân mô hình sinh gây ra; và chưa có chiến lược phân đoạn nào được thiết kế riêng cho cấu trúc văn bản pháp luật Việt Nam.

## 3. Mục tiêu và câu hỏi nghiên cứu

### 3.1 Mục tiêu tổng quát

Xây dựng hệ thống RAG cho tiếng Việt và định lượng một cách có hệ thống ảnh hưởng của chiến lược phân đoạn, mô hình nhúng và xếp hạng lại đến độ chính xác và ảo giác của câu trả lời, từ đó đưa ra khuyến nghị cấu hình.

### 3.2 Mục tiêu cụ thể

1. Xây dựng pipeline RAG mô-đun, tái lập được, cho phép hoán đổi từng thành phần.
2. Xây dựng bộ đánh giá gồm cả câu hỏi trả lời được và câu hỏi *không* trả lời được từ kho tài liệu.
3. Thiết kế bộ đo ảo giác phù hợp tiếng Việt (LLM-as-judge có hiệu chỉnh bằng nhãn người), trong đó đề xuất chỉ số **ảo giác quy cho truy xuất** (retrieval-attributable hallucination, RAH) để tách phần ảo giác do truy xuất khỏi phần do mô hình sinh.
4. Đề xuất chiến lược phân đoạn **ViStructChunk** nhận biết cấu trúc pháp lý (Điều/Khoản/Điểm) và ranh giới từ tiếng Việt, so sánh với các chiến lược chuẩn.
5. Tiến hành thực nghiệm ablation và phân tích thống kê.
6. Xây dựng khung khuyến nghị cấu hình theo kịch bản sử dụng dựa trên biên Pareto và mô hình quyết định đa tiêu chí; công bố bộ dữ liệu đánh giá.

### 3.3 Câu hỏi nghiên cứu và giả thuyết

| # | Câu hỏi nghiên cứu | Giả thuyết kiểm định |
| --- | --- | --- |
| RQ1 | Chiến lược phân đoạn ảnh hưởng thế nào đến chất lượng truy xuất và ảo giác? | H1a: Phân đoạn theo cấu trúc cho faithfulness cao hơn phân đoạn cố định cùng độ dài; chunk quá dài làm tăng ảo giác do nhiễu ngữ cảnh. H1b: Trên văn bản luật, ViStructChunk (gắn tiêu đề Luật/Điều/Khoản vào mỗi chunk) giảm loại ảo giác "nhầm điều luật" so với cắt theo Điều thuần túy. |
| RQ2 | Mô hình nhúng chuyên Việt có vượt mô hình đa ngôn ngữ không, và lợi thế có chuyển sang câu trả lời cuối không? | H2: Chênh lệch Recall giữa các embedding mạnh bị "nén" lại ở tầng sinh; hybrid BM25+dense giảm ảo giác nhiều nhất vì giữ được thực thể/tên riêng. |
| RQ3 | Xếp hạng lại đóng góp bao nhiêu vào độ đúng và giảm ảo giác, với chi phí độ trễ ra sao? | H3: Reranker cải thiện nDCG@5 rõ rệt và giảm tỷ lệ ảo giác với câu hỏi có nhiều đoạn gây nhiễu; lợi ích giảm khi retriever đã mạnh. |
| RQ4 | Bao nhiêu phần ảo giác trong RAG tiếng Việt là do tầng truy xuất gây ra và có thể sửa bằng lựa chọn thiết kế? | H4: Tỷ lệ ảo giác quy cho truy xuất khác biệt rõ giữa hai miền: cao hơn ở văn bản luật (kho lớn, truy xuất khó) và thấp hơn ở Wikipedia (LLM có sẵn tri thức nền). |
| RQ5 | Cấu hình nào cân bằng tốt nhất giữa độ đúng, ảo giác và chi phí cho từng loại văn bản và kịch bản sử dụng? | Khảo sát bằng biên Pareto và mô hình quyết định đa tiêu chí, không có giả thuyết tiên nghiệm. |

## 4. Phạm vi và giới hạn

- **Trong phạm vi:** RAG một bước (single-hop), truy vấn và tài liệu đều tiếng Việt; tài liệu dạng văn bản thuần; mô hình sinh được **cố định** để cô lập ảnh hưởng của retrieval.
- **Ngoài phạm vi:** fine-tune embedding/reranker; multi-hop; RAG đa phương thức; tối ưu prompt sinh câu trả lời (chỉ dùng một prompt chuẩn).
- **Mở rộng tùy chọn (nếu tiến độ cho phép):** cổng từ chối dựa trên bằng chứng (evidence-gated generation) – một bộ quyết định nhỏ dùng điểm reranker để từ chối trước khi sinh, hiệu chỉnh ngưỡng trên tập không trả lời được. Nếu thực hiện, giảm yếu tố E từ 6 xuống 4 mức để giữ tổng khối lượng.
- **Giới hạn thừa nhận:** đánh giá tự động bằng LLM có sai số; kết quả có thể phụ thuộc vào mô hình sinh được chọn (sẽ kiểm tra độ bền với một mô hình sinh thứ hai trên tập con).

## 5. Phương pháp nghiên cứu

### 5.1 Kiến trúc hệ thống

```
Tài liệu ──► Tiền xử lý ──► Phân đoạn (C) ──► Nhúng (E) ──► Chỉ mục (FAISS / BM25)
                                                                    │
Câu hỏi ──► Nhúng truy vấn ──► Truy xuất top-k (k=20) ──► Xếp hạng lại (R) ──► top-n (n=5)
                                                                    │
                                              Prompt + ngữ cảnh ──► LLM sinh (cố định) ──► Câu trả lời
                                                                    │
                                     Đánh giá: truy xuất · độ đúng · ảo giác · chi phí
```

Công nghệ dự kiến: Python, `sentence-transformers`, `FlagEmbedding`, `rank_bm25`/Pyserini, FAISS, `underthesea` hoặc `pyvi` (tách từ), `vLLM` hoặc `transformers` để chạy LLM, `ragas`/`deepeval` làm tham chiếu cho bộ đo tự xây.

### 5.2 Các yếu tố thiết kế (biến độc lập)

**Yếu tố C – Phân đoạn (6 mức)**

| Mã | Chiến lược | Chi tiết |
| --- | --- | --- |
| C1 | Cố định 256 token, không chồng lấn | Baseline phổ biến |
| C2 | Cố định 512 token, chồng lấn 64 | Kiểm tra ảnh hưởng độ dài + overlap |
| C3 | Theo câu, gộp tới \~256 token | Dùng tách câu tiếng Việt, không cắt giữa câu |
| C4 | Theo cấu trúc tài liệu (baseline) | Wikipedia: đoạn văn gốc; pháp luật: cắt theo Điều |
| C5 | **ViStructChunk** (đề xuất) | Pháp luật: cắt theo cây Điều → Khoản → Điểm, mỗi chunk được gắn tiêu đề cha ("Luật X, Điều 8, Khoản 2: …") để tự chứa ngữ cảnh; văn bản thường: không cắt giữa câu và giữa từ ghép đã tách bằng underthesea, gộp tới \~256 token |
| C6 | Semantic chunking | Cắt khi độ tương tự cosine giữa câu liền kề giảm mạnh |

Token được đếm bằng tokenizer của chính mô hình nhúng để công bằng giữa các mô hình. Với C6 dùng cùng một embedding nhỏ (bkai bi-encoder) để tách, tránh "rò rỉ" lợi thế sang yếu tố E. Cặp C4–C5 được thiết kế để cô lập đóng góp của việc gắn tiêu đề cha: cùng ranh giới cắt, chỉ khác phần tiêu đề.

**Yếu tố E – Mô hình nhúng / truy xuất (6 mức)**

| Mã | Mô hình | Lý do chọn |
| --- | --- | --- |
| E0 | BM25 (tách từ bằng underthesea) | Baseline lexical; rất mạnh ở văn bản pháp luật |
| E1 | `bkai-foundation-models/vietnamese-bi-encoder` | Mô hình chuyên Việt nhỏ (135M), phổ biến trong cộng đồng |
| E2 | `AITeamVN/Vietnamese_Embedding_v2` | Mô hình chuyên Việt mạnh nhất hiện nay, nền BGE-M3 |
| E3 | `BAAI/bge-m3` | Đa ngôn ngữ, điểm tổng hợp cao nhất trên benchmark đa miền |
| E4 | `intfloat/multilingual-e5-large` | Đa ngôn ngữ, xếp hạng tổng thể số 1 khi kết hợp BM25 |
| E5 | Hybrid: E3 + BM25, nội suy α = 0,7 | Cấu hình được khuyến nghị bởi nghiên cứu gần nhất |

Bốn mô hình dense đều \~560M tham số trở xuống, chạy được trên GPU 16 GB. Có thể bổ sung `Qwen/Qwen3-Embedding-0.6B` nếu còn thời gian để đại diện nhóm embedding từ LLM.

**Yếu tố R – Xếp hạng lại (4 mức)**

| Mã | Mô hình | Ghi chú |
| --- | --- | --- |
| R0 | Không xếp hạng lại | Lấy top-5 trực tiếp từ retriever |
| R1 | `BAAI/bge-reranker-v2-m3` | Reranker đa ngôn ngữ tham chiếu |
| R2 | `AITeamVN/Vietnamese_Reranker` | Tinh chỉnh cho tiếng Việt từ R1, cho phép so sánh "cùng gốc" |
| R3 | `namdp-ptit/ViRanker` (hoặc `itdainb/PhoRanker`) | Reranker chuyên Việt kiến trúc khác |

Tất cả reranker nhận top-20 từ retriever và trả về top-5.

### 5.3 Thiết kế thực nghiệm

Lưới đầy đủ 6 × 6 × 4 = 144 cấu hình là quá lớn cho bước sinh câu trả lời, nên chia hai giai đoạn:

**Giai đoạn A – Đánh giá truy xuất trên toàn lưới (144 cấu hình).** Chỉ cần nhúng + truy xuất, không gọi LLM, chi phí thấp. Cho phép vẽ bản đồ đầy đủ về Recall/nDCG và xác định các cấu hình đáng chú ý.

**Giai đoạn B – Đánh giá đầu cuối (độ đúng + ảo giác) theo thiết kế ablation có kiểm soát:**

- Cấu hình neo: C3 – E3 – R0 (lựa chọn "an toàn" theo tài liệu).
- Thay từng yếu tố một (OFAT): 6 + 6 + 4 − 2 = 14 cấu hình.
- Thêm 4 cấu hình tổ hợp tốt nhất từ Giai đoạn A.
- Thêm hai điều kiện tham chiếu dùng cho chỉ số RAH (mục 5.6): **closed-book** (không ngữ cảnh) đo ảo giác nền của LLM, và **oracle** (luôn đưa đúng đoạn vàng vào ngữ cảnh) đo "sàn" ảo giác mà truy xuất hoàn hảo cũng không hạ thêm được.
- Tổng ≈ 20 cấu hình × 2 bộ dữ liệu × \~1.000 câu hỏi ≈ 40.000 lượt sinh, khả thi với LLM 8B trên một GPU trong vài ngày.

**Kiểm soát nhiễu:** mô hình sinh cố định, temperature = 0, một prompt duy nhất (hướng dẫn rõ: "chỉ dùng thông tin trong ngữ cảnh; nếu không đủ thông tin hãy trả lời *Không tìm thấy thông tin*"), cùng n = 5 đoạn ngữ cảnh, cùng seed.

### 5.4 Dữ liệu

Chọn hai bộ đại diện cho hai kiểu văn bản khác nhau rõ rệt, để khuyến nghị có tính "theo miền":

| Bộ dữ liệu | Miền | Vai trò | Lý do chọn |
| --- | --- | --- | --- |
| **UIT-ViQuAD 2.0** | Bách khoa (Wikipedia), 5.173 đoạn từ 176 bài, \~24.500 câu hỏi trả lời được + \~11.500 câu **không** trả lời được | Bộ chính | Duy nhất có sẵn câu hỏi không trả lời được được viết đối kháng – cực kỳ phù hợp để đo ảo giác; được dùng rộng rãi, dễ so sánh |
| **Zalo Legal Text Retrieval 2021** (bổ sung ALQAC) | Pháp luật, \~61.000 điều luật, truy vấn tự nhiên | Bộ thứ hai | Tài liệu dài, có cấu trúc Điều/Khoản → phép thử lý tưởng cho phân đoạn; miền có giá trị ứng dụng cao tại Việt Nam |

**Xây dựng tập đánh giá:**

- Từ mỗi bộ lấy mẫu phân tầng **1.000 câu hỏi**: 700 trả lời được, 300 không trả lời được.
- Với Zalo Legal, vốn không có câu hỏi "không trả lời được", sẽ tạo bằng hai cách: (i) câu hỏi thật nhưng **loại điều luật vàng khỏi kho** (unanswerable-by-removal); (ii) câu hỏi về nội dung ngoài kho do sinh viên viết, kiểm tra chéo bởi hai người.
- Kho tài liệu ViQuAD khá nhỏ; để truy xuất không quá dễ, bổ sung \~20.000 đoạn Wikipedia tiếng Việt cùng chủ đề làm "nhiễu" (distractor).
- Với mỗi câu hỏi lưu: đáp án vàng, đoạn vàng, nhãn trả lời được/không.

**Bộ hiệu chỉnh judge:** lấy 500 mẫu từ ViHallu (DSC 2025) để kiểm tra bộ chấm ảo giác trước khi dùng.

### 5.5 Mô hình sinh câu trả lời

- **Mô hình chính:** một LLM mã nguồn mở cỡ 8–12B hỗ trợ tiếng Việt tốt, chạy cục bộ, ví dụ `Qwen/Qwen3-8B` hoặc `google/gemma-3-12b-it` (chọn sau khi chạy thử nhanh 100 câu trên ViQuAD; ưu tiên mô hình tuân thủ lệnh "không bịa" tốt hơn). Chạy cục bộ đảm bảo tái lập và không tốn chi phí API cho 38.000 lượt sinh.
- **Kiểm tra độ bền:** lặp lại 5 cấu hình quan trọng nhất với mô hình sinh thứ hai (một API thương mại) trên 300 câu hỏi để xem kết luận có đổi không.

### 5.6 Chỉ số đánh giá (biến phụ thuộc)

**(a) Truy xuất:** Recall@5, Recall@20, MRR@10, nDCG@5 – tính theo đoạn vàng (với chunk, một đoạn được coi là đúng nếu chứa ≥ 80% đáp án vàng).

**(b) Độ đúng câu trả lời (tập trả lời được):**

- Exact Match và token-F1 (chuẩn SQuAD, sau tách từ và chuẩn hóa dấu).
- **Correctness** theo LLM-as-judge thang 0/1/2 (sai / đúng một phần / đúng), vì câu trả lời sinh ra thường dài hơn span trích xuất.

**(c) Ảo giác** – tách thành ba chỉ số, vì "ảo giác" trong RAG có nhiều dạng:

- **Faithfulness (tính trung thực với ngữ cảnh):** tách câu trả lời thành các mệnh đề, judge kiểm tra từng mệnh đề có được ngữ cảnh truy xuất hỗ trợ không; điểm = tỷ lệ mệnh đề được hỗ trợ. Tỷ lệ câu trả lời có faithfulness \< 1 gọi là **tỷ lệ ảo giác**.
- **Tỷ lệ bịa đặt trên tập không trả lời được (fabrication rate):** phần trăm câu mô hình đưa ra một câu trả lời cụ thể thay vì từ chối. Đây là chỉ số "sạch" nhất vì không phụ thuộc judge.
- **Tỷ lệ từ chối sai (false refusal):** phần trăm câu trả lời được nhưng mô hình từ chối – để đảm bảo giảm ảo giác không phải bằng cách từ chối tất cả.
- Phân loại thêm ảo giác **nội tại** (mâu thuẫn ngữ cảnh) và **ngoại lai** (thêm thông tin ngoài ngữ cảnh), theo cách phân loại của ViHallu, để phân tích định tính.

**(c') Ảo giác quy cho truy xuất – chỉ số đề xuất.** Với mỗi cấu hình *k*, gọi H(k) là tỷ lệ ảo giác đầu cuối, H(oracle) là tỷ lệ ảo giác khi luôn cung cấp đúng đoạn vàng, H(cb) là tỷ lệ ảo giác closed-book, tất cả đo trên cùng tập câu hỏi. Định nghĩa:

- **RAH(k) = H(k) − H(oracle):** phần ảo giác do truy xuất sai/thiếu/nhiễu gây ra, tức phần mà chunking, embedding, reranking có thể sửa.
- **Tỷ lệ quy cho truy xuất = RAH(k) / H(k):** cho biết bao nhiêu phần trăm ảo giác của cấu hình *k* "thuộc trách nhiệm" của tầng truy xuất.
- H(oracle) là sàn do mô hình sinh (bỏ qua hoặc bóp méo ngữ cảnh đúng); H(cb) là trần tham chiếu.

Chỉ số này trả lời trực tiếp RQ4 và cho phép so sánh các miền: miền có tỷ lệ quy cho truy xuất cao là miền mà đầu tư vào retrieval đáng giá nhất.

**(d) Chi phí:** độ trễ truy xuất + xếp hạng lại trung bình/câu, kích thước chỉ mục, VRAM.

### 5.7 Kiểm chứng bộ chấm tự động

- Judge là một LLM khác với mô hình sinh (tránh thiên vị "tự chấm"), prompt bằng tiếng Việt, đầu ra JSON.
- Hai người gán nhãn độc lập **300 câu trả lời** (150 mỗi bộ dữ liệu) cho correctness và faithfulness; đo Cohen's κ giữa người với người và giữa judge với người. Mục tiêu κ ≥ 0,7; nếu thấp hơn sẽ sửa prompt judge và lặp lại.
- Báo cáo kết quả chính kèm khoảng tin cậy có tính đến sai số của judge.

### 5.8 Phân tích thống kê

- Khoảng tin cậy 95% bằng bootstrap trên câu hỏi (1.000 lần lấy mẫu lại).
- So sánh từng cặp cấu hình bằng kiểm định hoán vị theo cặp (paired permutation test), hiệu chỉnh Holm cho nhiều so sánh.
- Phân tích hồi quy logistic: xác suất ảo giác \~ Recall@5 + độ dài chunk + reranker, để tách ảnh hưởng trực tiếp của từng yếu tố khỏi ảnh hưởng gián tiếp qua chất lượng truy xuất.
- Phân tích lỗi định tính: 100 trường hợp ảo giác được chọn ngẫu nhiên, gắn nhãn nguyên nhân (truy xuất sai / truy xuất đúng nhưng mô hình bỏ qua / chunk cắt mất thông tin / nhiễu từ đoạn không liên quan / nhầm điều luật). Nhãn này dùng để kiểm chứng chéo chỉ số RAH ở cấp tổng thể.

### 5.9 Khung khuyến nghị cấu hình (mô hình quyết định đa tiêu chí)

Thay vì chọn cấu hình theo cảm nhận, phần khuyến nghị được xây dựng theo hai bước:

1. **Biên Pareto:** với mỗi bộ dữ liệu, đặt các cấu hình trong không gian ba tiêu chí (độ đúng ↑, tỷ lệ ảo giác ↓, độ trễ ↓) và giữ lại các cấu hình không bị cấu hình nào khác vượt trội ở cả ba tiêu chí. Các cấu hình bị trội bị loại khỏi khuyến nghị bất kể điểm từng mặt.
2. **Điểm có trọng số theo kịch bản:** chuẩn hóa min–max từng tiêu chí trên tập Pareto, rồi tính điểm tổng với ba bộ trọng số đại diện cho ba kịch bản sử dụng: *pháp luật/y tế* (ảo giác 0,6 – độ đúng 0,3 – độ trễ 0,1), *tra cứu nhanh* (0,2 – 0,3 – 0,5), *cân bằng* (0,34 – 0,33 – 0,33). Cấu hình điểm cao nhất mỗi kịch bản là khuyến nghị; kèm phân tích độ nhạy bằng cách dao động trọng số ±0,1 để xem khuyến nghị có đổi không.

Kết quả là một bảng khuyến nghị có thể bảo vệ được: mỗi khuyến nghị đi kèm lý do bằng số và điều kiện áp dụng.

## 6. Kết quả dự kiến và đóng góp

**Đóng góp về tri thức**

1. Nghiên cứu có kiểm soát đầu tiên cho tiếng Việt đo ảnh hưởng của chunking, embedding và reranking lên độ đúng và ảo giác đầu cuối, với bằng chứng thống kê (khoảng tin cậy, kiểm định có hiệu chỉnh) thay vì so sánh điểm đơn lẻ.
2. Ước lượng định lượng về **phần ảo giác quy cho truy xuất** trong hai miền văn bản, trả lời câu hỏi: đầu tư vào tầng truy xuất có thể giảm tối đa bao nhiêu ảo giác, và phần còn lại thuộc về mô hình sinh.

**Đóng góp về phương pháp** 3. Chỉ số **RAH (retrieval-attributable hallucination)** dựa trên bộ ba điều kiện closed-book / cấu hình / oracle, áp dụng được cho bất kỳ hệ RAG nào. 4. Chiến lược phân đoạn **ViStructChunk** cho văn bản pháp luật Việt Nam và văn bản thường, cùng bằng chứng thực nghiệm về tác động của việc gắn tiêu đề cha lên ảo giác nhầm điều luật. 5. **Khung khuyến nghị cấu hình** theo kịch bản dựa trên biên Pareto và điểm đa tiêu chí có phân tích độ nhạy.

**Sản phẩm** 6. Hệ thống RAG tiếng Việt mã nguồn mở, mô-đun, kèm script tái lập toàn bộ thực nghiệm. 7. Bộ dữ liệu **ViRAG-Hallu**: 2.000 câu hỏi có nhãn trả lời được/không và đoạn vàng, 300 mẫu gán nhãn người cho faithfulness, 100 trường hợp ảo giác đã phân loại nguyên nhân – công bố trên Hugging Face. 8. Một bài báo gửi hội nghị trong nước (VLSP, KSE, SoICT) hoặc workshop quốc tế.

## 7. Kế hoạch thực hiện (16 tuần)

| Tuần | Công việc | Sản phẩm |
| --- | --- | --- |
| 1–2 | Tổng quan tài liệu, hoàn thiện đề cương, xin dữ liệu Zalo Legal/ALQAC | Đề cương được duyệt |
| 3–4 | Xây dựng pipeline cơ bản (chunking, index, retrieval, generation), chạy thử trên 100 câu | Pipeline chạy đầu-cuối |
| 5–6 | Xây dựng tập đánh giá (lấy mẫu, tạo câu không trả lời được, kho distractor); viết parser Điều/Khoản/Điểm cho ViStructChunk | 2 bộ × 1.000 câu hỏi; mô-đun chunking C5 |
| 7 | Xây dựng và hiệu chỉnh judge; gán nhãn người 300 mẫu | Báo cáo κ |
| 8–9 | Giai đoạn A: chạy toàn lưới truy xuất 144 cấu hình | Bảng Recall/nDCG |
| 10–12 | Giai đoạn B: chạy 20 cấu hình đầu cuối (gồm closed-book và oracle), kiểm tra độ bền với LLM thứ hai | Kết quả thô |
| 13 | Phân tích thống kê, tính RAH, biên Pareto và điểm theo kịch bản, phân tích lỗi định tính | Hình, bảng, bảng khuyến nghị |
| 14–15 | Viết báo cáo, bảng khuyến nghị | Bản thảo đầy đủ |
| 16 | Chỉnh sửa, phản biện thử, nộp | Khóa luận + mã nguồn |

Tuần 8–12 có thể chạy song song với việc viết chương Tổng quan và Phương pháp.

## 8. Tài nguyên cần thiết

- **Phần cứng:** 1 GPU ≥ 16 GB VRAM (T4/A10/RTX 4080 trở lên; Colab Pro hoặc Kaggle đủ cho embedding/reranker; LLM 8B nên chạy định lượng 4-bit nếu VRAM hạn chế, hoặc thuê GPU theo giờ \~30–50 giờ cho Giai đoạn B).
- **Lưu trữ:** \~20 GB cho mô hình và chỉ mục.
- **Phần mềm:** toàn bộ mã nguồn mở; chi phí API chỉ phát sinh ở bước judge và kiểm tra độ bền (ước tính dưới 50 USD).

## 9. Rủi ro và phương án dự phòng

| Rủi ro | Khả năng | Phương án |
| --- | --- | --- |
| Không xin được dữ liệu Zalo Legal | Thấp (đã công khai rộng rãi) | Thay bằng ALQAC hoặc bộ luật tự thu thập từ cổng văn bản pháp luật |
| Judge không đạt κ ≥ 0,7 | Trung bình | Chuyển sang chấm mệnh đề bằng mô hình NLI đa ngôn ngữ kết hợp judge; tăng mẫu gán nhãn người |
| Không đủ GPU cho Giai đoạn B | Trung bình | Giảm xuống 500 câu/bộ; dùng LLM 4B; thuê GPU |
| Kết quả giữa các cấu hình không khác biệt có ý nghĩa | Trung bình | Bản thân đó là phát hiện có giá trị ("yếu tố X không quan trọng cho tiếng Việt"); tập trung phân tích miền khó hơn |
| Mô hình sinh "biết sẵn" đáp án Wikipedia (rò rỉ từ huấn luyện) | Cao với ViQuAD | Baseline closed-book đo mức này; tập pháp luật ít bị ảnh hưởng; báo cáo kết quả có/không trừ nền |

## 10. Tài liệu tham khảo chính

1. Nguyen, L. S. T., & Quan, T. T. (2026). *Which Works Best for Vietnamese? A Practical Study of Information Retrieval Methods across Domains.* Findings of EACL 2026.
2. Pham, L. et al. (2025). *VN-MTEB: Vietnamese Massive Text Embedding Benchmark.* arXiv:2507.21500.
3. Nguyen, V. et al. (2024). *Advancing Vietnamese Information Retrieval with Learning Objective and Benchmark.* PACLIC 38.
4. Nguyen, A. T.-H. et al. (2026). *DSC2025 – ViHallu Challenge: Detecting Hallucination in Vietnamese LLMs.* arXiv:2601.04711.
5. *VietPS-Hallu: A Vietnamese Dataset for Hallucination Detection in LLMs within the Public Services* (2026). Springer.
6. Dang, P. N. et al. (2026). *ViRanker: A BGE-M3 & Blockwise Parallel Transformer Cross-Encoder for Vietnamese Reranking.* Springer.
7. Nguyen, K. V. et al. (2022). *VLSP 2021 – ViMRC Challenge: Vietnamese Machine Reading Comprehension* (UIT-ViQuAD 2.0).
8. Niu, C. et al. (2024). *RAGTruth: A Hallucination Corpus for Developing Trustworthy RAG LLMs.* ACL 2024.
9. Friel, R. et al. (2024). *RAGBench: Explainable Benchmark for RAG Systems.*
10. Es, S. et al. (2024). *RAGAS: Automated Evaluation of Retrieval Augmented Generation.* EACL 2024.
11. Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS.
12. Chen, J. et al. (2024). *BGE M3-Embedding.* arXiv:2402.03216.
13. Wang, L. et al. (2024). *Multilingual E5 Text Embeddings.* arXiv:2402.05672.