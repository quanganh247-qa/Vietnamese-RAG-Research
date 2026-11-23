# Phân tích định tính 30 trường hợp ảo giác (`H_gold = 1`, Ngày 23 – 04/12)

Chọn ngẫu nhiên 30 câu trả lời có `H_gold = 1` ở các cấu hình RAG Giai đoạn B (`15 ViQuAD test + 15 Zalo test`, `random.Random(0)`), gắn nhãn theo 5 nhóm nguyên nhân của đề cương (Mục 5.4):
1. **Truy xuất sai** (Top-5 không chứa đoạn/điều luật vàng).
2. **Chunk cắt mất thông tin** (Top-5 trúng tài liệu/điều luật vàng nhưng thiếu chunk chứa khoản/câu đáp án hoặc bị cắt ở trần token).
3. **Nhiễu từ đoạn không liên quan** (Top-5 có đoạn vàng nhưng mô hình tổng hợp/suy diễn thêm thông tin từ các đoạn khác trong top-5).
4. **Nhầm điều luật** (Top-5 chứa các điều luật cùng chủ đề hoặc các chunk mất tiêu đề Điều/Văn bản làm mô hình áp nhầm mức phạt/quy định của điều luật khác).
5. **Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai** (Top-5 có đủ thông tin đáp án vàng nhưng mô hình tự suy diễn hoặc trích vượt phạm vi đáp án vàng — lỗi nội tại ở tầng sinh/judge, thường xuất hiện ở cả `oracle`).

## 1. Bảng tổng hợp phân bố nguyên nhân và đối chiếu với chỉ số RAH

| Nhóm nguyên nhân | Thuộc tầng truy xuất / phân đoạn? | ViQuAD test (`n = 15`) | Zalo Legal test (`n = 15`) | Tổng (`n = 30`) |
|---|:---:|---:|---:|---:|
| 1. Truy xuất sai | Có | 3 (20,0%) | 3 (20,0%) | 6 (20,0%) |
| 2. Chunk cắt mất thông tin | Có | 1 (6,7%) | 2 (13,3%) | 3 (10,0%) |
| 3. Nhiễu từ đoạn không liên quan | Có | 5 (33,3%) | 1 (6,7%) | 6 (20,0%) |
| 4. Nhầm điều luật | Có | 0 (0,0%) | **7 (46,7%)** | 7 (23,3%) |
| 5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai | Không (nội tại tầng sinh) | **6 (40,0%)** | 2 (13,3%) | 8 (26,7%) |
| **Tổng tỷ lệ quy cho truy xuất / phân đoạn (Nhóm 1–4)** | **Có** | **9 / 15 (60,0%)** *(3/15 = 20,0% không có ở Oracle)* | **13 / 15 (86,7%)** | **22 / 30 (73,3%)** |
| **Đối chiếu tỷ phần định lượng `RAH / H_gold` (Mục 5.3)** | – | **32,5% – 46,5%** *(TB: 38,3%)* | **69,5% – 83,0%** *(TB: 76,3%)* | – |

> **Nhận xét kiểm chứng chéo `RAH`:**
> - Trên **Zalo Legal**, **13/15 ca (`86,7%`)** bắt nguồn trực tiếp từ tầng truy xuất và phân đoạn (đặc biệt là `Nhầm điều luật` chiếm `7/15 = 46,7%` khi các chunk `C3` của Nghị định `100/2019/NĐ-CP` mất tiêu đề Điều 5/6/7/8 nên mô hình áp nhầm mức phạt xe máy/xe đạp cho xe ô tô, cùng `3/15` ca truy xuất sai và `2/15` ca chunk cắt mất khoản), hoàn toàn nhất quán với tỷ phần định lượng **`RAH / H_gold = 69,5% – 83,0%`**.
> - Trên **ViQuAD**, có tới **8/15 ca (`53,3%`)** cũng bị đánh dấu `H_gold = 1` ngay cả ở điều kiện **`oracle`** (do mô hình trích nguyên câu văn dài hơn span đáp án vàng ngắn hoặc gộp thêm thông tin từ các đoạn cùng bài Wikipedia), khớp chặt chẽ với việc `RAH / H_gold` trên ViQuAD chỉ chiếm **`32,5% – 46,5%`**.

## 2. Chi tiết 15 trường hợp trên ViQuAD test (`seed = 0`)

### Mẫu VIQUAD-01 — Cấu hình `C3-E5-R0` | Mã câu hỏi `train:0138-0012-0003`

- **Câu hỏi:** Mỹ đã cung cấp cho quân đội Pháp ở Đông Dương bao nhiêu tiền?
- **Tài liệu vàng:** `['66911f17a6128315']` | **Top-5 chunk truy xuất:** `['ec46c6db69fb0d99#0', '8af062d52fa2050f#0', '45f8a7640e3e8551#0', 'b29a7abf3a250c09#0', 'f9175e68ad5e77cb#1']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Mỹ đã viện trợ trên 1 tỷ USD mỗi năm cho Pháp ở Đông Dương, tương đương khoảng 5,8 tỷ USD theo thời giá năm 2004.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Mỹ đã viện trợ trên 1 tỷ USD mỗi năm cho Pháp ở Đông Dương", "tương đương khoảng 5,8 tỷ USD theo thời giá năm 2004"]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** Top-5 không chứa đoạn vàng `66911f17a6128315` (nêu con số 160 triệu USD) mà lấy đoạn khác trong bài Chiến tranh Đông Dương nêu viện trợ cuối chiến tranh trên 1 tỷ USD/năm.

### Mẫu VIQUAD-02 — Cấu hình `C3-E3-R0` | Mã câu hỏi `train:0096-0005-0001`

- **Câu hỏi:** Tổ chức tự nguyện được biểu hiện qua những mặt nào?
- **Tài liệu vàng:** `['1f32b4a4454808ab']` | **Top-5 chunk truy xuất:** `['1f32b4a4454808ab#0', '93f6add66bd918a0#0', '4210fb0bfe2371ba#0', '6849e46bd48496ba#1', '69be24c956fa4211#1']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Tổ chức tự nguyện được biểu hiện qua việc hoạt động dựa trên thành viên không hưởng lương, thiếu cơ cấu quyền lực cưỡng bức, hành động không bị ràng buộc chặt chẽ, thu hút đông đảo thành viên, tạo ra nguồn kinh phí lớn từ đóng góp và tài trợ, có thể phát triển thành bộ máy quan liêu, đáp ứng nhu cầu tổ chức hoạt động đời sống đồng thời tôn trọng tự do cá nhân của thành viên.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["hành động không bị ràng buộc chặt chẽ", "thu hút đông đảo thành viên", "tạo ra nguồn kinh phí lớn từ đóng góp và tài trợ", "có thể phát triển thành bộ máy quan liêu", "đáp ứng nhu cầu tổ chức hoạt động đời sống đồng thời tôn trọng tự do cá nhân của thành viên"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = None`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Đoạn vàng `1f32b4a4454808ab#0` đứng thứ #1 và mô hình trả lời đủ ý đúng (`correctness = 2`), nhưng gộp thêm các mệnh đề mở rộng từ đoạn #2 `93f6add66bd918a0#0` cùng bài.

### Mẫu VIQUAD-03 — Cấu hình `C3-E5-R0` | Mã câu hỏi `train:0080-0014-0004`

- **Câu hỏi:** Tổng thống nào được người dân tín nhiệm?
- **Tài liệu vàng:** `['2f3ad45762f8fb2d']` | **Top-5 chunk truy xuất:** `['6c7d70e78caec4fb#0', '388eb56200e0a8e0#1', '729b9f723ad4490e#0', 'a0d7966dc6c805fd#1', 'fd68b23c5753f5e2#0']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Theo thông tin trong ngữ cảnh, Tổng thống Barack Obama được nhân dân trên toàn thế giới tín nhiệm với tỉ lệ ủng hộ 53%, và tại Việt Nam, người dân cũng dành cho ông tỉ lệ ủng hộ là 80%.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Tổng thống Barack Obama được nhân dân trên toàn thế giới tín nhiệm với tỉ lệ ủng hộ 53%", "Tại Việt Nam, người dân cũng dành cho ông tỉ lệ ủng hộ là 80%"]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = None`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** Câu hỏi thiếu tên quốc gia (Mali) nên top-5 truy xuất các đoạn khảo sát tín nhiệm của Barack Obama và Vladimir Putin thay vì đoạn vàng về Amadou Toumani Touré.

### Mẫu VIQUAD-04 — Cấu hình `C3-E3-R0` | Mã câu hỏi `train:0126-0044-0002`

- **Câu hỏi:** Những tổ chức quốc tế nổi tiếng nào có trụ sở tại Pháp?
- **Tài liệu vàng:** `['53add1b7f62c295c']` | **Top-5 chunk truy xuất:** `['53add1b7f62c295c#0', 'efd791ce0fea7b46#0', 'b07ec8c602a5038d#0', 'fbfe39c97960e7de#0', 'd1c0a4ad25db4902#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Các tổ chức quốc tế có trụ sở tại Pháp bao gồm OECD, UNESCO, Interpol, Văn phòng Cân đo Quốc tế, Cộng đồng Pháp ngữ và Ủy ban Olympic Quốc tế.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Ủy ban Olympic Quốc tế có trụ sở tại Pháp"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Đoạn vàng `53add1b7f62c295c#0` liệt kê đúng 5 tổ chức quốc tế tại Pháp, nhưng đoạn #5 `d1c0a4ad25db4902#0` nói về Pierre de Coubertin và Thế vận hội tại Pháp khiến mô hình suy diễn thêm "Ủy ban Olympic Quốc tế".

### Mẫu VIQUAD-05 — Cấu hình `C1-E3-R0` | Mã câu hỏi `train:0035-0002-0001`

- **Câu hỏi:** Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực nào?
- **Tài liệu vàng:** `['3bfb515d87a9256d']` | **Top-5 chunk truy xuất:** `['3bfb515d87a9256d#0', 'e3919ef60808e97b#0', 'e37073a6e4045c30#0', '9e65111961446af5#0', 'f804f4e111730260#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực: kinh tế học, xã hội học, phân tích pháp lý, phê bình văn học, nghiên cứu tôn giáo, khoa học chính trị, vật lý (tạo ra phản ứng hạt nhân nhân tạo và tự duy trì đầu tiên của thế giới), khoa học sinh học, khoa học vật lý, khoa học xã hội, y khoa, kinh doanh, luật, thần học, chính sách công, quản trị dịch vụ xã hội, giáo dục, và các lĩnh vực liên quan đến Fermilab cùng Phòng Thí nghiệm Quốc gia Argonne.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["khoa học sinh học", "khoa học vật lý", "khoa học xã hội", "y khoa", "kinh doanh", "luật", "thần học", "chính sách công", "quản trị dịch vụ xã hội", "giáo dục", "các lĩnh vực liên quan đến Fermilab cùng Phòng Thí nghiệm Quốc gia Argonne"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Đoạn vàng `#1` liệt kê các trường phái học thuật tại Đại học Chicago, nhưng các đoạn `#2` và `#3` liệt kê bốn phân khoa sau đại học (Khoa học Sinh học, Khoa học Vật lý...) khiến mô hình gộp chung vào câu trả lời.

### Mẫu VIQUAD-06 — Cấu hình `C3-E0-R0` | Mã câu hỏi `train:0119-0022-0005`

- **Câu hỏi:** Castro dần chuyển sự ủng hộ của mình sang những ai?
- **Tài liệu vàng:** `['b4ed31bae96a648a']` | **Top-5 chunk truy xuất:** `['25851bcbd3791f54#0', 'b4e1deca72521df3#0', 'f6e359c37e3ebcf3#0', '692f554f1080613f#0', '3d47b80432e8abc8#0']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Castro dần chuyển sự ủng hộ của mình sang Liên bang Xô viết và các nước đồng minh của Liên Xô.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Castro dần chuyển sự ủng hộ của mình sang Liên bang Xô viết và các nước đồng minh của Liên Xô."]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** BM25 (`C3-E0-R0`) không truy xuất được đoạn vàng `b4ed31bae96a648a` mà lấy các đoạn khác về quan hệ Cuba – Liên Xô.

### Mẫu VIQUAD-07 — Cấu hình `C3-E3-R1` | Mã câu hỏi `train:0035-0002-0001`

- **Câu hỏi:** Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực nào?
- **Tài liệu vàng:** `['3bfb515d87a9256d']` | **Top-5 chunk truy xuất:** `['3bfb515d87a9256d#0', 'e3919ef60808e97b#0', '8f8390978d1684f9#0', 'e37073a6e4045c30#0', '9e65111961446af5#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực: kinh tế học, xã hội học, phân tích pháp lý, phê bình văn học, nghiên cứu tôn giáo, khoa học chính trị, vật lý (tạo ra phản ứng hạt nhân nhân tạo và tự duy trì đầu tiên), y khoa, và các chương trình sau đại học cũng như ủy ban liên ngành.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực: y khoa", "Viện Đại học Chicago đã tham gia nghiên cứu vào các lĩnh vực: các chương trình sau đại học cũng như ủy ban liên ngành"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Cùng câu hỏi Đại học Chicago như mẫu #5: mô hình gộp thêm trường Y khoa Pritzker và các chương trình sau đại học/ủy ban liên ngành từ đoạn #4 `e37073a6e4045c30#0`.

### Mẫu VIQUAD-08 — Cấu hình `C3-E3-R1` | Mã câu hỏi `train:0006-0051-0003`

- **Câu hỏi:** Nguyên nhân dẫn đến mâu thuẫn giữa Hàn Quốc và Nhật Bản là gì?
- **Tài liệu vàng:** `['d7e0debdf9d41515']` | **Top-5 chunk truy xuất:** `['d7e0debdf9d41515#0', 'e427604a2fe2f478#0', '36a63fdc2adaaf6a#0', 'cc95da6ed462ac49#1', '2bfd2d2aa4529e91#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Nguyên nhân dẫn đến mâu thuẫn giữa Hàn Quốc và Nhật Bản là tranh chấp về chủ quyền trên đảo Liancourt.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Nguyên nhân dẫn đến mâu thuẫn giữa Hàn Quốc và Nhật Bản là tranh chấp về chủ quyền trên đảo Liancourt."]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Đoạn vàng `d7e0debdf9d41515#0` đứng thứ #1; câu văn trong đoạn vàng nêu tranh chấp với Hàn Quốc về đảo Liancourt rồi mới nêu vấn đề Triều Tiên. Cả RAG lẫn `oracle` (`ora_h_gold = 1`) đều trích mệnh đề đúng thực tế về đảo Liancourt nhưng lệch span đáp án vàng của ViQuAD.

### Mẫu VIQUAD-09 — Cấu hình `C3-E3-R0` | Mã câu hỏi `train:0119-0019-0002`

- **Câu hỏi:** Batista đã làm gì khi khu vực phía đông La Habana đã rơi vào tay phe nổi dậy?
- **Tài liệu vàng:** `['9fcecaaf5b46ae1f']` | **Top-5 chunk truy xuất:** `['9fcecaaf5b46ae1f#0', '20161bb9a3bf1bb4#0', 'c25185516508158a#0', '3d47b80432e8abc8#0', '06ef19934436d9c8#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Batista cho rằng chiến đấu là vô ích và bỏ chạy khỏi đất nước tới Bồ Đào Nha và sau này là Tây Ban Nha.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Batista cho rằng chiến đấu là vô ích", "và sau này là Tây Ban Nha"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Mô hình trích nguyên câu văn trong đoạn vàng ("cho rằng chiến đấu là vô ích và bỏ chạy khỏi đất nước tới Bồ Đào Nha và sau này là Tây Ban Nha"), dài hơn cụm đáp án ngắn nên bị Judge đánh dấu phần ngoài span vàng ở cả RAG lẫn `oracle`.

### Mẫu VIQUAD-10 — Cấu hình `C3-E5-R0` | Mã câu hỏi `train:0101-0008-0001`

- **Câu hỏi:** Lý do nào được những người có tài từ chối trong việc cống hiến cho triều đình mới?
- **Tài liệu vàng:** `['cfc9fc084e097d0d']` | **Top-5 chunk truy xuất:** `['cfc9fc084e097d0d#0', '03aee74840fa9cd3#0', '18e9bb34be0e14f1#1', '64ba28503cf613ec#0', '4b290fdc205a91ab#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Lý do những người có tài từ chối cống hiến cho triều đình mới là vì họ không muốn làm quan.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Lý do những người có tài từ chối cống hiến cho triều đình mới là vì họ không muốn làm quan."]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = None`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Đoạn vàng viết "không muốn làm quan cống hiến cho triều đình mới, do đó chọn các cách thức như tự sát...". Câu hỏi hỏi "Lý do nào" nhưng đáp án vàng lại gán cho các cách thức, còn mô hình trích đúng mệnh đề lý do.

### Mẫu VIQUAD-11 — Cấu hình `C3-E5-R0` | Mã câu hỏi `train:0131-0003-0003`

- **Câu hỏi:** Từ nhỏ Kepler đã nổi bật hơn anh chị em trong gia đình nhờ vào đặc điểm nào?
- **Tài liệu vàng:** `['b6ff537d62ed77de']` | **Top-5 chunk truy xuất:** `['b6ff537d62ed77de#0', '07aaf44f67200fe7#0', '6970ea3bba354813#0', '1139e183d9c98536#0', '845c47bcc19318eb#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Kepler nổi bật hơn anh chị em nhờ khả năng toán học kỳ lạ.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Kepler nổi bật hơn anh chị em nhờ khả năng toán học kỳ lạ."]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **2. Chunk cắt mất thông tin**
- **Giải thích:** Đoạn vàng `b6ff537d62ed77de` bị `C3` cắt thành hai chunk `#0` và `#1`. Top-5 chỉ chứa `#0` (nêu "khả năng toán học kỳ lạ"), còn cụm đáp án vàng "thông minh hơn người" nằm ở chunk `#1` ngoài top-5.

### Mẫu VIQUAD-12 — Cấu hình `C3-E0-R0` | Mã câu hỏi `validation:0017-0001-0008`

- **Câu hỏi:** Franklin Delano Roosevelt có vai trò gì trong tình hình chiến sự thế giới trong giữa thế kỷ XX?
- **Tài liệu vàng:** `['bce512364e2546f9']` | **Top-5 chunk truy xuất:** `['759194104dcd9f26#0', 'bce512364e2546f9#0', '05c5fb2460caef8d#0', 'd5b3b2fdc912442c#0', '1fa929305604bada#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Franklin Delano Roosevelt là một khuôn mặt trung tâm của các sự kiện thế giới trong giữa thế kỷ XX và ông đã lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["ông đã lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Mô hình trích cả vế sau của câu trong đoạn vàng ("và ông đã lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai"), vượt ra ngoài span đáp án vàng ngắn ở cả RAG lẫn `oracle` (`ora_h_gold = 1`).

### Mẫu VIQUAD-13 — Cấu hình `C3-E3-R0` | Mã câu hỏi `validation:0017-0001-0008`

- **Câu hỏi:** Franklin Delano Roosevelt có vai trò gì trong tình hình chiến sự thế giới trong giữa thế kỷ XX?
- **Tài liệu vàng:** `['bce512364e2546f9']` | **Top-5 chunk truy xuất:** `['bce512364e2546f9#0', '2b4ffbd70b65d3dc#1', '6ddc53e863451dbc#0', 'bba9b2f77b232908#0', '97e23872035eb4bd#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Franklin Delano Roosevelt là một khuôn mặt trung tâm của các sự kiện thế giới trong giữa thế kỷ XX và là người lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Franklin Delano Roosevelt là người lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Cùng câu hỏi Franklin Delano Roosevelt như mẫu #12 ở cấu hình `C3-E3-R0`: trích thêm vế sau của cùng câu trong đoạn vàng (xuất hiện ở cả `oracle`).

### Mẫu VIQUAD-14 — Cấu hình `C3-E3-R0` | Mã câu hỏi `train:0057-0058-0001`

- **Câu hỏi:** Algarve dẫn đầu với dố lượng khách nghỉ qua đêm là bao nhiêu?
- **Tài liệu vàng:** `['af8394f20749ef09']` | **Top-5 chunk truy xuất:** `['af8394f20749ef09#0', '235adf7a12576d78#0', '25057ae5678d8ce4#0', '00c5328338266aeb#0', '043918349159e062#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Algarve dẫn đầu với 4,2 triệu khách nghỉ qua đêm theo số liệu năm 2016.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Algarve dẫn đầu với 4,2 triệu khách nghỉ qua đêm theo số liệu năm 2016."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Đoạn vàng viết "Lisboa (6,3 triệu), Porto và miền bắc (4,4 triệu), Algarve (4,2 triệu)". Nhãn vàng ViQuAD gán nhầm con số 6,3 triệu của Lisboa cho Algarve, trong khi mô hình đọc đúng con số 4,2 triệu của Algarve ở cả RAG lẫn `oracle`.

### Mẫu VIQUAD-15 — Cấu hình `C3-E3-R1` | Mã câu hỏi `train:0104-0025-0002`

- **Câu hỏi:** Bắc Kinh trở thành thủ đô của những chính phủ nào?
- **Tài liệu vàng:** `['06a6ed703008a75d']` | **Top-5 chunk truy xuất:** `['06a6ed703008a75d#0', '8e61ef64d2dff50b#1', 'bb130b9666b8d704#0', '0d2805953c61345a#2', 'f12d153395d286e0#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Bắc Kinh trở thành thủ đô của Chính phủ Lâm thời Trung Hoa Dân Quốc, Chính phủ Bắc Dương, triều Thanh và nước Cộng hòa Nhân dân Trung Hoa.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Bắc Kinh trở thành thủ đô của triều Thanh", "Bắc Kinh trở thành thủ đô của nước Cộng hòa Nhân dân Trung Hoa"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Đoạn vàng `#1` nêu Chính phủ Lâm thời và Chính phủ Bắc Dương, nhưng các đoạn `#2, #3, #4` cùng bài Bắc Kinh nêu thủ đô triều Thanh và Cộng hòa Nhân dân Trung Hoa nên mô hình liệt kê gộp cả 4 chính phủ.

## 3. Chi tiết 15 trường hợp trên Zalo Legal test (`seed = 0`)

### Mẫu ZALO-01 — Cấu hình `C3-E5-R0` | Mã câu hỏi `b99998cd09993202d452be4372167247`

- **Câu hỏi:** Người chấp hành biện pháp bắt buộc chữa bệnh sẽ chữa bệnh ở đâu?
- **Tài liệu vàng:** `['41/2019/qh14+133']` | **Top-5 chunk truy xuất:** `['101/2015/qh13+454#0', '41/2019/qh14+138#0', '64/2011/nđ-cp+8#1', '53/2010/qh12+116#0', '41/2019/qh14+136#0']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Người bị bắt buộc chữa bệnh sẽ được điều trị tại cơ sở bắt buộc chữa bệnh tâm thần do Viện kiểm sát hoặc Tòa án chỉ định.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Cơ sở này do Viện kiểm sát hoặc Tòa án chỉ định"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** Top-5 không có điều vàng `41/2019/qh14+133` (Luật Thi hành án hình sự 2019) mà lấy `101/2015/qh13+454` (Bộ luật Tố tụng hình sự 2015) nên mô hình trả lời theo quy định của BLTTHS.

### Mẫu ZALO-02 — Cấu hình `C3-E5-R0` | Mã câu hỏi `ff3be43955f04b55a0d4d16c502b6d58`

- **Câu hỏi:** Mức phạt khi điều khiển xe ô tô đi ngược chiều trên đường có biển cấm đi ngược chiều?
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+6#12', '100/2019/nđ-cp+5#20', '100/2019/nđ-cp+7#13', '100/2019/nđ-cp+5#16', '100/2019/nđ-cp+6#13']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Mức phạt tùy thuộc vào hậu quả của hành vi:
- Nếu **gây tai nạn giao thông**: Phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng (khoản 8 điểm a) hoặc từ 6.000.000 đồng đến 8.000.000 đồng (khoản 8 điểm a, tùy điều khoản áp dụng).
- Nếu **không gây tai nạn giao thông**: Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng (khoản 1) hoặc từ 3.000.000 đồng đến 5.000.000 đồng (khoản 4 điểm c).
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Nếu gây tai nạn giao thông: Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi về xe ô tô đi ngược chiều (`100/2019/nđ-cp+5`), nhưng các chunk `C3` trong top-5 mất tiêu đề Điều và chứa cả `100/2019/nđ-cp+7#13` (Điều 7: máy kéo, phạt 6–8 triệu), làm mô hình ghép nhầm mức phạt 6–8 triệu của Điều 7 vào câu trả lời.

### Mẫu ZALO-03 — Cấu hình `C3-E0-R0` | Mã câu hỏi `61ca2e2e85ce7af6a08d3bc5313b6cb5`

- **Câu hỏi:** Đánh dấu ngư cụ khai thác thủy sản tại ngư trường được quy định như thế nào?
- **Tài liệu vàng:** `['19/2018/tt-bnnptnt+12']` | **Top-5 chunk truy xuất:** `['19/2018/tt-bnnptnt+12#0', '19/2018/tt-bnnptnt+1#0', '18/2017/qh14+52#1', '42/2019/nđ-cp+27#0', '19/2018/tt-bnnptnt+13#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Việc đánh dấu ngư cụ khai thác thủy sản tại ngư trường được quy định như sau: nghề câu vàng, lưới rê khi vàng lưới và nghề lưới kéo phải đánh dấu theo quy định của Quy tắc phòng ngừa tàu thuyền đâm va trên biển; nghề sử dụng chà trên biển phải có dấu hiệu chỉ rõ khu vực đang hoạt động; đồng thời tổ chức, cá nhân khai thác thủy sản phải đánh dấu ngư cụ đang sử dụng tại ngư trường theo quy định của Bộ trưởng Bộ Nông nghiệp và Phát triển nông thôn.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Tổ chức, cá nhân khai thác thủy sản phải đánh dấu ngư cụ đang sử dụng tại ngư trường theo quy định của Bộ trưởng Bộ Nông nghiệp và Phát triển nông thôn"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **3. Nhiễu từ đoạn không liên quan**
- **Giải thích:** Top-5 có điều vàng `19/2018/tt-bnnptnt+12#0` (`correctness = 2`), nhưng kèm thêm `18/2017/qh14+52#1` (Điều 52 Luật Thủy sản) nên mô hình tổng hợp thêm mệnh đề từ Luật Thủy sản nằm ngoài điều luật vàng.

### Mẫu ZALO-04 — Cấu hình `C3-E3-R1` | Mã câu hỏi `8023b031184aa2d7b8d26bde390a06d7`

- **Câu hỏi:** Mức phạt khi điều khiển xe ô tô vượt xe trong những trường hợp không được vượt
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+5#16', '100/2019/nđ-cp+6#11', '100/2019/nđ-cp+23#0', '100/2019/nđ-cp+33#0', '100/2019/nđ-cp+6#1']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Phạt tiền từ 600.000 đồng đến 1.000.000 đồng.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Mức phạt khi điều khiển xe ô tô vượt xe trong những trường hợp không được vượt là từ 600.000 đồng đến 1.000.000 đồng."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi mức phạt xe ô tô vượt xe không đúng quy định (`100/2019/nđ-cp+5`, phạt 3–5 triệu). Top-5 có `100/2019/nđ-cp+6#11` (Điều 6: xe máy vượt xe phạt 600.000–1.000.000 đồng) không gắn tiêu đề Điều 6 nên mô hình áp nhầm mức phạt xe máy cho xe ô tô.

### Mẫu ZALO-05 — Cấu hình `C4-E3-R0` | Mã câu hỏi `d97142b6fdb9f07251f43cac696b9df3`

- **Câu hỏi:** Xe ô tô không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ sẽ bị xử phạt bao nhiêu?
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['142/2017/nđ-cp+17#0', '100/2019/nđ-cp+5#0', '100/2019/nđ-cp+8#0', '100/2019/nđ-cp+10#0', '100/2019/nđ-cp+6#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Phạt tiền từ 200.000 đồng đến 300.000 đồng.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Phạt tiền từ 200.000 đồng đến 300.000 đồng."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **2. Chunk cắt mất thông tin**
- **Giải thích:** Cấu hình `C4-E3-R0` truy xuất đúng nguyên Điều 5 (`100/2019/nđ-cp+5#0`), nhưng vì nguyên Điều 5 quá dài nên bị cắt ở trần `CTX_LIMIT = 1024` token, làm mất khoản quy định hành vi xe ô tô chạy từ trong ngõ không nhường đường.

### Mẫu ZALO-06 — Cấu hình `C4-E3-R0` | Mã câu hỏi `a0bc8ef92770b546ed517bd5e1d181eb`

- **Câu hỏi:** Loại trừ yếu tố khách quan khi xác định quỹ tiền lương, thù lao trong doanh nghiệp nhà nước được quy định như thế nào?
- **Tài liệu vàng:** `['31/2016/tt-blđtbxh+8']` | **Top-5 chunk truy xuất:** `['53/2016/nđ-cp+7#0', '31/2016/tt-blđtbxh+8#0', '20/2020/nđ-cp+4#0', '33/2016/tt-blđtbxh+10#0', '27/2016/tt-blđtbxh+13#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Theo ngữ cảnh, việc loại trừ yếu tố khách quan khi xác định quỹ tiền lương, thù lao trong doanh nghiệp nhà nước được quy định tại Điều 7, Điều 8, Điều 4 và Điều 13, bao gồm các yếu tố như: Nhà nước điều chỉnh giá, ưu đãi thuế, tăng/giảm vốn nhà nước, điều chỉnh cơ chế chính sách, yêu cầu di dời địa điểm, các nhiệm vụ an sinh xã hội, mở rộng sản xuất, đầu tư mới, chênh lệch trả thưởng xổ số, và các nguyên nhân bất khả kháng (thiên tai, hỏa hoạn, dịch bệnh, chiến tranh).
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Việc loại trừ yếu tố khách quan khi xác định quỹ tiền lương, thù lao trong doanh nghiệp nhà nước được quy định tại Điều 7, Điều 8, Điều 4 và Điều 13", "Các yếu tố bao gồm: Nhà nước điều chỉnh giá, ưu đãi thuế, tăng/giảm vốn nhà nước, điều chỉnh cơ chế chính sách, yêu cầu di dời địa điểm", "Các yếu tố bao gồm: các nhiệm vụ an sinh xã hội, mở rộng sản xuất, đầu tư mới", "Các yếu tố bao gồm: chênh lệch trả thưởng xổ số", "Các yếu tố bao gồm: các nguyên nhân bất khả kháng (thiên tai, hỏa hoạn, dịch bệnh, chiến tranh)"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = None`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Top-5 chứa 5 điều luật từ 5 văn bản khác nhau cùng quy định về "loại trừ yếu tố khách quan khi xác định quỹ tiền lương" (`53/2016/nđ-cp+7`, `31/2016/tt-blđtbxh+8`, `20/2020/nđ-cp+4`, `33/2016/tt-blđtbxh+10`, `27/2016/tt-blđtbxh+13`); mô hình trích dẫn gộp cả Điều 7, 8, 4, 13 (`wrong_article = True`).

### Mẫu ZALO-07 — Cấu hình `C3-E5-R0` | Mã câu hỏi `e492714e89c323c3da653b430dac254d`

- **Câu hỏi:** Người được hưởng án treo có được rút hết thời gian thử thách không?
- **Tài liệu vàng:** `['41/2019/qh14+89']` | **Top-5 chunk truy xuất:** `['41/2019/qh14+89#0', '08/2012/ttlt-bca-bqp-tandtc-vksndtc+4#1', '08/2012/ttlt-bca-bqp-tandtc-vksndtc+4#0', '41/2019/qh14+89#1', '08/2012/ttlt-bca-bqp-tandtc-vksndtc+6#2']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Có, người được hưởng án treo có thể được rút hết thời gian thử thách còn lại nếu đã chấp hành được một phần hai thời gian thử thách, có nhiều tiến bộ và được cơ quan giám sát giáo dục đề nghị, hoặc trong trường hợp lập công hoặc mắc bệnh hiểm nghèo.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Người được hưởng án treo có thể được rút hết thời gian thử thách còn lại nếu đã chấp hành được một phần hai thời gian thử thách, có nhiều tiến bộ và được cơ quan giám sát giáo dục đề nghị"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Top-5 có đủ cả 2 chunk của điều vàng `41/2019/qh14+89` (`#0` và `#1`), nhưng mô hình trộn điều kiện "rút ngắn một phần thời gian thử thách" ở Khoản 1 với điều kiện "rút hết thời gian thử thách còn lại" (khi lập công hoặc bệnh hiểm nghèo) ở Khoản 2.

### Mẫu ZALO-08 — Cấu hình `C3-E3-R1` | Mã câu hỏi `f07141f2b40d488b351192302afeb85c`

- **Câu hỏi:** Chạy xe ô tô chuyển hướng không giảm tốc độ sẽ bị xử phạt bao nhiêu?
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+6#9', '100/2019/nđ-cp+5#8', '100/2019/nđ-cp+7#13', '100/2019/nđ-cp+5#20', '100/2019/nđ-cp+6#13']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Chạy xe ô tô chuyển hướng không giảm tốc độ sẽ bị phạt tiền từ 400.000 đồng đến 600.000 đồng hoặc từ 800.000 đồng đến 1.000.000 đồng tùy thuộc vào mức độ vi phạm cụ thể theo quy định.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Chạy xe ô tô chuyển hướng không giảm tốc độ sẽ bị phạt tiền từ 400.000 đồng đến 600.000 đồng"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi xe ô tô chuyển hướng không giảm tốc độ (`100/2019/nđ-cp+5#8`: 800k–1tr). Top-5 xếp `100/2019/nđ-cp+6#9` (Điều 6: xe máy phạt 400k–600k) lên vị trí #1 và thiếu tiêu đề Điều, làm mô hình nêu cả mức phạt 400k–600k của Điều 6.

### Mẫu ZALO-09 — Cấu hình `C4-E3-R0` | Mã câu hỏi `93a095b3bb5671b1c718b1c7b9d21a16`

- **Câu hỏi:** Tổ chức lựa chọn nhà thầu và bàn giao mặt bằng thi công nạo vét duy tu luồng đường thủy nội địa được quy định như thế nào?
- **Tài liệu vàng:** `['33/2019/tt-bgtvt+6']` | **Top-5 chunk truy xuất:** `['159/2018/nđ-cp+17#0', '159/2018/nđ-cp+11#0', '159/2018/nđ-cp+19#0', '35/2019/tt-bgtvt+8#0', '159/2018/nđ-cp+12#0']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Đối với công trình nạo vét duy tu luồng đường thủy nội địa quốc gia, Cơ quan quản lý đường thủy nội địa khu vực được giao tổ chức lựa chọn nhà thầu và trình Cục Đường thủy nội địa Việt Nam phê duyệt; đối với công trình nạo vét duy tu luồng đường thủy nội địa địa phương, Ủy ban nhân dân cấp tỉnh tổ chức thực hiện công tác lựa chọn nhà thầu.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Đối với công trình nạo vét duy tu luồng đường thủy nội địa quốc gia, Cơ quan quản lý đường thủy nội địa khu vực được giao tổ chức lựa chọn nhà thầu và trình Cục Đường thủy nội địa Việt Nam phê duyệt", "đối với công trình nạo vét duy tu luồng đường thủy nội địa địa phương, Ủy ban nhân dân cấp tỉnh tổ chức thực hiện công tác lựa chọn nhà thầu"]
- **Điểm Judge:** `correctness = 1`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** Top-5 không chứa điều vàng `33/2019/tt-bgtvt+6` (luồng đường thủy nội địa) mà lấy các điều của `159/2018/nđ-cp` và `35/2019/tt-bgtvt+8` (luồng hàng hải).

### Mẫu ZALO-10 — Cấu hình `C3-E5-R0` | Mã câu hỏi `6f9703de97210d152655eff80145f384`

- **Câu hỏi:** Không thực hiện hợp đồng có bị mất tiền cọc không?
- **Tài liệu vàng:** `['91/2015/qh13+328']` | **Top-5 chunk truy xuất:** `['91/2015/qh13+328#0', '176/2016/tt-btc+1#7', '51/2014/qh13+62#0', '98/2020/nđ-cp+51#0', '91/2015/qh13+426#0']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Có, nếu bên đặt cọc từ chối việc giao kết hoặc thực hiện hợp đồng thì tài sản đặt cọc thuộc về bên nhận đặt cọc.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Không thực hiện hợp đồng có bị mất tiền cọc không?"]
- **Điểm Judge:** `correctness = 2`, `H_gold = 1`, `H_ctx = 1`, `oracle H_gold = 1`
- **Nhãn nguyên nhân:** **5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai**
- **Giải thích:** Top-5 chứa đúng điều vàng `91/2015/qh13+328#0` (Điều 328 BLDS về Đặt cọc) và câu trả lời đúng hoàn toàn (`correctness = 2`), nhưng ở cả RAG lẫn `oracle` (`ora_h_gold = 1`) Judge tách mệnh đề dẫn nhập không khớp nguyên văn câu chữ điều luật.

### Mẫu ZALO-11 — Cấu hình `C5-E3-R0` | Mã câu hỏi `745fe5c67f6cb233e3cc88d823580c89`

- **Câu hỏi:** Mức phạt khi tự ý xây dựng hoặc thành lập bến xe, bãi đỗ xe, trạm dừng nghỉ, trạm thu phí đường bộ
- **Tài liệu vàng:** `['100/2019/nđ-cp+14']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+14#1', '100/2019/nđ-cp+12#21', '100/2019/nđ-cp+14#0', '96/2020/nđ-cp+10#5', '100/2019/nđ-cp+12#20']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Phạt tiền từ 15.000.000 đồng đến 20.000.000 đồng đối với cá nhân và từ 30.000.000 đồng đến 40.000.000 đồng đối với tổ chức.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Phạt tiền từ 15.000.000 đồng đến 20.000.000 đồng đối với cá nhân", "Phạt tiền từ 30.000.000 đồng đến 40.000.000 đồng đối với tổ chức"]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **2. Chunk cắt mất thông tin**
- **Giải thích:** Câu hỏi hỏi Khoản 2 Điều 14 (`100/2019/nđ-cp+14`: tự ý xây dựng bến xe, bãi đỗ xe, trạm dừng nghỉ, trạm thu phí phạt 40–60 triệu). Top-5 chỉ chứa chunk `#0` (Khoản 1: phạt 15–20 triệu) và `#1` (Khoản 3: biện pháp khắc phục), thiếu chunk Khoản 2 nên mô hình lấy mức phạt của Khoản 1.

### Mẫu ZALO-12 — Cấu hình `C3-E3-R1` | Mã câu hỏi `1c06a80f4ea9f55a15371bcc9f9c4b71`

- **Câu hỏi:** Mức phạt khi điều khiển xe ô tô lạng lách
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+5#20', '100/2019/nđ-cp+6#14', '100/2019/nđ-cp+30#23', '100/2019/nđ-cp+30#22', '100/2019/nđ-cp+8#5']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện hành vi lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện hành vi lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi xe ô tô lạng lách (`100/2019/nđ-cp+5`: phạt 10–12 triệu). Top-5 thiếu chunk khoản lạng lách của Điều 5 nhưng có `100/2019/nđ-cp+6#14` (Điều 6: xe máy lạng lách phạt 6–8 triệu) không có tiêu đề Điều 6, nên mô hình áp nhầm mức phạt 6–8 triệu của Điều 6.

### Mẫu ZALO-13 — Cấu hình `C4-E3-R0` | Mã câu hỏi `caf09404d5d5c42e5829396a25eedc8d`

- **Câu hỏi:** Mức phạt khi chạy xe ô tô quá tốc độ quy định trên 20 km/h đến 35 km/h
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['142/2017/nđ-cp+17#0', '100/2019/nđ-cp+20#0', '100/2019/nđ-cp+25#0', '100/2019/nđ-cp+30#0', '132/2015/nđ-cp+21#0']` (Trúng tài liệu vàng trong top-5: `False`)
- **Câu trả lời của mô hình:** Mức phạt tiền từ 5.000.000 đồng đến 6.000.000 đồng.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Mức phạt tiền từ 5.000.000 đồng đến 6.000.000 đồng."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **1. Truy xuất sai**
- **Giải thích:** Cấu hình `C4-E3-R0` nhúng nguyên Điều 5 bị cắt ở 512 token đầu nên không khớp truy vấn "chạy quá tốc độ trên 20 km/h đến 35 km/h"; top-5 không chứa `100/2019/nđ-cp+5`.

### Mẫu ZALO-14 — Cấu hình `C3-E3-R0` | Mã câu hỏi `5eac9d1fa1fca2aaa72c6ba9336ac3ce`

- **Câu hỏi:** Điều khiển xe ô tô không đi bên phải theo chiều đi sẽ bị xử phạt bao nhiêu?
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+5#20', '100/2019/nđ-cp+7#13', '100/2019/nđ-cp+6#12', '100/2019/nđ-cp+5#16', '100/2019/nđ-cp+8#1']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Phạt tiền từ 80.000 đồng đến 100.000 đồng.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Phạt tiền từ 80.000 đồng đến 100.000 đồng."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi xe ô tô không đi bên phải theo chiều đi (`100/2019/nđ-cp+5`). Top-5 chứa `100/2019/nđ-cp+8#1` (Điều 8: xe đạp, xe thô sơ không đi bên phải theo chiều đi phạt 80.000–100.000 đồng) bị mất tiêu đề Điều 8 trong `C3`, khiến mô hình trả lời mức phạt của xe đạp cho xe ô tô.

### Mẫu ZALO-15 — Cấu hình `C3-E3-R1` | Mã câu hỏi `b68bab46b1e27ef4b41c87fb0a1e3d8c`

- **Câu hỏi:** Mức phạt khi chạy xe ô tô bấm còi, rú ga liên tục trong đô thị, khu đông dân cư được quy định như thế nào?
- **Tài liệu vàng:** `['100/2019/nđ-cp+5']` | **Top-5 chunk truy xuất:** `['100/2019/nđ-cp+5#8', '100/2019/nđ-cp+6#9', '100/2019/nđ-cp+7#6', '100/2019/nđ-cp+30#23', '100/2019/nđ-cp+30#14']` (Trúng tài liệu vàng trong top-5: `True`)
- **Câu trả lời của mô hình:** Mức phạt đối với hành vi bấm còi, rú ga liên tục trong đô thị, khu đông dân cư là từ 400.000 đồng đến 600.000 đồng.
- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** ["Mức phạt đối với hành vi bấm còi, rú ga liên tục trong đô thị, khu đông dân cư là từ 400.000 đồng đến 600.000 đồng."]
- **Điểm Judge:** `correctness = 0`, `H_gold = 1`, `H_ctx = 0`, `oracle H_gold = 0`
- **Nhãn nguyên nhân:** **4. Nhầm điều luật**
- **Giải thích:** Câu hỏi hỏi xe ô tô bấm còi, rú ga liên tục (`100/2019/nđ-cp+5`: phạt 800k–1tr). Top-5 có `100/2019/nđ-cp+6#9` (Điều 6: xe máy phạt 400k–600k) không có tiêu đề Điều 6 trong `C3`, khiến mô hình lấy mức phạt 400k–600k của Điều 6.

