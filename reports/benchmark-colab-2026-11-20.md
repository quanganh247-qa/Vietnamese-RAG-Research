# Benchmark truy xuất trên Colab L4 — 20/11/2026

**Cấu hình:** C3–E3–R0 (phân đoạn theo câu, BGE-M3 dense, không reranker), top 20, không huấn luyện. Chạy bằng `bash colab_run.sh benchmark`. Sáu lượt truy xuất mất tổng cộng khoảng **15 phút 3 giây** theo thời gian thực của từng lệnh, gồm phân đoạn/nhúng và ghi kết quả, không tính cấp máy và cài gói.

| Tập | Đã truy xuất | Có điểm | Recall@5 | Recall@20 | MRR@10 | nDCG@5 |
|---|---:|---:|---:|---:|---:|---:|
| ViQuAD nguồn train | 28.454 | 19.238 | 87,44% | 94,90% | 0,7568 | 0,7820 |
| ViQuAD nguồn validation | 3.814 | 2.653 | 87,03% | 94,42% | 0,7475 | 0,7741 |
| ViQuAD nguồn test | 7.301 | 0 | — | — | — | — |
| ViQuAD dev đóng băng | 100 | 77 | 84,42% | 93,51% | 0,7379 | 0,7588 |
| ViQuAD test đóng băng | 400 | 280 | 88,93% | 95,71% | 0,7609 | 0,7894 |
| Zalo nguồn | 788 | 788 | 80,96% | 92,64% | 0,6567 | 0,6870 |
| Zalo dev đóng băng | 100 | 100 | 51,00% | 81,00% | 0,3740 | 0,3883 |
| Zalo test đóng băng | 400 | 280 | 81,43% | 92,68% | 0,6229 | 0,6642 |

- “Có điểm” chỉ gồm câu có đáp án/bằng chứng vàng. Test nguồn ViQuAD không có nhãn công khai trong bản dữ liệu này; không đồng nhất với test đóng băng. Tập đóng băng ViQuAD lấy từ train/validation; không cộng chung hai loại tập để tính điểm tổng. Zalo nguồn gồm 788 truy vấn duy nhất sau khử trùng; Zalo test đóng băng dùng kho đã bỏ điều luật theo D1/D6.
- Zalo dev có khoảng cách 30 điểm phần trăm giữa Recall@20 và Recall@5. Nên xem lại thứ hạng bằng chứng trên dev khi kiểm tra reranker; đây chưa phải kết quả của reranker.
- Bảng này chỉ báo cáo **truy xuất**. Ở thời điểm ghi nhận, chưa có kết quả sinh/chấm. Không suy ra correctness, H_gold, H_ctx, RAH hay fabrication từ điểm truy xuất.

Chỉ lưu số liệu tổng hợp lên Git; log runtime và JSONL nằm trong thư mục `results/` bị bỏ qua.
