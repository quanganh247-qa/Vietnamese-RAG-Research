# Kế hoạch chi tiết 30 ngày (12/11–11/12/2026)

Chi tiết hóa `Kế hoạch 30 ngày (hạn 11-12).md`. Mỗi ngày có một dòng **Mục tiêu cuối ngày** nêu kết quả phải có khi kết thúc ngày đó; nếu chưa đạt thì chưa sang việc của ngày sau. Mỗi ngày khoảng 2 giờ; các lượt chạy GPU dài để chạy nền ngoài 2 giờ này. Việc nặng được xếp vào cuối tuần (14–15/11, 21–22/11, 28–29/11, 05–06/12) để có thể thêm giờ nếu cần.

Lý do của các quyết định D1–D9 nằm trong `Kế hoạch chi tiết từng ngày.md` (bản 14 ngày cũ); mã pilot BM25, dense, hybrid và bootstrap cũng ở đó (ngày 7–9) và được dùng lại nguyên. Các đoạn mã trong file này chưa được chạy thử, vì dữ liệu chỉ có trên Google Drive.

## Quy ước chung

**Gói mã** `src/ragvi/`, mỗi yếu tố một file: `data.py`, `chunking.py`, `retrieval.py`, `rerank.py`, `generate.py`, `judge.py`, `metrics.py`, `run.py`, cộng `app.py` cho demo (thêm ngày 27/11). Notebook Colab chỉ gọi gói này.

**Đưa mã lên Colab:** máy này không đồng bộ với Drive. Đề xuất đẩy lên một kho GitHub riêng tư và `git clone` trong Colab; dữ liệu vẫn ở Drive.

**Bản ghi chunk:** mọi hàm phân đoạn trả về danh sách `(chunk_id, doc_id, start, end, text)`, với `start`/`end` là vị trí ký tự trong tài liệu gốc. Nhờ đó việc xác định chunk đúng không phụ thuộc cách phân đoạn.

**Tiêu chí chunk đúng:**

- Zalo: `doc_id` của chunk nằm trong qrels. Mỗi điều luật vàng chỉ được tính một lần, ở lần xuất hiện đầu tiên trong danh sách xếp hạng.
- ViQuAD: chunk thuộc đúng đoạn gốc và phủ ít nhất 80% số ký tự của đáp án vàng.

**Bảng kết quả:** một dòng cho mỗi cặp (cấu hình, câu hỏi), ghi nối tiếp vào file JSONL ngay khi có kết quả. Lượt chạy bị ngắt thì chạy lại sẽ bỏ qua các dòng đã có.

**Giới hạn độ dài:** mô hình nhúng cắt ở 512 token. Mỗi đoạn đưa vào prompt cắt ở 1.024 token tham chiếu; điều luật vàng ở điều kiện oracle cắt ở 4.000 token. Báo cáo tỷ lệ bị cắt ở mỗi chỗ.

---

## Tuần 1 – Thiết kế, dữ liệu, truy xuất

### Ngày 1 – Thứ Năm 12/11: Khởi động

**Mục tiêu cuối ngày:** dữ liệu đã xử lý nằm trên Drive; chín quyết định D1–D9 được ghi thành văn bản; người hướng dẫn đã nhận ba câu hỏi về thứ phải nộp, phạm vi và hình thức nộp sản phẩm.

- **0–15'** Gửi người hướng dẫn ba câu hỏi: thứ phải nộp trước 12/12 là gì và nộp ở đâu; phạm vi thu hẹp có được chấp nhận không; sản phẩm nộp theo hình thức nào (demo trực tiếp, video, hay chỉ báo cáo và mã nguồn). Đính kèm bảng phạm vi.
- **15–55'** Chạy `01_dataset_exploration.ipynb` trên Colab, xác nhận `PASS`, chạy cell lưu ở mục 8.
- **55–105'** Tạo `reports/quyet-dinh-thiet-ke.md`, ghi chín quyết định theo bảng dưới.
- **105–120'** Tạo kho GitHub riêng tư; `git init`; commit đầu tiên.

| # | Quyết định cho kế hoạch 30 ngày |
|---|---|
| D1 | Zalo: 280 câu trả lời được + 120 không trả lời được (test), 100 câu dev; lấy mẫu theo nhóm điều luật vàng |
| D2 | Tiêu chí chunk đúng như phần quy ước; độ đúng trên Zalo do judge chấm so với điều luật vàng, không dùng EM/F1 |
| D3–D4 | Hai đại lượng: H_ctx (so với ngữ cảnh đã cung cấp) và H_gold (so với bằng chứng vàng); H_gold là chỉ số chính |
| D5 | RAH = H_gold(cấu hình) − H_gold(oracle), chỉ trên câu trả lời được; câu không trả lời được chỉ báo cáo fabrication rate |
| D6 | Đọc tay 30 câu không trả lời được mỗi bộ; báo cáo tỷ lệ vẫn trả lời được từ kho |
| D7 | Ranh giới chunk đặt theo tokenizer của `BAAI/bge-m3` cho mọi cấu hình |
| D8 | Cấu hình Giai đoạn B cố định trước; tập dev chỉ dùng để chỉnh prompt và judge |
| D9 | (9 + 7) × 400 = 6.400 lượt sinh |

**Xong khi:** bốn thư mục processed đọc được bằng `load_from_disk` trong một runtime mới; file quyết định có đủ chín dòng.

### Ngày 2 – Thứ Sáu 13/11: Khung mã và BM25

**Mục tiêu cuối ngày:** có bốn chỉ số truy xuất (Recall@5, Recall@20, MRR@10, nDCG@5) của BM25 trên 788 truy vấn Zalo, tính bằng gói mã mới; đã chọn cách tách từ cho BM25.

- **0–30'** Tạo gói `src/ragvi/`; `data.py` nạp Zalo (ghép `title` và `text`, bỏ 30 dòng truy vấn trùng) và ViQuAD.
- **30–60'** `metrics.py` (mã dưới), kèm hai `assert`.
- **60–90'** `retrieval.py`: BM25 theo âm tiết, mỗi điều luật một tài liệu; chạy trên 788 truy vấn.
- **90–120'** Đo tốc độ `underthesea.word_tokenize` trên 500 điều luật và ước lượng cho cả kho.

```python
import math

def metrics(hits, n_rel):
    """hits: danh sách True/False theo thứ hạng, mỗi tài liệu vàng chỉ True một lần."""
    dcg = sum(h / math.log2(i + 2) for i, h in enumerate(hits[:5]))
    idcg = sum(1 / math.log2(i + 2) for i in range(min(n_rel, 5)))
    return {'r5': sum(hits[:5]) / n_rel, 'r20': sum(hits[:20]) / n_rel,
            'mrr10': next((1 / (i + 1) for i, h in enumerate(hits[:10]) if h), 0.0),
            'ndcg5': dcg / idcg}

def zalo_hits(ranked_doc_ids, gold):
    seen, hits = set(), []
    for d in ranked_doc_ids:
        hits.append(d in gold and d not in seen)
        seen.add(d)
    return hits

assert metrics([True, False], 1) == {'r5': 1, 'r20': 1, 'mrr10': 1, 'ndcg5': 1}
assert zalo_hits(['a', 'a', 'b'], {'a'}) == [True, False, False]   # hai chunk cùng điều luật chỉ tính một lần
```

**Quy tắc chọn cách tách từ cho BM25:** nếu tách từ cả kho mất dưới 30 phút thì E0 dùng underthesea như đề cương, tách lại cho từng cách phân đoạn và lưu đệm. Nếu lâu hơn thì E0 dùng âm tiết cho mọi cấu hình, và BM25 tách từ chỉ báo cáo ở mức điều luật như một so sánh phụ; ghi rõ đây là khác biệt so với đề cương.

**Xong khi:** có bốn chỉ số BM25 trên 788 truy vấn; đã chọn cách tách từ.

### Ngày 3 – Thứ Bảy 14/11: Dense và hybrid

**Mục tiêu cuối ngày:** có bảng so sánh BM25, dense và hybrid trên Zalo ở mức điều luật; biết tốc độ nhúng (tài liệu mỗi giây).

- **0–15'** Mở bài của Nguyen & Quan (EACL 2026), ghi lại công thức hybrid: α nhân với thành phần nào và điểm được chuẩn hóa thế nào.
- **15–75'** Nhúng kho Zalo ở mức điều luật bằng `BAAI/bge-m3`; lưu đệm theo khóa (bộ dữ liệu, cách phân đoạn, mô hình). Ghi số tài liệu mỗi giây.
- **75–105'** Hybrid: với từng truy vấn, chuẩn hóa min–max vector điểm BM25 và dense trên cả kho, cộng theo α = 0,7, lấy 20 kết quả đầu. Xử lý từng truy vấn một để không phải giữ cả ma trận điểm trong bộ nhớ.
- **105–120'** Bảng ba dòng (BM25, dense, hybrid) trên 788 truy vấn; commit.

**Xong khi:** có bảng ba dòng; biết thông lượng nhúng để ước lượng ngày 10.

**Nếu trễ:** hybrid chuyển sang ngày 4.

### Ngày 4 – Chủ nhật 15/11: Phân đoạn C1, C3, C4

**Mục tiêu cuối ngày:** ba cách phân đoạn C1, C3, C4 sinh được chunk cho cả hai kho; có bảng số chunk và độ dài chunk.

- **0–40'** C1: 256 token, không chồng lấn, dùng vị trí ký tự do tokenizer trả về (mã dưới).
- **40–85'** C3: tách câu bằng `underthesea.sent_tokenize`, tìm vị trí từng câu trong văn bản gốc, gộp câu tới 256 token; câu dài hơn 256 token thì cắt bằng C1.
- **85–100'** C4: ViQuAD là nguyên đoạn; Zalo là nguyên điều luật.
- **100–120'** Chạy ba cách trên cả hai kho; ghi số chunk và phân phối độ dài.

```python
def chunk_fixed(doc_id, text, tok, size=256):
    off = tok(text, add_special_tokens=False, return_offsets_mapping=True)['offset_mapping']
    out = []
    for i in range(0, len(off), size):
        s, e = off[i][0], off[min(i + size, len(off)) - 1][1]
        out.append((f'{doc_id}#{i // size}', doc_id, s, e, text[s:e]))
    return out

# kiểm tra: các chunk nối lại phủ hết văn bản, không chồng lấn
chunks = chunk_fixed('d', text, tok)
assert all(a[3] <= b[2] for a, b in zip(chunks, chunks[1:]))
```

**Xong khi:** ba cách phân đoạn sinh chunk cho cả hai kho, mỗi hàm có một `assert`; có bảng số chunk.

### Ngày 5 – Thứ Hai 16/11: Tập đánh giá Zalo

**Mục tiêu cuối ngày:** tập test Zalo (280 trả lời được + 120 không trả lời được), tập dev (100 câu) và kho thu hẹp đã lưu trên Drive kèm seed và mã băm.

- **0–50'** Nhóm truy vấn theo điều luật vàng dùng chung (thành phần liên thông); chia nhóm vào ba phần (mã dưới).
- **50–80'** Dựng kho thu hẹp: kho gốc trừ các điều luật vàng của 120 câu không trả lời được. Kiểm tra không điều luật nào bị loại là điều luật vàng của câu ở phần khác.
- **80–110'** Lưu tập test, tập dev, danh sách điều luật bị loại; ghi seed và mã băm SHA-256 của từng file.
- **110–120'** Bảng thống kê: số câu, số điều luật vàng, số nhóm ở mỗi phần.

```python
import random, networkx as nx

G = nx.Graph()
for qid, docs in gold.items():
    G.add_edges_from((('q', qid), ('d', d)) for d in docs)
groups = [[n[1] for n in comp if n[0] == 'q'] for comp in nx.connected_components(G)]
random.Random(0).shuffle(groups)

parts, sizes = {'unans': [], 'dev': [], 'ans': []}, {'unans': 120, 'dev': 100, 'ans': 280}
for g in groups:
    for name in parts:
        if len(parts[name]) + len(g) <= sizes[name]:
            parts[name] += g
            break
assert all(len(parts[n]) == sizes[n] for n in parts), 'điều chỉnh seed hoặc cho phép lệch vài câu'
```

**Xong khi:** các file tập đánh giá Zalo đã lưu trên Drive kèm mã băm.

### Ngày 6 – Thứ Ba 17/11: Tập đánh giá ViQuAD và kiểm tra tay

**Mục tiêu cuối ngày:** tập test và dev ViQuAD đã đóng băng; biết tỷ lệ câu "không trả lời được" vẫn trả lời được từ kho ở cả hai bộ.

- **0–45'** Kho: các đoạn `context` duy nhất từ cả ba split (split test không có đáp án nhưng vẫn dùng làm đoạn nhiễu); `doc_id` là mã băm của nội dung đoạn.
- **45–75'** Lấy mẫu từ train và validation: chọn ngẫu nhiên các `title` cho dev tới khi đủ 100 câu; từ các `title` còn lại lấy 280 câu trả lời được và 120 câu `is_impossible`, mỗi đoạn tối đa một câu. Lưu vị trí đáp án vàng theo ký tự.
- **75–120'** Đọc tay 30 câu không trả lời được mỗi bộ: lấy 5 kết quả đầu của hybrid, xem kho còn đoạn nào trả lời được không. Ghi tỷ lệ vào file quyết định.

**Xong khi:** hai tập test đóng băng; có hai con số tỷ lệ của D6.

**Nếu tỷ lệ vẫn trả lời được trên 20%:** thay các câu đó bằng câu khác cùng loại trước khi đóng băng, và ghi lại quy trình.

### Ngày 7 – Thứ Tư 18/11: ViStructChunk (C5)

**Mục tiêu cuối ngày:** C5 và biến thể không tiêu đề sinh được chunk cho toàn bộ kho Zalo; biết tỷ lệ điều luật parse được.

- **0–60'** Parser Điều → Khoản → Điểm trên văn bản đã chuẩn hóa (cấu trúc dòng được giữ nguyên khi làm sạch).
- **60–80'** Biến thể không tiêu đề: cùng ranh giới, không gắn tiêu đề cha.
- **80–110'** Đối chiếu tay 30 điều luật chọn ngẫu nhiên; ghi tỷ lệ điều luật có ít nhất một khoản được nhận diện.
- **110–120'** Số chunk và phân phối độ dài của C5; ước lượng thời gian nhúng cho 5 cách phân đoạn trên Zalo.

**Quy tắc parser:**

- Khoản: dòng bắt đầu bằng `^\d+\.\s`. Điểm: dòng bắt đầu bằng `^[a-zđ]\)\s`.
- Đơn vị chunk là Khoản. Khoản dài hơn 256 token thì tách theo Điểm. Phần mở đầu trước khoản 1 là một chunk riêng.
- Điều luật không có khoản: một chunk; nếu dài hơn 256 token thì cắt bằng C3.
- Tiêu đề cha: số hiệu văn bản lấy từ `id` (ví dụ `01/2009/tt-bnn+1` thành "Văn bản 01/2009/TT-BNN"), tiếp theo là tiêu đề Điều và số Khoản: "Văn bản 01/2009/TT-BNN, Điều 1. Phạm vi áp dụng, Khoản 2: …". Kho không có tên đầy đủ của văn bản, nên dùng số hiệu.
- Kiểm tra bằng một điều luật tự viết có hai khoản, một khoản có hai điểm: `assert` đúng số chunk và đúng tiêu đề.

**Xong khi:** C5 và biến thể không tiêu đề sinh chunk cho kho Zalo; có tỷ lệ parse.

**Cổng tuần 1:** hai tập test đóng băng; năm cách phân đoạn trên Zalo và ba trên ViQuAD chạy được; BM25, dense, hybrid chạy được.

---

## Tuần 2 – Sinh câu trả lời và judge

### Ngày 8 – Thứ Năm 19/11: Mô hình sinh

**Mục tiêu cuối ngày:** đã chọn một mô hình sinh, kèm số liệu so sánh trên 50 câu dev.

- **0–20'** Ghi tiêu chí chọn trước khi chạy: tỷ lệ từ chối trên câu không trả lời được, rồi đến tỷ lệ câu trả lời chứa đáp án vàng.
- **20–100'** Chạy hai ứng viên trên 50 câu dev ViQuAD (35 trả lời được, 15 không) với đoạn gốc làm ngữ cảnh; lượng tử hóa 4-bit, `do_sample=False`, tối đa 256 token mới.
- **100–120'** Chọn mô hình; ghi lý do và số liệu.

**Lưu ý kỹ thuật (cần xác minh khi chạy):** `Qwen/Qwen3-8B` có chế độ suy luận, phải tắt trong chat template (`enable_thinking=False`) để đầu ra chỉ gồm câu trả lời. `google/gemma-3-12b-it` yêu cầu chấp nhận điều khoản trên Hugging Face và token truy cập.

**Prompt (đóng băng ngày 25/11):**

```
Chỉ dùng thông tin trong phần Ngữ cảnh để trả lời câu hỏi. Nếu ngữ cảnh không đủ thông tin,
hãy trả lời đúng một câu: "Không tìm thấy thông tin". Trả lời ngắn gọn bằng tiếng Việt.

Ngữ cảnh:
[1] {đoạn 1}
...
[5] {đoạn 5}

Câu hỏi: {câu hỏi}
```

**Nếu trễ:** ứng viên thứ hai không tải được trong 20 phút thì dùng ứng viên thứ nhất và ghi rõ là không so sánh.

### Ngày 9 – Thứ Sáu 20/11: Pipeline đầu-cuối

**Mục tiêu cuối ngày:** một lệnh chạy được từ câu hỏi đến câu trả lời cho cấu hình neo, closed-book và oracle; có ước lượng số giờ GPU cho Giai đoạn B.

- **0–30'** `generate.py`: sinh theo lô; ghi từng dòng kết quả ngay; bỏ qua cặp (cấu hình, câu hỏi) đã có.
- **30–55'** Closed-book: cùng prompt, bỏ phần Ngữ cảnh, câu chỉ dẫn đổi thành "Nếu không biết…". Oracle: chỉ đưa đoạn vàng (ViQuAD) hoặc các điều luật vàng (Zalo), không kèm đoạn truy xuất.
- **55–85'** Quy tắc nhận diện từ chối: chuẩn hóa chữ thường và dấu câu, khớp "không tìm thấy thông tin" và các biến thể gặp trong đầu ra; đọc tay 50 câu trả lời để tìm biến thể bị sót.
- **85–120'** Chạy cấu hình neo trên 50 câu dev mỗi bộ; đo số câu mỗi phút và ước lượng thời gian cho 6.400 lượt.

**Xong khi:** một lệnh chạy từ câu hỏi đến câu trả lời cho cấu hình neo, closed-book và oracle; có ước lượng thời gian Giai đoạn B.

**Nếu ước lượng vượt 20 giờ GPU:** quyết định ngay việc giảm còn 300 câu mỗi bộ (bậc cắt 3), không đợi đến tuần 3.

### Ngày 10 – Thứ Bảy 21/11: Reranker và hàng đợi nhúng

**Mục tiêu cuối ngày:** reranker R1 chạy được trên dev; 24 lượt nhúng cho Giai đoạn A đã khởi động (8 lượt `BAAI/bge-m3` xếp trước) và đang lưu đệm.

- **0–40'** `rerank.py`: `CrossEncoder('BAAI/bge-reranker-v2-m3', max_length=512)`, nhận 20 chunk, trả 5.
- **40–70'** Chạy thử reranking trên dev với cấu hình neo; so chỉ số trước và sau.
- **70–120'** Khởi động 24 lượt nhúng và dựng BM25 cho từng cách phân đoạn; để chạy nền, mỗi lượt lưu đệm ngay khi xong. Thứ tự: 8 lượt `BAAI/bge-m3` trước (5 cách phân đoạn trên Zalo, 3 trên ViQuAD) vì Giai đoạn B cần chúng; sau đó 8 lượt E4 (`intfloat/multilingual-e5-large`) và 8 lượt E2 (`AITeamVN/Vietnamese_Embedding_v2`).

**Lưu ý cho E2 và E4:** `multilingual-e5-large` yêu cầu thêm tiền tố `query: ` cho truy vấn và `passage: ` cho tài liệu, và giới hạn 512 token; thiếu tiền tố thì kết quả thấp giả tạo. Với E2, đọc thẻ mô hình để biết độ dài tối đa và có cần tiền tố không (cần xác minh). E2 và E4 chỉ dùng ở Giai đoạn A, không sinh câu trả lời.

**Nếu ước lượng từ ngày 14/11 cho thấy 24 lượt không xong trước 02/12:** E2 và E4 chỉ chạy với C3 và C4 (bậc cắt 1).

**Xong khi:** reranker chạy được; hàng đợi nhúng đang chạy.

### Ngày 11 – Chủ nhật 22/11: Judge

**Mục tiêu cuối ngày:** judge trả về JSON hợp lệ trên 20 câu dev; chỉ số "nhầm điều luật" chạy được.

- **0–20'** Chọn mô hình judge, khác mô hình sinh. Hai lựa chọn: một mô hình API giá thấp (nhanh, JSON ổn định, khoảng 4.500 lượt gọi), hoặc ứng viên còn lại của ngày 8 chạy cục bộ (không tốn phí).
- **20–80'** `judge.py`: một lượt gọi cho mỗi câu trả lời, đầu ra JSON theo mẫu dưới. Đầu vào: câu hỏi, ngữ cảnh đã cung cấp, bằng chứng vàng (đoạn vàng và đáp án vàng với ViQuAD; điều luật vàng với Zalo), câu trả lời.
- **80–100'** Chỉ số "nhầm điều luật": lấy các số Điều trong câu trả lời bằng biểu thức chính quy, so với số điều của điều luật vàng (phần sau dấu `+` trong `id`).
- **100–120'** Chạy judge trên 20 câu dev; kiểm tra đầu ra hợp lệ.

```json
{"claims": [{"text": "...", "supported_by_context": true, "supported_by_gold": false}],
 "correctness": 1}
```

**Phạm vi chấm:** judge chỉ chấm câu trả lời của các câu **trả lời được** (280 × 16 cấu hình = 4.480 lượt). Câu không trả lời được chỉ dùng quy tắc từ chối để tính fabrication rate, không cần judge. Ở closed-book, `supported_by_context` để trống.

**Từ điểm chấm ra chỉ số:** H_gold = 1 nếu có ít nhất một mệnh đề `supported_by_gold` là false; H_ctx tương tự với `supported_by_context`. Câu từ chối không có mệnh đề nào, được tính vào false refusal chứ không vào H.

### Ngày 12 – Thứ Hai 23/11: Câu trả lời dev và gán nhãn

**Mục tiêu cuối ngày:** có 100 câu trả lời dev đã xáo trộn để gán nhãn; 50 câu đầu đã có nhãn người.

- **0–30'** Sinh câu trả lời của cấu hình neo, closed-book và oracle trên câu trả lời được của hai tập dev.
- **30–40'** Lấy 100 câu trả lời để gán nhãn: 50 mỗi bộ, trộn ba điều kiện, xáo thứ tự, ẩn tên điều kiện.
- **40–120'** Gán nhãn 50 câu đầu, **trước khi** xem đầu ra của judge. Mỗi câu ba nhãn: correctness 0/1/2; có mệnh đề nào không được bằng chứng vàng hỗ trợ (có/không); có mệnh đề nào không được ngữ cảnh hỗ trợ (có/không).

**Nếu có người thứ hai:** gửi cùng 100 câu và hướng dẫn gán nhãn trong hôm nay.

### Ngày 13 – Thứ Ba 24/11: κ

**Mục tiêu cuối ngày:** 100 câu có đủ nhãn người; có Cohen's κ giữa judge và người cho H_gold, H_ctx và correctness.

- **0–60'** Gán nhãn 50 câu còn lại.
- **60–85'** Chạy judge trên 100 câu; tính Cohen's κ cho H_gold và H_ctx, κ có trọng số cho correctness (`sklearn.metrics.cohen_kappa_score`).
- **85–120'** Nếu κ dưới 0,6: đọc các bất đồng trong 50 câu đầu, sửa prompt judge một lần, tính lại κ trên 50 câu sau. Ghi cả hai con số.

**Xong khi:** có κ cho ba nhãn.

### Ngày 14 – Thứ Tư 25/11: Cổng quyết định

**Mục tiêu cuối ngày:** có quyết định tiếp tục hay chuyển phương án dự phòng; prompt, cấu hình và tập test đã đóng băng (thẻ `freeze-b`); người hướng dẫn đã nhận bản tóm tắt thiết kế.

- **0–40'** Chạy thử cả 9 cấu hình Zalo và 7 cấu hình ViQuAD trên 10 câu dev, từ truy xuất đến judge, để bắt lỗi trước khi chạy thật.
- **40–60'** Kiểm tra 8 lượt nhúng `BAAI/bge-m3` đã xong (bắt buộc cho Giai đoạn B); ghi tiến độ của 16 lượt E2 và E4.
- **60–100'** Viết bản tóm tắt thiết kế một trang (câu hỏi nghiên cứu, cấu hình, chỉ số, cỡ mẫu, κ) và gửi người hướng dẫn.
- **100–120'** Đóng băng: prompt sinh, prompt judge, danh sách cấu hình, tập test. Commit và gắn thẻ `freeze-b`.

**Tiếp tục khi:** pipeline chạy được trên dev của cả hai bộ; tập test đã đóng băng; κ của H_gold từ 0,6 trở lên.

**Nếu không đạt:** chuyển sang phương án dự phòng. Tuần 3 chỉ chạy Giai đoạn A; tuần 4 viết bài protocol kèm kết quả truy xuất theo mục lục trong `Kế hoạch 14 ngày và mục lục bài báo.md`.

---

## Tuần 3 – Chạy thực nghiệm

### Ngày 15 – Thứ Năm 26/11: Giai đoạn A

**Mục tiêu cuối ngày:** có bảng Giai đoạn A kèm khoảng tin cậy cho mọi cấu hình dùng BM25, `BAAI/bge-m3` và hybrid (30 trên Zalo, 18 trên ViQuAD); các cấu hình E2 và E4 (20 + 12) có trong bảng hoặc có ngày hoàn thành không muộn hơn 02/12.

- **0–70'** Chạy truy xuất và reranking cho 50 cấu hình Zalo và 30 cấu hình ViQuAD trên câu trả lời được của tập test. Các cấu hình E2 và E4 chưa nhúng xong thì chạy bổ sung khi có embedding, chậm nhất ngày 02/12; Giai đoạn B không phụ thuộc vào chúng. Lưu 20 kết quả đầu của từng cấu hình để Giai đoạn B dùng lại.
- **70–110'** Bảng Recall@5, Recall@20, MRR@10, nDCG@5 kèm khoảng tin cậy bootstrap.
- **110–120'** Kiểm tra hợp lý: reranker không làm đổi Recall@20; C5 và biến thể không tiêu đề có cùng số chunk.

**Xong khi:** có bảng Giai đoạn A cho cả hai bộ.

### Ngày 16 – Thứ Sáu 27/11: Giai đoạn B trên Zalo

**Mục tiêu cuối ngày:** 3.600 lượt sinh trên Zalo đã chạy xong hoặc đang chạy mà không có lỗi định dạng; demo thô chạy được ở phần truy xuất (chọn cấu hình, hiển thị 5 đoạn căn cứ).

- **0–20'** Khởi động sinh câu trả lời cho 9 cấu hình × 400 câu (3.600 lượt), chạy nền.
- **20–50'** Đọc tay 20 câu trả lời đầu tiên: định dạng, ngôn ngữ, câu từ chối, ngữ cảnh có đúng 5 đoạn.
- **50–120'** Trong lúc chờ: dựng demo thô `app.py` trên một runtime CPU riêng (GPU đang bận sinh câu trả lời). Hôm nay chỉ cần phần truy xuất; phần sinh câu trả lời để trống và nối vào ngày 02/12.

**Demo (giao diện web một file, Gradio):**

- Đầu vào: bộ dữ liệu, cách phân đoạn, cách truy xuất, có hay không reranker, câu hỏi.
- Đầu ra: câu trả lời và bảng 5 đoạn căn cứ kèm nguồn (số hiệu văn bản, Điều, Khoản với văn bản luật; tên bài với Wikipedia) và điểm.
- Dùng lại chunk, embedding đã lưu đệm và prompt đã đóng băng; không viết lại logic truy xuất.
- Hiển thị hai dòng lưu ý: kho luật là văn bản đến năm 2021; đây là công cụ tra cứu phục vụ nghiên cứu, không thay cho tư vấn pháp lý.

```python
import gradio as gr
from ragvi import run            # tên hàm theo gói đã viết ở tuần 1–2

def answer(dataset, c, e, rerank, question):
    passages = run.retrieve(dataset, c, e, 'R1' if rerank else 'R0', question)   # 5 đoạn: nguồn, điểm, văn bản
    text = run.generate(question, passages)        # ngày 27/11: trả về chuỗi rỗng, nối mô hình sinh ngày 02/12
    return text, [[p.source, round(p.score, 3), p.text] for p in passages]

gr.Interface(
    answer,
    [gr.Dropdown(['zalo', 'viquad'], value='zalo', label='Bộ dữ liệu'),
     gr.Dropdown(['C1', 'C3', 'C4', 'C5'], value='C3', label='Phân đoạn (C5 chỉ cho văn bản luật)'),
     gr.Dropdown(['E0', 'E3', 'E5'], value='E3', label='Truy xuất'),
     gr.Checkbox(label='Xếp hạng lại (R1)'),
     gr.Textbox(label='Câu hỏi')],
    [gr.Textbox(label='Câu trả lời'),
     gr.Dataframe(headers=['Nguồn', 'Điểm', 'Đoạn văn'], label='Căn cứ')],
    title='RAG tiếng Việt: thử các lựa chọn thiết kế',
).launch(share=True)
```

Việc gán nhãn lại 30 câu (đo độ nhất quán của một người gán nhãn) đã bỏ để dành thời gian cho demo; ghi thành hạn chế trong báo cáo.

### Ngày 17 – Thứ Bảy 28/11: Giai đoạn B trên ViQuAD

**Mục tiêu cuối ngày:** đủ 6.400 câu trả lời, không thiếu, không trùng; có fabrication rate và false refusal sơ bộ.

- **0–20'** Khởi động 7 cấu hình × 400 câu (2.800 lượt).
- **20–50'** Đọc tay 20 câu trả lời đầu tiên.
- **50–120'** Kiểm tra bảng kết quả: đủ 6.400 dòng, không trùng, không thiếu; chạy lại phần thiếu. Tính fabrication rate và false refusal (không cần judge) để có số liệu sớm.

**Xong khi:** đủ 6.400 câu trả lời.

### Ngày 18 – Chủ nhật 29/11: Chấm điểm

**Mục tiêu cuối ngày:** khoảng 4.480 câu trả lời cần chấm đều có điểm judge, hoặc được ghi rõ là lỗi.

- **0–30'** Khởi động judge trên 4.480 câu trả lời của câu trả lời được.
- **30–90'** Theo dõi tỷ lệ đầu ra không hợp lệ; chạy lại các dòng lỗi, tối đa hai lần; ghi số dòng vẫn lỗi.
- **90–120'** Chạy chỉ số "nhầm điều luật" trên Zalo; đọc tay 20 trường hợp được đánh dấu.

**Xong khi:** mọi câu trả lời cần chấm đã có điểm, hoặc được ghi là lỗi.

### Ngày 19 – Thứ Hai 30/11: Chỉ số

**Mục tiêu cuối ngày:** bảng kết quả một dòng cho mỗi cặp (cấu hình, câu hỏi) có đủ mọi chỉ số và qua được các kiểm tra hợp lý.

- **0–60'** Tính mọi chỉ số vào bảng một dòng cho mỗi cặp (cấu hình, câu hỏi): correctness, H_gold, H_ctx, từ chối, nhầm điều luật; EM và token-F1 theo âm tiết cho ViQuAD.
- **60–100'** Kiểm tra hợp lý: oracle có độ đúng cao hơn cấu hình neo; closed-book có độ đúng thấp nhất trên Zalo; không cấu hình nào từ chối gần 100%.
- **100–120'** Bảng trung bình theo cấu hình (chưa có khoảng tin cậy).

**Nếu kiểm tra hợp lý không đạt:** dừng lại tìm lỗi trước khi phân tích; dùng ngày 21.

### Ngày 20 – Thứ Ba 01/12: Chi phí

**Mục tiêu cuối ngày:** có bảng chi phí: độ trễ (trung vị, phân vị 95), kích thước chỉ mục, môi trường chạy.

- **0–70'** Đo độ trễ truy xuất và reranking trên 100 truy vấn cho từng tổ hợp E × R, cùng một GPU, bỏ lượt đầu; ghi trung vị và phân vị 95.
- **70–100'** Kích thước chỉ mục theo cách phân đoạn; số chunk.
- **100–120'** Ghi môi trường: GPU, phiên bản thư viện, mã commit.

### Ngày 21 – Thứ Tư 02/12: Dự phòng

**Mục tiêu cuối ngày:** không còn việc tồn của tuần 3; demo đã nối mô hình sinh và trả lời được 10 câu hỏi thử.

Dùng cho phần trễ của tuần 3. Việc cố định của ngày (khoảng 30 phút): nối mô hình sinh vào demo và thử 10 câu hỏi, gồm vài câu không có trong kho để xem demo có từ chối không. Nếu còn thời gian: viết trước mục phương pháp. Nếu cả ngày phải dùng để bù trễ, việc nối mô hình sinh chuyển sang ngày 09/12.

**Cổng tuần 3:** bảng kết quả đầy đủ cho Giai đoạn A và B; bảng chi phí.

---

## Tuần 4 – Phân tích và viết

### Ngày 22 – Thứ Năm 03/12: Thống kê

**Mục tiêu cuối ngày:** mọi chỉ số có khoảng tin cậy 95%; mọi so sánh trong họ đã ghi trước có giá trị p hiệu chỉnh Holm; có RAH cho từng cấu hình và từng miền.

- **0–40'** Khoảng tin cậy bootstrap 95% cho mọi chỉ số, 1.000 lần lấy mẫu lại theo cụm: `title` với ViQuAD, nhóm điều luật với Zalo.
- **40–80'** Kiểm định hoán vị ghép cặp trên H_gold và correctness (mã dưới), rồi hiệu chỉnh Holm bằng `statsmodels.stats.multitest.multipletests(p, method='holm')`.
- **80–120'** RAH cho từng cấu hình kèm khoảng tin cậy của hiệu số ghép cặp; tỷ lệ RAH/H chỉ báo cáo khi H từ 10% trở lên; so sánh hai miền.

```python
import numpy as np
rng = np.random.default_rng(0)

def paired_perm(a, b, n=10000):
    d = np.asarray(a, float) - np.asarray(b, float)
    flips = rng.choice([-1, 1], (n, len(d)))
    return ((np.abs((flips * d).mean(1)) >= abs(d.mean())).sum() + 1) / (n + 1)
```

**Họ phép so sánh (ghi trước khi chạy):** Zalo có 7 so sánh trên mỗi chỉ số chính (sáu cấu hình so với neo, và C5 so với C5 không tiêu đề); ViQuAD có 4. Mọi so sánh khác ghi là khám phá.

### Ngày 23 – Thứ Sáu 04/12: Phân tích lỗi và hình

**Mục tiêu cuối ngày:** 30 trường hợp ảo giác đã gắn nguyên nhân; có ba hình, các bảng cuối cùng và bảng khuyến nghị có điều kiện theo miền; demo chạy mặc định bằng cấu hình khuyến nghị.

- **0–50'** Chọn ngẫu nhiên 30 câu trả lời có H_gold = 1 (15 mỗi bộ); gắn một trong năm nguyên nhân của đề cương. So tỷ lệ "do truy xuất" với RAH.
- **50–90'** Ba hình: bảng nhiệt Giai đoạn A; H_gold theo cấu hình kèm khoảng tin cậy; RAH theo miền. Các bảng: kết quả Giai đoạn B, chi phí, κ.
- **90–120'** Bảng khuyến nghị có điều kiện (mẫu dưới); đặt cấu hình khuyến nghị của từng miền làm giá trị mặc định trong demo.

**Bảng khuyến nghị có điều kiện:**

| Miền | Tiêu chí | Cấu hình tốt nhất trong số đã thử | Hiệu số so với cấu hình neo (khoảng tin cậy 95%) | Điều kiện áp dụng |
|---|---|---|---|---|
| Pháp luật | Ảo giác thấp nhất (H_gold) | | | |
| Pháp luật | Độ đúng cao nhất | | | |
| Pháp luật | Độ trễ thấp nhất | | | |
| Wikipedia | (ba dòng tương tự) | | | |
| Cả hai | Mô hình nhúng tốt nhất ở tầng truy xuất (E2, E3, E4) | | | Chỉ dựa trên Recall và nDCG của Giai đoạn A |

Quy tắc điền: chỉ ghi một cấu hình là "tốt nhất" khi khoảng tin cậy của hiệu số so với cấu hình đứng thứ hai không chứa 0; nếu không thì ghi "không phân biệt được giữa X và Y". Ghi rõ trong bài rằng đây là khuyến nghị trong phạm vi 9 + 7 cấu hình đã thử, chưa phải khuyến nghị chung cho tiếng Việt.

### Ngày 24 – Thứ Bảy 05/12: Tài liệu và phương pháp

**Mục tiêu cuối ngày:** mọi tài liệu sẽ trích đã được xác minh từ nguồn gốc; có bản nháp mục phương pháp và thiết lập thực nghiệm.

- **0–50'** Xác minh từ nguồn gốc các tài liệu sẽ trích (khoảng 8–10 nguồn): tác giả, năm, nơi công bố, và đúng khẳng định mà bài dùng. Xác định phiên bản ViQuAD đang dùng (bản trên Drive có 39.569 dòng, khác con số trong đề cương).
- **50–120'** Tạo `reports/ban-thao.md`; viết mục phương pháp và thiết lập thực nghiệm (khoảng 1.400 từ) từ file quyết định, gồm bảng cấu hình và sơ đồ pipeline, cộng một mục mô tả hệ thống và demo (khoảng 300 từ, có ảnh chụp giao diện). Đầu ra là báo cáo đề tài, không phải bài báo hội nghị.

### Ngày 25 – Chủ nhật 06/12: Kết quả và thảo luận

**Mục tiêu cuối ngày:** có bản nháp mục kết quả và thảo luận; mỗi câu hỏi RQ1–RQ4 có một kết luận kèm số liệu.

- **0–80'** Mục kết quả theo thứ tự RQ1, RQ2, RQ3, RQ4, rồi bảng khuyến nghị có điều kiện (RQ5); mỗi kết luận kèm hiệu số, khoảng tin cậy và giá trị p đã hiệu chỉnh. Với RQ2, tách rõ kết quả ở tầng truy xuất (ba mô hình nhúng) và ở tầng câu trả lời (chỉ `BAAI/bge-m3`).
- **80–120'** Thảo luận: giả thuyết nào được ủng hộ, bị bác bỏ, chưa kết luận được. Với khoảng tin cậy rộng, viết "không phát hiện khác biệt", không viết "không có khác biệt".

### Ngày 26 – Thứ Hai 07/12: Giới thiệu và công trình liên quan

**Mục tiêu cuối ngày:** có bản nháp mục giới thiệu và công trình liên quan.

- **0–60'** Công trình liên quan (khoảng 300 từ, ngắn hơn bài báo), chỉ dùng nguồn đã xác minh.
- **60–120'** Giới thiệu (khoảng 600 từ): bối cảnh, khoảng trống, câu hỏi nghiên cứu, đóng góp. Đóng góp nêu đúng phạm vi đã làm.

### Ngày 27 – Thứ Ba 08/12: Hạn chế, tóm tắt, kiểm tra

**Mục tiêu cuối ngày:** bản thảo đủ mọi mục, kể cả tóm tắt và hạn chế, và qua được danh sách kiểm tra nhất quán.

- **0–40'** Hạn chế: cỡ mẫu 400 và sức mạnh thống kê; số người gán nhãn và κ đạt được; kho ViQuAD không có đoạn nhiễu ngoài; một mô hình sinh; H_gold phạt cả tri thức đúng nằm ngoài đoạn vàng; các mức yếu tố đã bỏ.
- **40–70'** Tóm tắt và kết luận.
- **70–120'** Danh sách kiểm tra: số cấu hình (50 và 30 ở Giai đoạn A, 9 và 7 ở Giai đoạn B) và cỡ mẫu khớp giữa văn bản và bảng; mọi con số truy được về bảng kết quả; ký hiệu thống nhất; mọi trích dẫn có trong danh mục.

### Ngày 28 – Thứ Tư 09/12: Gửi người hướng dẫn

**Mục tiêu cuối ngày:** người hướng dẫn đã nhận báo cáo hoàn chỉnh và demo; kho mã có README (cách chạy demo, cách tái lập từng bảng), video demo ngắn và thẻ phiên bản.

- **0–45'** Đọc liền mạch báo cáo một lần và sửa.
- **45–75'** README cho kho mã: cách chạy demo, lệnh tái lập từng bảng; gắn thẻ phiên bản.
- **75–100'** Quay video demo 2–3 phút: một câu hỏi luật trả lời được có trích dẫn, một câu không có trong kho bị từ chối, và cùng một câu hỏi với hai cấu hình khác nhau.
- **100–120'** Gửi báo cáo, đường dẫn kho mã và video, kèm ba điểm cần ý kiến nhất.

### Ngày 29 – Thứ Năm 10/12: Sửa theo phản hồi

**Mục tiêu cuối ngày:** mọi phản hồi ảnh hưởng đến kết luận đã được xử lý; nếu chưa có phản hồi, mọi con số trong mục kết quả đã được đối chiếu lại với bảng.

Ưu tiên phản hồi ảnh hưởng đến kết luận, rồi đến trình bày. Nếu chưa có phản hồi: đọc lại mục kết quả và đối chiếu từng con số với bảng.

### Ngày 30 – Thứ Sáu 11/12: Nộp

**Mục tiêu cuối ngày:** bài đã nộp; có danh sách việc còn lại cho khóa luận.

- **0–60'** Kiểm tra lần cuối: tài liệu tham khảo, số thứ tự bảng và hình, định dạng theo yêu cầu nơi nộp.
- **60–90'** Nộp.
- **90–120'** Ghi danh sách việc còn lại cho khóa luận theo `Kế hoạch 16 tuần.md`: các mức yếu tố đã bỏ, cỡ mẫu 1.000, nhãn hai người, khung khuyến nghị, công bố dữ liệu.

---

## Các điểm quyết định trong lịch

| Ngày | Quyết định | Căn cứ |
|---|---|---|
| 13/11 | BM25 tách từ hay theo âm tiết | Thời gian tách từ cả kho |
| 17/11 | Có thay câu không trả lời được không | Tỷ lệ đọc tay ở D6 |
| 19/11 | Mô hình sinh | Thử trên 50 câu dev |
| 20/11 | Giữ 400 hay giảm còn 300 câu mỗi bộ | Ước lượng giờ GPU |
| 22/11 | Mô hình judge | Ngân sách và độ ổn định JSON |
| 25/11 | Tiếp tục hay chuyển phương án dự phòng | Ba điều kiện của cổng |
