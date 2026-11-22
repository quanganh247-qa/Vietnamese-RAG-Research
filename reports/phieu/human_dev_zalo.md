# Phiếu gán nhãn tay đối chiếu Judge (Ngày 12–13)

Hướng dẫn: với mỗi mẫu (đã ẩn tên cấu hình), đọc Câu hỏi, Ngữ cảnh đã cung cấp, Bằng chứng vàng và Câu trả lời rồi đánh `[x]` vào đúng một ô cho mỗi dòng:
- `Correctness` (so với Bằng chứng vàng): `0` (sai), `1` (đúng một phần), `2` (đúng và đầy đủ).
- `H_gold`: Câu trả lời có mệnh đề nào KHÔNG được Bằng chứng vàng hỗ trợ không? (`0` = không, `1` = có).
- `H_ctx`: Câu trả lời có mệnh đề nào KHÔNG được Ngữ cảnh hỗ trợ không? (`0` = không, `1` = có, `NA` = không có ngữ cảnh).

---

## Mẫu 1 — `7e40ba0146`

**Câu hỏi:** Mức phạt khi chạy xe máy đi không đúng phần đường, làn đường quy định

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt là từ 80.000 đồng đến 100.000 đồng theo Nghị định 100/2019/NĐ-CP.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 2 — `4ac9888e19`

**Câu hỏi:** Năm 2020, mức phạt cho hành vi quẹt chân chống xuống đường được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [x] 1   [ ] NA

---

## Mẫu 3 — `1138a361c7`

**Câu hỏi:** Quy định về các biện pháp khắc phục hậu quả vi phạm hành chính trong lĩnh vực giao thông đường bộ, đường sắt

**Ngữ cảnh đã cung cấp:**
> [1] Điều 4. Các biện pháp khắc phục hậu quả và nguyên tắc áp dụng
> 1. Các biện pháp khắc phục hậu quả vi phạm hành chính trong lĩnh vực giao thông đường bộ, đường sắt bao gồm:
> a) Buộc khôi phục lại tình trạng ban đầu đã bị thay đổi do vi phạm hành chính gây ra;
> b) Buộc tháo dỡ công trình, phần công trình xây dựng không có giấy phép hoặc xây dựng không đúng với giấy phép;
> c) Buộc thực hiện biện pháp để khắc phục tình trạng ô nhiễm môi trường do vi phạm hành chính gây ra;
> d) Buộc tái xuất phương tiện khỏi Việt Nam;
> đ) Buộc nộp lại số lợi bất hợp pháp có được do thực hiện vi phạm hành chính;
> e) Các biện pháp khắc phục hậu quả khác được quy định tại khoản 2 và khoản 3 Điều này.
> 2.
> [2] Điều 1. Phạm vi điều chỉnh
> 1. Nghị định này quy định về hành vi vi phạm hành chính; hình thức, mức xử phạt, biện pháp khắc phục hậu quả đối với từng hành vi vi phạm hành chính; thẩm quyền lập biên bản, thẩm quyền xử phạt, mức phạt tiền cụ thể theo từng chức danh đối với hành vi vi phạm hành chính trong lĩnh vực giao thông đường bộ và đường sắt.
> 2. Các hành vi vi phạm hành chính trong các lĩnh vực quản lý nhà nước khác liên quan đến lĩnh vực giao thông đường bộ và đường sắt mà không quy định tại Nghị định này thì áp dụng quy định tại các Nghị định quy định về xử phạt vi phạm hành chính trong các lĩnh vực đó để xử phạt.
> [3] Điều 78. Nguyên tắc xác định thẩm quyền xử phạt vi phạm hành chính và áp dụng biện pháp khắc phục hậu quả
> 1. Nguyên tắc xác định thẩm quyền xử phạt vi phạm hành chính và áp dụng biện pháp khắc phục hậu quả trong lĩnh vực giao thông đường bộ, đường sắt thực hiện theo quy định tại Điều 52 của Luật Xử lý vi phạm hành chính.
> 2. Thẩm quyền xử phạt vi phạm hành chính của những chức danh được quy định tại các Điều 75, 76 và 77 của Nghị định này là thẩm quyền áp dụng đối với một hành vi vi phạm hành chính của cá nhân; trong trường hợp phạt tiền, thẩm quyền xử phạt tổ chức gấp 02 lần thẩm quyền xử phạt cá nhân tương ứng với từng lĩnh vực.
> 3.
> [4] Điều 3. Biện pháp khắc phục hậu quả
> Ngoài các biện pháp khắc phục hậu quả quy định tại các điểm a, b, c, d, đ, e, g, h và i Khoản 1 Điều 28 của Luật Xử lý vi phạm hành chính, cá nhân, tổ chức vi phạm hành chính trong lĩnh vực giáo dục nghề nghiệp có thể bị áp dụng một hoặc nhiều biện pháp khắc phục hậu quả quy định tại Khoản 4 Điều 5, Khoản 9 Điều 6, Khoản 2 Điều 7, Khoản 7 Điều 8, Khoản 5 Điều 9, Khoản 8 Điều 10, Khoản 2 Điều 11, Khoản 5 Điều 12, Khoản 2 Điều 13, Khoản 2 Điều 14, Khoản 8 Điều 15, Khoản 6 Điều 16, Khoản 7 Điều 17, Khoản 3 Điều 18, Khoản 2 Điều 19, Khoản 2 Điều 20, Khoản 3 Điều 21, Khoản 2 Điều 22, Khoản 2 Điều 23, Khoản 5 Điều 24, Khoản 9 Điều 25, Khoản 7 Điều 26, Khoản 3 Điều 27, Khoản 3 Điều 28 Nghị định này.
> [5] Điều 4. Biện pháp khắc phục hậu quả
> Các biện pháp khắc phục hậu quả được áp dụng trong Nghị định này bao gồm:
> 1. Các biện pháp khắc phục hậu quả được quy định tại các Điểm a, b, c, d, đ, e, g, h và i Khoản 1 Điều 28 Luật xử lý vi phạm hành chính.
> 2. Buộc người, tàu thuyền vi phạm rời khỏi vùng biển, đảo và thềm lục địa của nước Cộng hòa xã hội chủ nghĩa Việt Nam.
> 3. Buộc tàu ngầm và phương tiện đi ngầm phải hoạt động nổi trên mặt nước.
> 4. Buộc treo Quốc kỳ Việt Nam hoặc cờ quốc tịch theo quy định.
> 5. Buộc di dời về vùng hoạt động cho phù hợp với cấp tàu.

**Bằng chứng vàng:**
> Điều 4. Các biện pháp khắc phục hậu quả và nguyên tắc áp dụng
> 1. Các biện pháp khắc phục hậu quả vi phạm hành chính trong lĩnh vực giao thông đường bộ, đường sắt bao gồm:
> a) Buộc khôi phục lại tình trạng ban đầu đã bị thay đổi do vi phạm hành chính gây ra;
> b) Buộc tháo dỡ công trình, phần công trình xây dựng không có giấy phép hoặc xây dựng không đúng với giấy phép;
> c) Buộc thực hiện biện pháp để khắc phục tình trạng ô nhiễm môi trường do vi phạm hành chính gây ra;
> d) Buộc tái xuất phương tiện khỏi Việt Nam;
> đ) Buộc nộp lại số lợi bất hợp pháp có được do thực hiện vi phạm hành chính;
> e) Các biện pháp khắc phục hậu quả khác được quy định tại khoản 2 và khoản 3 Điều này.
> 2.
>  biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:
> a) Buộc phải tháo dỡ các vật che khuất biển báo hiệu đường bộ, đèn tín hiệu giao thông hoặc buộc phải di dời cây trồng không đúng quy định;
> b) Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác;
> c) Buộc phải thực hiện ngay các biện pháp bảo đảm an toàn giao thông theo quy định hoặc buộc phải treo biển báo thông tin công trình có đầy đủ nội dung theo quy định;
> d) Buộc phải xây dựng lại bến xe, bãi đỗ xe, trạm dừng nghỉ, trạm thu phí đường bộ theo đúng quy định, bảo đảm tiêu chuẩn kỹ thuật;
> đ) Buộc phải bổ sung hoặc sửa chữa các biển báo hiệu bị mất, bị hư hỏng và khắc phục các hư hỏng của công trình đường bộ;
> e) Buộc phải lắp đầy đủ thiết bị hoặc thay thế thiết bị đủ tiêu chuẩn an toàn kỹ thuật hoặc khôi phục lại tính năng kỹ thuật của phương tiện, thiết bị theo quy định hoặc tháo bỏ những thiết bị lắp thêm không đúng quy định;
> g) Buộc phải bố trí phương tiện khác để chở số hành khách vượt quá quy định được phép chở của phương tiện;
> h) Buộc phải đăng ký, niêm yết đầy đủ, chính xác các thông tin theo quy định;
> i) Buộc phải gắn hộp đèn với chữ “TAXI” hoặc buộc phải niêm yết cụm từ “XE TAXI”, “XE HỢP ĐỒNG”, “XE DU LỊCH” theo đúng quy định;
> k) Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;
> l) Buộc phải tổ chức tập huấn nghiệp vụ hoặc tổ chức khám sức khỏe định kỳ cho lái xe và nhân viên phục vụ trên xe theo quy định;
> m) Buộc phải ký hợp đồng với lái xe và nhân viên phục vụ trên xe;
> n) Buộc phải xây dựng và thực hiện quy trình bảo đảm an toàn giao thông theo quy định;
> o) Buộc phải bố trí người trực tiếp điều hành hoạt động vận tải đủ điều kiện theo quy định;
> p) Buộc phải lắp đặt camera, dây an toàn, đồng hồ tính tiền cước, thiết bị in hóa đơn, thiết bị giám sát hành trình trên xe theo đúng quy định;
> q) Buộc phải cung cấp, cập nhật, truyền, lưu trữ, quản lý các thông tin từ thiết bị giám sát hành trình, camera lắp trên xe ô tô theo quy định;
> r) Buộc phải cung cấp tên đăng nhập, mật khẩu truy cập vào phần mềm xử lý dữ liệu từ thiết bị giám sát hành trình của xe ô tô hoặc máy chủ của đơn vị cho cơ quan có thẩm quyền theo quy định;
> s) Buộc phải lập, cập nhật, lưu trữ đầy đủ, chính xác lý lịch phương tiện, lý lịch hành nghề của lái xe, các hồ sơ, tài liệu có liên quan trong quá trình quản lý, điều hành hoạt động vận tải của đơn vị theo quy định;
> t) Buộc phải khôi phục lại nhãn hiệu, màu sơn ghi trong Giấy đăng ký xe theo quy định hoặc buộc phải thực hiện đúng quy định về biển số, quy định về kẻ chữ trên thành xe và cửa xe;
> u) Buộc phải khôi phục lại hình dáng, kích thước, tình trạng an toàn kỹ thuật ban đầu của xe và đăng kiểm lại trước khi đưa phương tiện ra tham gia giao thông;
> v) Buộc phải thực hiện điều chỉnh thùng xe theo đúng quy định hiện hành, đăng kiểm lại và điều chỉnh lại khối lượng hàng hóa cho phép chuyên chở ghi trong Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường theo quy định hiện hành trước khi đưa phương tiện ra tham gia giao thông;
> x) Buộc phải làm thủ tục đăng ký xe, đăng ký sang tên hoặc thủ tục đổi lại, thu hồi Giấy đăng ký xe, biển số xe, Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường theo quy định;
> y) Buộc phải đưa phương tiện quay trở lại Khu kinh tế thương mại đặc biệt, Khu kinh tế cửa khẩu quốc tế.
> 3.
>  biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường sắt:
> a) Buộc phải lắp đặt đúng, đủ và duy trì hoạt động bình thường của hệ thống báo hiệu, tín hiệu, thiết bị theo quy định;
> b) Buộc phải tổ chức thử hãm hoặc tổ chức thực hiện phòng vệ theo quy định;
> c) Buộc phải để toa xe chở hàng nguy hiểm (chất nổ, chất cháy) hoặc để ghi dẫn sang đường khác theo đúng quy định về dồn tàu;
> d) Buộc phải ra khỏi đường sắt, cầu, hầm dành riêng cho đường sắt;
> đ) Buộc phải đưa đất, đá, cát, vật chướng ngại, rơm, rạ, nông sản, rác thải sinh hoạt, chất độc hại, chất phế thải, chất dễ cháy, dễ nổ các loại vật tư, vật liệu, vật phẩm khác ra khỏi đường sắt, công trình đường sắt khác hoặc phạm vi đất dành cho đường sắt;
> e) Buộc phải đưa bè, mảng, phương tiện vận tải thủy hoặc các vật thể khác ra khỏi phạm vi bảo vệ cầu đường sắt;
> g) Buộc phải đưa phương tiện giao thông đường bộ, vật tư, vật liệu, máy móc thiết bị, hàng hóa, biển phòng vệ, biển báo tạm thời ra khỏi khổ giới hạn tiếp giáp kiến trúc đường sắt;
> h) Buộc phải thực hiện ngay các biện pháp bảo đảm an toàn công trình đường sắt, bảo đảm an toàn giao thông đường sắt theo quy định;
> i) Buộc phải dỡ bỏ vật che khuất biển hiệu, mốc hiệu, tín hiệu của công trình đường sắt hoặc đưa tấm đan bê tông, gỗ, sắt thép, các vật liệu khác (đặt trái phép) ra khỏi phạm vi bảo vệ công trình đường sắt hoặc hạ độ cao của cây trồng có chiều cao vượt quá quy định, di dời cây trồng không đúng quy định hoặc có ảnh hưởng đến an toàn công trình, an toàn giao thông đường sắt;
> k) Buộc đưa phương tiện, thiết bị, vật liệu, hàng hóa, chất phế thải, các vật phẩm khác (để trái phép) ra khỏi phạm vi bảo vệ công trình đường sắt, hành lang an toàn giao thông đường sắt;
> l) Buộc phải tháo dỡ, di chuyển các công trình, nhà ở, lều, quán gây trở ngại cho việc xây dựng, cải tạo, mở rộng và bảo đảm an toàn công trình đường sắt hoặc buộc phải tháo dỡ, di chuyển lều, quán (dựng trái phép), biển quảng cáo, biển chỉ dẫn, các vật che chắn khác (đặt, treo trái phép) ra khỏi phạm vi đất dành cho đường sắt hoặc buộc phải phá dỡ công trình hết hạn sử dụng, tháo dỡ công trình bị thu hồi, hủy giấy phép;
> m) Buộc phải gia cố, di chuyển hoặc cải tạo công trình gây ảnh hưởng đến an toàn giao thông đường sắt theo yêu cầu của cơ quan có thẩm quyền;
> n) Buộc phải tổ chức sửa chữa, bổ sung, gia cố, thay thế các hư hỏng kết cấu hạ tầng đường sắt để bảo đảm chất lượng theo công lệnh tốc độ, công lệnh tải trọng đã công bố;
> o) Buộc phải bố trí đủ thiết bị an toàn, tín hiệu, biển báo, tín hiệu phòng vệ theo quy định;
> p) Buộc phải để phương tiện, vật liệu, thiết bị thi công theo đúng quy định, không gây cản trở chạy tàu;
> q) Buộc phải lắp đầy đủ theo đúng quy định hoặc thay thế thiết bị đủ tiêu chuẩn an toàn kỹ thuật hoặc khôi phục lại tính năng kỹ thuật của các thiết bị, gồm: thiết bị hãm tự động, hãm bằng tay; van hãm khẩn cấp, đồng hồ áp suất (tại vị trí làm việc của trưởng tàu và trên toa xe khách); thiết bị ghép nối đầu máy, toa xe; thiết bị tín hiệu đuôi tàu; đồng hồ báo tốc độ, thiết bị ghi tốc độ và các thông tin liên quan đến việc điều hành chạy tàu (hộp đen); thiết bị cảnh báo để lái tàu tỉnh táo trong khi lái tàu; thiết bị đo tốc độ tàu, thiết bị thông tin liên lạc giữa trưởng tàu và lái tàu (tại vị trí làm việc của trưởng tàu);
> r) Buộc phải khôi phục lại kết cấu, hình dáng, tính năng sử dụng ban đầu của phương tiện trước khi đưa phương tiện tham gia giao thông trên đường sắt;
> s) Buộc phải bổ sung đầy đủ theo quy định trên tàu khách hoặc tàu hàng về: thiết bị, dụng cụ, vật liệu chữa cháy; thuốc sơ, cấp cứu; dụng cụ thoát hiểm; dụng cụ chèn tàu; dụng cụ, vật liệu để sửa chữa đơn giản; tín hiệu cầm tay;
> t) Buộc phải hướng dẫn người vi phạm về vị trí quy định hoặc đưa người, hàng hóa ra khỏi đầu máy;
> u) Buộc phải bố trí phương tiện khác để chở số hành khách vượt quá quy định được phép chở của toa xe;
> v) Buộc thu hồi và tiêu hủy bằng, chứng chỉ chuyên môn đã cấp trái phép;
> x) Buộc phải đưa thi hài, hài cốt, động vật sống, động vật có dịch bệnh, chất dễ cháy, dễ nổ, vũ khí, hàng nguy hiểm, xuống tàu (tại ga đến gần nhất trong trường hợp tàu đang chạy), ra ga để xử lý theo quy định;
> y) Buộc phải thực hiện ngay nhiệm vụ vận tải đặc biệt, an sinh xã hội theo yêu cầu của người đứng đầu cơ quan quản lý nhà nước có thẩm quyền theo quy định.
> 4. Nguyên tắc áp dụng biện pháp khắc phục hậu quả được thực hiện theo quy định tại khoản 2 Điều 28 của Luật Xử lý vi phạm hành chính.

**Câu trả lời:** Các biện pháp khắc phục hậu quả vi phạm hành chính trong lĩnh vực giao thông đường bộ, đường sắt bao gồm: buộc khôi phục lại tình trạng ban đầu, buộc tháo dỡ công trình không có giấy phép hoặc xây dựng không đúng giấy phép, buộc thực hiện biện pháp khắc phục tình trạng ô nhiễm môi trường, buộc tái xuất phương tiện khỏi Việt Nam, buộc nộp lại số lợi bất hợp pháp và các biện pháp khác được quy định tại khoản 2 và khoản 3 Điều 4 của Nghị định này.

Correctness: [ ] 0   [x] 1   [ ] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 4 — `9edbf60ecb`

**Câu hỏi:** Mức phạt khi chạy xe máy mà trong người có chất ma túy

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt là từ 100.000.000 đồng đến 200.000.000 đồng và bị tước quyền sử dụng giấy phép lái xe từ 02 năm đến 04 năm.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 5 — `52c1594731`

**Câu hỏi:** Mức phạt khi quay người về phía sau để điều khiển xe máy

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với hành vi quay người về phía sau để điều khiển xe.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 6 — `6204ab428c`

**Câu hỏi:** Mức phạt hành vi điều khiển xe máy khi có sương mù mà không bật đèn

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 100.000 đồng đến 200.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 7 — `b3c3a727b3`

**Câu hỏi:** Năm 2020, trẻ em dưới mấy tuổi thì không cần đội mũ bảo hiểm được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Trẻ em dưới 6 tuổi không bắt buộc phải đội mũ bảo hiểm khi ngồi trên xe máy.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 8 — `485424cf6e`

**Câu hỏi:** Mức phạt khi chở người ngồi trên xe máy không đội mũ bảo hiểm

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt là từ 80.000 đồng đến 100.000 đồng và tước quyền sử dụng giấy phép lái xe từ 1 đến 2 tháng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 9 — `88be58bf55`

**Câu hỏi:** Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật bị phạt như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 10. Vi phạm các quy định về bảo đảm an toàn, an ninh trong cung ứng và sử dụng dịch vụ bưu chính
> 1. Phạt tiền từ 3.000.000 đồng đến 5.000.000 đồng đối với hành vi không thực hiện việc kiểm kê, lập biên bản và gói, bọc lại trong trường hợp vỏ bọc bưu gửi bị rách, hư hại.
> 2. Phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng đối với một trong các hành vi sau:
> a) Mạo danh người khác khi sử dụng dịch vụ bưu chính;
> b) Thực hiện không đúng, không đầy đủ các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính.
> 3.
> Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng đối với một trong các hành vi sau:
> a) Không thực hiện các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính;
> b) Đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính không có biên bản, chữ ký của các bên liên quan;
> c) Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật;
> d) Không đình chỉ vận chuyển, phát bưu gửi hoặc không thông báo cho cơ quan nhà nước có thẩm quyền liên quan để xử lý khi phát hiện bưu gửi vi phạm quy định về vật phẩm, hàng hóa không được gửi, chấp nhận, vận chuyển qua mạng bưu chính.
> 4.
> Phạt tiền từ 20.000.000 đồng đến 30.000.000 đồng đối với một trong các hành vi như sau:
> a) Bóc mở bưu gửi trái pháp luật;
> b) Tráo đổi nội dung bưu gửi;
> c) Chiếm đoạt, trộm cắp bưu gửi có trị giá dưới 2.000.000 đồng hoặc hủy bưu gửi trái pháp luật;
> d) Không phối hợp với cơ quan nhà nước có thẩm quyền thực hiện việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc cung cấp thông tin về sử dụng dịch vụ bưu chính theo quy định của pháp luật.
> 5. Phạt tiền từ 30.000.000 đồng đến 40.000.000 đồng đối với một trong các hành vi sau:
> a) Lợi dụng việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính gây thiệt hại đến lợi ích của nhà nước, quyền và lợi ích hợp pháp của tổ chức, cá nhân cung ứng và sử dụng dịch vụ bưu chính;
> b) Cản trở trái pháp luật hoạt động bưu chính.
> 6.
> Biện pháp khắc phục hậu quả:
> Buộc hoàn trả lại bưu gửi đối với hành vi quy định tại các điểm b và c khoản 4 Điều này.

**Bằng chứng vàng:**
> Điều 10. Vi phạm các quy định về bảo đảm an toàn, an ninh trong cung ứng và sử dụng dịch vụ bưu chính
> 1. Phạt tiền từ 3.000.000 đồng đến 5.000.000 đồng đối với hành vi không thực hiện việc kiểm kê, lập biên bản và gói, bọc lại trong trường hợp vỏ bọc bưu gửi bị rách, hư hại.
> 2. Phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng đối với một trong các hành vi sau:
> a) Mạo danh người khác khi sử dụng dịch vụ bưu chính;
> b) Thực hiện không đúng, không đầy đủ các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính.
> 3.
> Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng đối với một trong các hành vi sau:
> a) Không thực hiện các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính;
> b) Đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính không có biên bản, chữ ký của các bên liên quan;
> c) Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật;
> d) Không đình chỉ vận chuyển, phát bưu gửi hoặc không thông báo cho cơ quan nhà nước có thẩm quyền liên quan để xử lý khi phát hiện bưu gửi vi phạm quy định về vật phẩm, hàng hóa không được gửi, chấp nhận, vận chuyển qua mạng bưu chính.
> 4.
> Phạt tiền từ 20.000.000 đồng đến 30.000.000 đồng đối với một trong các hành vi như sau:
> a) Bóc mở bưu gửi trái pháp luật;
> b) Tráo đổi nội dung bưu gửi;
> c) Chiếm đoạt, trộm cắp bưu gửi có trị giá dưới 2.000.000 đồng hoặc hủy bưu gửi trái pháp luật;
> d) Không phối hợp với cơ quan nhà nước có thẩm quyền thực hiện việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc cung cấp thông tin về sử dụng dịch vụ bưu chính theo quy định của pháp luật.
> 5. Phạt tiền từ 30.000.000 đồng đến 40.000.000 đồng đối với một trong các hành vi sau:
> a) Lợi dụng việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính gây thiệt hại đến lợi ích của nhà nước, quyền và lợi ích hợp pháp của tổ chức, cá nhân cung ứng và sử dụng dịch vụ bưu chính;
> b) Cản trở trái pháp luật hoạt động bưu chính.
> 6.
> Biện pháp khắc phục hậu quả:
> Buộc hoàn trả lại bưu gửi đối với hành vi quy định tại các điểm b và c khoản 4 Điều này.

**Câu trả lời:** Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật bị phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 10 — `91dd6054a3`

**Câu hỏi:** Người quảng cáo không được phép gọi quá 01 cuộc gọi quảng cáo trong vòng 24 giờ?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 13. Nguyên tắc gửi tin nhắn quảng cáo, thư điện tử quảng cáo, gọi điện thoại quảng cáo
> 1. Không được phép gửi tin nhắn quảng cáo, gọi điện thoại quảng cáo đến các số điện thoại nằm trong Danh sách không quảng cáo quy định tại khoản 1 Điều 7 Nghị định này hoặc Người sử dụng không đồng ý nhận quảng cáo trước đó.
> 2. Đối với quảng cáo qua tin nhắn và đối với số điện thoại ngoài Danh sách không quảng cáo, Người quảng cáo chỉ được phép gửi tin nhắn đăng ký quảng cáo đầu tiên và duy nhất. Bộ Thông tin và Truyền thông quy định chi tiết việc gửi tin nhắn đăng ký quảng cáo.
> 3. Trường hợp Người sử dụng từ chối nhận quảng cáo hoặc không trả lời sau khi nhận tin nhắn đăng ký quảng cáo đầu tiên, Người quảng cáo không được phép gửi bất kỳ tin nhắn đăng ký quảng cáo hoặc tin nhắn quảng cáo nào đến số điện thoại đó.
> 4. Phải chấm dứt việc gửi đến Người sử dụng nhận các tin nhắn quảng cáo, thư điện tử quảng cáo hoặc thực hiện gọi điện thoại quảng cáo ngay sau khi nhận được yêu cầu từ chối của Người sử dụng.
> 5.
> Mỗi Người quảng cáo không được phép gửi quá 03 tin nhắn quảng cáo tới một số điện thoại, 03 thư điện tử quảng cáo tới một địa chỉ thư điện tử, 01 cuộc gọi điện thoại quảng cáo tới một số điện thoại trong vòng 24 giờ trừ trường hợp đã có thỏa thuận khác với Người sử dụng.
> 6. Chỉ được gửi tin nhắn trong khoảng thời gian từ 07 giờ đến 22 giờ mỗi ngày, gọi điện thoại quảng cáo từ 08 giờ đến 17 giờ mỗi ngày trừ trường hợp đã có thỏa thuận khác với Người sử dụng.
> 7. Nội dung quảng cáo phải phù hợp với quy định của pháp luật về quảng cáo.
> 8. Chỉ được gửi tin nhắn quảng cáo, gọi điện thoại quảng cáo khi đã được cấp tên định danh và không được phép sử dụng số điện thoại để gửi tin nhắn quảng cáo hoặc gọi điện thoại quảng cáo.

**Câu trả lời:** Không, người quảng cáo không bị giới hạn chỉ được gọi tối đa 01 cuộc gọi trong vòng 24 giờ theo quy định pháp luật hiện hành của Việt Nam.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 11 — `bc668adfae`

**Câu hỏi:** Điều khiển xe máy thả hai tay sẽ bị xử phạt như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Người điều khiển xe máy buông cả hai tay khi đang điều khiển xe sẽ bị phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 12 — `b88a48492f`

**Câu hỏi:** Điều khiển xe máy chuyển làn đường không đúng quy định gây tai nạn giao thông sẽ bị xử phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Người nào chịu trách nhiệm trực tiếp về việc điều động hoặc về tình trạng kỹ thuật mà cho phép đưa vào sử dụng phương tiện giao thông cơ giới đường bộ, xe máy chuyên dùng rõ ràng không bảo đảm tiêu chuẩn an toàn kỹ thuật gây thiệt hại cho người khác thuộc một trong các trường hợp sau đây, thì bị phạt tiền từ 20.000.000 đồng đến 100.000.000 đồng, phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm:
> a) Làm chết người;
> b) Gây thương tích hoặc gây tổn hại cho sức khỏe của 01 người mà tỷ lệ tổn thương cơ thể 61% trở lên;
> c) Gây thương tích hoặc gây tổn hại cho sức khỏe của 02 người trở lên mà tổng tỷ lệ tổn thương cơ thể của những người này từ 61% đến 121%;
> d) Gây thiệt hại về tài sản từ 100.000.000 đồng đến dưới 500.000.000 đồng.
> 2.
> [2] Phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ các hành vi vi phạm quy định tại điểm a khoản 8 Điều này;
> b) Điều khiển xe lạng lách, đánh võng; chạy quá tốc độ đuổi nhau trên đường bộ; dùng chân điều khiển vô lăng xe khi xe đang chạy trên đường;
> c) Điều khiển xe chạy quá tốc độ quy định trên 35 km/h.
> 8.
> [3] ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển làn đường không đúng nơi cho phép hoặc không có tín hiệu báo trước, trừ các hành vi vi phạm quy định tại điểm g khoản 5 Điều này;
> b) Điều khiển xe chạy tốc độ thấp hơn các xe khác đi cùng chiều mà không đi về bên phải phần đường xe chạy, trừ trường hợp các xe khác đi cùng chiều chạy quá tốc độ quy định;
> c) Chở người trên buồng lái quá số lượng quy định;
> d) Không tuân thủ các quy định về nhường đường tại nơi đường bộ giao nhau, trừ các hành vi vi phạm quy định tại điểm m, điểm n khoản 3 Điều này;
> đ) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm b khoản 8 Điều này;
> e) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có giấy phép của cơ quan có thẩm quyền cấp hoặc có
> [4] Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ các hành vi vi phạm quy định tại điểm a, điểm b khoản 8 Điều này;
> b) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> [5] Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d, điểm đ, điểm e khoản 2; điểm a, điểm b, điểm c, điểm đ, điểm h, điểm i khoản 3; điểm a, điểm b, điểm c, điểm d, điểm đ, điểm g khoản 4; điểm a, điểm c, điểm đ khoản 5; điểm a, điểm b khoản 6; điểm a khoản 7; điểm a, điểm b khoản 8 Điều này;
> b) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> c) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ.
> 2.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 13 — `d6df5bb3a4`

**Câu hỏi:** Nhiệm vụ, quyền hạn của Bộ Xây dựng trong hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 42. Nhiệm vụ, quyền hạn của Bộ Xây dựng
> Chủ trì, phối hợp với Bộ Quốc phòng trong thẩm định, ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.

**Bằng chứng vàng:**
> Điều 42. Nhiệm vụ, quyền hạn của Bộ Xây dựng
> Chủ trì, phối hợp với Bộ Quốc phòng trong thẩm định, ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.

**Câu trả lời:** Bộ Xây dựng có nhiệm vụ chủ trì, phối hợp với Bộ Quốc phòng trong việc thẩm định và ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 14 — `253812f334`

**Câu hỏi:** Chạy xe máy chở người ngồi trên xe sử dụng ô, dù bị phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 11. Xử phạt các hành vi vi phạm khác về quy tắc giao thông đường bộ
> 1. Phạt tiền từ 80.000 đồng đến 100.000 đồng đối với người được chở trên xe đạp, xe đạp máy sử dụng ô (dù).
> 2. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với cá nhân thực hiện một trong các hành vi vi phạm sau đây:
> a) Tập trung đông người trái phép, nằm, ngồi trên đường bộ gây cản trở giao thông;
> b) Đá bóng, đá cầu, chơi cầu lông hoặc các hoạt động thể thao khác trái phép trên đường bộ; sử dụng bàn trượt, pa-tanh, các thiết bị tương tự trên phần đường xe chạy;
> c) Người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy sử dụng ô (dù);
> d) Người được chở trên xe đạp, xe đạp máy bám, kéo, đẩy xe khác, vật khác, mang vác vật cồng kềnh.
> 3.
> [2] Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô, các loại xe tương tự xe gắn máy, xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ.
> 4. Phạt tiền từ 200.000 đồng đến 400.000 đồng đối với cá nhân, từ 400.000 đồng đến 800.000 đồng đối với tổ chức để vật che khuất biển báo, đèn tín hiệu giao thông.
> 5. Phạt tiền từ 300.000 đồng đến 500.000 đồng đối với người được chở trên xe ô tô không thắt dây an toàn (tại vị trí có trang bị dây an toàn) khi xe đang chạy.
> 6.
> [3] Điều 23. Xử phạt người điều khiển xe ô tô chở hành khách, ô tô chở người và các loại xe tương tự xe ô tô chở hành khách, chở người vi phạm quy định về vận tải đường bộ
> 1. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Không hướng dẫn hành khách đứng, nằm, ngồi đúng vị trí quy định trong xe;
> b) Không mặc đồng phục, không đeo thẻ tên của lái xe theo quy định.
> 2. Phạt tiền từ 400.000 đồng đến 600.000 đồng trên mỗi người vượt quá quy định được phép chở của phương tiện nhưng tổng mức phạt tiền tối đa không vượt quá 40.000.000 đồng đối với người điều khiển xe ô tô chở hành khách, ô tô chở người (trừ xe buýt) thực hiện hành vi vi phạm: Chở quá từ 02 người trở lên trên xe đến 9 chỗ, chở quá từ 03 người trở lên trên xe 10 chỗ đến xe 15 chỗ, chở quá từ 04 người trở lên trên xe 16 chỗ đến xe 30 chỗ, chở quá từ 05 người trở lên trên xe trên 30 chỗ, trừ các hành vi vi phạm quy định tại khoản 4 Điều này.
> 3.
> [4] Điều 16. Xử phạt người điều khiển xe ô tô (bao gồm cả rơ moóc hoặc sơ mi rơ moóc được kéo theo) và các loại xe tương tự xe ô tô vi phạm quy định về điều kiện của phương tiện khi tham gia giao thông
> 1. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với hành vi điều khiển xe không có kính chắn gió hoặc có nhưng vỡ hoặc có nhưng không có tác dụng (đối với xe có thiết kế lắp kính chắn gió).
> 2.
> [5] Phạt tiền từ 400.000 đồng đến 600.000 đồng đối với người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô, các loại xe tương tự xe gắn máy bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh, đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái.
> 7. Phạt tiền từ 500.000 đồng đến 1.000.000 đồng đối với cá nhân, từ 1.000.000 đồng đến 2.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Không cứu giúp người bị tai nạn giao thông khi có yêu cầu;
> b) Ném gạch, đất, đá, cát hoặc vật thể khác vào phương tiện đang tham gia giao thông trên đường bộ.
> 8.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người được chở trên xe mô tô, xe gắn máy sử dụng ô (dù).

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 15 — `669f72b4b0`

**Câu hỏi:** Mức phạt khi chạy xe máy gây tai nạn giao thông không tham gia cấp cứu người bị nạn là bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt là từ 10.000.000 đồng đến 20.000.000 đồng và bị tước quyền sử dụng giấy phép lái xe từ 02 đến 04 tháng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 16 — `a2b876a48f`

**Câu hỏi:** Điều khiển xe máy trong hơi thở có nồng độ cồn vượt quá 0,4 miligam/1 lít là bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng và bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 17 — `71633a2f80`

**Câu hỏi:** Mức phạt khi nằm trên yên xe điều khiển xe máy

**Ngữ cảnh đã cung cấp:**
> [1] Phạt tiền từ 400.000 đồng đến 600.000 đồng đối với người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô, các loại xe tương tự xe gắn máy bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh, đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái.
> 7. Phạt tiền từ 500.000 đồng đến 1.000.000 đồng đối với cá nhân, từ 1.000.000 đồng đến 2.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Không cứu giúp người bị tai nạn giao thông khi có yêu cầu;
> b) Ném gạch, đất, đá, cát hoặc vật thể khác vào phương tiện đang tham gia giao thông trên đường bộ.
> 8.
> [2] ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công
> [3] ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe lạng lách, đánh võng; đuổi nhau trên đường;
> b) Đi xe bằng một bánh đối với xe đạp, xe đạp máy; đi xe bằng hai bánh đối với xe xích lô;
> c) Đi vào khu vực cấm; đường có biển báo hiệu nội dung cấm đi vào đối với loại phương tiện đang điều khiển; đi ngược chiều đường của đường một chiều, đường có biển “Cấm đi ngược chiều”;
> d) Người điều khiển xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ;
> đ) Chở người ngồi trên xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06
> [4] Điều 11. Xử phạt các hành vi vi phạm khác về quy tắc giao thông đường bộ
> 1. Phạt tiền từ 80.000 đồng đến 100.000 đồng đối với người được chở trên xe đạp, xe đạp máy sử dụng ô (dù).
> 2. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với cá nhân thực hiện một trong các hành vi vi phạm sau đây:
> a) Tập trung đông người trái phép, nằm, ngồi trên đường bộ gây cản trở giao thông;
> b) Đá bóng, đá cầu, chơi cầu lông hoặc các hoạt động thể thao khác trái phép trên đường bộ; sử dụng bàn trượt, pa-tanh, các thiết bị tương tự trên phần đường xe chạy;
> c) Người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy sử dụng ô (dù);
> d) Người được chở trên xe đạp, xe đạp máy bám, kéo, đẩy xe khác, vật khác, mang vác vật cồng kềnh.
> 3.
> [5] Người nào chịu trách nhiệm trực tiếp về việc điều động hoặc về tình trạng kỹ thuật mà cho phép đưa vào sử dụng phương tiện giao thông cơ giới đường bộ, xe máy chuyên dùng rõ ràng không bảo đảm tiêu chuẩn an toàn kỹ thuật gây thiệt hại cho người khác thuộc một trong các trường hợp sau đây, thì bị phạt tiền từ 20.000.000 đồng đến 100.000.000 đồng, phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm:
> a) Làm chết người;
> b) Gây thương tích hoặc gây tổn hại cho sức khỏe của 01 người mà tỷ lệ tổn thương cơ thể 61% trở lên;
> c) Gây thương tích hoặc gây tổn hại cho sức khỏe của 02 người trở lên mà tổng tỷ lệ tổn thương cơ thể của những người này từ 61% đến 121%;
> d) Gây thiệt hại về tài sản từ 100.000.000 đồng đến dưới 500.000.000 đồng.
> 2.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 18 — `c8dca0ca42`

**Câu hỏi:** Mức phạt hành vi để xe máy ở lòng đường đô thị, hè phố trái quy định

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 200.000 đồng đến 300.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 19 — `6350b9679d`

**Câu hỏi:** Điều khiển xe máy bấm còi trong thời gian từ 22 giờ đến 5 giờ sáng trong đô thị bị phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 80.000 đồng đến 200.000 đồng và tước quyền sử dụng giấy phép lái xe từ 1 đến 4 tháng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 20 — `cc0682672c`

**Câu hỏi:** Vượt xe máy không đúng quy định gây tai nạn giao thông sẽ bị xử phạt thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Người điều khiển xe gây tai nạn giao thông do vượt xe không đúng quy định sẽ bị phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng và bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 21 — `f6274cc652`

**Câu hỏi:** Mức phạt hành vi chạy xe máy gây tai nạn giao thông mà không tham gia cấp cứu người bị nạn

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng và bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

Correctness: [ ] 0   [x] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [x] 1   [ ] NA

---

## Mẫu 22 — `83d865828d`

**Câu hỏi:** Hành vi dừng xe, đỗ xe máy ở lòng đường đô thị gây cản trở giao thông bị phạt thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] 7. Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với cá nhân, từ 12.000.000 đồng đến 16.000.000 đồng đối với tổ chức thực hiện hành vi chiếm dụng lòng đường đô thị hoặc hè phố từ 10 m2 đến dưới 20 m2 làm nơi trông, giữ xe.
> 8. Phạt tiền từ 10.000.000 đồng đến 15.000.000 đồng đối với cá nhân, từ 20.000.000 đồng đến 30.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Chiếm dụng lòng đường đô thị hoặc hè phố từ 20 m2 trở lên làm nơi trông, giữ xe;
> b) Dựng biển quảng cáo trên đất hành lang an toàn đường bộ khi chưa được cơ quan quản lý đường bộ có thẩm quyền đồng ý bằng văn bản hoặc dựng biển quảng cáo trên phần đất dọc hai bên đường bộ dùng để quản lý, bảo trì, bảo vệ công trình đường bộ.
> 9.
> [2] ạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với cá nhân, từ 4.000.000 đồng đến 6.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Dựng rạp, lều quán, cổng ra vào, tường rào các loại, công trình khác trái phép trong phạm vi đất dành cho đường bộ, trừ các hành vi vi phạm quy định tại điểm đ khoản 6, điểm b khoản 8, điểm a khoản 9 Điều này;
> b) Sử dụng trái phép lòng đường đô thị, hè phố để: Họp chợ; kinh doanh dịch vụ ăn uống; bày, bán hàng hóa; sửa chữa phương tiện, máy móc, thiết bị; rửa xe; đặt, treo biển hiệu, biển quảng cáo; xây, đặt bục bệ; làm mái che hoặc thực hiện các hoạt động khác gây cản trở giao thông, trừ các hành vi vi phạm quy định tại điểm d, điểm đ, điểm e, điểm g khoản 6; khoản 7; điểm a khoản 8 Điều này;
> c) Chiếm dụng lòng đường đô thị hoặc hè phố dưới 05 m2 làm nơi trông, giữ xe;
> d) Chiếm dụng phần đường xe chạy hoặc lề đường của đường ngoài
> [3] Cản trở giao thông đường bộ trong trường hợp có khả năng thực tế dẫn đến hậu quả quy định tại một trong các điểm a, b và c khoản 3 Điều này nếu không được ngăn chặn kịp thời, thì bị phạt tiền từ 5.000.000 đồng đến 20.000.000 đồng hoặc phạt cải tạo không giam giữ đến 01 năm.”.
> 74. Sửa đổi, bổ sung Điều 262 như sau:
> “Điều 262. Tội đưa vào sử dụng phương tiện giao thông cơ giới đường bộ, xe máy chuyên dùng không bảo đảm an toàn
> 1.
> [4] ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe
> [5] Phạt tiền từ 500.000 đồng đến 1.000.000 đồng đối với cá nhân, từ 1.000.000 đồng đến 2.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng đường bộ trái quy định để tổ chức các hoạt động văn hóa, thể thao, diễu hành, lễ hội;
> b) Dựng cổng chào hoặc các vật che chắn khác trái quy định trong phạm vi đất dành cho đường bộ gây ảnh hưởng đến trật tự, an toàn giao thông đường bộ;
> c) Treo băng rôn, biểu ngữ trái phép trong phạm vi đất dành cho đường bộ gây ảnh hưởng đến trật tự an toàn giao thông đường bộ;
> d) Đặt, treo biển hiệu, biển quảng cáo trên đất của đường bộ ở đoạn đường ngoài đô thị, trừ các hành vi vi phạm quy định tại điểm b khoản 8 Điều này;
> đ) Chiếm dụng dải phân cách giữa của đường đôi làm nơi để xe, trông, giữ xe;
> e) Sử dụng trái phép đất của đường bộ ở đoạn đường ngoài đô thị làm nơi sửa chữa phương tiện, máy móc, thiết bị; rửa xe, bơm nước mui xe gây ảnh hưởng đến trật tự an toàn giao thông đường bộ.
> 4.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Hành vi dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông bị phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 23 — `5d4c5e7619`

**Câu hỏi:** Kiểm soát viên ngân hàng nhà nước được thi tuyển hay bổ nhiệm?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 33. Kiểm soát viên ngân hàng
> 1. Công chức trực tiếp làm công tác kiểm soát nội bộ, kiểm toán nội bộ chuyên trách thuộc Ngân hàng Nhà nước được xem xét bổ nhiệm vào ngạch kiểm soát viên ngân hàng khi đáp ứng đủ điều kiện, tiêu chuẩn theo quy định của Ngân hàng Nhà nước.
> 2. Ngạch kiểm soát viên ngân hàng bao gồm: Ngạch kiểm soát viên ngân hàng, ngạch kiểm soát viên chính ngân hàng, ngạch kiểm soát viên cao cấp ngân hàng.
> 3. Kiểm soát viên ngân hàng thực hiện chức trách, nhiệm vụ theo quy định do Thống đốc ban hành và các văn bản khác có liên quan; được hưởng các chế độ, chính sách theo quy định của nhà nước và Ngân hàng Nhà nước.

**Câu trả lời:** Kiểm soát viên Ngân hàng Nhà nước được bổ nhiệm.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 24 — `66d9d0ad6a`

**Câu hỏi:** Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 4. Quy chế hoạt động của Trung tâm dịch vụ việc làm
> Quy chế hoạt động của Trung tâm dịch vụ việc làm quy định tại khoản 2 Điều 8 Nghị định số 196/2013/NĐ-CP được hướng dẫn như sau:
> 1. Nội dung của Quy chế hoạt động của Trung tâm dịch vụ việc làm gồm: vị trí, chức năng nhiệm vụ của Trung tâm; cơ cấu tổ chức bộ máy; chức năng nhiệm vụ của các phòng ban; nguyên tắc hoạt động dịch vụ việc làm; thời giờ làm việc; quy trình thực hiện cung cấp các dịch vụ; trách nhiệm xây dựng và quản lý cơ sở dữ liệu thị trường lao động; quy chế phối hợp công tác; thông tin liên lạc, lập biểu theo dõi các hoạt động dịch vụ việc làm của Trung tâm.
> 2. Thủ trưởng cơ quan, tổ chức chủ quản trực tiếp Trung tâm dịch vụ việc làm ký ban hành Quy chế hoạt động của Trung tâm dịch vụ việc làm.
> 3. Quy chế hoạt động của Trung tâm dịch vụ việc làm được niêm yết công khai tại trụ sở của Trung tâm dịch vụ việc làm.
> 4. Giám đốc Trung tâm dịch vụ việc làm có trách nhiệm tổ chức, thực hiện Quy chế hoạt động của Trung tâm dịch vụ việc làm.
> [2] Quyết định việc thành lập, tổ chức lại, giải thể, chấn chỉnh hoạt động của các Trung tâm thuộc quyền quản lý.
> Đối với các Trung tâm giới thiệu việc làm đang thực hiện chính sách bảo hiểm thất nghiệp thì Chủ tịch Ủy ban nhân dân cấp tỉnh quyết định đổi tên theo quy định tại Nghị định này để bảo đảm tính liên tục của việc thực hiện chính sách bảo hiểm thất nghiệp.
> 4. Quyết định số vị trí việc làm của Trung tâm dịch vụ việc làm và bảo đảm kinh phí hoạt động thường xuyên cho Trung tâm thuộc quyền quản lý.
> 5. Chỉ đạo việc theo dõi, kiểm tra, thanh tra hoạt động của các Trung tâm dịch vụ việc làm trên địa bàn.
> 6. Khen thưởng và xử lý các vi phạm theo quy định của pháp luật.
> 7. Báo cáo Bộ Lao động - Thương binh và Xã hội về tình hình thành lập và hoạt động của Trung tâm dịch vụ việc làm trên địa bàn thuộc phạm vi quản lý định kỳ 6 tháng, hằng năm hoặc đột xuất khi có yêu cầu.
> [3] Điều 12. Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm
> 1. Trung tâm dịch vụ việc làm tiếp nhận, lập hồ sơ các cơ quan, tổ chức và cá nhân đến đăng ký dịch vụ việc làm theo các Mẫu số 01, 01 a, 02, 03, 03a Phụ lục I ban hành kèm theo Nghị định này.
> 2. Trung tâm dịch vụ việc làm thực hiện theo dõi tình trạng việc làm cho người lao động được giới thiệu hoặc cung ứng tối thiểu 03 tháng hoặc trong thời gian thực hiện hợp đồng lao động đối với những trường hợp thực hiện hợp đồng lao động dưới 03 tháng theo Mẫu số 04 Phụ lục 01 ban hành kèm theo Nghị định này.
> 3. Thực hiện ứng dụng công nghệ thông tin trong việc tổ chức cung cấp các dịch vụ và quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm đảm bảo theo các quy định của pháp luật và hướng dẫn của Bộ Lao động - Thương binh và Xã hội.
> [4] Điều 11. Quy chế hoạt động của trung tâm dịch vụ việc làm
> 1. Quy chế hoạt động của trung tâm dịch vụ việc làm phải có các nội dung chủ yếu sau đây:
> a) Tên, địa chỉ trụ sở, số điện thoại, website;
> b) Mục tiêu, nhiệm vụ của trung tâm;
> c) Nhiệm vụ và trách nhiệm của lãnh đạo, các phòng thuộc trung tâm;
> d) Trách nhiệm xây dựng và quản lý cơ sở dữ liệu về lao động, việc làm;
> đ) Quy trình cung cấp dịch vụ việc làm;
> e) Cơ chế quản lý tài sản, tài chính;
> g) Cơ chế phối hợp công tác;
> h) Những quy định có tính chất hành chính và những vấn đề liên quan khác, phù hợp với đặc điểm của trung tâm.
> 2. Trung tâm dịch vụ việc làm xây dựng Quy chế hoạt động của trung tâm theo quy định tại khoản 1 Điều này và trình Thủ trưởng cơ quan trực tiếp quản lý ký ban hành.
> 3. Quy chế hoạt động của trung tâm dịch vụ việc làm được niêm yết công khai tại trụ sở của trung tâm.
> 4. Giám đốc trung tâm dịch vụ việc làm có trách nhiệm tổ chức, thực hiện Quy chế hoạt động của trung tâm.
> [5] Điều 9. Số lượng người làm việc
> Số lượng người làm việc của trung tâm dịch vụ việc làm được xác định trên cơ sở vị trí việc làm, khối lượng công việc của từng vị trí việc làm, định mức kinh tế - kỹ thuật theo chức năng, nhiệm vụ quy định tại Điều 7 Nghị định này.
> Bộ trưởng Bộ Lao động - Thương binh và Xã hội hướng dẫn về vị trí việc làm lãnh đạo, quản lý và chức danh nghề nghiệp chuyên ngành, cơ cấu viên chức theo chức danh nghề nghiệp và định mức số lượng người làm việc trong trung tâm dịch vụ việc làm sau khi có ý kiến của Bộ trưởng Bộ Nội vụ.

**Bằng chứng vàng:**
> Điều 12. Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm
> 1. Trung tâm dịch vụ việc làm tiếp nhận, lập hồ sơ các cơ quan, tổ chức và cá nhân đến đăng ký dịch vụ việc làm theo các Mẫu số 01, 01 a, 02, 03, 03a Phụ lục I ban hành kèm theo Nghị định này.
> 2. Trung tâm dịch vụ việc làm thực hiện theo dõi tình trạng việc làm cho người lao động được giới thiệu hoặc cung ứng tối thiểu 03 tháng hoặc trong thời gian thực hiện hợp đồng lao động đối với những trường hợp thực hiện hợp đồng lao động dưới 03 tháng theo Mẫu số 04 Phụ lục 01 ban hành kèm theo Nghị định này.
> 3. Thực hiện ứng dụng công nghệ thông tin trong việc tổ chức cung cấp các dịch vụ và quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm đảm bảo theo các quy định của pháp luật và hướng dẫn của Bộ Lao động - Thương binh và Xã hội.

**Câu trả lời:** Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm được thực hiện thông qua việc xây dựng và ban hành Quy chế hoạt động (bao gồm vị trí, chức năng, quy trình, cơ chế quản lý tài chính, cơ sở dữ liệu...), niêm yết công khai tại trụ sở, do Giám đốc tổ chức thực hiện, đồng thời áp dụng công nghệ thông tin và tuân thủ các quy định của pháp luật cùng hướng dẫn của Bộ Lao động - Thương binh và Xã hội.

Correctness: [ ] 0   [x] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 25 — `19b9b6cc68`

**Câu hỏi:** Chạy xe máy mà kéo hoặc đẩy xe khác bị phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Phạt tiền từ 400.000 đồng đến 600.000 đồng đối với người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô, các loại xe tương tự xe gắn máy bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh, đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái.
> 7. Phạt tiền từ 500.000 đồng đến 1.000.000 đồng đối với cá nhân, từ 1.000.000 đồng đến 2.000.000 đồng đối với tổ chức thực hiện một trong các hành vi vi phạm sau đây:
> a) Không cứu giúp người bị tai nạn giao thông khi có yêu cầu;
> b) Ném gạch, đất, đá, cát hoặc vật thể khác vào phương tiện đang tham gia giao thông trên đường bộ.
> 8.
> [2] ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe lạng lách, đánh võng; đuổi nhau trên đường;
> b) Đi xe bằng một bánh đối với xe đạp, xe đạp máy; đi xe bằng hai bánh đối với xe xích lô;
> c) Đi vào khu vực cấm; đường có biển báo hiệu nội dung cấm đi vào đối với loại phương tiện đang điều khiển; đi ngược chiều đường của đường một chiều, đường có biển “Cấm đi ngược chiều”;
> d) Người điều khiển xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ;
> đ) Chở người ngồi trên xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06
> [3] Điều 24. Xử phạt người điều khiển xe ô tô tải, máy kéo (bao gồm cả rơ moóc hoặc sơ mi rơ moóc được kéo theo) và các loại xe tương tự xe ô tô vận chuyển hàng hóa vi phạm quy định về vận tải đường bộ
> 1. Phạt tiền từ 600.000 đồng đến 800.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Vận chuyển hàng trên xe phải chằng buộc mà không chằng buộc hoặc có chằng buộc nhưng không chắc chắn, trừ hành vi vi phạm quy định tại điểm c khoản 4 Điều này;
> b) Điều khiển xe xếp hàng trên nóc buồng lái, xếp hàng làm lệch xe;
> c) Không chốt, đóng cố định cửa sau thùng xe khi xe đang chạy.
> 2.
> [4] 2. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe đạp, xe đạp máy buông cả hai tay; chuyển hướng đột ngột trước đầu xe cơ giới đang chạy; dùng chân điều khiển xe đạp, xe đạp máy;
> b) Không chấp hành hiệu lệnh, chỉ dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> c) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, mang vác vật cồng kềnh; điều khiển xe kéo theo xe khác, vật khác;
> d) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn hoặc gây cản trở đối với xe cơ giới xin vượt, gây cản trở xe ưu tiên;
> đ) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông.
> 3.
> [5] Phạt tiền từ 7.000.000 đồng đến 8.000.000 đồng đối với hành vi điều khiển xe mà tổng trọng lượng (khối lượng toàn bộ) của xe hoặc tải trọng trục xe (bao gồm cả hàng hóa xếp trên xe, người được chở trên xe) vượt quá tải trọng cho phép của cầu, đường trên 100% đến 150%, trừ trường hợp có Giấy phép lưu hành còn giá trị sử dụng.
> 6. Phạt tiền từ 14.000.000 đồng đến 16.000.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe mà tổng trọng lượng (khối lượng toàn bộ) của xe hoặc tải trọng trục xe (bao gồm cả hàng hóa xếp trên xe, người được chở trên xe) vượt quá tải trọng cho phép của cầu, đường trên 150%, trừ trường hợp có Giấy phép lưu hành còn giá trị sử dụng;
> b) Không chấp hành việc kiểm tra tải trọng, khổ giới hạn xe khi có tín hiệu, hiệu lệnh yêu cầu kiểm tra tải trọng, khổ giới hạn xe; chuyển tải hoặc dùng các thủ đoạn khác để trốn tránh việc phát hiện xe chở quá tải, quá khổ.
> 7.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện hành vi bám, kéo, đẩy xe khác.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [x] 1   [ ] NA

---

## Mẫu 26 — `67988466ad`

**Câu hỏi:** Mức phạt hành vi điều khiển xe máy vào ban đêm mà không bật đèn

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt hành vi điều khiển xe máy vào ban đêm mà không bật đèn là từ 80.000 đồng đến 200.000 đồng theo quy định tại Điều 10 Nghị định 100/2019/NĐ-CP.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 27 — `9595bc9f49`

**Câu hỏi:** Mức phạt khi chạy xe máy mà trong người có chất ma túy

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng và bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 28 — `d99f3a5ef8`

**Câu hỏi:** Mức phạt khi chở người ngồi trên xe máy không đội mũ bảo hiểm

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe chở người ngồi trên xe không đội mũ bảo hiểm hoặc đội mũ bảo hiểm không cài quai đúng quy cách.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 29 — `fdcf93d0b7`

**Câu hỏi:** Dừng xe máy trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường bị phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Dừng xe máy trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường bị phạt tiền từ 200.000 đồng đến 300.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 30 — `27f237caac`

**Câu hỏi:** Mức phạt đối với hành vi điều khiển xe máy đi trên hè phố

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt đối với hành vi điều khiển xe máy đi trên hè phố là từ 80.000 đồng đến 200.000 đồng theo quy định tại Điều 8 Nghị định 100/2019/NĐ-CP (và các văn bản sửa đổi liên quan).

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 31 — `4a96540801`

**Câu hỏi:** Tụ tập từ 3 xe máy trở lên ở lòng đường bị phạt thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Người điều khiển xe tụ tập từ 03 xe trở lên ở lòng đường bị phạt tiền từ 200.000 đồng đến 300.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 32 — `e11589f2e5`

**Câu hỏi:** Trường hợp nào chạy xe máy ban ngày nhưng vẫn phải bật đèn xe?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Trường hợp chạy xe máy ban ngày nhưng vẫn phải bật đèn xe là khi trời tối hoặc có sương mù làm giảm tầm nhìn.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 33 — `1d26a1bc9c`

**Câu hỏi:** Xuất khẩu nguồn phóng xạ phải đảm bảo những yêu cầu gì?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 11. Xuất khẩu nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân, thiết bị hạt nhân
> 1. Có tài liệu chứng minh xuất xứ nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân, thiết bị hạt nhân.
> 2. Kiện hàng nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân phải được đóng gói, dán nhãn theo quy định về vận chuyển an toàn nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân.
> 3. Trường hợp xuất khẩu nguồn phóng xạ thuộc Nhóm 1, Nhóm 2 theo QCVN 06:2010/BKHCN, vật liệu hạt nhân thì phải có văn bản cho phép nhập khẩu của cơ quan có thẩm quyền nước nhập khẩu.

**Bằng chứng vàng:**
> Điều 11. Xuất khẩu nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân, thiết bị hạt nhân
> 1. Có tài liệu chứng minh xuất xứ nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân, thiết bị hạt nhân.
> 2. Kiện hàng nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân phải được đóng gói, dán nhãn theo quy định về vận chuyển an toàn nguồn phóng xạ, vật liệu hạt nhân nguồn, vật liệu hạt nhân.
> 3. Trường hợp xuất khẩu nguồn phóng xạ thuộc Nhóm 1, Nhóm 2 theo QCVN 06:2010/BKHCN, vật liệu hạt nhân thì phải có văn bản cho phép nhập khẩu của cơ quan có thẩm quyền nước nhập khẩu.

**Câu trả lời:** Xuất khẩu nguồn phóng xạ phải có tài liệu chứng minh xuất xứ, được đóng gói và dán nhãn theo quy định về vận chuyển an toàn; nếu thuộc Nhóm 1, Nhóm 2 hoặc là vật liệu hạt nhân thì phải có văn bản cho phép nhập khẩu của cơ quan có thẩm quyền nước nhập khẩu.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 34 — `3cefd610b1`

**Câu hỏi:** Mức phạt đối với hành vi dừng, đỗ xe máy trên cầu ?

**Ngữ cảnh đã cung cấp:**
> [1] Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe đạp, xe đạp máy, người điều khiển xe thô sơ dừng xe, đỗ xe trong phạm vi an toàn đường ngang, cầu chung; vượt rào chắn đường ngang, cầu chung khi chắn đang dịch chuyển; vượt đường ngang, cầu chung khi đèn đỏ đã bật sáng; không chấp hành hiệu lệnh, chỉ dẫn của nhân viên gác đường ngang, cầu chung khi đi qua đường ngang, cầu chung.
> 4. Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy dừng xe, đỗ xe trong phạm vi an toàn đường ngang, cầu chung; không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường khi đi qua đường ngang, cầu chung.
> 5.
> [2] Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vượt rào chắn đường ngang, cầu chung khi chắn đang dịch chuyển; vượt đường ngang, cầu chung khi đèn đỏ đã bật sáng; không chấp hành hiệu lệnh, chỉ dẫn của nhân viên gác đường ngang, cầu chung khi đi qua đường ngang, cầu chung.
> 6. Phạt tiền từ 800.000 đồng đến 1.000.000 đồng đối với người điều khiển xe ô tô, các loại xe tương tự xe ô tô, máy kéo, xe máy chuyên dùng dừng xe, đỗ xe quay đầu xe trong phạm vi an toàn đường ngang, cầu chung; không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường khi đi qua đường ngang, cầu chung.
> 7.
> [3] Phạt tiền từ 5.000.000 đồng đến 7.000.000 đồng đối với hành vi điều khiển phương tiện mà tổng trọng lượng (khối lượng toàn bộ) của phương tiện hoặc tải trọng trục phương tiện (bao gồm cả hàng hóa xếp trên phương tiện, người được chở trên phương tiện) vượt quá tải trọng cho phép của cầu, đường trên 50% đến 100%, trừ trường hợp có quy định khác.
> 4. Phạt tiền từ 7.000.000 đồng đến 8.000.000 đồng đối với hành vi điều khiển phương tiện mà tổng trọng lượng (khối lượng toàn bộ) của phương tiện hoặc tải trọng trục phương tiện (bao gồm cả hàng hóa xếp trên phương tiện, người được chở trên phương tiện) vượt quá tải trọng cho phép của cầu, đường trên 100% đến 150%, trừ trường hợp có quy định khác.
> 5.
> [4] Phạt tiền từ 14.000.000 đồng đến 16.000.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Điều khiển phương tiện mà tổng trọng lượng (khối lượng toàn bộ) của phương tiện hoặc tải trọng trục phương tiện (bao gồm cả hàng hóa xếp trên phương tiện, người được chở trên phương tiện) vượt quá tải trọng cho phép của cầu, đường trên 150%;
> b) Không chấp hành việc kiểm tra tải trọng, khổ giới hạn phương tiện khi có tín hiệu, hiệu lệnh yêu cầu kiểm tra tải trọng, khổ giới hạn phương tiện; chuyển tải hoặc dùng các thủ đoạn khác để trốn tránh việc phát hiện phương tiện chở quá tải, quá khổ.
> 6.
> [5] Phạt tiền từ 7.000.000 đồng đến 8.000.000 đồng đối với hành vi điều khiển xe mà tổng trọng lượng (khối lượng toàn bộ) của xe hoặc tải trọng trục xe (bao gồm cả hàng hóa xếp trên xe, người được chở trên xe) vượt quá tải trọng cho phép của cầu, đường trên 100% đến 150%, trừ trường hợp có Giấy phép lưu hành còn giá trị sử dụng.
> 6. Phạt tiền từ 14.000.000 đồng đến 16.000.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe mà tổng trọng lượng (khối lượng toàn bộ) của xe hoặc tải trọng trục xe (bao gồm cả hàng hóa xếp trên xe, người được chở trên xe) vượt quá tải trọng cho phép của cầu, đường trên 150%, trừ trường hợp có Giấy phép lưu hành còn giá trị sử dụng;
> b) Không chấp hành việc kiểm tra tải trọng, khổ giới hạn xe khi có tín hiệu, hiệu lệnh yêu cầu kiểm tra tải trọng, khổ giới hạn xe; chuyển tải hoặc dùng các thủ đoạn khác để trốn tránh việc phát hiện xe chở quá tải, quá khổ.
> 7.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện) dừng xe, đỗ xe trong phạm vi an toàn đường ngang, cầu chung.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 35 — `0789347324`

**Câu hỏi:** Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 12. Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm
> 1. Trung tâm dịch vụ việc làm tiếp nhận, lập hồ sơ các cơ quan, tổ chức và cá nhân đến đăng ký dịch vụ việc làm theo các Mẫu số 01, 01 a, 02, 03, 03a Phụ lục I ban hành kèm theo Nghị định này.
> 2. Trung tâm dịch vụ việc làm thực hiện theo dõi tình trạng việc làm cho người lao động được giới thiệu hoặc cung ứng tối thiểu 03 tháng hoặc trong thời gian thực hiện hợp đồng lao động đối với những trường hợp thực hiện hợp đồng lao động dưới 03 tháng theo Mẫu số 04 Phụ lục 01 ban hành kèm theo Nghị định này.
> 3. Thực hiện ứng dụng công nghệ thông tin trong việc tổ chức cung cấp các dịch vụ và quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm đảm bảo theo các quy định của pháp luật và hướng dẫn của Bộ Lao động - Thương binh và Xã hội.

**Bằng chứng vàng:**
> Điều 12. Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm
> 1. Trung tâm dịch vụ việc làm tiếp nhận, lập hồ sơ các cơ quan, tổ chức và cá nhân đến đăng ký dịch vụ việc làm theo các Mẫu số 01, 01 a, 02, 03, 03a Phụ lục I ban hành kèm theo Nghị định này.
> 2. Trung tâm dịch vụ việc làm thực hiện theo dõi tình trạng việc làm cho người lao động được giới thiệu hoặc cung ứng tối thiểu 03 tháng hoặc trong thời gian thực hiện hợp đồng lao động đối với những trường hợp thực hiện hợp đồng lao động dưới 03 tháng theo Mẫu số 04 Phụ lục 01 ban hành kèm theo Nghị định này.
> 3. Thực hiện ứng dụng công nghệ thông tin trong việc tổ chức cung cấp các dịch vụ và quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm đảm bảo theo các quy định của pháp luật và hướng dẫn của Bộ Lao động - Thương binh và Xã hội.

**Câu trả lời:** Quản lý hoạt động dịch vụ việc làm tại trung tâm dịch vụ việc làm được quy định bao gồm việc tiếp nhận và lập hồ sơ cho các đối tượng đăng ký dịch vụ, theo dõi tình trạng việc làm cho người lao động được giới thiệu hoặc cung ứng, và ứng dụng công nghệ thông tin trong tổ chức cung cấp dịch vụ cũng như quản lý hoạt động.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 36 — `5033305433`

**Câu hỏi:** Điều khiển xe máy đi không đúng làn đường gây tai nạn giao thông sẽ bị xử phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 37 — `5c1c5426f1`

**Câu hỏi:** Mức phạt hành vi không chấp hành hiệu lệnh của cảnh sát giao thông

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt tiền đối với hành vi không chấp hành hiệu lệnh của người điều khiển giao thông (cảnh sát giao thông) là từ 600.000 đồng đến 1.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 38 — `826984baa9`

**Câu hỏi:** Mức phạt khi bóc mở bưu gửi trái pháp luật được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 10. Vi phạm các quy định về bảo đảm an toàn, an ninh trong cung ứng và sử dụng dịch vụ bưu chính
> 1. Phạt tiền từ 3.000.000 đồng đến 5.000.000 đồng đối với hành vi không thực hiện việc kiểm kê, lập biên bản và gói, bọc lại trong trường hợp vỏ bọc bưu gửi bị rách, hư hại.
> 2. Phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng đối với một trong các hành vi sau:
> a) Mạo danh người khác khi sử dụng dịch vụ bưu chính;
> b) Thực hiện không đúng, không đầy đủ các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính.
> 3.
> Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng đối với một trong các hành vi sau:
> a) Không thực hiện các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính;
> b) Đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính không có biên bản, chữ ký của các bên liên quan;
> c) Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật;
> d) Không đình chỉ vận chuyển, phát bưu gửi hoặc không thông báo cho cơ quan nhà nước có thẩm quyền liên quan để xử lý khi phát hiện bưu gửi vi phạm quy định về vật phẩm, hàng hóa không được gửi, chấp nhận, vận chuyển qua mạng bưu chính.
> 4.
> Phạt tiền từ 20.000.000 đồng đến 30.000.000 đồng đối với một trong các hành vi như sau:
> a) Bóc mở bưu gửi trái pháp luật;
> b) Tráo đổi nội dung bưu gửi;
> c) Chiếm đoạt, trộm cắp bưu gửi có trị giá dưới 2.000.000 đồng hoặc hủy bưu gửi trái pháp luật;
> d) Không phối hợp với cơ quan nhà nước có thẩm quyền thực hiện việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc cung cấp thông tin về sử dụng dịch vụ bưu chính theo quy định của pháp luật.
> 5. Phạt tiền từ 30.000.000 đồng đến 40.000.000 đồng đối với một trong các hành vi sau:
> a) Lợi dụng việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính gây thiệt hại đến lợi ích của nhà nước, quyền và lợi ích hợp pháp của tổ chức, cá nhân cung ứng và sử dụng dịch vụ bưu chính;
> b) Cản trở trái pháp luật hoạt động bưu chính.
> 6.
> Biện pháp khắc phục hậu quả:
> Buộc hoàn trả lại bưu gửi đối với hành vi quy định tại các điểm b và c khoản 4 Điều này.

**Bằng chứng vàng:**
> Điều 10. Vi phạm các quy định về bảo đảm an toàn, an ninh trong cung ứng và sử dụng dịch vụ bưu chính
> 1. Phạt tiền từ 3.000.000 đồng đến 5.000.000 đồng đối với hành vi không thực hiện việc kiểm kê, lập biên bản và gói, bọc lại trong trường hợp vỏ bọc bưu gửi bị rách, hư hại.
> 2. Phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng đối với một trong các hành vi sau:
> a) Mạo danh người khác khi sử dụng dịch vụ bưu chính;
> b) Thực hiện không đúng, không đầy đủ các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính.
> 3.
> Phạt tiền từ 10.000.000 đồng đến 20.000.000 đồng đối với một trong các hành vi sau:
> a) Không thực hiện các biện pháp bảo đảm an toàn, an ninh trong cung ứng dịch vụ bưu chính;
> b) Đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính không có biên bản, chữ ký của các bên liên quan;
> c) Tiết lộ thông tin về sử dụng dịch vụ bưu chính trái pháp luật;
> d) Không đình chỉ vận chuyển, phát bưu gửi hoặc không thông báo cho cơ quan nhà nước có thẩm quyền liên quan để xử lý khi phát hiện bưu gửi vi phạm quy định về vật phẩm, hàng hóa không được gửi, chấp nhận, vận chuyển qua mạng bưu chính.
> 4.
> Phạt tiền từ 20.000.000 đồng đến 30.000.000 đồng đối với một trong các hành vi như sau:
> a) Bóc mở bưu gửi trái pháp luật;
> b) Tráo đổi nội dung bưu gửi;
> c) Chiếm đoạt, trộm cắp bưu gửi có trị giá dưới 2.000.000 đồng hoặc hủy bưu gửi trái pháp luật;
> d) Không phối hợp với cơ quan nhà nước có thẩm quyền thực hiện việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra, xử lý bưu gửi hoặc cung cấp thông tin về sử dụng dịch vụ bưu chính theo quy định của pháp luật.
> 5. Phạt tiền từ 30.000.000 đồng đến 40.000.000 đồng đối với một trong các hành vi sau:
> a) Lợi dụng việc đình chỉ, tạm đình chỉ vận chuyển, phát bưu gửi hoặc kiểm tra xử lý bưu gửi hoặc yêu cầu cung cấp thông tin về sử dụng dịch vụ bưu chính gây thiệt hại đến lợi ích của nhà nước, quyền và lợi ích hợp pháp của tổ chức, cá nhân cung ứng và sử dụng dịch vụ bưu chính;
> b) Cản trở trái pháp luật hoạt động bưu chính.
> 6.
> Biện pháp khắc phục hậu quả:
> Buộc hoàn trả lại bưu gửi đối với hành vi quy định tại các điểm b và c khoản 4 Điều này.

**Câu trả lời:** Mức phạt tiền đối với hành vi bóc mở bưu gửi trái pháp luật là từ 20.000.000 đồng đến 30.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 39 — `11e187524b`

**Câu hỏi:** Điều khiển xe máy chuyển làn đường không đúng quy định gây tai nạn giao thông sẽ bị xử phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng và bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 40 — `d48285f0b7`

**Câu hỏi:** Một cuộc đua chó có ít nhất bao nhiêu trọng tài?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 5. Trọng tài, giám sát
> 1. Trọng tài, giám sát do doanh nghiệp kinh doanh đặt cược đua chó lựa chọn phải bảo đảm các tiêu chuẩn sau đây:
> a) Từ đủ 18 tuổi trở lên;
> b) Có phẩm chất đạo đức tốt;
> c) Nắm vững Điều lệ đua chó.
> 2. Một cuộc đua chó bảo đảm có Ban trọng tài, gồm ít nhất 06 trọng tài, cụ thể: Trọng tài chính, trọng tài cân, trọng tài nhận dạng, trọng tài xuất phát, trọng tài đích đến, trọng tài thư ký.
> 3. Nhiệm vụ của các trọng tài
> a) Trọng tài chính có nhiệm vụ: Phân công nhiệm vụ cho các trọng tài; quyết định chó đua bị loại ra trước khi diễn ra cuộc đua nếu phát hiện có vi phạm Điều lệ đua hoặc quy định của pháp luật; ra các quyết định cuối cùng của Ban trọng tài về cuộc đua trên cơ sở xem xét kết quả thực hiện nhiệm vụ của các trọng tài khác; ký và gửi Hội đồng giám sát cuộc đua biên bản xác định kết quả cuộc đua.
> [2] b) Trọng tài cân có nhiệm vụ: Cân chó đua trước khi cuộc đua bắt đầu; bốc thăm số chuồng xuất phát cho chó đua trong phạm vi hoạt động của camera, với sự chứng kiến của chủ sở hữu chó đua hoặc người huấn luyện chó đua, hoặc người chăm sóc chó đua; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> c) Trọng tài nhận dạng có nhiệm vụ: Nhận dạng chó đua theo tên, đặc điểm nhận dạng, mã số, màu áo đã đăng ký; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> d) Trọng tài xuất phát có nhiệm vụ: Đưa chó đua vào vị trí hộc xuất phát; phát lệnh xuất phát cuộc đua; theo dõi sức khỏe và biểu hiện của chó đua; giám sát việc đưa chó đua về khu vực nhà cân sau khi chó đua về đích; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> [3] đ) Trọng tài đích đến có nhiệm vụ: Xác định thứ hạng về đích của từng chó đua; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> e) Trọng tài thư ký có nhiệm vụ: Tổng hợp, ký và gửi biên bản xác định kết quả thực hiện nhiệm vụ được giao của các trọng tài cho trọng tài chính.
> 4. Giám sát phải có đủ tiêu chuẩn theo quy định tại điểm b và điểm c Khoản 1 Điều này và đã qua thực tế hoạt động trong lĩnh vực công tác từ đủ 5 năm trở lên.
> [4] Điều 28. Trọng tài
> 1. Trọng tài là người do doanh nghiệp kinh doanh đặt cược đua ngựa, đặt cược đua chó lựa chọn đảm bảo đáp ứng tiêu chuẩn Trọng tài do Bộ Văn hóa, Thể thao và Du lịch ban hành.
> 2. Doanh nghiệp phải bố trí đủ số lượng Trọng tài cần thiết để đảm bảo việc giám sát toàn bộ từ khâu kiểm tra tiêu chuẩn ngựa đua, chó đua, đưa ngựa đua, chó đua vào điểm xuất phát, quá trình diễn ra trong cuộc đua và xác định ngựa đua, chó đua khi về đích. Các Trọng tài được tổ chức thành Ban Trọng tài, trong Ban Trọng tài có một Trọng tài chính để ra các quyết định cuối cùng của Ban Trọng tài và chịu trách nhiệm toàn bộ về các quyết định của Ban Trọng tài.
> 3. Trước khi tổ chức các cuộc đua ngựa, đua chó tối thiểu 05 ngày làm việc doanh nghiệp kinh doanh đặt cược đua ngựa, đặt cược đua chó phải gửi danh sách Trọng tài cho Hội đồng giám sát cuộc đua để theo dõi, quản lý.
> [5] iệm vụ của các trọng tài
> a) Trọng tài chính có nhiệm vụ: Phân công nhiệm vụ cho các thành viên Ban trọng tài; quyết định ngựa đua bị loại trước khi diễn ra cuộc đua trong trường hợp có sự gian lận; ra các quyết định cuối cùng của Ban trọng tài về cuộc đua trên cơ sở xem xét kết quả thực hiện nhiệm vụ của các trọng tài khác; ký và gửi Hội đồng giám sát cuộc đua biên bản xác định kết quả cuộc đua;
> b) Trọng tài cân có nhiệm vụ: Cân nài ngựa trước khi bắt đầu cuộc đua và sau khi kết thúc cuộc đua; bốc thăm số chuồng xuất phát cho nài ngựa và ngựa đua; nhận dạng ngựa đua căn cứ vào lý lịch ngựa đua; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký;
> c) Trọng tài xuất phát có nhiệm vụ: Đưa ngựa đua vào vị trí xuất phát; kiểm tra các trang thiết bị của nài ngựa và ngựa đua; phát lệnh xuất phát cuộc đua; giám sát việc đưa ngựa đua và nài ngựa về khu vực nhà cân sau khi ngựa đua về đích; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi

**Bằng chứng vàng:**
> Điều 5. Trọng tài, giám sát
> 1. Trọng tài, giám sát do doanh nghiệp kinh doanh đặt cược đua chó lựa chọn phải bảo đảm các tiêu chuẩn sau đây:
> a) Từ đủ 18 tuổi trở lên;
> b) Có phẩm chất đạo đức tốt;
> c) Nắm vững Điều lệ đua chó.
> 2. Một cuộc đua chó bảo đảm có Ban trọng tài, gồm ít nhất 06 trọng tài, cụ thể: Trọng tài chính, trọng tài cân, trọng tài nhận dạng, trọng tài xuất phát, trọng tài đích đến, trọng tài thư ký.
> 3. Nhiệm vụ của các trọng tài
> a) Trọng tài chính có nhiệm vụ: Phân công nhiệm vụ cho các trọng tài; quyết định chó đua bị loại ra trước khi diễn ra cuộc đua nếu phát hiện có vi phạm Điều lệ đua hoặc quy định của pháp luật; ra các quyết định cuối cùng của Ban trọng tài về cuộc đua trên cơ sở xem xét kết quả thực hiện nhiệm vụ của các trọng tài khác; ký và gửi Hội đồng giám sát cuộc đua biên bản xác định kết quả cuộc đua.
> b) Trọng tài cân có nhiệm vụ: Cân chó đua trước khi cuộc đua bắt đầu; bốc thăm số chuồng xuất phát cho chó đua trong phạm vi hoạt động của camera, với sự chứng kiến của chủ sở hữu chó đua hoặc người huấn luyện chó đua, hoặc người chăm sóc chó đua; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> c) Trọng tài nhận dạng có nhiệm vụ: Nhận dạng chó đua theo tên, đặc điểm nhận dạng, mã số, màu áo đã đăng ký; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> d) Trọng tài xuất phát có nhiệm vụ: Đưa chó đua vào vị trí hộc xuất phát; phát lệnh xuất phát cuộc đua; theo dõi sức khỏe và biểu hiện của chó đua; giám sát việc đưa chó đua về khu vực nhà cân sau khi chó đua về đích; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> đ) Trọng tài đích đến có nhiệm vụ: Xác định thứ hạng về đích của từng chó đua; ký biên bản xác định kết quả thực hiện nhiệm vụ được giao và gửi cho trọng tài thư ký.
> e) Trọng tài thư ký có nhiệm vụ: Tổng hợp, ký và gửi biên bản xác định kết quả thực hiện nhiệm vụ được giao của các trọng tài cho trọng tài chính.
> 4. Giám sát phải có đủ tiêu chuẩn theo quy định tại điểm b và điểm c Khoản 1 Điều này và đã qua thực tế hoạt động trong lĩnh vực công tác từ đủ 5 năm trở lên.

**Câu trả lời:** Một cuộc đua chó phải có Ban trọng tài gồm ít nhất 06 trọng tài.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 41 — `e21605e737`

**Câu hỏi:** Mức phạt khi nằm trên yên xe điều khiển xe máy

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 42 — `bfb95d40b3`

**Câu hỏi:** Tránh xe máy không đúng quy định gây tai nạn giao thông sẽ bị xử phạt thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ các hành vi vi phạm quy định tại điểm a khoản 8 Điều này;
> b) Điều khiển xe lạng lách, đánh võng; chạy quá tốc độ đuổi nhau trên đường bộ; dùng chân điều khiển vô lăng xe khi xe đang chạy trên đường;
> c) Điều khiển xe chạy quá tốc độ quy định trên 35 km/h.
> 8.
> [2] Phạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ các hành vi vi phạm quy định tại điểm a, điểm b khoản 8 Điều này;
> b) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> [3] ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe lạng lách, đánh võng; đuổi nhau trên đường;
> b) Đi xe bằng một bánh đối với xe đạp, xe đạp máy; đi xe bằng hai bánh đối với xe xích lô;
> c) Đi vào khu vực cấm; đường có biển báo hiệu nội dung cấm đi vào đối với loại phương tiện đang điều khiển; đi ngược chiều đường của đường một chiều, đường có biển “Cấm đi ngược chiều”;
> d) Người điều khiển xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ;
> đ) Chở người ngồi trên xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06
> [4] Người nào chịu trách nhiệm trực tiếp về việc điều động hoặc về tình trạng kỹ thuật mà cho phép đưa vào sử dụng phương tiện giao thông cơ giới đường bộ, xe máy chuyên dùng rõ ràng không bảo đảm tiêu chuẩn an toàn kỹ thuật gây thiệt hại cho người khác thuộc một trong các trường hợp sau đây, thì bị phạt tiền từ 20.000.000 đồng đến 100.000.000 đồng, phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm:
> a) Làm chết người;
> b) Gây thương tích hoặc gây tổn hại cho sức khỏe của 01 người mà tỷ lệ tổn thương cơ thể 61% trở lên;
> c) Gây thương tích hoặc gây tổn hại cho sức khỏe của 02 người trở lên mà tổng tỷ lệ tổn thương cơ thể của những người này từ 61% đến 121%;
> d) Gây thiệt hại về tài sản từ 100.000.000 đồng đến dưới 500.000.000 đồng.
> 2.
> [5] Phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Lùi xe trên đường cao tốc; đi ngược chiều trên đường cao tốc;
> b) Điều khiển xe máy chuyên dùng có tốc độ thiết kế nhỏ hơn 70 km/h, máy kéo đi vào đường cao tốc, trừ phương tiện, thiết bị phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn.
> 9.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Người điều khiển xe thực hiện hành vi tránh xe không đúng quy định gây tai nạn giao thông sẽ bị phạt tiền từ 10.000.000 đồng đến 12.000.000 đồng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 43 — `87f4506b57`

**Câu hỏi:** Dùng chân điều khiển xe máy sẽ bị xử phạt như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] 2. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe đạp, xe đạp máy buông cả hai tay; chuyển hướng đột ngột trước đầu xe cơ giới đang chạy; dùng chân điều khiển xe đạp, xe đạp máy;
> b) Không chấp hành hiệu lệnh, chỉ dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> c) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, mang vác vật cồng kềnh; điều khiển xe kéo theo xe khác, vật khác;
> d) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn hoặc gây cản trở đối với xe cơ giới xin vượt, gây cản trở xe ưu tiên;
> đ) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông.
> 3.
> [2] ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe lạng lách, đánh võng; đuổi nhau trên đường;
> b) Đi xe bằng một bánh đối với xe đạp, xe đạp máy; đi xe bằng hai bánh đối với xe xích lô;
> c) Đi vào khu vực cấm; đường có biển báo hiệu nội dung cấm đi vào đối với loại phương tiện đang điều khiển; đi ngược chiều đường của đường một chiều, đường có biển “Cấm đi ngược chiều”;
> d) Người điều khiển xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ;
> đ) Chở người ngồi trên xe đạp máy (kể cả xe đạp điện) không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06
> [3] Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe đạp, xe đạp máy, người điều khiển xe thô sơ dừng xe, đỗ xe trong phạm vi an toàn đường ngang, cầu chung; vượt rào chắn đường ngang, cầu chung khi chắn đang dịch chuyển; vượt đường ngang, cầu chung khi đèn đỏ đã bật sáng; không chấp hành hiệu lệnh, chỉ dẫn của nhân viên gác đường ngang, cầu chung khi đi qua đường ngang, cầu chung.
> 4. Phạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy dừng xe, đỗ xe trong phạm vi an toàn đường ngang, cầu chung; không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường khi đi qua đường ngang, cầu chung.
> 5.
> [4] Điều 22. Xử phạt các hành vi vi phạm quy định về điều kiện của người điều khiển xe máy chuyên dùng
> 1. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Người điều khiển xe máy chuyên dùng không đúng độ tuổi hoặc tuổi không phù hợp với ngành nghề theo quy định;
> b) Người điều khiển xe máy chuyên dùng không mang theo bằng (hoặc chứng chỉ) điều khiển, chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ;
> c) Người điều khiển xe máy chuyên dùng không mang theo Giấy đăng ký xe;
> d) Người điều khiển xe máy chuyên dùng không mang theo Giấy chứng nhận an toàn kỹ thuật và bảo vệ môi trường (đối với loại xe có quy định phải kiểm định).
> 2. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe máy chuyên dùng không có bằng (hoặc chứng chỉ) điều khiển, chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ.
> [5] ạt tiền từ 80.000 đồng đến 100.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không đi bên phải theo chiều đi của mình, đi không đúng phần đường quy định;
> b) Dừng xe đột ngột; chuyển hướng không báo hiệu trước;
> c) Không chấp hành hiệu lệnh hoặc chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm đ khoản 2, điểm c khoản 3 Điều này;
> d) Vượt bên phải trong các trường hợp không được phép;
> đ) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> e) Chạy trong hầm đường bộ không có đèn hoặc vật phát sáng báo hiệu; dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> g) Điều khiển xe đạp, xe đạp máy đi dàn hàng ngang từ 03 xe trở lên, xe thô sơ khác đi dàn hàng ngang từ 02 xe trở lên;
> h) Người điều khiển xe đạp, xe đạp máy sử dụng ô (dù), điện thoại di động; chở người ngồi trên xe đạp

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Bị phạt tiền từ 100.000 đồng đến 200.000 đồng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 44 — `8b6f8327af`

**Câu hỏi:** Đi xe máy bấm còi, rú ga liên tục trong đô thị khu dân cư bị phạt bao nhiêu?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 80.000 đồng đến 100.000 đồng và tước quyền sử dụng giấy phép lái xe từ 1 đến 2 tháng.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 45 — `fe8432c604`

**Câu hỏi:** Mức phạt đối với hành vi điều khiển xe máy có sử dụng ô (dù)

**Ngữ cảnh đã cung cấp:**
> [1] Điều 11. Xử phạt các hành vi vi phạm khác về quy tắc giao thông đường bộ
> 1. Phạt tiền từ 80.000 đồng đến 100.000 đồng đối với người được chở trên xe đạp, xe đạp máy sử dụng ô (dù).
> 2. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với cá nhân thực hiện một trong các hành vi vi phạm sau đây:
> a) Tập trung đông người trái phép, nằm, ngồi trên đường bộ gây cản trở giao thông;
> b) Đá bóng, đá cầu, chơi cầu lông hoặc các hoạt động thể thao khác trái phép trên đường bộ; sử dụng bàn trượt, pa-tanh, các thiết bị tương tự trên phần đường xe chạy;
> c) Người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy sử dụng ô (dù);
> d) Người được chở trên xe đạp, xe đạp máy bám, kéo, đẩy xe khác, vật khác, mang vác vật cồng kềnh.
> 3.
> [2] Điều 16. Xử phạt người điều khiển xe ô tô (bao gồm cả rơ moóc hoặc sơ mi rơ moóc được kéo theo) và các loại xe tương tự xe ô tô vi phạm quy định về điều kiện của phương tiện khi tham gia giao thông
> 1. Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với hành vi điều khiển xe không có kính chắn gió hoặc có nhưng vỡ hoặc có nhưng không có tác dụng (đối với xe có thiết kế lắp kính chắn gió).
> 2.
> [3] Phạt tiền từ 800.000 đồng đến 1.200.000 đồng đối với người điều khiển xe mô tô hai bánh có dung tích xi lanh dưới 175 cm3 và các loại xe tương tự xe mô tô thực hiện một trong các hành vi vi phạm sau đây:
> a) Không có Giấy phép lái xe hoặc sử dụng Giấy phép lái xe không do cơ quan có thẩm quyền cấp, Giấy phép lái xe bị tẩy xóa;
> b) Có Giấy phép lái xe quốc tế do các nước tham gia Công ước về Giao thông đường bộ năm 1968 cấp (trừ Giấy phép lái xe quốc tế do Việt Nam cấp) nhưng không mang theo Giấy phép lái xe quốc gia;
> c) Sử dụng Giấy phép lái xe không hợp lệ (Giấy phép lái xe có số phôi ghi ở mặt sau không trùng với số phôi được cấp mới nhất trong hệ thống thông tin quản lý Giấy phép lái xe).
> 6. Phạt tiền từ 1.200.000 đồng đến 3.000.000 đồng đối với người từ đủ 16 tuổi đến dưới 18 tuổi điều khiển xe ô tô, máy kéo, các loại xe tương tự xe ô tô.
> 7.
> [4] Phạt tiền từ 28.000.000 đồng đến 32.000.000 đồng đối với cá nhân, từ 56.000.000 đồng đến 64.000.000 đồng đối với tổ chức là chủ xe ô tô, máy kéo, xe máy chuyên dùng và các loại xe tương tự xe ô tô khi giao phương tiện hoặc để cho người làm công, người đại diện điều khiển phương tiện thực hiện hành vi vi phạm quy định tại điểm a khoản 6 Điều 33 Nghị định này hoặc trực tiếp điều khiển phương tiện thực hiện hành vi vi phạm quy định tại điểm a khoản 6 Điều 33 Nghị định này.
> 14.
> [5] Phạt tiền từ 200.000 đồng đến 400.000 đồng đối với một trong các hành vi vi phạm sau đây:
> a) Người điều khiển xe ô tô, máy kéo và các loại xe tương tự xe ô tô không mang theo Giấy phép lái xe, trừ hành vi vi phạm quy định tại điểm c khoản 8 Điều này;
> b) Người điều khiển xe ô tô, máy kéo và các loại xe tương tự xe ô tô không mang theo Giấy đăng ký xe (kể cả rơ moóc và sơ mi rơ moóc);
> c) Người điều khiển xe ô tô, máy kéo và các loại xe tương tự xe ô tô không mang theo Giấy chứng nhận kiểm định an toàn kỹ thuật và bảo vệ môi trường (đối với loại xe có quy định phải kiểm định, kể cả rơ moóc và sơ mi rơ moóc).
> 4.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người được chở trên xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy sử dụng ô (dù).

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 46 — `960e37c28c`

**Câu hỏi:** Mức phạt khi nằm trên yên xe điều khiển xe máy mà không chấp hành hiệu lệnh dừng xe được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Người điều khiển xe nằm trên yên xe điều khiển xe máy mà không chấp hành hiệu lệnh dừng xe của người thi hành công vụ bị phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA

---

## Mẫu 47 — `7bee29d8b2`

**Câu hỏi:** Mức phạt hành vi chạy xe máy gây tai nạn giao thông mà không tham gia cấp cứu người bị nạn

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt hành vi chạy xe máy gây tai nạn giao thông mà không tham gia cấp cứu người bị nạn là từ 2.000.000 đồng đến 4.000.000 đồng và bị tước quyền sử dụng giấy phép lái xe từ 2 tháng đến 4 tháng theo quy định tại Điều 171 Luật Giao thông đường bộ 2008.

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 48 — `ae79f5de05`

**Câu hỏi:** Mức phạt hành vi không chấp hành hiệu lệnh của cảnh sát giao thông

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt hành vi không chấp hành hiệu lệnh của cảnh sát giao thông là từ 800.000 đồng đến 1.000.000 đồng theo quy định tại Điều 8 của Nghị định 100/2019/NĐ-CP (được sửa đổi, bổ sung bởi Nghị định 123/2021/NĐ-CP).

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 49 — `1ab13e4c51`

**Câu hỏi:** Mức phạt đối với hành vi điều khiển xe máy mà mang vác vật cồng kềnh ?

**Ngữ cảnh đã cung cấp:**
> (không cung cấp - closed-book)

**Bằng chứng vàng:**
> Điều 6. Xử phạt người điều khiển xe mô tô, xe gắn máy (kể cả xe máy điện), các loại xe tương tự xe mô tô và các loại xe tương tự xe gắn máy vi phạm quy tắc giao thông đường bộ
> 1.
> ạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Không chấp hành hiệu lệnh, chỉ dẫn của biển báo hiệu, vạch kẻ đường, trừ các hành vi vi phạm quy định tại điểm c, điểm đ, điểm e, điểm h khoản 2; điểm d, điểm g, điểm i, điểm m khoản 3; điểm a, điểm b, điểm c, điểm d, điểm e khoản 4; khoản 5; điểm b khoản 6; điểm a, điểm b khoản 7; điểm d khoản 8 Điều này;
> b) Không có báo hiệu xin vượt trước khi vượt;
> c) Không giữ khoảng cách an toàn để xảy ra va chạm với xe chạy liền trước hoặc không giữ khoảng cách theo quy định của biển báo hiệu “Cự ly tối thiểu giữa hai xe”;
> d) Chuyển hướng không nhường quyền đi trước cho: Người đi bộ, xe lăn của người khuyết tật qua đường tại nơi có vạch kẻ đường dành cho người đi bộ; xe thô sơ đang đi trên phần đường dành cho xe thô sơ;
> đ) Chuyển hướng không nhường đường cho: Các xe đi ngược chiều; người đi bộ, xe lăn của người khuyết tật đang qua đường tại nơi không có vạch kẻ đường cho người đi bộ;
> e) Lùi xe mô tô ba bánh không quan sát hoặc không có tín hiệu báo trước;
> g) Chở người ngồi trên xe sử dụng ô (dù);
> h) Không tuân thủ các quy định về nhường đường tại nơi đường giao nhau, trừ các hành vi vi phạm quy định tại điểm b, điểm e khoản 2 Điều này;
> i) Chuyển làn đường không đúng nơi được phép hoặc không có tín hiệu báo trước;
> k) Điều khiển xe chạy dàn hàng ngang từ 03 xe trở lên;
> l) Không sử dụng đèn chiếu sáng trong thời gian từ 19 giờ ngày hôm trước đến 05 giờ ngày hôm sau hoặc khi sương mù, thời tiết xấu hạn chế tầm nhìn;
> m) Tránh xe không đúng quy định; sử dụng đèn chiếu xa khi tránh xe đi ngược chiều; không nhường đường cho xe đi ngược chiều theo quy định tại nơi đường hẹp, đường dốc, nơi có chướng ngại vật;
> n) Bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> o) Xe được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu ưu tiên không đúng quy định hoặc sử dụng thiết bị phát tín hiệu ưu tiên mà không có Giấy phép của cơ quan có thẩm quyền cấp hoặc có Giấy phép của cơ quan có thẩm quyền cấp nhưng không còn giá trị sử dụng theo quy định;
> p) Quay đầu xe tại nơi không được quay đầu xe, trừ hành vi vi phạm quy định tại điểm d khoản 4 Điều này;
> q) Điều khiển xe chạy dưới tốc độ tối thiểu trên những đoạn đường bộ có quy định tốc độ tối thiểu cho phép.
> 2.
> ạt tiền từ 200.000 đồng đến 300.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Dừng xe, đỗ xe trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường;
> b) Không giảm tốc độ và nhường đường khi điều khiển xe chạy từ trong ngõ, đường nhánh ra đường chính;
> c) Điều khiển xe chạy quá tốc độ quy định từ 05 km/h đến dưới 10 km/h;
> d) Điều khiển xe chạy tốc độ thấp mà không đi bên phải phần đường xe chạy gây cản trở giao thông;
> đ) Dừng xe, đỗ xe ở lòng đường đô thị gây cản trở giao thông; tụ tập từ 03 xe trở lên ở lòng đường, trong hầm đường bộ; đỗ, để xe ở lòng đường đô thị, hè phố trái quy định của pháp luật;
> e) Không nhường đường cho xe xin vượt khi có đủ điều kiện an toàn; không nhường đường cho xe đi trên đường ưu tiên, đường chính từ bất kỳ hướng nào tới tại nơi đường giao nhau;
> g) Xe không được quyền ưu tiên lắp đặt, sử dụng thiết bị phát tín hiệu của xe được quyền ưu tiên;
> h) Dừng xe, đỗ xe trên đường xe điện, điểm dừng đón trả khách của xe buýt, nơi đường bộ giao nhau, trên phần đường dành cho người đi bộ qua đường; dừng xe nơi có biển “Cấm dừng xe và đỗ xe”; đỗ xe tại nơi có biển “Cấm đỗ xe” hoặc biển “Cấm dừng xe và đỗ xe”; không tuân thủ các quy định về dừng xe, đỗ xe tại nơi đường bộ giao nhau cùng mức với đường sắt; dừng xe, đỗ xe trong phạm vi an toàn của đường sắt, trừ hành vi vi phạm quy định tại điểm b khoản 2, điểm b khoản 3 Điều 49 Nghị định này;
> i) Không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi điều khiển xe tham gia giao thông trên đường bộ;
> k) Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật;
> l) Chở theo 02 người trên xe, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 14 tuổi, áp giải người có hành vi vi phạm pháp luật;
> m) Ngồi phía sau vòng tay qua người ngồi trước để điều khiển xe, trừ trường hợp chở trẻ em ngồi phía trước.
> 3.
> ạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Chuyển hướng không giảm tốc độ hoặc không có tín hiệu báo hướng rẽ (trừ trường hợp điều khiển xe đi theo hướng cong của đoạn đường bộ ở nơi đường không giao nhau cùng mức);
> b) Chở theo từ 03 người trở lên trên xe;
> c) Bấm còi, rú ga (nẹt pô) liên tục trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định;
> d) Dừng xe, đỗ xe trên cầu;
> đ) Điều khiển xe thành đoàn gây cản trở giao thông, trừ trường hợp được cơ quan có thẩm quyền cấp phép;
> e) Điều khiển xe có liên quan trực tiếp đến vụ tai nạn giao thông mà không dừng lại, không giữ nguyên hiện trường, không tham gia cấp cứu người bị nạn, trừ hành vi vi phạm quy định tại điểm đ khoản 8 Điều này;
> g) Điều khiển xe không đi bên phải theo chiều đi của mình; đi không đúng phần đường, làn đường quy định (làn cùng chiều hoặc làn ngược chiều); điều khiển xe đi qua dải phân cách cố định ở giữa hai phần đường xe chạy; điều khiển xe đi trên hè phố, trừ trường hợp điều khiển xe đi qua hè phố để vào nhà;
> h) Vượt bên phải trong trường hợp không được phép;
> i) Đi vào khu vực cấm, đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại khoản 5, điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định;
> k) Người đang điều khiển xe hoặc chở người ngồi trên xe bám, kéo, đẩy xe khác, vật khác, dẫn dắt súc vật, mang vác vật cồng kềnh; chở người đứng trên yên, giá đèo hàng hoặc ngồi trên tay lái; xếp hàng hóa trên xe vượt quá giới hạn quy định; điều khiển xe kéo theo xe khác, vật khác;
> l) Chở hàng vượt trọng tải thiết kế được ghi trong Giấy đăng ký xe đối với loại xe có quy định về trọng tải thiết kế;
> m) Chạy trong hầm đường bộ không sử dụng đèn chiếu sáng gần.
> 4. Phạt tiền từ 600.000 đồng đến 1.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;
> b) Dừng xe, đỗ xe trong hầm đường bộ không đúng nơi quy định;
> c) Vượt xe trong những trường hợp không được vượt, vượt xe tại đoạn đường có biển báo hiệu có nội dung cấm vượt đối với loại phương tiện đang điều khiển, trừ các hành vi vi phạm quy định tại điểm h khoản 3 Điều này;
> d) Vượt xe trong hầm đường bộ không đúng nơi quy định; quay đầu xe trong hầm đường bộ;
> đ) Không nhường đường hoặc gây cản trở xe được quyền ưu tiên đang phát tín hiệu ưu tiên đi làm nhiệm vụ;
> e) Không chấp hành hiệu lệnh của đèn tín hiệu giao thông;
> g) Không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông;
> h) Người đang điều khiển xe sử dụng ô (dù), điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.
> 5.
> Phạt tiền từ 1.000.000 đồng đến 2.000.000 đồng đối với người điều khiển xe thực hiện hành vi đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều”, trừ hành vi vi phạm quy định tại điểm b khoản 6 Điều này và các trường hợp xe ưu tiên đang đi làm nhiệm vụ khẩn cấp theo quy định.
> 6. Phạt tiền từ 2.000.000 đồng đến 3.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Sử dụng chân chống hoặc vật khác quệt xuống đường khi xe đang chạy;
> b) Điều khiển xe đi vào đường cao tốc, trừ xe phục vụ việc quản lý, bảo trì đường cao tốc;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn nhưng chưa vượt quá 50 miligam/100 mililít máu hoặc chưa vượt quá 0,25 miligam/1 lít khí thở.
> 7.
> Phạt tiền từ 4.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Điều khiển xe chạy quá tốc độ quy định trên 20 km/h;
> b) Không chú ý quan sát, điều khiển xe chạy quá tốc độ quy định gây tai nạn giao thông; đi vào đường cao tốc, dừng xe, đỗ xe, quay đầu xe, lùi xe, tránh xe, vượt xe, chuyển hướng, chuyển làn đường không đúng quy định gây tai nạn giao thông; không đi đúng phần đường, làn đường, không giữ khoảng cách an toàn giữa hai xe theo quy định gây tai nạn giao thông hoặc đi vào đường có biển báo hiệu có nội dung cấm đi vào đối với loại phương tiện đang điều khiển, đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển “Cấm đi ngược chiều” gây tai nạn giao thông, trừ hành vi vi phạm quy định tại điểm d khoản 8 Điều này;
> c) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 50 miligam đến 80 miligam/100 mililít máu hoặc vượt quá 0,25 miligam đến 0,4 miligam/1 lít khí thở.
> 8.
> ạt tiền từ 6.000.000 đồng đến 8.000.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau đây:
> a) Buông cả hai tay khi đang điều khiển xe; dùng chân điều khiển xe; ngồi về một bên điều khiển xe; nằm trên yên xe điều khiển xe; thay người điều khiển khi xe đang chạy; quay người về phía sau để điều khiển xe hoặc bịt mắt điều khiển xe;
> b) Điều khiển xe lạng lách hoặc đánh võng trên đường bộ trong, ngoài đô thị;
> c) Điều khiển xe chạy bằng một bánh đối với xe hai bánh, chạy bằng hai bánh đối với xe ba bánh;
> d) Điều khiển xe thành nhóm từ 02 xe trở lên chạy quá tốc độ quy định;
> đ) Gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn;
> e) Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;
> g) Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;
> h) Điều khiển xe trên đường mà trong cơ thể có chất ma túy;
> i) Không chấp hành yêu cầu kiểm tra về chất ma túy của người thi hành công vụ.
> 9. Phạt tiền từ 10.000.000 đồng đến 14.000.000 đồng đối với hành vi vi phạm quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này mà gây tai nạn giao thông hoặc không chấp hành hiệu lệnh dừng xe của người thi hành công vụ.
> 10.
> Ngoài việc bị phạt tiền, người điều khiển xe thực hiện hành vi vi phạm còn bị áp dụng các hình thức xử phạt bổ sung sau đây:
> a) Thực hiện hành vi quy định tại điểm g khoản 2 Điều này bị tịch thu thiết bị phát tín hiệu ưu tiên lắp đặt, sử dụng trái quy định;
> b) Thực hiện hành vi quy định tại điểm b, điểm e, điểm i khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4; khoản 5 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 01 tháng đến 03 tháng;
> c) Thực hiện hành vi quy định tại điểm a khoản 6; điểm a, điểm b khoản 7; điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng; tái phạm hoặc vi phạm nhiều lần hành vi quy định tại điểm a, điểm b, điểm c, điểm d khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng, tịch thu phương tiện.
>  hiện hành vi quy định tại một trong các điểm, khoản sau của Điều này mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng: Điểm a, điểm g, điểm h, điểm k, điểm l, điểm m, điểm n, điểm q khoản 1; điểm b, điểm d, điểm e, điểm g, điểm l, điểm m khoản 2; điểm b, điểm c, điểm k, điểm m khoản 3; điểm đ, điểm e, điểm g, điểm h khoản 4 Điều này;
> d) Thực hiện hành vi quy định tại điểm b khoản 6; điểm đ khoản 8; khoản 9 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 03 tháng đến 05 tháng;
> đ) Thực hiện hành vi quy định tại điểm c khoản 6 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 10 tháng đến 12 tháng;
> e) Thực hiện hành vi quy định tại điểm c khoản 7 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 16 tháng đến 18 tháng;
> g) Thực hiện hành vi quy định tại điểm e, điểm g, điểm h, điểm i khoản 8 Điều này bị tước quyền sử dụng Giấy phép lái xe từ 22 tháng đến 24 tháng.

**Câu trả lời:** Mức phạt đối với hành vi điều khiển xe máy mang vác vật cồng kềnh là từ 80.000 đồng đến 200.000 đồng theo quy định tại Điều 8 của Nghị định 100/2019/NĐ-CP (và các văn bản sửa đổi liên quan).

Correctness: [x] 0   [ ] 1   [ ] 2
H_gold: [ ] 0   [x] 1
H_ctx: [ ] 0   [ ] 1   [x] NA

---

## Mẫu 50 — `69d0180d7e`

**Câu hỏi:** Nhiệm vụ, quyền hạn của Bộ Xây dựng trong hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh được quy định như thế nào?

**Ngữ cảnh đã cung cấp:**
> [1] Điều 42. Nhiệm vụ, quyền hạn của Bộ Xây dựng
> Chủ trì, phối hợp với Bộ Quốc phòng trong thẩm định, ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.
> [2] Điều 36. Nhiệm vụ, quyền hạn của Bộ Quốc phòng
> Bộ Quốc phòng chịu trách nhiệm trước Chính phủ thực hiện thống nhất quản lý nhà nước trong hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh, có nhiệm vụ và quyền hạn sau:
> 1. Quản lý hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh; đào tạo, nghiên cứu khoa học kỹ thuật và công nghệ rà phá bom mìn vật nổ; quản lý tiêu chuẩn kỹ thuật rà phá bom mìn vật nổ; quản lý thông tin, dữ liệu về hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh.
> 2. Chủ trì và phối hợp với các bộ, cơ quan, tổ chức và các địa phương liên quan xây dựng tiêu chí lựa chọn đề xuất chương trình khắc phục hậu quả bom mìn vật nổ sau chiến tranh; xây dựng và ban hành các quy chuẩn, tiêu chuẩn, quy trình, định mức kỹ thuật áp dụng trong hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh theo thẩm quyền.
> 3.
> [3] Điều 46. Nhiệm vụ, quyền hạn của chủ đầu tư và các tổ chức tham gia hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh
> 1. Thực hiện nghiêm các quy định của Nghị định này và các văn bản hướng dẫn thực hiện liên quan.
> 2. Thực hiện quy định đăng ký cấp mới hoặc cấp lại chứng chỉ năng lực hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh theo quy định của Bộ Quốc phòng.
> 3. Chịu trách nhiệm tổng hợp, cung cấp cho Trung tâm Hành động bom mìn quốc gia Việt Nam thông tin, dữ liệu về tình hình và kết quả thực hiện hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh của đơn vị, tổ chức mình.
> [4] Nhiệm vụ khắc phục hậu quả bom mìn vật nổ sau chiến tranh là các hoạt động khắc phục hậu quả bom mìn vật nổ được Chính phủ, Bộ Quốc phòng hoặc cấp có thẩm quyền giao các đơn vị quân đội hoặc các tổ chức khắc phục hậu quả bom mìn vật nổ thực hiện.
> [5] Điều 44. Nhiệm vụ, quyền hạn của các bộ, ngành liên quan
> Bộ, cơ quan ngang bộ theo chức năng, nhiệm vụ được giao có trách nhiệm phối hợp thực hiện hoạt động khắc phục hậu quả bom mìn vật nổ sau chiến tranh.

**Bằng chứng vàng:**
> Điều 42. Nhiệm vụ, quyền hạn của Bộ Xây dựng
> Chủ trì, phối hợp với Bộ Quốc phòng trong thẩm định, ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.

**Câu trả lời:** Bộ Xây dựng có nhiệm vụ chủ trì, phối hợp với Bộ Quốc phòng trong việc thẩm định và ban hành các quy trình, định mức liên quan đến hoạt động điều tra, khảo sát, rà phá bom mìn vật nổ sau chiến tranh.

Correctness: [ ] 0   [ ] 1   [x] 2
H_gold: [x] 0   [ ] 1
H_ctx: [x] 0   [ ] 1   [ ] NA
