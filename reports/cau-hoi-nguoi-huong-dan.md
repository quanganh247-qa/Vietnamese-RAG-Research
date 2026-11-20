# Thư gửi người hướng dẫn (bản nháp, gửi ngày 12/11)

Bản nháp để chép vào email hoặc tin nhắn. Sửa cách xưng hô cho phù hợp trước khi gửi.

---

**Tiêu đề:** Xin ý kiến về phạm vi và hình thức nộp đề tài RAG tiếng Việt (hạn 12/12)

Kính gửi Thầy/Cô,

Em đang thực hiện đề tài "Đánh giá ảnh hưởng của các lựa chọn thiết kế đến độ chính xác và ảo giác trong RAG tiếng Việt". Đề cương đầy đủ cần khoảng 16 tuần, trong khi hạn nộp là trước 12/12, nên em dự định thu hẹp phạm vi để kịp có sản phẩm chạy được và kết quả đo thật. Em xin ý kiến Thầy/Cô về ba điểm:

1. **Thứ phải nộp trước 12/12** là gì (báo cáo đề tài, bài báo, hay báo cáo tiến độ) và nộp ở đâu ạ?
2. **Phạm vi thu hẹp** dưới đây có chấp nhận được không ạ?
3. **Hình thức nộp sản phẩm:** demo trực tiếp, video demo, hay chỉ cần báo cáo và mã nguồn ạ?

**Phạm vi em đề xuất:**

| Hạng mục | Đề cương | Đề xuất cho hạn 12/12 |
|---|---|---|
| Phân đoạn | 6 chiến lược | 4 chiến lược, gồm ViStructChunk cho văn bản luật |
| Truy xuất | BM25, 4 mô hình nhúng, hybrid | BM25, `BAAI/bge-m3`, hybrid; thêm 2 mô hình nhúng ở bước chỉ đánh giá truy xuất |
| Xếp hạng lại | 3 reranker | 1 reranker |
| Đánh giá truy xuất | 144 cấu hình | 50 cấu hình trên Zalo Legal, 30 trên ViQuAD |
| Đánh giá đầu-cuối | Khoảng 20 cấu hình × 1.000 câu mỗi bộ | 9 và 7 cấu hình × 400 câu mỗi bộ (280 trả lời được, 120 không) |
| Nhãn người | 300 mẫu, hai người | 100 mẫu |
| Khuyến nghị | Biên Pareto, điểm theo kịch bản | Một bảng khuyến nghị theo miền, trong phạm vi các cấu hình đã thử |
| Sản phẩm | Pipeline, bộ dữ liệu, khóa luận | Hệ thống RAG có demo web, mã nguồn, kết quả đánh giá, báo cáo |

Hai đóng góp chính của đề cương vẫn được giữ: chỉ số ảo giác quy cho truy xuất (RAH, cần hai điều kiện closed-book và oracle) và chiến lược phân đoạn ViStructChunk. Hạn chế chính là cỡ mẫu nhỏ hơn nên chỉ phát hiện được khác biệt lớn giữa các cấu hình (khoảng tin cậy rộng khoảng ±5 điểm phần trăm).

Nếu Thầy/Cô yêu cầu đủ phạm vi như đề cương thì em xin phép trao đổi thêm về thời hạn, vì 30 ngày không đủ để chạy toàn bộ thực nghiệm.

Em mong nhận được ý kiến của Thầy/Cô trước ngày 16/11 để kịp điều chỉnh kế hoạch. Em sẽ gửi bản tóm tắt thiết kế một trang vào ngày 25/11.

Em cảm ơn Thầy/Cô.

Trân trọng,
[Họ tên]
