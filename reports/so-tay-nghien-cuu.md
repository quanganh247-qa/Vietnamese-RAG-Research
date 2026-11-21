# Sổ tay nghiên cứu – phần Tuần 1

**Ngày viết:** 14/11/2026. **Phạm vi:** mã Tuần 1 trong `src/ragvi/` (`metrics.py`, `retrieval.py`, `chunking.py`, `data.py`) và các test trong `tests/`.

Sổ tay này giúp chủ đề tài tự giải thích từng thành phần đã làm: nó trả lời câu hỏi nghiên cứu nào, chạy ra sao, nằm ở đâu trong mã, vì sao thiết kế như vậy, và hội đồng có thể hỏi gì. Các quy ước tên gọi (RQ1–RQ5, C/E/R, D1–D9) lấy từ đề cương v2, `Kế hoạch 30 ngày (hạn 11-12).md` và `reports/quyet-dinh-thiet-ke.md`.

**Tình trạng số liệu (cập nhật 14/11, sau lượt chạy Colab đầu tiên).** Mục "Kết quả" cuối file đã có số liệu thật cho BM25, dense, hybrid, hai tập đánh giá và phân đoạn Zalo. Đoạn dưới đây mô tả tình trạng lúc viết sổ tay: đến ngày viết, **chưa có kết quả nào trên dữ liệu thật**. Mã mới chỉ chạy qua 26 test trên dữ liệu giả (`PYTHONPATH=src .venv/bin/python -m pytest -q tests`); dữ liệu, mô hình `BAAI/bge-m3` và `underthesea` chỉ có trên Colab. Mọi con số trong các ví dụ dưới đây là **ví dụ minh họa** tự đặt ra để tính tay, không phải kết quả thực nghiệm. Các bảng ở mục "Kết quả" cuối file để trống, điền khi chạy thật.

**Cách tự kiểm tra chung.** Từ thư mục gốc của kho mã, chạy toàn bộ test bằng lệnh trên. Trong notebook Colab, sau khi `git clone` kho mã, thêm `src` vào đường dẫn rồi gọi thẳng các hàm:

```python
import sys; sys.path.insert(0, 'src')
```

---

## 1. Chỉ số truy xuất: Recall@k, MRR@10, nDCG@5

### Nó là gì và để trả lời câu hỏi nào

Bốn chỉ số này đo chất lượng **tầng truy xuất** (retrieval): với mỗi câu hỏi, hệ thống trả về một danh sách đoạn văn xếp theo độ liên quan, và ta hỏi "đoạn đúng có nằm trong danh sách không, và nằm ở vị trí thứ mấy". Đây là biến phụ thuộc của Giai đoạn A (chỉ truy xuất, không gọi LLM) và là đầu vào để trả lời RQ1 (ảnh hưởng của phân đoạn C), RQ2 (mô hình nhúng và hybrid E) và RQ3 (reranking R) ở tầng truy xuất. Đề cương mục 5.6(a) chọn đúng bốn chỉ số này.

### Cách hoạt động

Trước hết, mỗi kết quả trong danh sách xếp hạng được đánh dấu **đúng** (True) hoặc **sai** (False) theo tiêu chí ở mục 2. Gọi `n_rel` là số tài liệu vàng (gold, tức tài liệu được gán nhãn là đúng) của câu hỏi.

- **Recall@k** (độ phủ tại k): số tài liệu vàng tìm được trong k kết quả đầu, chia cho `n_rel`. Câu hỏi có 2 điều luật vàng mà top-5 chứa 1 thì Recall@5 = 0,5. Recall@20 quan trọng vì reranker nhận top-20; Recall@5 quan trọng vì prompt nhận 5 đoạn.
- **MRR@10** (mean reciprocal rank): lấy vị trí r của kết quả đúng **đầu tiên** trong 10 kết quả đầu, điểm là 1/r; không có kết quả đúng nào trong top-10 thì điểm là 0. Lấy trung bình trên các câu hỏi. Chỉ số này chỉ quan tâm "câu trả lời đúng đầu tiên xuất hiện sớm đến đâu".
- **nDCG@5** (normalized discounted cumulative gain): mỗi kết quả đúng ở vị trí i (đếm từ 1) đóng góp 1/log₂(i+1), nên đúng ở vị trí 1 được 1 điểm, ở vị trí 2 được 0,63, ở vị trí 5 chỉ còn 0,39. Tổng này gọi là DCG. Chia cho IDCG, là DCG của danh sách lý tưởng (mọi tài liệu vàng đứng đầu), để điểm nằm trong [0, 1]. Liên quan được tính nhị phân (đúng/sai), không có mức "đúng một phần".

**Quy tắc mỗi tài liệu vàng chỉ tính một lần.** Khi kho đã được phân đoạn, một điều luật vàng có thể xuất hiện nhiều lần trong danh sách (nhiều chunk của cùng điều luật). Chỉ lần xuất hiện đầu tiên được đánh dấu đúng; các lần sau bị đánh dấu sai nhưng **vẫn giữ chỗ** trong danh sách. Nếu không có quy tắc này, Recall có thể vượt 1.

**Ví dụ minh họa (tính tay).** Câu hỏi có hai điều luật vàng {A, B}, nên `n_rel` = 2. Hệ thống trả về năm chunk đầu thuộc các điều luật `[X, A, A, Y, B]`, và từ vị trí 6 đến 20 không có A hay B.

| Vị trí i | Điều luật | Đúng? | Đóng góp DCG = 1/log₂(i+1) |
|---|---|---|---|
| 1 | X | Sai | 0 |
| 2 | A | Đúng (lần đầu) | 1/log₂3 = 0,6309 |
| 3 | A | Sai (A đã tính) | 0 |
| 4 | Y | Sai | 0 |
| 5 | B | Đúng | 1/log₂6 = 0,3869 |

- Recall@5 = 2/2 = 1,0. Recall@20 = 2/2 = 1,0.
- MRR@10: kết quả đúng đầu tiên ở vị trí 2, nên 1/2 = 0,5.
- nDCG@5: DCG = 0,6309 + 0,3869 = 1,0178. IDCG (A và B ở vị trí 1 và 2) = 1 + 0,6309 = 1,6309. nDCG@5 = 1,0178 / 1,6309 = **0,6241**.
- Nếu bỏ quy tắc "một lần", vị trí 3 cũng được tính đúng và Recall@5 thành 3/2 = 1,5, vô nghĩa.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/metrics.py`: hàm `metrics` tính bốn chỉ số từ danh sách True/False và `n_rel`; `zalo_hits` biến danh sách mã điều luật xếp hạng thành danh sách True/False theo quy tắc "một lần"; `mean_metrics` lấy trung bình trên nhiều câu hỏi. Test ở `tests/test_retrieval.py` (`test_metrics`, `test_zalo_hits_counts_each_gold_doc_once`, `test_mean_metrics`). Thử lại ví dụ trên:

```python
from ragvi.metrics import metrics, zalo_hits
hits = zalo_hits(['X', 'A', 'A', 'Y', 'B'], {'A', 'B'})   # [False, True, False, False, True]
metrics(hits, 2)   # {'r5': 1.0, 'r20': 1.0, 'mrr10': 0.5, 'ndcg5': 0.624...}
```

### Lựa chọn thiết kế và lý do

- Bốn chỉ số và các mốc k (5, 10, 20) giữ nguyên đề cương. Vị trí được đếm theo **chunk**, không theo điều luật đã gộp: chunk trùng điều luật vẫn chiếm chỗ. Hệ quả: với C5 (nhiều chunk nhỏ mỗi điều luật), 20 chunk đầu có thể chỉ thuộc vài điều luật khác nhau, nên Recall@20 của C5 và của C4 (mỗi điều luật một chunk) đo trên số tài liệu phân biệt khác nhau. Đây là đặc điểm có chủ ý (pipeline thật đưa chunk vào prompt, không đưa điều luật), nhưng cần nói rõ khi so sánh các mức C.
- IDCG dùng min(`n_rel`, 5), nên câu hỏi có hơn 5 tài liệu vàng vẫn có thể đạt nDCG@5 = 1, nhưng Recall@5 thì không.
- **Điểm còn mở:** chỉ số truy xuất chỉ có nghĩa với câu trả lời được. Câu không trả lời được của Zalo không còn điều luật vàng trong kho thu hẹp, nên khi chạy Giai đoạn A trên tập test phải lọc chúng ra; mã hiện chưa làm việc lọc này (lệnh hiện tại chỉ chạy thử trên 788 truy vấn với kho đầy đủ).

### Câu hỏi hội đồng có thể hỏi

1. *Vì sao cần cả Recall và nDCG?* Recall chỉ hỏi "có hay không" trong top-k; nDCG thưởng thêm cho việc xếp đúng lên đầu. Reranker (R1) không đổi Recall@20 (cùng 20 ứng viên) nhưng có thể đổi nDCG@5 và Recall@5, nên cần cả hai để đo RQ3.
2. *Một điều luật xuất hiện ba lần trong top-5 thì tính thế nào?* Chỉ lần đầu được tính; hai lần sau là sai nhưng vẫn chiếm chỗ, phản ánh đúng việc chúng chiếm chỗ của đoạn khác trong prompt.
3. *Có so được con số truy xuất giữa Zalo và ViQuAD không?* Không trực tiếp, vì tiêu chí "chunk đúng" khác nhau (mục 2); chỉ so thứ tự các cấu hình trong từng miền.

---

## 2. Tiêu chí "chunk đúng"

### Nó là gì và để trả lời câu hỏi nào

Mọi chỉ số ở mục 1 cần trả lời câu hỏi "chunk này có đúng không". Tiêu chí phải **không phụ thuộc cách phân đoạn**, nếu không thì so sánh C1, C3, C4, C5 (RQ1) sẽ thiên lệch. Đây là quyết định D2.

### Cách hoạt động

Mọi hàm phân đoạn trả về bản ghi `(chunk_id, doc_id, start, end, text)`: chunk thuộc tài liệu nào (`doc_id`) và chiếm khoảng ký tự `[start, end)` nào trong tài liệu gốc. Nhờ đó tiêu chí chỉ cần nhìn vào `doc_id` và vị trí, không cần biết chunk được cắt bằng cách nào.

- **Zalo Legal: theo điều luật cha.** Zalo chỉ có qrels (cặp câu hỏi – điều luật liên quan), không có đáp án dạng chuỗi. Một chunk đúng nếu `doc_id` của nó nằm trong tập điều luật vàng của câu hỏi; mỗi điều luật vàng tính một lần (mục 1).
- **ViQuAD: theo 80% ký tự đáp án.** Một chunk đúng nếu thuộc đúng đoạn gốc (`doc_id` trùng `gold_doc_id`) và khoảng `[start, end)` của chunk phủ ít nhất 80% số ký tự của đáp án vàng.

**Ví dụ minh họa ViQuAD.** Đáp án vàng nằm ở ký tự 100–120 của đoạn (20 ký tự).

| Chunk | Khoảng ký tự | Số ký tự đáp án phủ được | Tỷ lệ | Đúng? |
|---|---|---|---|---|
| C4 (nguyên đoạn) | 0–400 | 20 | 100% | Đúng |
| C1, chunk 1 | 0–112 | 12 (100–112) | 60% | Sai |
| C1, chunk 2 | 112–400 | 8 (112–120) | 40% | Sai |
| C3, câu chứa đáp án | 90–150 | 20 | 100% | Đúng |

Với C1 trong ví dụ này, ranh giới cắt rơi giữa đáp án nên **không chunk nào đúng**: câu hỏi trở thành không truy xuất được do cách cắt chứ không do mô hình nhúng. Đó chính là loại hiệu ứng RQ1 muốn đo.

### Nằm ở đâu trong mã và cách tự kiểm tra

- Zalo: `zalo_hits` trong `src/ragvi/metrics.py` (đã có, đã test). Hiện truy xuất chạy ở mức điều luật nên `doc_id` của kết quả chính là mã điều luật.
- ViQuAD: **chưa cài đặt.** Phần đã có là dữ liệu đầu vào cho tiêu chí: `locate_answers` trong `src/ragvi/data.py` lưu vị trí ký tự `start`/`end` của từng đáp án sao cho `context[start:end]` đúng bằng chuỗi đáp án (test `test_locate_answers_fixes_shifted_start` trong `tests/test_data.py`).

### Lựa chọn thiết kế và lý do

- Đề cương mục 5.6(a) dùng quy tắc 80% cho cả hai bộ. D2 đổi riêng Zalo sang "theo điều luật cha" vì Zalo không có đáp án dạng chuỗi.
- **Hạn chế phải nêu:** tiêu chí Zalo rộng hơn (đúng điều luật nhưng sai khoản vẫn tính đúng). Do đó lợi thế của C5 (cắt theo khoản) không hiện ra ở tầng truy xuất của Zalo; nó chỉ có thể hiện ra ở tầng câu trả lời (chỉ số "nhầm điều luật" của H1b).
- **Đã chốt 15/11 cho ViQuAD** (hàm `viquad_hits` trong `metrics.py`): chunk đúng khi thuộc đoạn gốc của câu hỏi và phủ ít nhất 80% số ký tự của **ít nhất một** đáp án vàng, tính theo vị trí `start`/`end` lưu trong tập đánh giá; mỗi câu có đúng một đơn vị vàng (`n_rel = 1`) và chỉ lần trúng đầu tiên trong danh sách được tính. Hệ quả cần biết: nếu chuỗi đáp án xuất hiện ở chỗ khác trong đoạn, chunk chứa lần xuất hiện khác đó không được tính. Ở mức đoạn (C4), tiêu chí rút gọn thành "trả về đúng đoạn gốc". Hàm đã có test nhưng chưa nối vào lệnh chạy; truy xuất mức chunk là việc của ngày 21/11.

### Câu hỏi hội đồng có thể hỏi

1. *Vì sao không dùng một tiêu chí chung cho hai bộ?* Zalo không có đáp án dạng chuỗi, chỉ có qrels ở mức điều luật, nên quy tắc 80% không áp dụng được (D2).
2. *Ngưỡng 80% lấy từ đâu?* Từ đề cương; nó cho phép đáp án bị cắt nhẹ ở mép chunk mà vẫn tính đúng. Có thể báo cáo thêm ở ngưỡng 100% như phân tích độ nhạy nếu còn thời gian.
3. *Tiêu chí Zalo có ưu ái C4 không?* Có thể: C4 là cả điều luật nên mỗi chunk trúng là một điều luật. Vì vậy so sánh C4 với C5 trên Zalo phải xem cả tầng câu trả lời.

---

## 3. BM25 (E0) và việc tách âm tiết hay tách từ

### Nó là gì và để trả lời câu hỏi nào

BM25 là phương pháp truy xuất **từ vựng** (lexical): chấm điểm tài liệu theo số lần các từ của câu hỏi xuất hiện trong tài liệu. Nó là mức E0 của yếu tố E, mốc so sánh cho RQ2 (dense có hơn BM25 không) và là một nửa của hybrid E5. Đề cương ghi BM25 "rất mạnh ở văn bản pháp luật", nơi câu hỏi thường lặp lại thuật ngữ trong luật.

### Cách hoạt động

Mỗi tài liệu và câu hỏi được tách thành danh sách **term** (đơn vị từ vựng). Với mỗi term t của câu hỏi, tài liệu d nhận điểm

  IDF(t) × tf · (k1 + 1) / (tf + k1 · (1 − b + b · |d| / avgdl))

rồi cộng qua mọi term. Trong đó tf là số lần t xuất hiện trong d; |d| là độ dài d (số term) và avgdl là độ dài trung bình của kho; IDF(t) = ln((N − n_t + 0,5) / (n_t + 0,5)) với N là số tài liệu và n_t là số tài liệu chứa t. Ý nghĩa: term hiếm (IDF cao) quan trọng hơn term phổ biến; tf tăng thì điểm tăng nhưng bão hòa dần (k1); tài liệu dài bị phạt nhẹ (b). Thư viện `rank_bm25` (lớp `BM25Okapi`) dùng k1 = 1,5, b = 0,75, và thay IDF âm (term có trong hơn nửa kho) bằng 0,25 lần IDF trung bình.

**Âm tiết hay từ.** Tiếng Việt viết cách nhau theo âm tiết, không theo từ: "thu nhập doanh nghiệp" là bốn âm tiết nhưng hai từ.

- Tách âm tiết (mã hiện tại): `['thu', 'nhập', 'doanh', 'nghiệp']`. Câu hỏi chứa "nhập" sẽ khớp cả "nhập khẩu" lẫn "thu nhập".
- Tách từ (ví dụ minh họa, đầu ra thật của `underthesea.word_tokenize` có thể khác): `['thu_nhập', 'doanh_nghiệp']`. Term chính xác hơn, IDF có nghĩa hơn, nhưng phụ thuộc chất lượng bộ tách từ và chậm hơn nhiều.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/retrieval.py`: `tokenize_syllables` (chữ thường, lấy các cụm ký tự chữ-số, bỏ dấu câu), `build_bm25` dựng chỉ mục với hàm tách truyền vào, `bm25_scores` trả về vector điểm trên cả kho, `time_word_tokenize` đo tốc độ `underthesea.word_tokenize` trên 500 điều luật ngẫu nhiên và ước lượng cho cả kho theo **số ký tự** (vì độ dài điều luật lệch rất mạnh). Test: `test_tokenize_syllables`, `test_bm25_ranks_gold_first`, `test_bm25_custom_tokenize`.

```python
from ragvi.retrieval import tokenize_syllables, build_bm25, bm25_scores
tokenize_syllables('Điều 1. Phạm vi, ÁP DỤNG!')   # ['điều', '1', 'phạm', 'vi', 'áp', 'dụng']
# Đổi sang tách từ: build_bm25(texts, tokenize=underthesea.word_tokenize), và truyền cùng hàm vào bm25_scores
```

Lệnh đo tốc độ trên Colab: `PYTHONPATH=src python -m ragvi.retrieval $P/zalo_legal $O/retrieval --time-tokenizer`.

### Lựa chọn thiết kế và lý do

- Đề cương chọn E0 = BM25 tách từ bằng underthesea. Kế hoạch đặt **quy tắc quyết định ghi trước**: nếu tách từ cả kho Zalo mất dưới 30 phút thì E0 dùng underthesea, tách lại cho từng cách phân đoạn và lưu đệm; nếu lâu hơn thì E0 dùng âm tiết cho mọi cấu hình, BM25 tách từ chỉ báo cáo ở mức điều luật như so sánh phụ, và ghi rõ là lệch đề cương. Quyết định này (hạn 13/11) **chưa chốt** vì chưa đo được trên Colab.
- Mã hiện mặc định âm tiết vì không cần thư viện ngoài và chạy nhanh; đổi sang tách từ chỉ cần truyền hàm khác.
- BM25 dùng ranh giới chunk do tokenizer `BAAI/bge-m3` quyết định (D7), nhưng term của BM25 vẫn do hàm tách riêng. Hai việc này độc lập: tokenizer quyết định *chunk ở đâu*, hàm tách quyết định *BM25 đếm cái gì*.

### Câu hỏi hội đồng có thể hỏi

1. *Tách âm tiết có làm BM25 yếu đi không?* Có thể, vì mất ranh giới từ ghép; đó là lý do đề cương chọn tách từ. Nếu buộc dùng âm tiết, kết quả E0 là cận dưới của BM25 và phải ghi là hạn chế; bảng phụ ở mức điều luật cho biết chênh lệch.
2. *Vì sao ước lượng thời gian theo ký tự mà không theo số tài liệu?* Điều luật dài nhất khoảng 250 nghìn ký tự, trong khi đa số ngắn; ước lượng theo số tài liệu sẽ sai nhiều nếu mẫu 500 điều tình cờ ít điều dài.
3. *BM25 có xử lý câu hỏi thiếu dấu không?* Không; "thue" và "thuế" là hai term khác nhau. Đây là giới hạn của E0, không được xử lý trong phạm vi hiện tại.

---

## 4. Dense retrieval với `BAAI/bge-m3` (E3)

### Nó là gì và để trả lời câu hỏi nào

Dense retrieval (truy xuất dày) biến câu hỏi và tài liệu thành **vector nhúng** (embedding), một dãy số thực (với bge-m3 là 1.024 chiều) mà các văn bản cùng nghĩa có vector gần nhau, kể cả khi không dùng chung từ. E3 là mức neo của yếu tố E: cấu hình neo của Giai đoạn B là C3–E3–R0. Nó trả lời RQ2 khi so với E0 (BM25), E5 (hybrid), và ở Giai đoạn A với E2, E4.

### Cách hoạt động

Mô hình nhúng mã hóa mọi tài liệu một lần (bước tốn GPU nhất), lưu thành ma trận. Với mỗi câu hỏi, mã hóa câu hỏi rồi tính **độ tương tự cosine** với mọi tài liệu. Vì mọi vector đã được chuẩn hóa về độ dài 1 (chuẩn hóa L2), cosine chính là tích vô hướng, nên điểm của cả kho là một phép nhân ma trận với vector.

Ví dụ minh họa với vector 3 chiều đã chuẩn hóa: câu hỏi q = (0,6; 0,8; 0); tài liệu d1 = (0,8; 0,6; 0) cho điểm 0,6·0,8 + 0,8·0,6 = 0,96; tài liệu d2 = (0; 0,6; 0,8) cho 0,48. d1 xếp trên d2.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/retrieval.py`: `embed` nhúng danh sách văn bản bằng `sentence-transformers`, giới hạn 512 token mỗi văn bản, chuẩn hóa L2, in số tài liệu mỗi giây, và đọc/ghi file đệm `.npy`; file đệm có số dòng khác số văn bản thì báo lỗi thay vì dùng nhầm. `embedding_cache_path` đặt tên file đệm theo khóa (bộ dữ liệu, cách phân đoạn, mô hình). Trong `main`, điểm dense của một câu hỏi là `doc_vectors @ query_vector`. Test `test_embed_reads_cache_without_loading_model` kiểm tra đọc đệm mà không tải mô hình. Nhánh dense **chưa chạy thật lần nào** (cần GPU Colab).

```
PYTHONPATH=src python -m ragvi.retrieval $P/zalo_legal $O/retrieval --methods dense
```

### Lựa chọn thiết kế và lý do

- **Cắt ở 512 token** (D7 và quy ước chung của kế hoạch) để giới hạn thời gian nhúng, dù bge-m3 nhận được dài hơn. Hệ quả: ở mức điều luật (C4), điều luật dài chỉ được nhúng phần đầu, còn BM25 thấy cả điều luật. Bảng ba dòng ngày 14/11 so BM25 với dense trên cùng kho nhưng dense thấy ít văn bản hơn; D7 yêu cầu báo cáo tỷ lệ bị cắt, **mã hiện chưa tính tỷ lệ này**.
- **Đệm theo khóa (bộ dữ liệu, C, E)**: nhúng kho là bước đắt nhất; Giai đoạn A cần 24 lượt nhúng, nên mỗi lượt chỉ chạy một lần và mất phiên Colab không mất kết quả.
- bge-m3 không cần tiền tố cho câu hỏi hay tài liệu. E4 (`intfloat/multilingual-e5-large`) thì cần `query: ` và `passage: `; việc này hẹn xác minh ngày 21/11 (D7) và chưa có trong `embed`.
- Chưa dùng FAISS: với khoảng 61 nghìn vector, nhân ma trận trực tiếp đủ nhanh và cho kết quả chính xác (không xấp xỉ).

### Câu hỏi hội đồng có thể hỏi

1. *Vì sao chọn bge-m3 làm neo?* Đề cương dẫn Nguyen & Quan (EACL 2026): mô hình đa ngôn ngữ như bge-m3 bền vững nhất giữa các miền; nó cũng là nền của E2 và các reranker.
2. *Cắt 512 token có làm thiệt dense ở Zalo không?* Có, ở mức điều luật. Đây là một lý do phân đoạn quan trọng với Zalo: C1, C3, C5 cắt điều luật dài thành mảnh ngắn hơn 512 token nên dense thấy đủ nội dung. Phải báo cáo tỷ lệ bị cắt.
3. *Tokenizer dùng để phân đoạn có phải của bge-m3 không, kể cả khi E là mô hình khác?* Có (D7); xem mục 6.

---

## 5. Hybrid (E5)

### Nó là gì và để trả lời câu hỏi nào

Hybrid kết hợp điểm BM25 và điểm dense thành một điểm duy nhất, với hy vọng giữ được cả khớp từ chính xác (tên riêng, số hiệu văn bản) lẫn khớp nghĩa. Đây là mức E5 và là phần thứ hai của H2 ("hybrid giảm ảo giác nhiều nhất vì giữ được thực thể/tên riêng").

### Cách hoạt động

Điểm BM25 (từ 0 đến vài chục) và cosine (thường 0,2–0,9) có thang khác nhau, nên không cộng trực tiếp được. Mỗi vector điểm được **chuẩn hóa min–max** trên cả kho: x' = (x − min) / (max − min), đưa về [0, 1]. Sau đó điểm hybrid = α · dense' + (1 − α) · BM25', với α = 0,7.

**Ví dụ minh họa (kho 3 tài liệu).**

| Tài liệu | Dense (cosine) | Dense' | BM25 | BM25' | α nhân dense: 0,7·D' + 0,3·B' | α nhân BM25: 0,3·D' + 0,7·B' |
|---|---|---|---|---|---|---|
| d1 | 0,80 | (0,80−0,40)/0,40 = 1,0 | 4 | 4/10 = 0,4 | 0,70 + 0,12 = **0,82** | 0,30 + 0,28 = 0,58 |
| d2 | 0,60 | 0,20/0,40 = 0,5 | 10 | 1,0 | 0,35 + 0,30 = 0,65 | 0,15 + 0,70 = **0,85** |
| d3 | 0,40 | 0 | 0 | 0 | 0 | 0 |

Với α nhân dense, d1 đứng đầu; nếu α nhân BM25, d2 đứng đầu. Chiều của α đổi thứ hạng, nên không phải chi tiết kỹ thuật vụn vặt.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/retrieval.py`: `minmax` (vector hằng thì trả về toàn 0 thay vì chia cho 0), `hybrid_scores`, `top_k` (điểm bằng nhau thì giữ thứ tự trong kho, để kết quả tái lập được). Mỗi câu hỏi được xử lý riêng nên không phải giữ ma trận điểm của cả 788 câu. Test `test_minmax_and_top_k`, `test_hybrid_with_fake_dense`.

```python
from ragvi.retrieval import hybrid_scores
hybrid_scores([0.80, 0.60, 0.40], [4, 10, 0], alpha=0.7)   # [0.82, 0.65, 0.  ]
hybrid_scores([0.80, 0.60, 0.40], [4, 10, 0], alpha=0.3)   # [0.58, 0.85, 0.  ]
```

Kết quả truy xuất của BM25, dense, hybrid được ghi nối tiếp vào `retrieval_zalo.jsonl`, mỗi dòng một cặp (phương pháp, câu hỏi), kèm bốn chỉ số và 20 mã điều luật đầu. Chạy lại sau khi mất phiên thì bỏ qua các cặp đã có (`run_retrieval`, test `test_run_retrieval_skips_existing_rows`). Đổi mô hình hoặc α thì nhãn phương pháp đổi theo (ví dụ `hybrid[alpha=0.5]`) để dòng cũ không bị coi là đã xong.

### Lựa chọn thiết kế và lý do

- α = 0,7 lấy từ đề cương, dựa trên khoảng α ≈ 0,6–0,8 mà Nguyen & Quan báo cáo.
- **Đã chốt 14/11:** s(q,d) = α · minmax(dense) + (1 − α) · minmax(BM25), chuẩn hóa min–max theo từng truy vấn trên cả kho, α = 0,7 (70% dense). Căn cứ: Nguyen & Quan, "Which Works Best for Vietnamese? A Practical Study of Information Retrieval Methods across Domains", Findings of EACL 2026 (https://aclanthology.org/2026.findings-eacl.110); mã nguồn ViRE (https://github.com/longstnguyen/ViRE, `src/vi_retrieval_eval/runner.py`). Bài báo ghi α = 0,7 và nêu α tốt nhất nằm trong khoảng 0,6–0,8; văn bản bài không nêu cách chuẩn hóa, cách chuẩn hóa lấy từ mã nguồn của tác giả. Việc đối chiếu do agent tra cứu thực hiện; bạn nên tự mở hai nguồn trên kiểm lại trước khi trích dẫn.
- Min–max trên cả kho phụ thuộc vào tài liệu điểm thấp nhất của kho. Trong kho lớn, BM25 nhỏ nhất gần như luôn là 0; dense nhỏ nhất là cosine của tài liệu kém liên quan nhất. Khi đổi cách phân đoạn (số chunk thay đổi), thang chuẩn hóa cũng đổi theo.

### Câu hỏi hội đồng có thể hỏi

1. *Vì sao không cộng trực tiếp hai điểm?* Hai thang khác nhau; BM25 có thể lên hàng chục và sẽ lấn át cosine.
2. *Có chỉnh α trên dữ liệu không?* Không. α cố định từ tài liệu trước khi có kết quả, để tránh chọn tham số trên chính tập đánh giá (cùng tinh thần D8).
3. *Vì sao không dùng Reciprocal Rank Fusion?* Nội suy tuyến tính là cách đề cương dẫn từ nghiên cứu gần nhất; RRF có thể là phân tích phụ nhưng ngoài phạm vi hiện tại.

---

## 6. Năm cách phân đoạn: C1, C3, C4, C5, C5 không tiêu đề

### Nó là gì và để trả lời câu hỏi nào

Phân đoạn (chunking) là cắt tài liệu thành các mảnh (chunk) để nhúng, truy xuất và đưa vào prompt. Đây là yếu tố C, trả lời RQ1 và giả thuyết H1b (gắn tiêu đề cha giảm lỗi "nhầm điều luật"). Kế hoạch 30 ngày giữ C1, C3, C4, C5 và thêm "C5 không tiêu đề"; bỏ C2 và C6.

### Cách hoạt động chung

Kích thước đo bằng **token** của tokenizer tham chiếu `BAAI/bge-m3` (D7). Tokenizer trả về vị trí ký tự của từng token, nên mã cắt ở vị trí ký tự trong văn bản gốc; chunk luôn là lát cắt nguyên văn `text[start:end]` (riêng C5 có thêm tiêu đề phía trước). Mọi cách đều trả về bản ghi `(chunk_id, doc_id, start, end, text)`.

- **C1 – cố định:** mỗi chunk 256 token liền nhau, không chồng lấn. Có thể cắt giữa câu, thậm chí giữa từ.
- **C3 – theo câu:** tách câu bằng `underthesea.sent_tokenize`, tìm lại vị trí từng câu trong văn bản gốc, rồi gộp các câu liên tiếp tới khi thêm câu nữa sẽ vượt 256 token. Câu đơn lẻ dài hơn 256 token thì cắt bằng C1. Phần chữ mà hàm tách câu bỏ sót vẫn được giữ, nên không mất ký tự nào.
- **C4 – nguyên tài liệu:** mỗi điều luật Zalo (tiêu đề + nội dung) hoặc mỗi đoạn ViQuAD là một chunk.
- **C5 – ViStructChunk:** dựng cây Điều → Khoản → Điểm. Khoản nhận diện bằng dòng bắt đầu `số. ` (regex `^\d+\.\s`), Điểm bằng dòng bắt đầu `chữ) ` (`^[a-zđ]\)\s`). Đơn vị chunk là Khoản; Khoản dài hơn 256 token thì tách theo Điểm (phần dẫn trước điểm a là một chunk riêng); phần mở đầu trước khoản 1 là một chunk; mảnh nào vẫn quá dài thì cắt bằng C3. Mỗi chunk được gắn **tiêu đề cha** phía trước, ví dụ `Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng, Khoản 2, Điểm a: `. Số hiệu văn bản lấy từ mã tài liệu vì kho không có tên đầy đủ của văn bản. Chunk bắt đầu từ đầu điều luật đã chứa dòng tiêu đề Điều, nên chỉ được gắn `Văn bản …, `. Điều luật không có khoản nào: một chunk nếu không quá 256 token (trùng C4, thêm `Văn bản …, `), dài hơn thì cắt bằng C3.
- **C5 không tiêu đề:** cùng ranh giới `start`/`end` với C5, chỉ bỏ tiêu đề cha.

**Ví dụ minh họa.** Điều luật tự viết (cũng là điều luật trong test), có phần mở đầu và hai khoản, khoản 2 có hai điểm:

```
Điều 1. Phạm vi áp dụng
Thông tư này quy định như sau:
1. Khoản một rất ngắn.
2. Khoản hai gồm các trường hợp sau:
a) trường hợp thứ nhất của khoản hai;
b) trường hợp thứ hai của khoản hai.
```

Để ví dụ có nhiều chunk, giới hạn đặt là **13 token** thay vì 256, tokenizer giả coi mỗi cụm không chứa khoảng trắng là một token, và hàm tách câu giả cắt sau mọi dấu chấm có khoảng trắng theo sau. Đầu ra dưới đây là đầu ra thật của mã với các giả định đó; với tokenizer bge-m3 và underthesea, ranh giới sẽ khác.

| Cách | Các chunk (`\n` là xuống dòng) |
|---|---|
| C1 | ① `Điều 1. Phạm vi áp dụng\nThông tư này quy định như sau:` ② `1. Khoản một rất ngắn.\n2. Khoản hai gồm các trường hợp sau:` ③ `a) trường hợp thứ nhất của khoản hai;\nb) trường hợp thứ hai` ④ `của khoản hai.` |
| C3 | ① `Điều 1.` ② `Phạm vi áp dụng\nThông tư này quy định như sau:\n1.` ③ `Khoản một rất ngắn.\n2.` ④ `Khoản hai gồm các trường hợp sau:\na) trường hợp thứ nhất của` ⑤ `khoản hai;\nb) trường hợp thứ hai của khoản hai.` |
| C4 | ① cả điều luật |
| C5 | ① `Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng\nThông tư này quy định như sau:` ② `Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng, Khoản 1: 1. Khoản một rất ngắn.` ③ `…, Khoản 2: 2. Khoản hai gồm các trường hợp sau:` ④ `…, Khoản 2, Điểm a: a) trường hợp thứ nhất của khoản hai;` ⑤ `…, Khoản 2, Điểm b: b) trường hợp thứ hai của khoản hai.` |
| C5 không tiêu đề | ① `Điều 1. Phạm vi áp dụng\nThông tư này quy định như sau:` ② `1. Khoản một rất ngắn.` ③ `2. Khoản hai gồm các trường hợp sau:` ④ `a) trường hợp thứ nhất của khoản hai;` ⑤ `b) trường hợp thứ hai của khoản hai.` |

Đọc bảng: C1 cắt ngang điểm b; C3 với hàm tách câu ngây thơ coi `1.` là hết câu nên số thứ tự khoản bị tách khỏi nội dung khoản; C5 giữ trọn từng khoản và điểm, và chunk ④ tự cho biết nó thuộc văn bản nào, điều nào, khoản nào. Nếu giới hạn là 30 token, khoản 2 không bị tách theo điểm và C5 chỉ có ba chunk (mở đầu, khoản 1, khoản 2).

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/chunking.py`: `chunk_fixed` (C1), `chunk_sentence` (C3), `chunk_document` (C4), `chunk_struct` (C5; tham số `heading=False` cho biến thể không tiêu đề), `chunk_stats` (số chunk, độ dài trung bình, trung vị, phân vị 95, lớn nhất, tính trên `text` kể cả tiêu đề), `clause_rate` (tỷ lệ điều luật có ít nhất một khoản được nhận diện). Test ở `tests/test_chunking.py` kiểm tra: chunk là lát cắt nguyên văn, không chồng lấn và phủ hết mọi ký tự khác khoảng trắng; C3 gộp câu đúng và rơi về C1 khi câu quá dài; C5 đúng số chunk, đúng tiêu đề; C5 và C5 không tiêu đề cùng ranh giới; điều luật không có khoản thì C5 không tiêu đề trùng C4.

Thử với tokenizer thật trong notebook:

```python
from transformers import AutoTokenizer
from ragvi.chunking import chunk_struct
tok = AutoTokenizer.from_pretrained('BAAI/bge-m3')
for c in chunk_struct('01/2009/tt-bnn+1', 'Điều 1. Phạm vi áp dụng', 'Thông tư này quy định như sau:\n1. ...\n2. ...', tok):
    print(c[2], c[3], c[4])
```

Thống kê cả kho Zalo: `PYTHONPATH=src python -m ragvi.chunking $P/zalo_legal --methods c1,c3,c4,c5,c5_nohead`. Lệnh này hiện chỉ cho Zalo; phân đoạn ViQuAD (C1, C3, C4) chưa có lệnh riêng.

### Lựa chọn thiết kế và lý do

- **Một tokenizer tham chiếu cho mọi cấu hình (D7).** Đề cương đếm token bằng tokenizer của từng mô hình nhúng; khi đó tập chunk đổi theo E, và hai yếu tố C và E không còn độc lập. Dùng chung tokenizer bge-m3 thì mọi mức E thấy đúng cùng một tập chunk.
- **Vì sao C4 và C5 không dùng chung ranh giới, và vì sao thêm C5 không tiêu đề.** Đề cương mục 5.2 nói cặp C4–C5 "cùng ranh giới cắt, chỉ khác phần tiêu đề". Điều này không đúng: C4 cắt theo Điều, C5 cắt theo Khoản/Điểm, nên C4 khác C5 ở *hai* chỗ (ranh giới và tiêu đề), và so sánh C4 với C5 không cô lập được tác động của tiêu đề cha. Kế hoạch 30 ngày (cấu hình 6) và D8 thêm "C5 không tiêu đề": cùng ranh giới với C5, chỉ khác tiêu đề. So C5 với C5 không tiêu đề kiểm định H1b; so C4 với C5 trả lời câu hỏi rộng hơn của RQ1 ("cắt theo cấu trúc mịn hơn có tốt hơn không").
- **C5 cho văn bản thường chưa có.** Đề cương mô tả thêm nhánh C5 cho văn bản không phải luật (không cắt giữa từ ghép); kế hoạch 30 ngày chỉ làm phần văn bản luật, nên ViQuAD chỉ có C1, C3, C4.
- **Giới hạn 256 token không tuyệt đối với C5:** kích thước được kiểm tra trên phần nội dung, tiêu đề được gắn sau, nên chunk C5 có thể dài hơn 256 token. Tiêu đề cũng được tính trong `chunk_stats`, nên độ dài C5 và C5 không tiêu đề chênh nhau đúng bằng tiêu đề.
- **Điểm còn mở:**
  - Regex khoản chỉ nhìn đầu dòng, không kiểm tra số khoản tăng dần; một danh sách đánh số nằm trong điểm có thể bị nhận nhầm là khoản. Chờ đối chiếu tay 30 điều (ngày 18/11).
  - (Đã sửa 14/11) Trước đây, khi khoản 1 nằm ngay sau dòng tiêu đề Điều, dòng `Điều N. …` không thuộc chunk nào của C5 không tiêu đề, làm so sánh C5 với C5 không tiêu đề thổi phồng tác dụng của tiêu đề cha. Nay dòng tiêu đề Điều luôn là một chunk riêng trong trường hợp đó, nên số chunk C5 tăng thêm một cho mỗi điều luật dạng này.
  - (Đã sửa 14/11) Tokenizer bge-m3 thật đôi khi sinh một token `▁` đứng riêng có vị trí trùng ký tự đầu của token sau (gặp ở chữ hoa có dấu như `Ủ`, `Ơ`), khiến hai chunk C1 liền nhau chồng nhau một ký tự. Nay điểm cuối mỗi chunk bị chặn tại điểm đầu của chunk kế tiếp.
  - `chunk_stats` token hóa lại văn bản của chunk, nên chunk C1 cắt giữa từ có thể được báo là 257 token dù ranh giới đúng 256. Chỉ lệch bảng thống kê.
  - C3 trên văn bản luật: với hàm tách câu giả ở ví dụ, số thứ tự `1.` bị tách khỏi khoản. Chưa biết `underthesea.sent_tokenize` có làm vậy không; cần xem vài điều luật thật.
  - Hai file kế hoạch nói khác nhau về điều luật không nhận diện được khoản: bảng rủi ro của `Kế hoạch 30 ngày (hạn 11-12).md` ghi "dùng chunk của C4", còn `Kế hoạch chi tiết 30 ngày.md` và mã thì dùng một chunk nếu ngắn, cắt bằng C3 nếu dài hơn 256 token.

### Câu hỏi hội đồng có thể hỏi

1. *Đóng góp của ViStructChunk là gì nếu Recall theo điều luật không đổi?* Tiêu chí Zalo tính đúng theo điều luật (mục 2), nên lợi ích chính được giả thuyết ở tầng câu trả lời: chunk tự chứa ngữ cảnh "văn bản nào, điều nào, khoản nào", giảm lỗi nhầm điều luật (H1b), đo bằng cặp C5 và C5 không tiêu đề.
2. *Vì sao không dùng tokenizer riêng của từng mô hình như đề cương?* Để yếu tố C không phụ thuộc E (D7); cái giá là với mô hình khác bge-m3, chunk 256 token tham chiếu có thể dài hơn hay ngắn hơn 256 token của chính mô hình đó.
3. *Parser sai thì sao?* Báo cáo tỷ lệ điều luật có khoản được nhận diện (`clause_rate`) và kết quả đối chiếu tay 30 điều; điều luật không có khoản vẫn được phân đoạn (một chunk hoặc C3), không bị bỏ.

---

## 7. Tập đánh giá Zalo Legal

### Nó là gì và để trả lời câu hỏi nào

Tập câu hỏi cố định dùng cho mọi cấu hình, gồm câu **trả lời được** (để đo độ đúng, ảo giác, RAH) và câu **không trả lời được** (để đo fabrication rate – tỷ lệ mô hình bịa thay vì từ chối). Phục vụ RQ1–RQ4 trên miền pháp luật. Đây là quyết định D1.

### Cách hoạt động

1. **Lấy truy vấn có nhãn:** đọc qrels (chỉ cặp có điểm dương), gom điều luật vàng theo truy vấn, bỏ các dòng truy vấn trùng mã (818 dòng còn 788 mã); truy vấn trùng mã mà khác nội dung thì báo lỗi.
2. **Nhóm theo điều luật vàng.** Hai truy vấn cùng nhóm nếu dùng chung ít nhất một điều luật vàng, trực tiếp hoặc bắc cầu. Ví dụ minh họa: q1 → {d1}, q2 → {d1, d2}, q3 → {d2}, q4 → {d9}. q1 và q3 không chung điều luật nào, nhưng cả hai chung với q2, nên {q1, q2, q3} là một nhóm và {q4} là nhóm khác. Mã dùng thuật toán union-find (hợp nhất – tìm gốc) trên đồ thị hai loại nút, truy vấn và điều luật.
3. **Chia nhóm vào các phần.** Xáo thứ tự nhóm bằng seed 0, rồi lần lượt đưa **trọn** từng nhóm vào phần đầu tiên còn đủ chỗ theo thứ tự ưu tiên: không trả lời được (120), dev (100), trả lời được (280). Nhóm không vừa phần nào vào phần dự trữ. Nếu phần nào thiếu quá 5 câu so với mục tiêu thì báo lỗi để thử seed khác.
4. **Tạo câu không trả lời được bằng cách loại điều luật:** mọi điều luật vàng của 120 câu đó bị loại khỏi kho. Mọi cấu hình dùng chung **một kho thu hẹp**. Mã kiểm tra không điều luật bị loại nào là điều luật vàng của câu ở phần khác.
5. **Đóng băng:** ghi `test.jsonl` (280 + 120), `dev.jsonl`, `removed_doc_ids.json`, và `manifest.json` chứa seed, kích thước mục tiêu và thực tế, số nhóm, số điều luật bị loại, mã băm SHA-256 từng file. Các truy vấn dư không được xuất thành tập riêng; vẫn nằm trong bộ nguồn. Thư mục đầu ra đã có dữ liệu thì từ chối ghi đè.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/data.py`: `load_zalo_queries`, `gold_groups`, `split_zalo`, `build_zalo_eval`; `load_zalo_corpus(processed_dir, exclude=...)` dựng kho thu hẹp từ danh sách điều luật bị loại. Test ở `tests/test_data.py`: `test_chain_stays_together` (đúng ví dụ bắc cầu trên), `test_split_has_no_leak_and_is_deterministic` (không phần nào chung điều luật vàng với phần khác; cùng seed cho cùng kết quả), `test_build_writes_frozen_files` (câu không trả lời được có mọi điều luật vàng trong danh sách loại, câu trả lời được thì không; từ chối ghi đè). Dữ liệu giả trong test được dựng có hình dạng giống Zalo, nhưng con số trong test không phải số liệu của Zalo.

```
PYTHONPATH=src python -m ragvi.data zalo $P/zalo_legal $O/eval_zalo --seed 0
```

### Lựa chọn thiết kế và lý do

- **Cỡ mẫu 280 + 120 thay vì 700 + 300 của đề cương:** chỉ có 788 truy vấn có nhãn; đạt 1.000 câu thì phải viết tay hơn 212 câu (D1). Hạn chế: khoảng tin cậy 95% của một tỷ lệ quanh 30% rộng khoảng ±5,4 điểm phần trăm trên 280 câu và ±8,2 trên 120 câu; nghiên cứu chỉ phát hiện được khác biệt lớn.
- **Vì sao nhóm theo điều luật vàng:** theo D1, 793 cặp qrels chỉ trỏ tới 447 điều luật khác nhau, nên nhiều truy vấn dùng chung điều luật. Nếu loại điều luật theo từng câu riêng lẻ, câu khác dùng chung điều luật đó cũng thành không trả lời được ngoài ý muốn; nếu tách dev/test theo câu, điều luật vàng rò rỉ giữa hai tập.
- **Chỉ loại điều luật, không viết tay câu ngoài kho** (lệch đề cương, theo kế hoạch 30 ngày). Hạn chế: câu không trả lời được là nhân tạo, câu hỏi thật nhưng kho bị bỏ bớt; và kho có thể còn văn bản khác chứa cùng nội dung (nghị định sửa đổi, thông tư hướng dẫn). D6 kiểm tra bằng cách đọc tay 30 câu với 5 kết quả đầu của hybrid; nếu trên 20% vẫn trả lời được thì thay câu bằng phần dự trữ trước khi đóng băng. Việc đọc tay **chưa làm**.
- Thứ tự ưu tiên "không trả lời được" trước giúp phần khó lấp đầy nhất được chọn trước. Trường `group` được lưu cho từng câu để bootstrap theo cụm (nhóm điều luật) ở Tuần 4.

### Câu hỏi hội đồng có thể hỏi

1. *Câu không trả lời được do loại điều luật có thật sự không trả lời được?* Không chắc chắn; đó là lý do có D6 (đọc tay 30 câu, ngưỡng 20%) và phải báo cáo tỷ lệ.
2. *Vì sao không lấy mẫu ngẫu nhiên theo câu?* Vì rò rỉ điều luật vàng giữa dev và test, và vì loại điều luật của một câu có thể làm hỏng câu khác.
3. *Kết quả có tái lập được không?* Có: seed cố định, cách chia tất định, mã băm SHA-256 từng file, và mã từ chối ghi đè tập đã đóng băng.

---

## 8. Tập đánh giá ViQuAD

### Nó là gì và để trả lời câu hỏi nào

Tập câu hỏi miền bách khoa (Wikipedia), cùng cỡ với Zalo (280 + 120, dev 100), để so sánh hai miền ở RQ4 (H4: RAH cao hơn ở văn bản luật). ViQuAD 2.0 có sẵn câu `is_impossible` do người viết đối kháng, nên không cần tạo câu không trả lời được.

### Cách hoạt động

1. **Kho:** mọi đoạn `context` duy nhất của cả ba split, kể cả split test (không có đáp án nhưng vẫn là đoạn nhiễu). Mã tài liệu là 16 ký tự hex đầu của SHA-256 nội dung đoạn, nên cùng một đoạn luôn có cùng mã dù xuất hiện ở split nào.
2. **Câu hỏi dùng được:** chỉ từ train và validation (split test không có đáp án). Mã câu hỏi là `split:id` vì `id` lặp lại giữa các split. Với câu trả lời được, vị trí đáp án được định vị lại: nếu `answer_start` lệch (ví dụ do bước làm sạch gộp khoảng trắng), lấy lần xuất hiện của chuỗi đáp án gần vị trí cũ nhất; đáp án không còn trong đoạn thì bỏ, và câu không còn đáp án nào thì bị loại.
3. **Tách theo `title`:** chọn ngẫu nhiên các bài (title) cho dev tới khi đủ 100 câu; tập test lấy 280 câu trả lời được và 120 câu `is_impossible` từ các bài còn lại. Mỗi đoạn có tối đa một câu hỏi, và đoạn đã thuộc bài của dev thì không vào test, kể cả khi nó xuất hiện dưới bài khác.
4. **Đóng băng:** `test.jsonl`, `dev.jsonl`, `corpus.jsonl`, `manifest.json` (seed, kích thước, số câu dùng được so với số dòng có nhãn, số đoạn trong kho, SHA-256). Không đủ đúng số câu thì báo lỗi; từ chối ghi đè.

### Nằm ở đâu trong mã và cách tự kiểm tra

`src/ragvi/data.py`: `load_viquad`, `passage_id`, `viquad_corpus`, `locate_answers`, `viquad_questions`, `split_viquad`, `build_viquad_eval`. Test: `test_locate_answers_fixes_shifted_start`, `test_viquad_split_sizes_no_leak_one_per_passage` (đúng cỡ, không chung title giữa dev và test, mỗi đoạn một câu, vị trí đáp án khớp chuỗi), `test_build_viquad_writes_frozen_files` (kho gồm cả đoạn của split test; chạy hai lần cho cùng mã băm).

```
PYTHONPATH=src python -m ragvi.data viquad $P/viquad $O/eval_viquad --seed 0
```

Sau khi chạy, xem `labeled_rows − usable_questions` trong manifest để biết bao nhiêu câu bị loại vì mất đáp án sau làm sạch.

### Lựa chọn thiết kế và lý do

- **Tách theo title** để dev và test không chung bài, tránh chỉnh prompt hay judge trên chính chủ đề sẽ kiểm tra. **Mỗi đoạn một câu** để các câu trong test gần độc lập; khoảng tin cậy bootstrap vẫn lấy mẫu theo cụm title.
- **Không thêm 20.000 đoạn nhiễu Wikipedia** như đề cương (lệch theo kế hoạch 30 ngày). Hạn chế: kho nhỏ nên truy xuất ViQuAD dễ hơn thực tế.
- **Lệch so với D1 và chưa xử lý:** dev ViQuAD đang trộn cả câu trả lời được và `is_impossible` (dev Zalo thì toàn câu trả lời được), và chưa có phần dự trữ để thay câu theo D6.
- **"Không trả lời được" ở hai bộ mang nghĩa khác nhau.** Ở Zalo, điều luật vàng bị loại khỏi kho; ở ViQuAD, đoạn gốc vẫn ở trong kho nhưng không chứa đáp án (câu được viết đối kháng với đoạn đó), và đoạn khác trong kho vẫn có thể chứa đáp án (lý do D6 áp dụng cho cả ViQuAD). So sánh fabrication rate giữa hai miền cần nêu khác biệt này.

### Câu hỏi hội đồng có thể hỏi

1. *Vì sao không dùng split test của ViQuAD?* Nó không có đáp án (`answers` rỗng ở mọi dòng), nên chỉ dùng làm đoạn nhiễu trong kho.
2. *Mô hình sinh có thể đã thấy Wikipedia lúc huấn luyện?* Có; đó là lý do có điều kiện closed-book (mục 9), và đề cương liệt kê rủi ro này là "cao với ViQuAD".
3. *Bỏ câu mất đáp án có gây thiên lệch không?* Có thể nếu tỷ lệ lớn; manifest ghi số câu bị bỏ để báo cáo.

---

## 9. Closed-book, oracle và RAH (chưa cài đặt)

Đây là phần Tuần 2 trở đi; ghi ngắn để hiểu vì sao Tuần 1 phải chuẩn bị dữ liệu như trên.

**Câu hỏi RQ4:** bao nhiêu phần ảo giác là do tầng truy xuất và có thể sửa bằng lựa chọn C/E/R? Một tỷ lệ ảo giác đơn lẻ không trả lời được, vì ảo giác có thể đến từ truy xuất sai *hoặc* từ mô hình sinh bóp méo ngữ cảnh đúng. Vì vậy chạy thêm hai điều kiện tham chiếu trên **cùng tập câu hỏi** với mọi cấu hình:

- **Closed-book:** không đưa ngữ cảnh; đo mô hình sinh tự trả lời bằng tri thức nền (trần tham chiếu, và cho ViQuAD là thước đo rò rỉ dữ liệu huấn luyện).
- **Oracle:** chỉ đưa bằng chứng vàng (đoạn vàng của ViQuAD, điều luật vàng của Zalo cắt ở 4.000 token tham chiếu); đo phần ảo giác còn lại khi truy xuất hoàn hảo (sàn).
- **RAH(k) = H_gold(k) − H_gold(oracle)**, chỉ trên câu trả lời được (D5), trong đó H_gold là tỷ lệ câu trả lời có ít nhất một mệnh đề không được bằng chứng vàng hỗ trợ (D3–D4). Ví dụ minh họa: nếu cấu hình k có H_gold = 30% và oracle có 12% thì RAH = 18 điểm phần trăm, và 18/30 = 60% ảo giác của k quy cho truy xuất. Tỷ lệ này chỉ báo cáo khi H_gold(k) ≥ 10%.

Lý do chỉ tính trên câu trả lời được: câu Zalo không trả lời được không còn điều luật vàng trong kho, nên oracle không xác định. Câu không trả lời được chỉ báo cáo fabrication rate, đo bằng quy tắc nhận diện câu từ chối, không cần judge. Hạn chế: RAH có thể âm; luôn kèm khoảng tin cậy của hiệu số ghép cặp; chỉ diễn giải nhân quả với giả định oracle chỉ khác cấu hình ở ngữ cảnh.

Hội đồng có thể hỏi: *vì sao dùng H_gold thay vì faithfulness với ngữ cảnh như đề cương?* Faithfulness so với ngữ cảnh không xác định ở closed-book (không có ngữ cảnh), và không bắt được trường hợp truy xuất sai mà mô hình bám đúng ngữ cảnh sai, đúng loại lỗi RAH muốn quy cho truy xuất (D4). H_ctx vẫn được báo cáo làm chỉ số phụ.

---

## Bảng thuật ngữ Việt – Anh

| Tiếng Việt | Tiếng Anh | Nghĩa trong đề tài |
|---|---|---|
| Tạo sinh tăng cường truy xuất | Retrieval-augmented generation (RAG) | Truy xuất đoạn văn rồi đưa vào prompt để LLM trả lời |
| Ảo giác | Hallucination | Câu trả lời có mệnh đề không được bằng chứng hỗ trợ |
| Phân đoạn | Chunking | Cắt tài liệu thành mảnh (chunk) để nhúng và truy xuất |
| Mô hình nhúng | Embedding model | Biến văn bản thành vector số |
| Truy xuất dày | Dense retrieval | Truy xuất bằng độ tương tự vector |
| Truy xuất từ vựng | Lexical / sparse retrieval | Truy xuất bằng khớp từ (BM25) |
| Truy xuất lai | Hybrid retrieval | Kết hợp điểm BM25 và dense |
| Xếp hạng lại | Reranking | Chấm lại top-20 bằng cross-encoder, giữ top-5 |
| Tài liệu vàng, đoạn vàng | Gold document / passage | Tài liệu được gán nhãn là đúng cho câu hỏi |
| Nhãn liên quan | Qrels (query relevance judgments) | Cặp câu hỏi – tài liệu liên quan của Zalo |
| Độ phủ tại k | Recall@k | Tỷ lệ tài liệu vàng có trong k kết quả đầu |
| Nghịch đảo thứ hạng trung bình | Mean reciprocal rank (MRR) | 1/vị trí của kết quả đúng đầu tiên |
| Lợi ích tích lũy có chiết khấu chuẩn hóa | nDCG | Chỉ số xếp hạng thưởng cho kết quả đúng đứng đầu |
| Tần suất nghịch đảo tài liệu | Inverse document frequency (IDF) | Term càng hiếm càng có trọng số cao |
| Tách từ / tách âm tiết | Word segmentation / syllable tokenization | Cách chia văn bản tiếng Việt thành term |
| Tokenizer tham chiếu | Reference tokenizer | Tokenizer `BAAI/bge-m3` dùng đếm token cho mọi cấu hình |
| Chuẩn hóa min–max | Min–max normalization | Đưa điểm về [0, 1] |
| Độ tương tự cosine | Cosine similarity | Góc giữa hai vector; bằng tích vô hướng khi vector đã chuẩn hóa |
| Câu không trả lời được | Unanswerable question | Kho không chứa thông tin để trả lời |
| Tỷ lệ bịa đặt | Fabrication rate | Tỷ lệ câu không trả lời được mà mô hình không từ chối |
| Tỷ lệ từ chối sai | False refusal rate | Tỷ lệ câu trả lời được mà mô hình từ chối |
| Không ngữ cảnh | Closed-book | Điều kiện không đưa đoạn nào vào prompt |
| Ngữ cảnh lý tưởng | Oracle | Điều kiện chỉ đưa bằng chứng vàng |
| Ảo giác quy cho truy xuất | Retrieval-attributable hallucination (RAH) | H_gold(k) − H_gold(oracle) |
| Mô hình chấm | LLM-as-judge | LLM khác mô hình sinh, chấm độ đúng và ảo giác |
| Tập phát triển | Dev set | Tập dùng chỉnh prompt, judge, chọn mô hình sinh |
| Đóng băng | Freeze | Cố định tập dữ liệu/cấu hình, lưu mã băm, không sửa sau đó |
| Thay từng yếu tố một | One-factor-at-a-time (OFAT) | Đổi một yếu tố so với cấu hình neo |
| Cấu hình neo | Anchor configuration | C3–E3–R0 |
| Hợp nhất – tìm gốc | Union-find | Thuật toán gom thành phần liên thông, dùng để nhóm truy vấn |
| Bootstrap theo cụm | Cluster bootstrap | Lấy mẫu lại theo nhóm (title hoặc nhóm điều luật) khi tính khoảng tin cậy |

---

## Chạy Colab không mở notebook và đọc EDA

- **`colab_run.sh` (máy người dùng):** gọi Google Colab CLI bằng `uvx`, thử GPU kế tiếp khi backend từ chối hoặc endpoint cấp máy trả 502/503/504. Dùng tiền tố `content/` ở đường dẫn CLI để khớp `/content` trong kernel. Chỉ tải đầu vào cần thiết; lấy kết quả và dừng runtime kể cả khi job lỗi. Không dùng WSL.
- **`scripts/colab_job.sh` (Colab):** khóa gói Python bằng `uv.lock`; dùng BGE-M3 cho truy xuất và llama.cpp CUDA cho sinh văn bản. Máy người dùng không tải trọng số GGUF. Bộ sinh llama.cpp dùng cùng prompt qua `--llama-url`, nhưng lượng tử hóa/giới hạn ngữ cảnh không tương đương với Transformers/NF4. Pilot 10 câu chỉ kiểm tra triển khai, không đo `H_gold`.
- **`ragvi.benchmark`:** tạo đầu vào truy xuất từ toàn bộ split nguồn, tách test ViQuAD không nhãn khỏi phép tính Recall/MRR/nDCG; đối chiếu SHA-256 tập đóng băng và không ghi đè. Sinh cả dev/test với neo, closed-book và oracle; oracle chỉ có câu trả lời được. `unsloth/Qwen3.5-9B-GGUF:Q4_K_M` chạy qua `llama-server` với continuous batching (`--parallel` + `--cont-batching` + `ThreadPoolExecutor`), kế thừa giới hạn 3.000 ký tự cho mỗi phần ngữ cảnh/bằng chứng vàng của judge. `summary.json` tách lỗi JSON, câu từ chối, mẫu số từng chỉ số, và RAH ghép cặp; đây là điểm Judge sơ bộ trước khi đối chiếu nhãn người.
- **`notebooks/06_eda_du_lieu.ipynb`:** xác minh cấu trúc Arrow/JSONL và tách dev/test; đếm BGE-M3 không cắt. Zalo có 10.719/61.425 điều dài hơn 512 token, so với 41/5.311 đoạn ViQuAD. Đây là lý do nên xem lỗi truy xuất theo độ dài và thử phân đoạn theo Khoản/Điểm; chưa chứng minh ảo giác giảm. Cụm câu chữ Zalo lớn nhất có 8 câu về xe máy và tai nạn; thay động từ *đỗ/chuyển hướng/tránh* có thể đổi điều khoản cần tìm. Cụm chữ là gợi ý đọc lỗi, không phải nhãn ngữ nghĩa. Dev ViQuAD chỉ có 3 bài, test có 118 bài.
- **Cách đọc điểm:** so `H_gold` và độ đúng trên cùng bộ câu trả lời được, theo dõi fabrication và false refusal để không nhầm từ chối nhiều với cải thiện. Khi Recall@20 khá mà Recall@5 còn thấp, ưu tiên xem reranking; nếu cả hai thấp, xem phân đoạn và retriever. Đo RAH so oracle sau khi đối chiếu judge với nhãn người.

## Kết quả

Số liệu dưới đây lấy từ output của `notebooks/02_tuan1_truy_xuat_phan_doan.ipynb`, chạy trên Colab ngày 14/11/2026 (mã chưa commit; file kết quả ở `results/tuan1/` và `data/eval/` trên Drive). Ô trống là chưa đo. Mỗi bảng ứng với mục tiêu cuối ngày trong `Kế hoạch chi tiết 30 ngày.md`. Ghi kèm ngày chạy, commit của mã và đường dẫn file kết quả trên Drive.

### 13/11 – BM25 trên 788 truy vấn Zalo, chọn cách tách từ

Đo tốc độ tách từ (`--time-tokenizer`):

| Số điều luật mẫu | Thời gian mẫu (giây) | Điều luật/giây | Ước lượng cả kho (phút) | Dùng underthesea (< 30 phút)? |
|---|---|---|---|---|
| 500 | 9,02 | 55,5 | 19,2 | Có |

Ước lượng ngoại suy theo số ký tự, cho một lượt tách cả kho ở mức điều luật trên CPU Colab.

BM25 mức điều luật:

| Cách tách | n | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---|---|
| Âm tiết (`bm25`) | 788 | 0,7005 | 0,8433 | 0,5160 | 0,5529 |
| Tách từ (`bm25[word]`, underthesea) | 788 | 0,7367 | 0,8909 | 0,5489 | 0,5855 |

Kho đầy đủ 61.425 điều luật, toàn bộ 788 truy vấn có nhãn (chưa phải tập test đã đóng băng).

Quyết định đã chọn và lý do: theo quy tắc ghi trước (dưới 30 phút thì dùng underthesea), E0 dùng BM25 tách từ bằng underthesea (ước lượng 19,2 phút). Trên kho Zalo đầy đủ, tách từ cao hơn tách âm tiết ở cả bốn chỉ số (+3,62 điểm phần trăm Recall@5 và +3,26 điểm phần trăm nDCG@5).

### 14/11 – BM25, dense, hybrid trên Zalo (mức điều luật) và tập test hai bộ

**Zalo, kho đầy đủ (61.425 điều luật, 788 truy vấn):**

| Phương pháp | n | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---|---|
| BM25 (âm tiết) | 788 | 0,7005 | 0,8433 | 0,5160 | 0,5529 |
| BM25 (tách từ, `bm25[word]`) | 788 | 0,7367 | 0,8909 | 0,5489 | 0,5855 |
| Dense (`BAAI/bge-m3`) | 788 | 0,8147 | 0,9226 | 0,6525 | 0,6847 |
| Hybrid (BM25 âm tiết, α = 0,7) | 788 | 0,8763 | 0,9581 | 0,6986 | 0,7376 |
| Hybrid (BM25 tách từ, `hybrid[word]`, α = 0,7) | 788 | 0,8839 | 0,9657 | 0,7000 | 0,7409 |

**Zalo, tập test đã đóng băng với kho thu hẹp (61.336 điều luật, 280 câu trả lời được / 400 câu test):**

| Phương pháp | n | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---|---|
| BM25 (âm tiết) | 280 | 0,6786 | 0,8321 | 0,5304 | 0,5604 |
| BM25 (tách từ, `bm25[word]`) | 280 | 0,7393 | 0,8804 | 0,5779 | 0,6096 |
| Dense (`BAAI/bge-m3`) | 280 | 0,7982 | 0,9268 | 0,6420 | 0,6697 |
| Hybrid (BM25 âm tiết, α = 0,7) | 280 | 0,8536 | 0,9518 | 0,6896 | 0,7236 |
| Hybrid (BM25 tách từ, `hybrid[word]`, α = 0,7) | 280 | 0,8768 | 0,9625 | 0,7147 | 0,7490 |

**ViQuAD, tập test ở mức đoạn (5.311 đoạn, 280 câu trả lời được / 400 câu test):**

| Phương pháp | n | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---|---|---|---|---|
| BM25 (âm tiết) | 280 | 0,8107 | 0,9071 | 0,7060 | 0,7275 |
| BM25 (tách từ, `bm25[word]`) | 280 | 0,7929 | 0,8643 | 0,7072 | 0,7253 |
| Dense (`BAAI/bge-m3`) | 280 | 0,8643 | 0,9536 | 0,7555 | 0,7780 |
| Hybrid (BM25 âm tiết, α = 0,7) | 280 | 0,9179 | 0,9643 | 0,8347 | 0,8526 |
| Hybrid (BM25 tách từ, `hybrid[word]`, α = 0,7) | 280 | 0,9250 | 0,9643 | 0,8394 | 0,8586 |

| Tốc độ nhúng (`BAAI/bge-m3`) | Số văn bản | Thời gian (giây) | Văn bản/giây | GPU | Tỷ lệ văn bản bị cắt ở 512 token |
|---|---|---|---|---|---|
| Kho Zalo | 61.425 | 3.288,8 | 18,7 | Colab GPU | 17,45% |
| Truy vấn Zalo (đầy đủ) | 788 | 4,4 | 180,2 | Colab GPU | – |
| Truy vấn Zalo (test) | 400 | 2,7 | 145,5 | T4 | – |
| Kho ViQuAD (C4, đoạn) | 5.311 | 254,1 | 20,9 | T4 | 0,77% |
| Truy vấn ViQuAD (test) | 400 | 2,0 | 196,1 | T4 | – |

*(Tách từ `underthesea` trên 5.311 đoạn ViQuAD mất 53,8 giây.)*

Công thức hybrid: xem mục 5 và Nhật ký thay đổi trong `reports/quyet-dinh-thiet-ke.md` (chốt 14/11).

### 15/11 – C1, C3, C4 trên hai kho

Số liệu lấy từ output của `notebooks/03_tuan1_hoan_tat.ipynb` (cell 12 và 13).

| Kho | Cách | Số tài liệu | Số chunk | Token trung bình | Trung vị | p95 | Lớn nhất | Tỷ lệ >512 token |
|---|---|---|---|---|---|---|---|---|
| Zalo | C1 | 61.425 | 113.962 | 185,0 | 231,0 | 256 | 258 | 0,00% |
| Zalo | C3 | 61.425 | 128.733 | 163,7 | 179,0 | 256 | 257 | 0,00% |
| Zalo | C4 | 61.425 | 61.425 | 343,1 | 223,0 | 946 | 67.395 | 17,45% |
| ViQuAD | C1 | 5.311 | 6.481 | 175,3 | 179,0 | 256 | 257 | 0,00% |
| ViQuAD | C3 | 5.311 | 6.504 | 174,7 | 179,5 | 249 | 256 | 0,00% |
| ViQuAD | C4 | 5.311 | 5.311 | 213,9 | 191,0 | 370 | 2.091 | 0,77% |

### 16/11 – Tập đánh giá Zalo

| Phần | Mục tiêu | Thực tế | Số nhóm | Số điều luật vàng |
|---|---|---|---|---|
| Không trả lời được (test) | 120 | 120 | chưa in | chưa in |
| Trả lời được (test) | 280 | 280 | chưa in | chưa in |
| Dev | 100 | 100 | chưa in | chưa in |
| Dự trữ | – | 288 | chưa in | chưa in |

| Seed | Số truy vấn có nhãn | Tổng số nhóm | Số điều luật bị loại | SHA-256 `test.jsonl` | SHA-256 `removed_doc_ids.json` |
|---|---|---|---|---|---|
| 0 | 788 | 442 | 89 | `f0d241c4…50885202f` | `c4ff6c30…95068673` |

Mã băm đầy đủ nằm trong `data/eval/zalo/manifest.json` trên Drive.

### 17/11 – Tập đánh giá ViQuAD và kiểm tra tay D6

| Phần | Mục tiêu | Thực tế | Số câu trả lời được | Số title |
|---|---|---|---|---|
| Không trả lời được (test) | 120 | 120 | 0 | 74 |
| Trả lời được (test) | 280 | 280 | 280 | 103 |
| Dev | 100 | 100 | 77 | 3 |

Lưu ý: 100 câu dev chỉ đến từ 3 bài Wikipedia, nên dev hẹp về chủ đề.

| Seed | Số dòng có nhãn | Số câu dùng được | Số câu bị bỏ do mất đáp án | Số đoạn trong kho | SHA-256 `test.jsonl` |
|---|---|---|---|---|---|
| 0 | 32.268 | 32.268 | 0 | 5.311 | `60d10838…cd15b14a` |

Kiểm tra tay câu không trả lời được (D6):

| Bộ | Số câu đã đọc | Số câu vẫn trả lời được từ top-5 `hybrid[word]` | Tỷ lệ | Vượt 20%? | Xử lý |
|---|---|---|---|---|---|
| Zalo | 30 | 8 (2 câu do bản trùng mã `24/2020/nd-cp` vs `nđ-cp`; 6 câu do văn bản khác trong kho chứa cùng quy định) | 26,7% (còn **20,0%** sau khi loại bản trùng `nd-cp` ↔ `nđ-cp`) | Không sau khi loại bản trùng (`6/30 = 20,0% ≤ 20%`) | Loại bản trùng `nd-cp` ↔ `nđ-cp` trong kho thu hẹp (`expand_zalo_doc_ids`), đóng băng tập test Zalo |
| ViQuAD | 30 | 2 (`validation:0004-0047-0008`, `train:0106-0047-0008`) | 6,7% | Không | Giữ nguyên, đóng băng tập test ViQuAD |

### 18/11 – C5 và C5 không tiêu đề trên Zalo

| Cách | Số chunk | Token trung bình | Trung vị | p95 | Lớn nhất | Tỷ lệ >512 token |
|---|---|---|---|---|---|---|
| C5 | 326.759 | 91,7 | 77,0 | 222 | 717 | 0,00% |
| C5 không tiêu đề | 326.759 | 64,5 | 47,0 | 188 | 257 | 0,00% |

Chẩn đoán tiêu đề cha C5 trên 61.425 điều luật (cell 13 của `03_tuan1_hoan_tat.ipynb`): trung vị 23,0 token, p95 43 token, max 460 token (`24/2019/tt-bgdđt+2`, do dữ liệu gốc đặt toàn bộ nội dung điều luật vào trường `title`).

| Tỷ lệ điều luật có ít nhất một khoản | Số điều đối chiếu tay | Số điều parse đúng | Loại lỗi gặp (khoản nhận nhầm, bỏ sót điểm, …) |
|---|---|---|---|
| 84,7% | 30 (`reports/phieu/c5_review.md`) | 30 (100%) | Không (0 khoản nhận nhầm, 0 bỏ sót khoản/điểm) |

| Ước lượng thời gian nhúng | C1 | C3 | C4 | C5 | C5 không tiêu đề |
|---|---|---|---|---|---|
| Zalo, `BAAI/bge-m3` (phút, ước lượng từ ~18,7–20,9 văn bản/giây trên T4) | ~91–102 | ~103–115 | 54,8 (đã nhúng) | ~260–290 | ~260–290 |

*(Với `bf16` + `batch_size=256` trên L4 và checkpoint mỗi 20.000 chunk, thời gian nhúng C3 Zalo thực tế giảm xuống **8,5 phút** = `251,8 chunk/giây`.)*

### 20–21/11 – Baseline đầu-cuối (`C3–E3–R0`, `closed_book`, `oracle`) với `Qwen3.5-9B` (`llama.cpp` continuous batching)

Chi tiết đầy đủ xem tại `reports/benchmark-colab-2026-11-20.md`. Tóm tắt các chỉ số chính trên tập kiểm tra đóng băng (`viquad_test` và `zalo_test`, mỗi bộ 400 câu = 280 trả lời được + 120 không trả lời được, mô hình sinh và judge `unsloth/Qwen3.5-9B-GGUF:Q4_K_M`, `n_judge_errors = 0` trên toàn bộ 2.211 lượt chấm):

| Tập | Cấu hình | Recall@5 / @20 | `correct_refusal` | `fabrication` | `false_refusal` | `contains_gold` | `F1` | `correctness` (0–2) | `H_gold` (`n`) | `H_ctx` (`n`) | `RAH` vs `oracle` |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `viquad_test` | `closed_book` | — | 88,33% | 11,67% | 75,00% | 3,93% | 0,0642 | 0,1964 | 77,14% (70) | — | — |
| `viquad_test` | `oracle` | — | — | — | 12,50% | 57,14% | 0,4326 | 1,7000 | 10,20% (245) | 1,22% (245) | — |
| `viquad_test` | `C3-E3-R0` | 88,93% / 95,71% | 64,17% | 35,83% | 15,71% | 52,14% | 0,3982 | 1,5643 | 19,07% (236) | 2,54% (236) | **+6,76%** (222 cặp) |
| `zalo_test` | `closed_book` | — | 57,50% | 42,50% | 55,71% | — | — | 0,1000 | 92,74% (124) | — | — |
| `zalo_test` | `oracle` | — | — | — | 14,29% | — | — | 1,1607 | 31,67% (240) | 31,67% (240) | — |
| `zalo_test` | `C3-E3-R0` | 81,43% / 92,68% | 56,67% | 43,33% | 27,50% | — | — | 1,0679 | 34,48% (203) | 10,34% (203) | **+6,35%** (189 cặp) |
