"""Sinh notebooks/05_tuan2_tiep_tuc.ipynb từ mã hiện tại trong src/ragvi/*.py.

Notebook 02, 03 (Tuần 1) và 04 (Tuần 2 đợt 1: Ngày 8, 9, 10 phần đầu) được giữ nguyên làm bản ghi.
Notebook 05 chạy tiếp phần còn lại của Tuần 2:
- Judge trên dev (Qwen/Qwen3-8B) + xuất 2 phiếu gán nhãn tay 100 câu dev ẩn cấu hình (Ngày 11–12).
- Nhúng nốt c5 và c5_nohead trên Zalo với checkpoint mỗi 20.000 chunk + tự động fp16/bf16 theo GPU (T4/L4/A100).

Chạy từ bất kỳ đâu: python scripts/build_colab_notebook.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'notebooks' / '05_tuan2_tiep_tuc.ipynb'
cells = []


def add(title, note, code):
    cells.append({'cell_type': 'markdown', 'metadata': {}, 'source': f'### {title}\n\n{note}'})
    cells.append({'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': code})


cells.append({'cell_type': 'markdown', 'metadata': {}, 'source': (
    '# Tuần 2 (tiếp tục): Judge trên dev, phiếu gán nhãn 100 câu, và nhúng nốt C5 / C5_nohead có checkpoint\n\n'
    'Notebook sinh tự động bởi `scripts/build_colab_notebook.py` từ `src/ragvi/` (đã nâng cấp `embed()` hỗ trợ '
    'checkpoint mỗi 20.000 chunk và tự động bật `bf16`/`fp16` + `batch_size` theo GPU T4/L4/A100).\n'
    'Các kết quả Ngày 8 (`GEN_MODEL = Qwen/Qwen2.5-7B-Instruct`, `JUDGE_MODEL = Qwen/Qwen3-8B`), Ngày 9, Reranker R1 '
    'và 6/8 lượt nhúng `BAAI/bge-m3` đã lưu trên Drive từ notebook 04.')})

add('[CHẠY MỘT LẦN / MỖI RUNTIME MỚI] Cài thư viện',
    'Cài các thư viện cần thiết cho retrieval, rerank, generate và judge 4-bit.',
    '%pip install -q rank_bm25 underthesea sentence-transformers datasets bitsandbytes accelerate')

add('[CHẠY MỘT LẦN / MỖI RUNTIME MỚI] Kết nối Google Drive',
    'Kết nối Google Drive chứa dữ liệu và các file đệm từ notebook 02–04.',
    "from google.colab import drive\n\ndrive.mount('/content/drive')")

add('[TÁI SỬ DỤNG] Đường dẫn và kiểm tra GPU',
    'In thông tin GPU đang kết nối (T4 / L4 / A100) và khởi tạo đường dẫn.',
    "from pathlib import Path\n"
    "import torch\n\n"
    "if not torch.cuda.is_available():\n"
    "    raise RuntimeError('Runtime không có GPU. Đổi sang runtime GPU (T4/L4/A100).')\n"
    "prop = torch.cuda.get_device_properties(0)\n"
    "print(f'GPU: {prop.name} | VRAM: {prop.total_memory / (1024**3):.1f} GB | bf16: {torch.cuda.is_bf16_supported()}')\n\n"
    "PROJECT_DIR = Path('/content/drive/MyDrive/Vietnamese-RAG-Research')\n"
    "if not PROJECT_DIR.is_dir():\n"
    "    raise FileNotFoundError(f'Không thấy {PROJECT_DIR}. Hãy chạy cell kết nối Drive trước.')\n"
    "P = PROJECT_DIR / 'data' / 'processed'\n"
    "Z = P / 'zalo_legal'\n"
    "EVAL = PROJECT_DIR / 'data' / 'eval'\n"
    "O = PROJECT_DIR / 'results' / 'tuan1'\n"
    "R = O / 'retrieval'\n"
    "O2 = PROJECT_DIR / 'results' / 'tuan2'\n"
    "GEN = O2 / 'generate'\n"
    "JUDGE = O2 / 'judge'\n"
    "SHEETS2 = O2 / 'review'\n"
    "GEN_MODEL = 'Qwen/Qwen2.5-7B-Instruct'\n"
    "JUDGE_MODEL = 'Qwen/Qwen3-8B'\n"
    "for d in (R, GEN, JUDGE, SHEETS2, Path('/content/src/ragvi')):\n"
    "    d.mkdir(parents=True, exist_ok=True)\n"
    "print(P, O, O2, EVAL, sep='\\n')")

for src in sorted((ROOT / 'src' / 'ragvi').glob('*.py')):
    add(f'[CHẠY MỘT LẦN / MỖI RUNTIME MỚI] Ghi mã `ragvi/{src.name}`',
        'Chép mã nguồn mới nhất (có checkpoint/resume embedding + fp16/bf16) vào `/content/src/ragvi/`.',
        f'%%writefile /content/src/ragvi/{src.name}\n' + src.read_text(encoding='utf-8'))

add('[TÁI SỬ DỤNG] Hàm chạy CLI và ghi log',
    'Đặt `PYTHONPATH` và định nghĩa `run()` để gọi CLI và ghi log vào `O2/logs/`.',
    "import os\nimport subprocess\nimport sys\n\n"
    "os.environ['PYTHONPATH'] = '/content/src'\n"
    "os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'\n"
    "if '/content/src' not in sys.path:\n"
    "    sys.path.insert(0, '/content/src')\n"
    "LOG = O2 / 'logs'\n"
    "LOG.mkdir(parents=True, exist_ok=True)\n\n\n"
    "def run(name, module, *args):\n"
    "    cmd = [sys.executable, '-m', module, *map(str, args)]\n"
    "    print('$', ' '.join(cmd))\n"
    "    with open(LOG / f'{name}.log', 'w', encoding='utf-8') as log, subprocess.Popen(\n"
    "            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:\n"
    "        for line in proc.stdout:\n"
    "            print(line, end='')\n"
    "            log.write(line)\n"
    "    if proc.returncode:\n"
    "        raise RuntimeError(f'Lệnh {name} lỗi (mã thoát {proc.returncode}); xem {LOG / name}.log')")

add('[CHẠY MỘT LẦN / KHI CẬP NHẬT] Ngày 11–12 (ưu tiên chạy trước): Judge trên dev (`Qwen/Qwen3-8B`) và xuất 2 phiếu gán nhãn tay 100 câu',
    'Chạy trước phần Judge (~15–20 phút) để có ngay 2 phiếu gán nhãn tay ẩn cấu hình (`human_dev_viquad.md`, `human_dev_zalo.md`) '
    'và kiểm tra JSON hợp lệ + chỉ số nhầm điều luật trên dev trước khi treo máy nhúng C5.',
    "for ds, corpus_unit, ds_key in [('viquad', EVAL / 'viquad' / 'corpus.jsonl', 'viquad'),\n"
    "                                ('zalo', Z, 'zalo_legal')]:\n"
    "    ans_path = GEN / f'dev_{ds}.jsonl'\n"
    "    q_dev = EVAL / ds / 'dev.jsonl'\n"
    "    c3_chunks = R / 'chunks' / f'{ds_key}__c3.jsonl'\n"
    "    sheet = SHEETS2 / f'human_dev_{ds}.md'\n"
    "    if not sheet.exists():\n"
    "        run(f'sheet_{ds}', 'ragvi.judge', ans_path, q_dev, corpus_unit, sheet,\n"
    "            '--chunks', c3_chunks, '--human-sheet', '--n', '50', '--seed', '0')\n"
    "    run(f'judge_{ds}_dev20', 'ragvi.judge', ans_path, q_dev, corpus_unit,\n"
    "        JUDGE / f'judge_dev_{ds}.jsonl', '--chunks', c3_chunks, '--model', JUDGE_MODEL, '--limit', '20')\n"
    "    run(f'judge_{ds}_dev_all', 'ragvi.judge', ans_path, q_dev, corpus_unit,\n"
    "        JUDGE / f'judge_dev_{ds}.jsonl', '--chunks', c3_chunks, '--model', JUDGE_MODEL)")

add('[CHẠY MỘT LẦN / KHI CẬP NHẬT] Ngày 10 (phần còn lại): Nhúng nốt `c5` và `c5_nohead` trên Zalo (có checkpoint mỗi 20.000 chunk + bf16/fp16)',
    '6/8 lượt `BAAI/bge-m3` đã xong ở notebook 04. Cell này nhúng nốt `c5` và `c5_nohead` với `bf16`/`fp16` và `batch_size` '
    'tự động theo GPU (T4=128, L4=256, A100=512). Mỗi 20.000 chunk lưu một shard vào `.parts/` trên Drive: nếu ngắt phiên hoặc '
    'đổi GPU chỉ cần chạy lại cell này sẽ tự nối tiếp.',
    "for c in ('c5', 'c5_nohead'):\n"
    "    run(f'ret_zalo_dense_{c}', 'ragvi.retrieval', Z, R,\n"
    "        '--run', 'zalo_phase_a', '--chunking', c, '--methods', 'dense',\n"
    "        '--questions', EVAL / 'zalo' / 'test.jsonl',\n"
    "        '--removed', EVAL / 'zalo' / 'removed_doc_ids.json')")

add('[TÁI SỬ DỤNG] Tổng hợp kết quả Tuần 2 và in 2 phiếu gán nhãn tay ra output',
    'In toàn bộ bảng truy xuất Giai đoạn A (`bge-m3`), tổng hợp Judge trên dev và xuất nội dung 2 phiếu gán nhãn tay.',
    "import json\n"
    "from ragvi.retrieval import format_table, read_rows, summarize\n\n"
    "for title, name in [('ViQuAD Phase A (dense bge-m3)', 'retrieval_viquad_phase_a.jsonl'),\n"
    "                    ('Zalo Phase A (dense bge-m3)', 'retrieval_zalo_phase_a.jsonl')]:\n"
    "    p = R / name\n"
    "    if p.exists():\n"
    "        methods = sorted({r['method'] for r in read_rows(p)})\n"
    "        print(f'\\n== {title} ==\\n' + format_table(summarize(p, methods)))\n\n"
    "print('\\n=== NGÀY 11: TỔNG HỢP JUDGE TRÊN DEV ===')\n"
    "for ds in ('viquad', 'zalo'):\n"
    "    p = JUDGE / f'judge_dev_{ds}.jsonl'\n"
    "    if p.exists():\n"
    "        rows = read_rows(p)\n"
    "        valid = [r for r in rows if r.get('error') is None]\n"
    "        non_ref = [r for r in valid if not r.get('refused')]\n"
    "        wrong_art = [r for r in non_ref if 'wrong_article' in r]\n"
    "        print(ds, json.dumps({\n"
    "            'total': len(rows), 'valid_json': len(valid), 'errors': len(rows) - len(valid),\n"
    "            'h_gold_mean': sum(r['h_gold'] for r in non_ref) / len(non_ref) if non_ref else None,\n"
    "            'correctness_mean': sum(r['correctness'] for r in valid) / len(valid) if valid else None,\n"
    "            'wrong_article_rate': sum(bool(r['wrong_article']) for r in wrong_art) / len(wrong_art) if wrong_art else None,\n"
    "        }, ensure_ascii=False))\n\n"
    "for name in ('human_dev_viquad.md', 'human_dev_zalo.md'):\n"
    "    path = SHEETS2 / name\n"
    "    print(f'<<<SHEET {name}>>>')\n"
    "    print(path.read_text(encoding='utf-8') if path.exists() else '(chưa có)')\n"
    "    print(f'<<<END {name}>>>')")

OUT.write_text(json.dumps({
    'cells': cells,
    'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
                 'language_info': {'name': 'python'}},
    'nbformat': 4, 'nbformat_minor': 4,
}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'Đã ghi {OUT} ({len(cells)} cell)')
