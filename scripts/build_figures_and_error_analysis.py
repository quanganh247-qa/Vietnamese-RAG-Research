"""Sinh phiếu phân tích nguyên nhân 30 ca ảo giác (H_gold=1, seed=0) và 3 hình SVG cho báo cáo (Ngày 23: 04/12)."""
import html
import json
import random
from pathlib import Path

from ragvi.retrieval import read_rows

VIQUAD_NOTES = {
    1: ('1. Truy xuất sai',
        'Top-5 không chứa đoạn vàng `66911f17a6128315` (nêu con số 160 triệu USD) mà lấy đoạn khác trong bài Chiến tranh Đông Dương nêu viện trợ cuối chiến tranh trên 1 tỷ USD/năm.'),
    2: ('3. Nhiễu từ đoạn không liên quan',
        'Đoạn vàng `1f32b4a4454808ab#0` đứng thứ #1 và mô hình trả lời đủ ý đúng (`correctness = 2`), nhưng gộp thêm các mệnh đề mở rộng từ đoạn #2 `93f6add66bd918a0#0` cùng bài.'),
    3: ('1. Truy xuất sai',
        'Câu hỏi thiếu tên quốc gia (Mali) nên top-5 truy xuất các đoạn khảo sát tín nhiệm của Barack Obama và Vladimir Putin thay vì đoạn vàng về Amadou Toumani Touré.'),
    4: ('3. Nhiễu từ đoạn không liên quan',
        'Đoạn vàng `53add1b7f62c295c#0` liệt kê đúng 5 tổ chức quốc tế tại Pháp, nhưng đoạn #5 `d1c0a4ad25db4902#0` nói về Pierre de Coubertin và Thế vận hội tại Pháp khiến mô hình suy diễn thêm "Ủy ban Olympic Quốc tế".'),
    5: ('3. Nhiễu từ đoạn không liên quan',
        'Đoạn vàng `#1` liệt kê các trường phái học thuật tại Đại học Chicago, nhưng các đoạn `#2` và `#3` liệt kê bốn phân khoa sau đại học (Khoa học Sinh học, Khoa học Vật lý...) khiến mô hình gộp chung vào câu trả lời.'),
    6: ('1. Truy xuất sai',
        'BM25 (`C3-E0-R0`) không truy xuất được đoạn vàng `b4ed31bae96a648a` mà lấy các đoạn khác về quan hệ Cuba – Liên Xô.'),
    7: ('3. Nhiễu từ đoạn không liên quan',
        'Cùng câu hỏi Đại học Chicago như mẫu #5: mô hình gộp thêm trường Y khoa Pritzker và các chương trình sau đại học/ủy ban liên ngành từ đoạn #4 `e37073a6e4045c30#0`.'),
    8: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
        'Đoạn vàng `d7e0debdf9d41515#0` đứng thứ #1; câu văn trong đoạn vàng nêu tranh chấp với Hàn Quốc về đảo Liancourt rồi mới nêu vấn đề Triều Tiên. Cả RAG lẫn `oracle` (`ora_h_gold = 1`) đều trích mệnh đề đúng thực tế về đảo Liancourt nhưng lệch span đáp án vàng của ViQuAD.'),
    9: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
        'Mô hình trích nguyên câu văn trong đoạn vàng ("cho rằng chiến đấu là vô ích và bỏ chạy khỏi đất nước tới Bồ Đào Nha và sau này là Tây Ban Nha"), dài hơn cụm đáp án ngắn nên bị Judge đánh dấu phần ngoài span vàng ở cả RAG lẫn `oracle`.'),
    10: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
         'Đoạn vàng viết "không muốn làm quan cống hiến cho triều đình mới, do đó chọn các cách thức như tự sát...". Câu hỏi hỏi "Lý do nào" nhưng đáp án vàng lại gán cho các cách thức, còn mô hình trích đúng mệnh đề lý do.'),
    11: ('2. Chunk cắt mất thông tin',
         'Đoạn vàng `b6ff537d62ed77de` bị `C3` cắt thành hai chunk `#0` và `#1`. Top-5 chỉ chứa `#0` (nêu "khả năng toán học kỳ lạ"), còn cụm đáp án vàng "thông minh hơn người" nằm ở chunk `#1` ngoài top-5.'),
    12: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
         'Mô hình trích cả vế sau của câu trong đoạn vàng ("và ông đã lãnh đạo Hoa Kỳ qua Chiến tranh thế giới thứ hai"), vượt ra ngoài span đáp án vàng ngắn ở cả RAG lẫn `oracle` (`ora_h_gold = 1`).'),
    13: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
         'Cùng câu hỏi Franklin Delano Roosevelt như mẫu #12 ở cấu hình `C3-E3-R0`: trích thêm vế sau của cùng câu trong đoạn vàng (xuất hiện ở cả `oracle`).'),
    14: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
         'Đoạn vàng viết "Lisboa (6,3 triệu), Porto và miền bắc (4,4 triệu), Algarve (4,2 triệu)". Nhãn vàng ViQuAD gán nhầm con số 6,3 triệu của Lisboa cho Algarve, trong khi mô hình đọc đúng con số 4,2 triệu của Algarve ở cả RAG lẫn `oracle`.'),
    15: ('3. Nhiễu từ đoạn không liên quan',
         'Đoạn vàng `#1` nêu Chính phủ Lâm thời và Chính phủ Bắc Dương, nhưng các đoạn `#2, #3, #4` cùng bài Bắc Kinh nêu thủ đô triều Thanh và Cộng hòa Nhân dân Trung Hoa nên mô hình liệt kê gộp cả 4 chính phủ.'),
}

ZALO_NOTES = {
    1: ('1. Truy xuất sai',
        'Top-5 không có điều vàng `41/2019/qh14+133` (Luật Thi hành án hình sự 2019) mà lấy `101/2015/qh13+454` (Bộ luật Tố tụng hình sự 2015) nên mô hình trả lời theo quy định của BLTTHS.'),
    2: ('4. Nhầm điều luật',
        'Câu hỏi hỏi về xe ô tô đi ngược chiều (`100/2019/nđ-cp+5`), nhưng các chunk `C3` trong top-5 mất tiêu đề Điều và chứa cả `100/2019/nđ-cp+7#13` (Điều 7: máy kéo, phạt 6–8 triệu), làm mô hình ghép nhầm mức phạt 6–8 triệu của Điều 7 vào câu trả lời.'),
    3: ('3. Nhiễu từ đoạn không liên quan',
        'Top-5 có điều vàng `19/2018/tt-bnnptnt+12#0` (`correctness = 2`), nhưng kèm thêm `18/2017/qh14+52#1` (Điều 52 Luật Thủy sản) nên mô hình tổng hợp thêm mệnh đề từ Luật Thủy sản nằm ngoài điều luật vàng.'),
    4: ('4. Nhầm điều luật',
        'Câu hỏi hỏi mức phạt xe ô tô vượt xe không đúng quy định (`100/2019/nđ-cp+5`, phạt 3–5 triệu). Top-5 có `100/2019/nđ-cp+6#11` (Điều 6: xe máy vượt xe phạt 600.000–1.000.000 đồng) không gắn tiêu đề Điều 6 nên mô hình áp nhầm mức phạt xe máy cho xe ô tô.'),
    5: ('2. Chunk cắt mất thông tin',
        'Cấu hình `C4-E3-R0` truy xuất đúng nguyên Điều 5 (`100/2019/nđ-cp+5#0`), nhưng vì nguyên Điều 5 quá dài nên bị cắt ở trần `CTX_LIMIT = 1024` token, làm mất khoản quy định hành vi xe ô tô chạy từ trong ngõ không nhường đường.'),
    6: ('4. Nhầm điều luật',
        'Top-5 chứa 5 điều luật từ 5 văn bản khác nhau cùng quy định về "loại trừ yếu tố khách quan khi xác định quỹ tiền lương" (`53/2016/nđ-cp+7`, `31/2016/tt-blđtbxh+8`, `20/2020/nđ-cp+4`, `33/2016/tt-blđtbxh+10`, `27/2016/tt-blđtbxh+13`); mô hình trích dẫn gộp cả Điều 7, 8, 4, 13 (`wrong_article = True`).'),
    7: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
        'Top-5 có đủ cả 2 chunk của điều vàng `41/2019/qh14+89` (`#0` và `#1`), nhưng mô hình trộn điều kiện "rút ngắn một phần thời gian thử thách" ở Khoản 1 với điều kiện "rút hết thời gian thử thách còn lại" (khi lập công hoặc bệnh hiểm nghèo) ở Khoản 2.'),
    8: ('4. Nhầm điều luật',
        'Câu hỏi hỏi xe ô tô chuyển hướng không giảm tốc độ (`100/2019/nđ-cp+5#8`: 800k–1tr). Top-5 xếp `100/2019/nđ-cp+6#9` (Điều 6: xe máy phạt 400k–600k) lên vị trí #1 và thiếu tiêu đề Điều, làm mô hình nêu cả mức phạt 400k–600k của Điều 6.'),
    9: ('1. Truy xuất sai',
        'Top-5 không chứa điều vàng `33/2019/tt-bgtvt+6` (luồng đường thủy nội địa) mà lấy các điều của `159/2018/nđ-cp` và `35/2019/tt-bgtvt+8` (luồng hàng hải).'),
    10: ('5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai',
         'Top-5 chứa đúng điều vàng `91/2015/qh13+328#0` (Điều 328 BLDS về Đặt cọc) và câu trả lời đúng hoàn toàn (`correctness = 2`), nhưng ở cả RAG lẫn `oracle` (`ora_h_gold = 1`) Judge tách mệnh đề dẫn nhập không khớp nguyên văn câu chữ điều luật.'),
    11: ('2. Chunk cắt mất thông tin',
         'Câu hỏi hỏi Khoản 2 Điều 14 (`100/2019/nđ-cp+14`: tự ý xây dựng bến xe, bãi đỗ xe, trạm dừng nghỉ, trạm thu phí phạt 40–60 triệu). Top-5 chỉ chứa chunk `#0` (Khoản 1: phạt 15–20 triệu) và `#1` (Khoản 3: biện pháp khắc phục), thiếu chunk Khoản 2 nên mô hình lấy mức phạt của Khoản 1.'),
    12: ('4. Nhầm điều luật',
         'Câu hỏi hỏi xe ô tô lạng lách (`100/2019/nđ-cp+5`: phạt 10–12 triệu). Top-5 thiếu chunk khoản lạng lách của Điều 5 nhưng có `100/2019/nđ-cp+6#14` (Điều 6: xe máy lạng lách phạt 6–8 triệu) không có tiêu đề Điều 6, nên mô hình áp nhầm mức phạt 6–8 triệu của Điều 6.'),
    13: ('1. Truy xuất sai',
         'Cấu hình `C4-E3-R0` nhúng nguyên Điều 5 bị cắt ở 512 token đầu nên không khớp truy vấn "chạy quá tốc độ trên 20 km/h đến 35 km/h"; top-5 không chứa `100/2019/nđ-cp+5`.'),
    14: ('4. Nhầm điều luật',
         'Câu hỏi hỏi xe ô tô không đi bên phải theo chiều đi (`100/2019/nđ-cp+5`). Top-5 chứa `100/2019/nđ-cp+8#1` (Điều 8: xe đạp, xe thô sơ không đi bên phải theo chiều đi phạt 80.000–100.000 đồng) bị mất tiêu đề Điều 8 trong `C3`, khiến mô hình trả lời mức phạt của xe đạp cho xe ô tô.'),
    15: ('4. Nhầm điều luật',
         'Câu hỏi hỏi xe ô tô bấm còi, rú ga liên tục (`100/2019/nđ-cp+5`: phạt 800k–1tr). Top-5 có `100/2019/nđ-cp+6#9` (Điều 6: xe máy phạt 400k–600k) không có tiêu đề Điều 6 trong `C3`, khiến mô hình lấy mức phạt 400k–600k của Điều 6.'),
}


def build_error_sheet():
    vq_q = {json.loads(line)['qid']: json.loads(line)
            for line in open('results/colab/benchmark-Pa3Gy3aM/viquad_test_oracle.jsonl', encoding='utf-8')}
    zl_q = {json.loads(line)['qid']: json.loads(line)
            for line in open('results/colab/benchmark-Pa3Gy3aM/zalo_test_oracle.jsonl', encoding='utf-8')}

    lines = [
        '# Phân tích định tính 30 trường hợp ảo giác (`H_gold = 1`, Ngày 23 – 04/12)\n\n',
        'Chọn ngẫu nhiên 30 câu trả lời có `H_gold = 1` ở các cấu hình RAG Giai đoạn B (`15 ViQuAD test + 15 Zalo test`, `random.Random(0)`), ',
        'gắn nhãn theo 5 nhóm nguyên nhân của đề cương (Mục 5.4):\n',
        '1. **Truy xuất sai** (Top-5 không chứa đoạn/điều luật vàng).\n',
        '2. **Chunk cắt mất thông tin** (Top-5 trúng tài liệu/điều luật vàng nhưng thiếu chunk chứa khoản/câu đáp án hoặc bị cắt ở trần token).\n',
        '3. **Nhiễu từ đoạn không liên quan** (Top-5 có đoạn vàng nhưng mô hình tổng hợp/suy diễn thêm thông tin từ các đoạn khác trong top-5).\n',
        '4. **Nhầm điều luật** (Top-5 chứa các điều luật cùng chủ đề hoặc các chunk mất tiêu đề Điều/Văn bản làm mô hình áp nhầm mức phạt/quy định của điều luật khác).\n',
        '5. **Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai** (Top-5 có đủ thông tin đáp án vàng nhưng mô hình tự suy diễn hoặc trích vượt phạm vi đáp án vàng — lỗi nội tại ở tầng sinh/judge, thường xuất hiện ở cả `oracle`).\n\n',
        '## 1. Bảng tổng hợp phân bố nguyên nhân và đối chiếu với chỉ số RAH\n\n',
        '| Nhóm nguyên nhân | Thuộc tầng truy xuất / phân đoạn? | ViQuAD test (`n = 15`) | Zalo Legal test (`n = 15`) | Tổng (`n = 30`) |\n',
        '|---|:---:|---:|---:|---:|\n',
        '| 1. Truy xuất sai | Có | 3 (20,0%) | 3 (20,0%) | 6 (20,0%) |\n',
        '| 2. Chunk cắt mất thông tin | Có | 1 (6,7%) | 2 (13,3%) | 3 (10,0%) |\n',
        '| 3. Nhiễu từ đoạn không liên quan | Có | 5 (33,3%) | 1 (6,7%) | 6 (20,0%) |\n',
        '| 4. Nhầm điều luật | Có | 0 (0,0%) | **7 (46,7%)** | 7 (23,3%) |\n',
        '| 5. Truy xuất đúng nhưng mô hình bỏ qua / suy diễn sai | Không (nội tại tầng sinh) | **6 (40,0%)** | 2 (13,3%) | 8 (26,7%) |\n',
        '| **Tổng tỷ lệ quy cho truy xuất / phân đoạn (Nhóm 1–4)** | **Có** | **9 / 15 (60,0%)** *(3/15 = 20,0% không có ở Oracle)* | **13 / 15 (86,7%)** | **22 / 30 (73,3%)** |\n',
        '| **Đối chiếu tỷ phần định lượng `RAH / H_gold` (Mục 5.3)** | – | **32,5% – 46,5%** *(TB: 38,3%)* | **69,5% – 83,0%** *(TB: 76,3%)* | – |\n\n',
        '> **Nhận xét kiểm chứng chéo `RAH`:**\n',
        '> - Trên **Zalo Legal**, **13/15 ca (`86,7%`)** bắt nguồn trực tiếp từ tầng truy xuất và phân đoạn (đặc biệt là `Nhầm điều luật` chiếm `7/15 = 46,7%` khi các chunk `C3` của Nghị định `100/2019/NĐ-CP` mất tiêu đề Điều 5/6/7/8 nên mô hình áp nhầm mức phạt xe máy/xe đạp cho xe ô tô, cùng `3/15` ca truy xuất sai và `2/15` ca chunk cắt mất khoản), hoàn toàn nhất quán với tỷ phần định lượng **`RAH / H_gold = 69,5% – 83,0%`**.\n',
        '> - Trên **ViQuAD**, có tới **8/15 ca (`53,3%`)** cũng bị đánh dấu `H_gold = 1` ngay cả ở điều kiện **`oracle`** (do mô hình trích nguyên câu văn dài hơn span đáp án vàng ngắn hoặc gộp thêm thông tin từ các đoạn cùng bài Wikipedia), khớp chặt chẽ với việc `RAH / H_gold` trên ViQuAD chỉ chiếm **`32,5% – 46,5%`**.\n\n',
    ]

    for ds, title, q_map, notes in [
        ('viquad', '2. Chi tiết 15 trường hợp trên ViQuAD test (`seed = 0`)', vq_q, VIQUAD_NOTES),
        ('zalo', '3. Chi tiết 15 trường hợp trên Zalo Legal test (`seed = 0`)', zl_q, ZALO_NOTES),
    ]:
        lines.append(f'## {title}\n\n')
        ans_map = {(r['config'], r['qid']): r for r in read_rows(f'data/retrieval_cache/answers_{ds}_test.jsonl')}
        all_jdg = read_rows(f'data/retrieval_cache/judge_{ds}_test.jsonl')
        ora_map = {r['qid']: r for r in all_jdg if r['config'] == 'oracle'}
        jdg_rows = [r for r in all_jdg if r.get('h_gold') == 1 and r['config'] not in ('closed_book', 'oracle')]
        jdg_rows.sort(key=lambda r: (r['config'], r['qid']))
        picked = random.Random(0).sample(jdg_rows, 15)
        for i, j in enumerate(picked, 1):
            cfg, qid = j['config'], j['qid']
            a = ans_map[(cfg, qid)]
            q = q_map[qid]
            ora = ora_map.get(qid, {})
            cids = a.get('context_ids', [])
            top_docs = [c.rsplit('#', 1)[0] for c in cids]
            golds = set(q.get('gold_doc_ids') or [q.get('gold_doc_id')])
            has_gold = bool(golds & set(top_docs))
            cause, explain = notes[i]
            bad_claims = [c['text'] for c in (j.get('claims') or []) if not c.get('supported_by_gold')]
            lines.append(
                f'### Mẫu {ds.upper()}-{i:02d} — Cấu hình `{cfg}` | Mã câu hỏi `{qid}`\n\n'
                f'- **Câu hỏi:** {q["question"]}\n'
                f'- **Tài liệu vàng:** `{sorted(golds)}` | **Top-5 chunk truy xuất:** `{cids}` (Trúng tài liệu vàng trong top-5: `{has_gold}`)\n'
                f'- **Câu trả lời của mô hình:** {a["answer"]}\n'
                f'- **Mệnh đề bị Judge đánh dấu `supported_by_gold = false`:** {json.dumps(bad_claims, ensure_ascii=False)}\n'
                f'- **Điểm Judge:** `correctness = {j["correctness"]}`, `H_gold = {j["h_gold"]}`, `H_ctx = {j["h_ctx"]}`, `oracle H_gold = {ora.get("h_gold")}`\n'
                f'- **Nhãn nguyên nhân:** **{cause}**\n'
                f'- **Giải thích:** {explain}\n\n'
            )

    out_path = Path('reports/phieu/hallucination_30_cases.md')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(''.join(lines), encoding='utf-8')
    print(f'Wrote {out_path}')


def _rgb_for_val(v, vmin=0.58, vmax=0.93):
    t = max(0.0, min(1.0, (v - vmin) / max(vmax - vmin, 1e-6)))
    # Interpolate from light amber/rose (#fef3c7) -> teal (#2dd4bf) -> deep blue (#1d4ed8)
    if t < 0.5:
        u = t * 2.0
        r = int(254 + u * (45 - 254))
        g = int(243 + u * (212 - 243))
        b = int(199 + u * (191 - 199))
    else:
        u = (t - 0.5) * 2.0
        r = int(45 + u * (29 - 45))
        g = int(212 + u * (78 - 212))
        b = int(191 + u * (216 - 191))
    text_col = '#ffffff' if t > 0.58 else '#0f172a'
    return f'rgb({r},{g},{b})', text_col


def build_fig1_heatmap():
    pa = json.loads(Path('reports/phase_a_summary.json').read_text(encoding='utf-8'))
    zl = pa['zalo_test_phase_a']
    vq = pa['viquad_test_phase_a']

    w, h = 1120, 560
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="560" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="#0f172a">Hình 1: Bảng nhiệt nDCG@5 (và Recall@5) trong Giai đoạn A trên Zalo Legal (30 cấu hình) và ViQuAD (30 cấu hình)</text>',
    ]

    # Panel A: Zalo Legal (5 chunkings x 6 E*R methods)
    svg.append('<text x="290" y="68" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">A. Zalo Legal test (n = 280 câu trả lời được)</text>')
    zl_cols = [
        ('E0 (R0)', lambda c: f'bm25[{c}][word]'),
        ('E3 (R0)', lambda c: f'dense[{c}]'),
        ('E5 (R0)', lambda c: f'hybrid[{c}][word]'),
        ('E0+R1', lambda c: f'bm25[{c}][word]+r1'),
        ('E3+R1', lambda c: f'dense[{c}]+r1'),
        ('E5+R1', lambda c: f'hybrid[{c}][word]+r1'),
    ]
    zl_rows = [('C1 (256 tok)', 'c1'), ('C3 (Câu ≤256)', 'c3'), ('C4 (Nguyên điều)', 'c4'),
               ('C5 (ViStructChunk)', 'c5'), ('C5_nohead', 'c5_nohead')]
    x0, y0, cw, ch = 135, 105, 68, 64
    for j, (clab, _) in enumerate(zl_cols):
        svg.append(f'<text x="{x0 + j*cw + cw/2}" y="{y0 - 10}" text-anchor="middle" font-size="11" font-weight="600" fill="#334155">{html.escape(clab)}</text>')
    for i, (rlab, ckey) in enumerate(zl_rows):
        fw = '700' if ckey == 'c5' else '500'
        svg.append(f'<text x="{x0 - 8}" y="{y0 + i*ch + ch/2 + 4}" text-anchor="end" font-size="11.5" font-weight="{fw}" fill="#0f172a">{html.escape(rlab)}</text>')
        for j, (_, mfn) in enumerate(zl_cols):
            m = zl[mfn(ckey)]
            ndcg, r5 = m['nDCG@5'], m['Recall@5']
            bg, fg = _rgb_for_val(ndcg, 0.58, 0.93)
            rx, ry = x0 + j * cw, y0 + i * ch
            svg.append(f'<rect x="{rx}" y="{ry}" width="{cw-2}" height="{ch-2}" rx="4" fill="{bg}"/>')
            svg.append(f'<text x="{rx + cw/2 - 1}" y="{ry + 26}" text-anchor="middle" font-size="12" font-weight="700" fill="{fg}">{ndcg:.4f}</text>')
            svg.append(f'<text x="{rx + cw/2 - 1}" y="{ry + 45}" text-anchor="middle" font-size="10" fill="{fg}">({r5*100:.1f}%)</text>')

    # Panel B: ViQuAD (5 E methods x 6 C*R columns)
    svg.append('<text x="835" y="68" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">B. ViQuAD test (n = 280 câu trả lời được)</text>')
    vq_cols = [('C1 (R0)', 'c1', ''), ('C3 (R0)', 'c3', ''), ('C4 (R0)', 'c4', ''),
               ('C1+R1', 'c1', '+r1'), ('C3+R1', 'c3', '+r1'), ('C4+R1', 'c4', '+r1')]
    vq_rows = [
        ('E0 (BM25 từ)', lambda c, r: f'bm25[{c}][word]{r}'),
        ('E2 (VN-Embed-v2)', lambda c, r: f'dense[{c}][AITeamVN/Vietnamese_Embedding_v2]{r}'),
        ('E3 (BGE-M3)', lambda c, r: f'dense[{c}]{r}'),
        ('E4 (mE5-large)', lambda c, r: f'dense[{c}][intfloat/multilingual-e5-large]{r}'),
        ('E5 (Hybrid)', lambda c, r: f'hybrid[{c}][word]{r}'),
    ]
    x1 = 685
    for j, (clab, _, _) in enumerate(vq_cols):
        svg.append(f'<text x="{x1 + j*cw + cw/2}" y="{y0 - 10}" text-anchor="middle" font-size="11" font-weight="600" fill="#334155">{html.escape(clab)}</text>')
    for i, (rlab, mfn) in enumerate(vq_rows):
        svg.append(f'<text x="{x1 - 8}" y="{y0 + i*ch + ch/2 + 4}" text-anchor="end" font-size="11.5" font-weight="500" fill="#0f172a">{html.escape(rlab)}</text>')
        for j, (_, ckey, rtag) in enumerate(vq_cols):
            m = vq[mfn(ckey, rtag)]
            ndcg, r5 = m['nDCG@5'], m['Recall@5']
            bg, fg = _rgb_for_val(ndcg, 0.58, 0.93)
            rx, ry = x1 + j * cw, y0 + i * ch
            svg.append(f'<rect x="{rx}" y="{ry}" width="{cw-2}" height="{ch-2}" rx="4" fill="{bg}"/>')
            svg.append(f'<text x="{rx + cw/2 - 1}" y="{ry + 26}" text-anchor="middle" font-size="12" font-weight="700" fill="{fg}">{ndcg:.4f}</text>')
            svg.append(f'<text x="{rx + cw/2 - 1}" y="{ry + 45}" text-anchor="middle" font-size="10" fill="{fg}">({r5*100:.1f}%)</text>')

    svg.append('<text x="560" y="465" text-anchor="middle" font-size="11.5" fill="#475569">Chú thích: Dòng trên trong mỗi ô là nDCG@5; dòng dưới trong ngoặc đơn là Recall@5 (%). Trên Zalo Legal, C5 (ViStructChunk) đạt đỉnh ở cả 6 cột (tới 0,8369 / 91,6%).</text>')
    svg.append('</svg>')
    out = Path('reports/figures/fig1_phase_a_heatmap.svg')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(svg), encoding='utf-8')
    print(f'Wrote {out}')


def build_fig2_h_gold():
    pb = json.loads(Path('reports/phase_b_summary.json').read_text(encoding='utf-8'))
    w, h = 1100, 520
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="550" y="34" text-anchor="middle" font-size="17.5" font-weight="700" fill="#0f172a">Hình 2: Tỷ lệ ảo giác H_gold (%) và Độ đúng Correctness (/2) theo cấu hình Giai đoạn B kèm Khoảng tin cậy 95%</text>',
    ]

    panels = [
        ('A. Zalo Legal test (9 cấu hình)', pb['end_to_end']['zalo_test']['configs'],
         ['oracle', 'C4-E3-R0', 'C3-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C3-E0-R0', 'C5-E3-R0', 'C5_nohead-E3-R0', 'closed_book'], 145),
        ('B. ViQuAD test (7 cấu hình)', pb['end_to_end']['viquad_test']['configs'],
         ['oracle', 'C3-E0-R0', 'C1-E3-R0', 'C3-E3-R0', 'C3-E3-R1', 'C3-E5-R0', 'closed_book'], 685),
    ]

    for title, cfgs, order, x0 in panels:
        pw = 360
        svg.append(f'<text x="{x0 + pw/2}" y="68" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">{html.escape(title)}</text>')
        for pct in (0, 20, 40, 60, 80, 100):
            gx = x0 + (pct / 100.0) * pw
            svg.append(f'<line x1="{gx}" y1="88" x2="{gx}" y2="440" stroke="#e2e8f0" stroke-width="1"/>')
            svg.append(f'<text x="{gx}" y="458" text-anchor="middle" font-size="10.5" fill="#64748b">{pct}%</text>')
        for i, cfg in enumerate(order):
            info = cfgs[cfg]
            hg = info['h_gold'] * 100.0
            lo, hi = [x * 100.0 for x in info['ci95']['h_gold']]
            corr = info['correctness']
            ry = 98 + i * 37
            col = '#10b981' if cfg == 'oracle' else ('#ef4444' if cfg == 'closed_book' else ('#2563eb' if cfg == 'C5-E3-R0' else '#3b82f6'))
            fw = '700' if cfg in ('C5-E3-R0', 'C3-E3-R0', 'C3-E3-R1') else '500'
            svg.append(f'<text x="{x0 - 8}" y="{ry + 15}" text-anchor="end" font-size="11.5" font-weight="{fw}" fill="#0f172a">{html.escape(cfg)}</text>')
            bw = (hg / 100.0) * pw
            svg.append(f'<rect x="{x0}" y="{ry}" width="{bw:.1f}" height="22" rx="3" fill="{col}" opacity="0.85"/>')
            x_lo, x_hi = x0 + (lo / 100.0) * pw, x0 + (hi / 100.0) * pw
            svg.append(f'<line x1="{x_lo:.1f}" y1="{ry+11}" x2="{x_hi:.1f}" y2="{ry+11}" stroke="#0f172a" stroke-width="1.8"/>')
            svg.append(f'<line x1="{x_lo:.1f}" y1="{ry+6}" x2="{x_lo:.1f}" y2="{ry+16}" stroke="#0f172a" stroke-width="1.8"/>')
            svg.append(f'<line x1="{x_hi:.1f}" y1="{ry+6}" x2="{x_hi:.1f}" y2="{ry+16}" stroke="#0f172a" stroke-width="1.8"/>')
            label_x = max(x_hi + 6, x0 + bw + 6)
            svg.append(f'<text x="{label_x:.1f}" y="{ry + 15}" font-size="10.5" font-weight="600" fill="#1e293b">{hg:.1f}% (Corr={corr:.2f})</text>')

    svg.append('<text x="550" y="492" text-anchor="middle" font-size="11.5" fill="#475569">Chú thích: Thanh ngang biểu diễn H_gold (%) kèm đoạn thẳng khoảng tin cậy Cluster Bootstrap 95%; số trong ngoặc là điểm độ đúng Correctness (thang 0–2).</text>')
    svg.append('</svg>')
    out = Path('reports/figures/fig2_phase_b_h_gold_ci.svg')
    out.write_text('\n'.join(svg), encoding='utf-8')
    print(f'Wrote {out}')


def build_fig3_rah():
    pb = json.loads(Path('reports/phase_b_summary.json').read_text(encoding='utf-8'))
    w, h = 980, 480
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="490" y="34" text-anchor="middle" font-size="17.5" font-weight="700" fill="#0f172a">Hình 3: So sánh Ảo giác quy cho truy xuất (RAH = H_gold(k) − H_gold(oracle)) giữa hai miền kèm 95% CI</text>',
    ]

    items = [
        ('Zalo: C3-E3-R0 (Neo)', pb['end_to_end']['zalo_test']['configs']['C3-E3-R0'], '#dc2626'),
        ('Zalo: C4-E3-R0 (Nguyên điều)', pb['end_to_end']['zalo_test']['configs']['C4-E3-R0'], '#dc2626'),
        ('Zalo: C3-E3-R1 (Dense+R1)', pb['end_to_end']['zalo_test']['configs']['C3-E3-R1'], '#dc2626'),
        ('Zalo: C3-E5-R0 (Hybrid)', pb['end_to_end']['zalo_test']['configs']['C3-E5-R0'], '#dc2626'),
        ('Zalo: C3-E0-R0 (BM25)', pb['end_to_end']['zalo_test']['configs']['C3-E0-R0'], '#dc2626'),
        ('Zalo: C5-E3-R0 (ViStructChunk)', pb['end_to_end']['zalo_test']['configs']['C5-E3-R0'], '#b91c1c'),
        ('Zalo: C5_nohead-E3-R0 (Bỏ tiêu đề)', pb['end_to_end']['zalo_test']['configs']['C5_nohead-E3-R0'], '#991b1b'),
        ('ViQuAD: C3-E0-R0 (BM25)', pb['end_to_end']['viquad_test']['configs']['C3-E0-R0'], '#0284c7'),
        ('ViQuAD: C3-E3-R0 (Neo)', pb['end_to_end']['viquad_test']['configs']['C3-E3-R0'], '#0284c7'),
        ('ViQuAD: C1-E3-R0 (Cố định 256)', pb['end_to_end']['viquad_test']['configs']['C1-E3-R0'], '#0284c7'),
        ('ViQuAD: C3-E3-R1 (Dense+R1)', pb['end_to_end']['viquad_test']['configs']['C3-E3-R1'], '#0284c7'),
        ('ViQuAD: C3-E5-R0 (Hybrid)', pb['end_to_end']['viquad_test']['configs']['C3-E5-R0'], '#0284c7'),
    ]

    x0, pw = 250, 520
    max_pct = 35.0
    for pct in (0, 5, 10, 15, 20, 25, 30, 35):
        gx = x0 + (pct / max_pct) * pw
        svg.append(f'<line x1="{gx:.1f}" y1="68" x2="{gx:.1f}" y2="418" stroke="#e2e8f0" stroke-width="1"/>')
        svg.append(f'<text x="{gx:.1f}" y="436" text-anchor="middle" font-size="10.5" fill="#64748b">+{pct}%</text>')

    for i, (label, info, col) in enumerate(items):
        rah_info = info['rah_against_oracle']
        val = rah_info['value'] * 100.0
        lo, hi = [x * 100.0 for x in rah_info['ci95']]
        share = rah_info['share_of_h_gold'] * 100.0
        ry = 76 + i * 28
        svg.append(f'<text x="{x0 - 10}" y="{ry + 15}" text-anchor="end" font-size="11.5" font-weight="600" fill="#0f172a">{html.escape(label)}</text>')
        bw = (val / max_pct) * pw
        svg.append(f'<rect x="{x0}" y="{ry}" width="{bw:.1f}" height="20" rx="3" fill="{col}" opacity="0.85"/>')
        x_lo, x_hi = x0 + (lo / max_pct) * pw, x0 + (hi / max_pct) * pw
        svg.append(f'<line x1="{x_lo:.1f}" y1="{ry+10}" x2="{x_hi:.1f}" y2="{ry+10}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x_lo:.1f}" y1="{ry+5}" x2="{x_lo:.1f}" y2="{ry+15}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x_hi:.1f}" y1="{ry+5}" x2="{x_hi:.1f}" y2="{ry+15}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<text x="{x_hi + 8:.1f}" y="{ry + 14}" font-size="10.5" font-weight="600" fill="#1e293b">+{val:.2f}% (RAH/H_gold = {share:.1f}%)</text>')

    svg.append('<text x="490" y="465" text-anchor="middle" font-size="11.5" fill="#475569">Chú thích: Miền pháp luật Zalo (đỏ: RAH từ +17,46% đến +26,59%, chiếm 69,5–83,0% H_gold) cao gấp 2,2×–3,9× so với miền Wikipedia ViQuAD (xanh: +5,50% đến +9,57%).</text>')
    svg.append('</svg>')
    out = Path('reports/figures/fig3_rah_by_domain.svg')
    out.write_text('\n'.join(svg), encoding='utf-8')
    print(f'Wrote {out}')


if __name__ == '__main__':
    build_error_sheet()
    build_fig1_heatmap()
    build_fig2_h_gold()
    build_fig3_rah()
