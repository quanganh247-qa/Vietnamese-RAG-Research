"""Giao diện web Demo (Gradio): chọn cấu hình, xem câu trả lời và 5 đoạn căn cứ kèm nguồn (Ngày 16, 21, 23).

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src python -m ragvi.app [--llama-url http://127.0.0.1:18080] [--share]
"""
import argparse
import os

from ragvi import run

DISCLAIMER = (
    '⚠️ **Lưu ý sử dụng:**\n'
    '1. Kho văn bản pháp luật Zalo Legal chỉ bao gồm các văn bản đến năm 2021.\n'
    '2. Đây là công cụ tra cứu phục vụ nghiên cứu khoa học, không thay thế cho tư vấn pháp lý chính thức.'
)


def answer(dataset, c, e, rerank, question):
    """Hàm xử lý chính của giao diện Demo: trả về `(câu_trả_lời, bảng_5_đoạn_căn_cứ)`."""
    r = 'R1' if rerank else 'R0'
    if dataset == 'viquad' and c.upper().startswith('C5'):
        c = 'C3'
    passages = run.retrieve(dataset, c, e, r, question)
    text = run.generate(
        question, passages, dataset=dataset, c=c, e=e, r=r,
        llama_url=os.environ.get('RAGVI_LLAMA_URL'),
        model_name=os.environ.get('RAGVI_MODEL', 'unsloth/Qwen3.5-9B-GGUF:Q4_K_M'),
    )
    rows = [[p.source, round(p.score, 3), p.text] for p in passages]
    return text, rows


def build_interface():
    """Khởi tạo đối tượng `gr.Interface` với cấu hình mặc định là cấu hình khuyến nghị (`C5–E3–R0` / `C3–E3–R1`)."""
    import gradio as gr

    return gr.Interface(
        fn=answer,
        inputs=[
            gr.Dropdown(['zalo', 'viquad'], value='zalo', label='Bộ dữ liệu'),
            gr.Dropdown(['C1', 'C3', 'C4', 'C5'], value='C5',
                        label='Phân đoạn (mặc định khuyến nghị: C5 ViStructChunk cho luật, C3 cho Wikipedia)'),
            gr.Dropdown(['E0', 'E3', 'E5'], value='E3', label='Truy xuất (E0: BM25 tách từ, E3: BGE-M3, E5: Hybrid)'),
            gr.Checkbox(value=False, label='Xếp hạng lại (R1: BAAI/bge-reranker-v2-m3)'),
            gr.Textbox(label='Câu hỏi', placeholder='Nhập câu hỏi pháp luật hoặc bách khoa tiếng Việt...'),
        ],
        outputs=[
            gr.Textbox(label='Câu trả lời'),
            gr.Dataframe(headers=['Nguồn', 'Điểm', 'Đoạn văn'], label='5 đoạn căn cứ truy xuất'),
        ],
        title='RAG tiếng Việt: Độ chính xác truy xuất và Ảo giác (ViStructChunk & RAH)',
        description=DISCLAIMER,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--llama-url', help='URL của llama-server (nếu sinh trực tiếp cho câu hỏi mới)')
    parser.add_argument('--model', default='unsloth/Qwen3.5-9B-GGUF:Q4_K_M')
    parser.add_argument('--port', type=int, default=7860)
    parser.add_argument('--share', action='store_true')
    args = parser.parse_args(argv)
    if args.llama_url:
        os.environ['RAGVI_LLAMA_URL'] = args.llama_url
    os.environ['RAGVI_MODEL'] = args.model
    build_interface().launch(server_port=args.port, share=args.share)


if __name__ == '__main__':
    main()
