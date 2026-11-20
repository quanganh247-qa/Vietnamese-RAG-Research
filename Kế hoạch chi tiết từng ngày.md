# Kế hoạch triển khai và nghiên cứu chi tiết từng ngày

Tài liệu này chi tiết hóa lịch trong `Kế hoạch 14 ngày và mục lục bài báo.md`. Mỗi ngày khoảng 2 giờ. Ký hiệu D1–D9 là các quyết định thiết kế trong bảng của file đó; C/E/R là các yếu tố trong đề cương v2.

Các phương án ghi "đề xuất" là khuyến nghị để bạn và người hướng dẫn quyết định, chưa phải lựa chọn đã chốt. Các chỗ ghi "cần xác minh" là điều tôi chưa kiểm tra từ nguồn gốc.

## File làm việc

Chỉ cần bốn file mới, tạo khi đến ngày dùng:

| File | Nội dung | Tạo vào |
|---|---|---|
| `reports/tai-lieu.md` | Bảng xác minh tài liệu tham khảo | Ngày 1 |
| `reports/quyet-dinh-thiet-ke.md` | Bảng RQ và quyết định D1–D9 kèm lý do | Ngày 2 |
| `notebooks/02_pilot_retrieval.ipynb` | Pilot truy xuất (chạy trên Colab) | Ngày 7 |
| `reports/ban-thao.md` | Bản thảo bài báo | Ngày 10 |

Kết quả trung gian của pilot lưu trên Drive tại `data/processed/pilot/` (văn bản đã tách từ, embedding, điểm BM25, chỉ số theo từng truy vấn), để mỗi bước nặng chỉ chạy một lần.

---

## Giai đoạn 1 – Chốt thiết kế (ngày 1–6)

### Ngày 1 – Khởi động, dữ liệu, xác minh nguồn

**Mục tiêu:** gỡ ba điểm chặn: nơi nộp, dữ liệu đã xử lý, độ tin cậy của các nguồn chính.

| Phút | Việc |
|---|---|
| 0–15 | Gửi người hướng dẫn ba câu hỏi: (1) dự định nộp ở đâu và hạn nộp; (2) bài protocol kèm pilot có phù hợp không, hay cần kết quả đầy đủ; (3) giới hạn số trang và ngôn ngữ viết. Ghi ngày cần phản hồi: cuối ngày 4. |
| 15–60 | Mở Colab, chạy `01_dataset_exploration.ipynb` từ trên xuống. Xác nhận cell kiểm định in `PASS`, rồi chạy cell lưu ở mục 8. Kiểm tra trên Drive có `data/processed/viquad` và `data/processed/zalo_legal/{corpus,queries,qrels}`. |
| 60–120 | Tạo `reports/tai-lieu.md` với các cột: nguồn, URL/DOI, đã mở bản gốc chưa, khẳng định mà đề cương trích, khẳng định đó có đúng không. Xác minh trước năm nguồn làm căn cứ cho khoảng trống nghiên cứu (danh sách bên dưới). |

**Năm nguồn ưu tiên và khẳng định cần đối chiếu:**

1. Nguyen & Quan (EACL 2026): 10 bộ dữ liệu, 6 lĩnh vực; hybrid nội suy tuyến tính α ≈ 0,6–0,8; không đánh giá phân đoạn, reranking hay câu trả lời sinh ra. Ghi lại α nhân với thành phần nào (dense hay BM25) và cách chuẩn hóa điểm, vì ngày 9 cần dùng.
2. ViHallu (arXiv:2601.04711): 10.000 bộ ba; ba nhãn; độ dài đoạn 88–1.500 token.
3. ViRanker và `AITeamVN/Vietnamese_Reranker`: nền mô hình, dữ liệu huấn luyện (khoảng 1,1 triệu bộ ba), độ dài tối đa 2.048 token.
4. VN-MTEB (arXiv:2507.21500): 41 bộ dữ liệu, 6 nhiệm vụ.
5. UIT-ViQuAD 2.0: đề cương ghi 5.173 đoạn, 176 bài, khoảng 24.500 câu trả lời được và 11.500 câu không trả lời được. Bản đang dùng có 39.569 dòng (train 28.454, validation 3.814, test 7.301), trong đó train có 9.216 và validation có 1.161 câu không trả lời được. Hai bộ số này không khớp; cần xác định bản trên Drive là phiên bản nào và sửa số trong bài cho đúng.

**Đầu ra:** câu hỏi đã gửi; dữ liệu đã xử lý trên Drive; bảng xác minh với năm dòng đầu đã điền.

**Xong khi:** `load_from_disk` đọc được cả bốn thư mục processed trong một runtime mới.

**Nếu trễ:** ưu tiên dữ liệu; chuyển nguồn 3–4 sang ngày 2.

### Ngày 2 – Khoảng trống và câu hỏi nghiên cứu

**Mục tiêu:** mỗi câu hỏi nghiên cứu gắn với một phép so sánh cụ thể.

| Phút | Việc |
|---|---|
| 0–30 | Xác minh tám nguồn còn lại ở mức thư mục (tác giả, năm, venue, URL). Tìm thêm 20 phút với các từ khóa "Vietnamese RAG hallucination", "Vietnamese chunking legal retrieval", "retrieval-attributable hallucination" để kiểm tra khẳng định "chưa có nghiên cứu nào". Ghi lại truy vấn và ngày tìm. |
| 30–60 | Viết đoạn khoảng trống (khoảng 150 từ) vào `reports/quyet-dinh-thiet-ke.md`, chỉ dùng nguồn đã mở bản gốc. Thay "chưa có nghiên cứu nào" bằng "theo khảo sát của chúng tôi đến tháng 11/2026" nếu không chắc. |
| 60–120 | Lập bảng RQ theo mẫu dưới đây cho RQ1–RQ5. |

**Mẫu bảng RQ (điền đủ năm dòng):**

| RQ | Giả thuyết | Cấu hình so sánh | Chỉ số chính | Tập con | Kết quả nào bác bỏ giả thuyết |
|---|---|---|---|---|---|
| RQ1/H1b | ViStructChunk giảm ảo giác nhầm điều luật so với cắt theo Điều | C5–E3–R0 so với C4–E3–R0 | Tỷ lệ câu trả lời dẫn sai điều luật | Zalo, câu trả lời được | Khoảng tin cậy của hiệu số chứa 0 hoặc nghiêng về C4 |

Lưu ý khi điền:

- H1b cần chỉ số "nhầm điều luật", hiện chưa có trong mục 5.6 của đề cương; phải định nghĩa ở ngày 5.
- H2 nói chênh lệch Recall bị "nén" ở tầng sinh; cần nêu phép đo cụ thể, ví dụ so khoảng biến thiên Recall@5 giữa E1–E4 với khoảng biến thiên tỷ lệ ảo giác.
- RQ5 không có giả thuyết; ghi rõ là phân tích khám phá.

**Đầu ra:** bảng RQ đủ năm dòng; đoạn khoảng trống; bảng tài liệu đủ 13 nguồn.

**Xong khi:** không còn ô trống ở cột "Chỉ số chính" và "Kết quả nào bác bỏ".

### Ngày 3 – Phân đoạn, truy xuất, reranking (D7)

**Mục tiêu:** đặc tả đủ để người khác cài đặt được, và tách yếu tố C khỏi yếu tố E.

| Phút | Việc |
|---|---|
| 0–40 | Trên Colab, kiểm tra độ dài tối đa và tokenizer của bốn mô hình dense (đoạn mã bên dưới). Ghi kết quả vào file quyết định. |
| 40–70 | Chốt D7. |
| 70–100 | Viết đặc tả C1–C6: đơn vị đếm, ranh giới, overlap, cách xử lý điều luật quá dài, chunk rỗng, văn bản không parse được. |
| 100–120 | Rà soát E0–E5 và R0–R3: đầu vào, đầu ra, top-20 rồi top-5; công thức hybrid và cách chuẩn hóa điểm lấy theo nguồn đã xác minh ở ngày 1. |

```python
from sentence_transformers import SentenceTransformer
for name in ['bkai-foundation-models/vietnamese-bi-encoder', 'AITeamVN/Vietnamese_Embedding_v2',
             'BAAI/bge-m3', 'intfloat/multilingual-e5-large']:
    m = SentenceTransformer(name)
    print(name, m.max_seq_length, type(m.tokenizer).__name__)
```

**Đề xuất cho D7:** đếm token và đặt ranh giới chunk bằng một tokenizer tham chiếu duy nhất (tokenizer của `BAAI/bge-m3`), thay vì tokenizer của từng mô hình. Khi đó tập chunk giống nhau với mọi mức E, và yếu tố C thực sự độc lập với E. Theo tôi nhớ, E2, E3 và E4 đều dùng tokenizer họ XLM-RoBERTa nên gần như không bị ảnh hưởng; chỉ E1 (nền PhoBERT, có thể giới hạn 256 token và cần tách từ trước) là khác. Cần xác minh bằng đoạn mã trên. Với E1, báo cáo tỷ lệ chunk bị cắt ở từng mức C thay vì loại mô hình.

**Các trường hợp biên phải có quy tắc (số liệu từ notebook):**

- 357 dòng kho Zalo có `text` rỗng: giữ lại với nội dung là tiêu đề, hay loại khỏi kho; báo cáo số lượng.
- Điều luật dài nhất khoảng 250 nghìn ký tự; phân vị 95 là 3.672 ký tự. C4 (cắt theo Điều) sẽ tạo chunk vượt giới hạn mô hình; nêu rõ là cắt cụt, hay chia tiếp, và tỷ lệ bị ảnh hưởng.
- Với C5: quy tắc khi Điều không có Khoản, khi Khoản không có Điểm, và khi biểu thức nhận diện "Điều/Khoản/Điểm" khớp nhầm phần trích dẫn điều luật khác trong nội dung.

**Đầu ra:** mục đặc tả C/E/R và quyết định D7 trong file quyết định.

**Xong khi:** với một điều luật bất kỳ, bạn nói được chính xác nó thành những chunk nào ở cả sáu mức C.

### Ngày 4 – Tập đánh giá (D1, D6, D8)

**Mục tiêu:** chốt cỡ mẫu thực tế và quy trình lấy mẫu.

| Phút | Việc |
|---|---|
| 0–50 | Chốt D1 và D8 cho Zalo Legal. |
| 50–90 | Quy trình tạo câu không trả lời được cho Zalo; chốt D6 cho ViQuAD. |
| 90–120 | Quy tắc lấy mẫu ViQuAD; kiểm tra giấy phép hai bộ dữ liệu và ghi vào danh sách rủi ro. |

**Dữ kiện cho D1 và D8:** Zalo có 788 truy vấn có nhãn, 793 cặp qrels, nhưng chỉ 447 điều luật vàng khác nhau. Nhiều truy vấn dùng chung điều luật vàng.

**Hệ quả quan trọng:** đơn vị lấy mẫu cho "loại điều luật vàng khỏi kho" phải là **điều luật**, không phải truy vấn. Loại một điều luật thì mọi truy vấn trỏ tới nó đều thành không trả lời được. Tương tự, tách dev/test phải theo điều luật vàng để tránh rò rỉ.

**Ba phương án cho D1:**

| Phương án | Tập test Zalo | Việc thêm | Nhận xét |
|---|---|---|---|
| A (đề xuất) | Khoảng 600 câu: 420 trả lời được, 180 không trả lời được do loại điều luật; khoảng 188 câu còn lại làm dev | Không | Khả thi ngay. Khoảng tin cậy 95% rộng hơn: khoảng ±4,4 điểm phần trăm trên 420 câu và ±6,7 trên 180 câu khi tỷ lệ quanh 30% |
| B | 700 + 300 như đề cương | Viết tay ít nhất 212 câu, kiểm tra chéo hai người, cộng thêm câu cho dev | Đúng đề cương nhưng tốn nhiều giờ ngoài 14 ngày |
| C | Bổ sung truy vấn ALQAC | Xin dữ liệu, hợp nhất kho | Hai nguồn truy vấn khác phân phối; cần báo cáo tách riêng |

Con số chính xác của phương án A phụ thuộc cách các truy vấn chia nhóm theo điều luật; tính lại bằng dữ liệu thật khi lấy mẫu.

**Kiểm tra câu không trả lời được (cả hai bộ):** sau khi loại điều luật, văn bản khác có thể chứa cùng nội dung (nghị định sửa đổi, thông tư hướng dẫn). Quy trình đề xuất: chạy truy xuất top-5, đọc tay một mẫu 50 câu, ghi tỷ lệ câu vẫn trả lời được từ kho. Áp dụng cùng quy trình cho D6: câu `is_impossible` của ViQuAD sau khi thêm đoạn nhiễu Wikipedia.

**Quy tắc lấy mẫu ViQuAD:**

- Chỉ lấy từ train và validation; split test không có đáp án.
- `id` lặp lại giữa các split, nên khóa duy nhất là (split, id).
- Phân tầng theo `is_impossible`; tách dev/test theo `title` để một bài Wikipedia không nằm ở cả hai.
- Ghi seed lấy mẫu vào file quyết định.

**Đầu ra:** quyết định D1, D6, D8; quy trình lấy mẫu từng bước; danh sách rủi ro dữ liệu.

**Xong khi:** cỡ mẫu test và dev của cả hai bộ là con số cụ thể, có lý do.

### Ngày 5 – Chỉ số và RAH (D2–D5)

**Mục tiêu:** mọi chỉ số có công thức, tập con áp dụng và cách xử lý trường hợp không xác định.

| Phút | Việc |
|---|---|
| 0–50 | Bảng chỉ số; chốt D2. |
| 50–120 | Đặc tả RAH; chốt D3, D4, D5. |

**Bảng chỉ số cần điền** (cột: tên, công thức, đơn vị, bộ dữ liệu, tập con, cần judge không):

- Truy xuất: Recall@5, Recall@20, MRR@10, nDCG@5.
- Độ đúng: EM, token-F1, correctness 0/1/2.
- Ảo giác: faithfulness, tỷ lệ ảo giác, fabrication, false refusal, nhầm điều luật (mới, phục vụ H1b).
- Chi phí: độ trễ, kích thước chỉ mục, VRAM.

**Đề xuất cho D2 (Zalo không có đáp án vàng):**

- Truy xuất: một chunk được tính là đúng nếu điều luật cha của nó nằm trong qrels. Ghi rõ đây là tiêu chí rộng: chunk thuộc đúng điều luật nhưng sai khoản vẫn được tính. Báo cáo thêm chỉ số ở mức điều luật sau khi gộp các chunk cùng điều.
- ViQuAD giữ tiêu chí của đề cương (chunk chứa ít nhất 80% đáp án vàng), nên hai bộ dùng hai tiêu chí khác nhau; không so trực tiếp con số truy xuất giữa hai miền.
- Độ đúng câu trả lời trên Zalo: không dùng EM/F1. Judge chấm 0/1/2 dựa trên câu hỏi, điều luật vàng và câu trả lời; kiểm chứng bằng 150 mẫu gán nhãn người đã có trong kế hoạch.
- "Nhầm điều luật": câu trả lời dẫn số Điều/tên văn bản không khớp điều luật vàng. Phần lớn đo được bằng biểu thức chính quy, không cần judge.

**Đề xuất cho D3 và D4:** tách hai đại lượng thay vì một.

| Đại lượng | Định nghĩa | Xác định ở closed-book | Dùng cho |
|---|---|---|---|
| H_ctx | Tỷ lệ câu trả lời có ít nhất một mệnh đề không được **ngữ cảnh đã cung cấp** hỗ trợ | Không | Chỉ số phụ: mô hình có bám ngữ cảnh không |
| H_gold | Tỷ lệ câu trả lời có ít nhất một mệnh đề không được **bằng chứng vàng** (đoạn vàng/điều luật vàng) hỗ trợ | Có | Chỉ số chính và RAH |

Lý do: H_ctx không bắt được trường hợp truy xuất sai mà mô hình bám đúng ngữ cảnh sai, tức đúng loại lỗi RAH muốn quy cho truy xuất. H_gold bắt được, và xác định ở cả ba điều kiện closed-book, cấu hình, oracle. Ở điều kiện oracle hai đại lượng trùng nhau.

Hạn chế phải ghi: H_gold phạt cả thông tin đúng nhưng nằm ngoài đoạn vàng (tri thức nền của mô hình). Đây là lý do cần báo cáo cả hai.

**Đề xuất cho D5:**

- RAH(k) = H_gold(k) − H_gold(oracle), chỉ tính trên câu **trả lời được**.
- Trên câu không trả lời được, báo cáo fabrication rate riêng, không tính RAH.
- Oracle với câu `is_impossible` của ViQuAD: đưa đoạn gốc đi kèm câu hỏi (đo mức bịa khi ngữ cảnh gây nhiễu). Với câu Zalo tạo bằng cách loại điều luật: không có điều kiện oracle; ghi rõ.

**Các cảnh báo về RAH đưa vào bài:** RAH có thể âm; tỷ lệ RAH/H không ổn định khi H gần 0 (đặt ngưỡng không báo cáo tỷ lệ khi H dưới một mức chọn trước); luôn kèm khoảng tin cậy; RAH là hiệu số mô tả, chỉ diễn giải nhân quả với giả định rằng oracle chỉ khác cấu hình ở ngữ cảnh.

**Đầu ra:** bảng chỉ số hoàn chỉnh; quyết định D2–D5.

**Xong khi:** với một câu hỏi và một câu trả lời bất kỳ, bạn nói được nó đóng góp vào những chỉ số nào và theo công thức nào.

### Ngày 6 – Thống kê, judge, chi phí (D9)

**Mục tiêu:** chốt kế hoạch phân tích trước khi thấy bất kỳ số liệu nào.

| Phút | Việc |
|---|---|
| 0–50 | Kế hoạch thống kê. |
| 50–90 | Quy trình judge và nhãn người. |
| 90–120 | Tiêu chí báo cáo chi phí; chốt D9; rà lại toàn bộ bảng D1–D9. |

**Kế hoạch thống kê cần viết ra:**

- Chỉ số chính (ghi trước): H_gold và correctness. Các chỉ số khác là phụ.
- Họ phép so sánh cho hiệu chỉnh Holm: 13 cấu hình OFAT so với cấu hình neo, tính riêng cho từng bộ dữ liệu và từng chỉ số chính. Các so sánh khác ghi là khám phá.
- Bootstrap: 1.000 lần lấy mẫu lại theo câu hỏi. Với ViQuAD, nhiều câu hỏi chung một đoạn/bài, nên lấy mẫu lại theo cụm `title`.
- Kiểm định hoán vị ghép cặp: đổi dấu ngẫu nhiên hiệu số theo từng câu hỏi, 10.000 hoán vị.
- Hồi quy logistic: ghi công thức và đơn vị quan sát; lưu ý các cấu hình dùng chung câu hỏi nên cần hiệu ứng ngẫu nhiên theo câu hỏi hoặc sai số chuẩn theo cụm.
- Cỡ mẫu: nêu độ rộng khoảng tin cậy kỳ vọng với cỡ mẫu đã chốt ở ngày 4.

**Quy trình judge:**

- Mô hình judge khác mô hình sinh; prompt tiếng Việt; đầu ra JSON với danh sách mệnh đề và nhãn từng mệnh đề.
- 300 mẫu gán nhãn người (150 mỗi bộ), lấy phân tầng theo cấu hình và theo câu trả lời được/không.
- Hai người gán nhãn độc lập, không thấy nhãn judge. Bất đồng do người thứ ba hoặc thảo luận phân xử; ghi lại tỷ lệ bất đồng.
- Báo cáo κ giữa hai người và giữa judge với nhãn đã phân xử. Nếu κ dưới 0,7: sửa prompt trên một nửa mẫu, kiểm tra lại trên nửa còn lại để không chỉnh prompt trên chính tập đánh giá.

**Chi phí:** độ trễ đo trên cùng một loại GPU, cùng batch size 1 cho truy vấn, bỏ lượt chạy đầu, lấy trung vị và phân vị 95; ghi tên GPU và phiên bản thư viện.

**D9:** tính lại tổng lượt sinh bằng cỡ mẫu đã chốt: số cấu hình × tổng số câu hỏi test của hai bộ. Sửa cả hai chỗ trong đề cương (mục 5.3 và 5.5).

**Cổng kiểm tra:** cả chín điểm D có quyết định hoặc được ghi thành hạn chế. Nếu còn điểm mở, ghi người quyết định và hạn, rồi vẫn sang giai đoạn 2.

---

## Giai đoạn 2 – Pilot truy xuất (ngày 7–9)

Pilot chạy trên Colab với dữ liệu đã xử lý của Zalo Legal. Mỗi điều luật là một chunk (tiêu đề + nội dung). Ba cấu hình: BM25, dense `BAAI/bge-m3`, hybrid. Không reranking, không sinh câu trả lời. Pilot dùng toàn bộ 788 truy vấn để mô tả, không dùng để chọn cấu hình.

### Ngày 7 – BM25

**Mục tiêu:** có bảng chỉ số BM25 và khung đánh giá dùng lại cho hai ngày sau.

| Phút | Việc |
|---|---|
| 0–20 | Tạo `02_pilot_retrieval.ipynb`; cài `rank_bm25 underthesea sentence-transformers datasets`; mount Drive; nạp dữ liệu. |
| 20–45 | Viết hàm chỉ số và kiểm tra bằng `assert`. |
| 45–75 | Chạy BM25 tách theo âm tiết (chạy trong vài phút, đảm bảo có số liệu). |
| 75–120 | Đo tốc độ underthesea trên 500 điều luật, ước lượng thời gian cho 61.425 điều. Nếu dưới 60 phút: chạy, lưu kết quả tách từ lên Drive, chạy BM25 tách theo từ. Nếu lâu hơn: để chạy nền và lấy kết quả vào ngày 8, hoặc dùng pyvi. |

```python
import math, re, numpy as np
from datasets import load_from_disk
from rank_bm25 import BM25Okapi

Z = PROCESSED_DIR / 'zalo_legal'
corpus, queries, qrels = (load_from_disk(str(Z / n)) for n in ('corpus', 'queries', 'qrels'))
doc_ids = corpus['id']
docs = [f'{t}\n{x}'.strip() for t, x in zip(corpus['title'], corpus['text'])]

gold = {}
for r in qrels:
    if r['score'] > 0:
        gold.setdefault(r['query-id'], set()).add(r['corpus-id'])
q = {r['id']: r['text'] for r in queries if r['id'] in gold}   # dict bỏ 30 dòng trùng
qids = list(q)
assert len(qids) == 788

def metrics(ranked, rel):
    hits = [d in rel for d in ranked]
    dcg = sum(h / math.log2(i + 2) for i, h in enumerate(hits[:5]))
    idcg = sum(1 / math.log2(i + 2) for i in range(min(len(rel), 5)))
    return {'r5': sum(hits[:5]) / len(rel), 'r20': sum(hits[:20]) / len(rel),
            'mrr10': next((1 / (i + 1) for i, h in enumerate(hits[:10]) if h), 0.0),
            'ndcg5': dcg / idcg}

assert metrics(['a', 'b'], {'a'}) == {'r5': 1, 'r20': 1, 'mrr10': 1, 'ndcg5': 1}
assert metrics(['x', 'a'], {'a'})['mrr10'] == 0.5

def evaluate(S):            # S: ma trận điểm (số truy vấn × số điều luật)
    top = np.argsort(-S, axis=1)[:, :20]
    return [metrics([doc_ids[j] for j in row], gold[qid]) for row, qid in zip(top, qids)]

tok = lambda s: re.findall(r'\w+', s.lower())        # âm tiết; với văn bản đã tách từ, "đường_cao_tốc" là một token
bm25 = BM25Okapi([tok(d) for d in docs])
S_bm25 = np.stack([bm25.get_scores(tok(q[i])) for i in qids]).astype('float32')
np.save(PILOT_DIR / 'S_bm25_syllable.npy', S_bm25)
```

Tách từ: `from underthesea import word_tokenize; word_tokenize(text, format='text')`, áp dụng cho cả tài liệu và truy vấn, rồi dùng lại `tok` ở trên.

**Đầu ra:** chỉ số theo từng truy vấn (lưu CSV) cho BM25 âm tiết, và BM25 tách từ nếu kịp; ma trận điểm lưu trên Drive.

**Xong khi:** có bốn con số trung bình cho ít nhất một biến thể BM25, và hai `assert` chạy qua.

**Kiểm tra nhanh:** đọc 10 truy vấn có Recall@20 bằng 0 để chắc lỗi nằm ở truy xuất chứ không ở cách ghép ID.

### Ngày 8 – Dense

**Mục tiêu:** chỉ số cho `BAAI/bge-m3` trên cùng truy vấn.

| Phút | Việc |
|---|---|
| 0–15 | Bật GPU trên Colab; nạp lại dữ liệu và hàm từ ngày 7. |
| 15–30 | Đếm số điều luật vượt 512 token (đoạn mã bên dưới). |
| 30–90 | Nhúng kho và truy vấn; lưu embedding lên Drive ngay khi xong. Ghi thời gian nhúng. |
| 90–120 | Tính điểm, chỉ số; ghi kích thước file embedding; lấy kết quả BM25 tách từ nếu hôm trước chạy nền. |

```python
from sentence_transformers import SentenceTransformer
m = SentenceTransformer('BAAI/bge-m3', device='cuda')
m.half()
m.max_seq_length = 512        # pilot: cắt cụt ở 512 token; mặc định của mô hình dài hơn nhiều

n_long = sum(len(ids) > 512 for ids in m.tokenizer(docs, truncation=False)['input_ids'])
print('Số điều luật bị cắt:', n_long, 'trên', len(docs))

D = m.encode(docs, batch_size=32, normalize_embeddings=True, show_progress_bar=True).astype('float32')
Q = m.encode([q[i] for i in qids], batch_size=32, normalize_embeddings=True).astype('float32')
np.save(PILOT_DIR / 'D_bgem3.npy', D); np.save(PILOT_DIR / 'Q_bgem3.npy', Q)
S_dense = Q @ D.T             # tìm kiếm chính xác, tương đương FAISS IndexFlatIP
```

Pilot dùng phép nhân ma trận thay cho FAISS vì kho chỉ có 61.425 vector và kết quả giống hệt chỉ mục phẳng. Pipeline chính vẫn dùng FAISS như đề cương.

**Đầu ra:** chỉ số theo từng truy vấn cho dense; số điều luật bị cắt; thời gian nhúng; kích thước embedding.

**Xong khi:** có bảng hai dòng (BM25, dense) với bốn chỉ số.

**Nếu trễ:** nếu hết phiên GPU giữa chừng, giảm `max_seq_length` xuống 256 và ghi rõ; kết quả pilot khi đó chỉ mang tính minh họa.

### Ngày 9 – Hybrid, khoảng tin cậy, ghi chép

**Mục tiêu:** bảng pilot hoàn chỉnh đưa được vào bài.

| Phút | Việc |
|---|---|
| 0–40 | Hybrid với α = 0,7. |
| 40–80 | Khoảng tin cậy bootstrap cho từng cấu hình và cho hiệu số từng cặp. |
| 80–120 | Ghi môi trường (GPU, phiên bản thư viện, seed), dựng bảng kết quả, viết ba đến năm câu về giới hạn của pilot. |

```python
mm = lambda S: (S - S.min(1, keepdims=True)) / (np.ptp(S, axis=1, keepdims=True) + 1e-9)
S_hyb = 0.7 * mm(S_dense) + 0.3 * mm(S_bm25)     # chiều của α và cách chuẩn hóa: theo nguồn đã xác minh ở ngày 1

rng = np.random.default_rng(0)
idx = rng.integers(0, len(qids), (1000, len(qids)))
ci = lambda x: np.percentile(np.asarray(x)[idx].mean(1), [2.5, 97.5])
# một cấu hình: ci(r5_dense); hiệu số ghép cặp: ci(np.array(r5_hyb) - np.array(r5_bm25))
```

**Bảng đưa vào bài:**

| Cấu hình | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---|
| BM25 (âm tiết) | | | | |
| BM25 (tách từ) | | | | |
| bge-m3 | | | | |
| Hybrid α = 0,7 | | | | |

Mỗi ô ghi giá trị và khoảng tin cậy 95%. Để trống ô nào chưa chạy; không ước lượng.

**Giới hạn phải viết kèm:** một bộ dữ liệu; một mức phân đoạn; điều luật dài bị cắt ở 512 token; truy vấn chung điều luật vàng nên các quan sát không hoàn toàn độc lập; không có tập dev nên α không được chỉnh.

**Đây là ngày dự phòng.** Nếu ngày 7–8 trễ: bỏ hybrid, ưu tiên khoảng tin cậy và ghi chép cho những gì đã có.

**Cổng kiểm tra:** có bảng với số liệu thật, hoặc quyết định bằng văn bản rằng bản thảo không có pilot.

---

## Giai đoạn 3 – Viết bản thảo (ngày 10–14)

Số từ dưới đây giả định bài khoảng 8 trang; điều chỉnh theo trả lời của người hướng dẫn ở ngày 1.

### Ngày 10 – Phương pháp, thiết lập, kế hoạch phân tích

| Phút | Việc |
|---|---|
| 0–70 | Tạo `reports/ban-thao.md` với khung mục lục. Viết mục 3 (khoảng 900 từ), mục 4 (khoảng 700 từ), mục 5 (khoảng 500 từ), chủ yếu chuyển từ file quyết định. |
| 70–100 | Sơ đồ pipeline; bảng các mức C/E/R; bảng cấu hình Giai đoạn B. |
| 100–120 | Gửi người hướng dẫn mục 3–5 và bảng D1–D9, kèm ba câu hỏi cụ thể cần ý kiến (đề xuất: phương án D1, việc tách H_ctx/H_gold, phạm vi pilot). Hẹn phản hồi trước ngày 14. |

**Xong khi:** email đã gửi; mục 3–5 không còn chỗ ghi "sẽ quyết định sau" mà không kèm người quyết định.

### Ngày 11 – Công trình liên quan và giới thiệu

| Phút | Việc |
|---|---|
| 0–60 | Mục 2 (khoảng 600 từ), năm tiểu mục. Mỗi đoạn kết thúc bằng một câu nêu công trình đó chưa làm gì so với nghiên cứu này. Chỉ trích nguồn có dấu "đã mở bản gốc" trong `reports/tai-lieu.md`. |
| 60–110 | Mục 1 (khoảng 600 từ): bối cảnh, đặc thù tiếng Việt, khoảng trống, RQ, đóng góp. Viết đóng góp ở thì tương lai/dự kiến, trừ thống kê dữ liệu và pilot. |
| 110–120 | Đối chiếu: mọi trích dẫn trong bài có trong danh mục và ngược lại. |

**Xong khi:** không còn trích dẫn nào chưa xác minh.

### Ngày 12 – Kết quả sơ bộ, hạn chế, bảng mẫu

| Phút | Việc |
|---|---|
| 0–50 | Mục 6 (khoảng 500 từ): 6.1 lấy số từ notebook đã chạy lại ở ngày 1 (số dòng, giá trị thiếu, trùng lặp, độ dài văn bản, số dòng thay đổi sau chuẩn hóa); 6.2 bảng pilot; 6.3 những gì pilot chưa cho phép kết luận. |
| 50–90 | Mục 7 (khoảng 500 từ): hạn chế theo bốn nhóm: đo lường (judge, H_gold phạt tri thức nền), dữ liệu (cỡ mẫu Zalo, câu không trả lời được nhân tạo, rò rỉ Wikipedia), thiết kế (một mô hình sinh, OFAT bỏ qua tương tác), khái quát (hai miền). |
| 90–120 | Bảng và hình mẫu cho mục 5.5: bảng Giai đoạn A, bảng Giai đoạn B, bảng RAH theo miền, hình biên Pareto. Để trống ô số liệu, ghi "sẽ báo cáo". |

**Xong khi:** bản thảo đủ mục 1–7; mọi con số trong mục 6 truy được về một cell notebook.

### Ngày 13 – Tóm tắt, kết luận, phản biện nội bộ

| Phút | Việc |
|---|---|
| 0–30 | Tóm tắt (khoảng 200 từ) và kết luận (khoảng 150 từ). |
| 30–90 | Đọc liền mạch một lần không sửa, ghi chú vấn đề; sau đó chạy danh sách kiểm tra bên dưới. |
| 90–120 | Sửa các điểm không khớp. |

**Danh sách kiểm tra nhất quán:**

- Số cấu hình: 144 ở Giai đoạn A; số cấu hình Giai đoạn B khớp giữa văn bản và bảng.
- Cỡ mẫu từng bộ khớp với quyết định D1; tổng lượt sinh khớp D9.
- Ký hiệu C1–C6, E0–E5, R0–R3, H_ctx, H_gold, RAH dùng thống nhất.
- Số liệu ViQuAD khớp với bản dữ liệu thực tế đã xác minh ở ngày 1.
- Mỗi RQ có ít nhất một chỉ số và một phép so sánh trong mục 5.
- Tìm các từ "cho thấy", "chứng minh", "vượt trội", "cải thiện": mỗi lần xuất hiện phải đi với số liệu đã đo, nếu không thì đổi sang "dự kiến kiểm định".

### Ngày 14 – Phản hồi và hoàn thiện

| Phút | Việc |
|---|---|
| 0–50 | Xử lý phản hồi của người hướng dẫn, ưu tiên điểm ảnh hưởng thiết kế. Nếu chưa có phản hồi: ghi thành việc còn chờ và dùng thời gian này để đọc lại mục 3 và 5. |
| 50–90 | Kiểm tra danh mục tham khảo, số thứ tự bảng/hình, chú thích, liên kết chéo. |
| 90–120 | Xuất bản nộp. Viết danh sách "điều kiện trước khi thành bài báo kết quả": pipeline đầy đủ, tập đánh giá, hiệu chỉnh judge, Giai đoạn A, Giai đoạn B, phân tích, kèm ước lượng số tuần theo lịch 16 tuần của đề cương. |

**Xong khi:** bản thảo đã gửi; file quyết định, notebook pilot và bảng tài liệu ở trạng thái mà người khác đọc hiểu được.

---

## Điểm phụ thuộc và rủi ro theo ngày

| Phụ thuộc | Ảnh hưởng tới | Xử lý nếu không đạt |
|---|---|---|
| Trả lời của người hướng dẫn về nơi nộp (hạn cuối ngày 4) | Độ dài và trọng tâm các ngày 10–13 | Viết theo giả định 8 trang, tiếng Việt; ghi giả định ở đầu bản thảo |
| Dữ liệu đã xử lý trên Drive (ngày 1) | Ngày 7–9 | Dùng dữ liệu thô và ghi rõ; chuẩn hóa không ảnh hưởng ID và qrels |
| Tốc độ underthesea (ngày 7) | Dòng "BM25 tách từ" | Dùng pyvi, hoặc để trống dòng đó |
| Phiên GPU Colab (ngày 8) | Dense và hybrid | Giảm `max_seq_length`; nếu vẫn không được, pilot chỉ gồm BM25 |
| Nguồn không xác minh được (ngày 1–2) | Khẳng định về khoảng trống | Bỏ trích dẫn đó và làm mềm khẳng định |
