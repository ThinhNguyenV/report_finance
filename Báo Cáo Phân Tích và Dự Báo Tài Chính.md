# Báo Cáo Phân Tích và Dự Báo Tài Chính

**Nguồn Dữ liệu:** `Database-Q3_2020.xlsx` (Quý 3 năm 2020)

## 1. Tóm Tắt Điều Hành

Báo cáo này trình bày kết quả phân tích dữ liệu tài chính từ Quý 3 năm 2020 và dự báo doanh thu cho 30 ngày tiếp theo (từ 03/10/2020 đến 01/11/2020).

Phân tích cho thấy **Doanh thu** có xu hướng biến động mạnh theo ngày, với một số đỉnh điểm đáng chú ý. Mô hình dự báo được xây dựng dựa trên thuật toán **Random Forest Regressor** sử dụng các đặc trưng chuỗi thời gian (như ngày trong tuần, ngày trong tháng, và các giá trị doanh thu trễ).

**Tổng Doanh thu Dự báo** cho 30 ngày tiếp theo là **680.565.999 VNĐ**.

## 2. Phân Tích Dữ Liệu Lịch Sử (Q3 2020)

Dữ liệu được tổng hợp từ các sheet **MKT** và **Sales** để tạo ra một chuỗi thời gian hàng ngày về **Chi phí Marketing** và **Doanh thu**.

### 2.1. Xu Hướng Doanh Thu và Chi Phí

Biểu đồ dưới đây minh họa xu hướng hàng ngày của Doanh thu (từ sheet MKT) và Chi phí Marketing trong Quý 3 năm 2020.

![Xu hướng Tài chính Q3 2020](predict/finance_trend.png)

**Nhận xét:**
*   **Doanh thu** (đường màu xanh) có sự biến động lớn, đạt đỉnh cao nhất vào khoảng cuối tháng 8 và đầu tháng 9.
*   **Chi phí Marketing** (đường màu cam) có xu hướng ổn định hơn, nhưng cũng có một số ngày chi phí tăng đột biến (đặc biệt là vào đầu tháng 8), có thể liên quan đến các chiến dịch quảng cáo lớn.
*   Mối quan hệ giữa Chi phí Marketing và Doanh thu không hoàn toàn tuyến tính, cho thấy các yếu tố khác (như chất lượng chiến dịch, ngày trong tuần, v.v.) cũng ảnh hưởng đáng kể.

## 3. Mô Hình Dự Báo

### 3.1. Phương Pháp Luận

*   **Mục tiêu:** Dự báo **Doanh thu** hàng ngày.
*   **Mô hình:** **Random Forest Regressor** (Hồi quy Rừng Ngẫu nhiên). Mô hình này được chọn vì khả năng xử lý tốt các mối quan hệ phi tuyến tính và không yêu cầu tính dừng của chuỗi thời gian như các mô hình ARIMA truyền thống.
*   **Đặc trưng (Features) sử dụng:**
    *   Các đặc trưng thời gian: Ngày trong tuần, Ngày trong tháng, Tháng.
    *   Các biến trễ (Lag features): Doanh thu của 7 ngày trước đó (`revenue_lag_1` đến `revenue_lag_7`).
    *   Trung bình trượt: Trung bình doanh thu của 7 ngày gần nhất (`revenue_rolling_mean_7`).

### 3.2. Đánh Giá Mô Hình

Mô hình được huấn luyện trên 80% dữ liệu và kiểm tra trên 20% dữ liệu còn lại.

| Chỉ số Đánh giá | Giá trị (VNĐ) |
| :--- | :--- |
| **Mean Absolute Error (MAE)** | 12.226.622 |
| **Root Mean Squared Error (RMSE)** | 16.828.903 |

MAE là sai số tuyệt đối trung bình, cho biết mức độ sai lệch trung bình của dự báo so với thực tế. Với MAE khoảng 12.2 triệu VNĐ, mô hình có mức độ chính xác chấp nhận được cho việc dự báo xu hướng tổng thể.

## 4. Kết Quả Dự Báo

Dự báo được thực hiện cho 30 ngày tiếp theo, bắt đầu từ ngày 03/10/2020.

### 4.1. Tổng Quan Dự Báo

| Chỉ số | Giá trị |
| :--- | :--- |
| **Giai đoạn Dự báo** | 03/10/2020 - 01/11/2020 |
| **Tổng Doanh thu Dự báo** | **680.565.999 VNĐ** |
| **Doanh thu Trung bình Dự báo/ngày** | 22.685.533 VNĐ |

### 4.2. Xu Hướng Dự Báo Chi Tiết

Biểu đồ dưới đây kết hợp dữ liệu lịch sử và dự báo.

![Xu hướng Doanh thu Lịch sử và Dự báo](predict/finance_forecast_combined_trend.png)

**Nhận xét về Dự báo:**
*   **Xu hướng:** Doanh thu dự báo (đường đứt nét màu đỏ) cho thấy một xu hướng tương đối ổn định trong tháng tới, dao động quanh mức 20-30 triệu VNĐ/ngày.
*   **So sánh:** Mức doanh thu dự báo này thấp hơn đáng kể so với các đỉnh điểm trong Quý 3 (đặc biệt là cuối tháng 8/đầu tháng 9), nhưng cao hơn mức đáy của chu kỳ. Điều này có thể phản ánh sự suy giảm tự nhiên sau một giai đoạn tăng trưởng mạnh hoặc sự thiếu vắng các yếu tố thúc đẩy doanh thu lớn trong dữ liệu trễ.

## 5. Phụ Lục: Dữ Liệu Dự Báo Chi Tiết

Dữ liệu dự báo chi tiết theo ngày đã được lưu trong tệp **`finance_forecast_next_month.csv`** đính kèm.

| Ngày | Doanh thu Dự báo (VNĐ) |
| :--- | :--- |
| 2020-10-03 | 31.787.690 |
| 2020-10-04 | 28.238.160 |
| 2020-10-05 | 28.847.960 |
| 2020-10-06 | 30.548.490 |
| 2020-10-07 | 31.140.220 |
| ... | ... |
| 2020-11-01 | 24.288.070 |

## 6. Khuyến Nghị

Để cải thiện độ chính xác của mô hình trong tương lai, cần xem xét:
1.  **Thêm Đặc trưng:** Đưa thêm các đặc trưng liên quan đến **Chi phí Marketing** và **Paid Revenue 1** vào mô hình dự báo Doanh thu, vì chúng có thể là các biến giải thích quan trọng.
2.  **Mô hình Chuyên sâu:** Thử nghiệm các mô hình chuỗi thời gian chuyên sâu hơn như Prophet của Facebook hoặc các mô hình mạng nơ-ron hồi quy (RNN/LSTM) nếu dữ liệu lịch sử dài hơn.
3.  **Phân tích Nguyên nhân:** Điều tra nguyên nhân của các đỉnh doanh thu và chi phí đột biến để có thể đưa các sự kiện này vào mô hình dưới dạng biến ngoại sinh (exogenous variables).
