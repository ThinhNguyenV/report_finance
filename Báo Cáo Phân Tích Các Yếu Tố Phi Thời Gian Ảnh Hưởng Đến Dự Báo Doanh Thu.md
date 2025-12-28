# Báo Cáo Phân Tích Các Yếu Tố Phi Thời Gian Ảnh Hưởng Đến Dự Báo Doanh Thu

**Nguồn Dữ liệu:** `Database-Q3_2020.xlsx` (Quý 3 năm 2020)

## 1. Tóm Tắt Điều Hành

Mô hình dự báo doanh thu ban đầu (sử dụng Random Forest Regressor) chỉ dựa trên các yếu tố chuỗi thời gian (doanh thu trễ, ngày trong tuần/tháng). Báo cáo này phân tích các yếu tố phi thời gian quan trọng khác (Marketing, Kênh, Nhân sự) có thể ảnh hưởng đến độ chính xác của dự báo và đề xuất cách tích hợp chúng.

Các yếu tố này, nếu không được tính đến, sẽ làm giảm độ chính xác của dự báo, đặc biệt trong các tình huống có sự thay đổi lớn về chiến lược Marketing hoặc hiệu suất hoạt động.

## 2. Phân Tích Tương Quan Giữa Chi Phí Marketing và Doanh Thu

Mối quan hệ giữa Chi phí Marketing và Doanh thu là yếu tố phi thời gian quan trọng nhất.

### 2.1. Hệ Số Tương Quan

Phân tích tương quan trên dữ liệu cấp độ chiến dịch/ngày cho thấy:

| Biến | Chi phí Marketing | Doanh thu | Lead MKT | Đơn hàng |
| :--- | :--- | :--- | :--- | :--- |
| **Chi phí Marketing** | 1.00 | **0.60** | 0.61 | 0.60 |
| **Doanh thu** | 0.60 | 1.00 | **0.99** | **1.00** |

*   **Tương quan Chi phí - Doanh thu:** Hệ số tương quan **0.60** cho thấy mối quan hệ tích cực và khá mạnh giữa Chi phí Marketing và Doanh thu. Việc tăng chi phí có xu hướng làm tăng doanh thu.
*   **Tương quan Lead - Doanh thu:** Mối tương quan gần như hoàn hảo (**0.99 - 1.00**) giữa **Lead MKT**, **Đơn hàng** và **Doanh thu** là điều hiển nhiên, cho thấy Lead là biến trung gian cực kỳ quan trọng.

### 2.2. Hiệu Quả Chi Tiêu Quảng Cáo (ROAS)

*   **ROAS Trung bình:** 4.73
*   **ROAS Trung vị:** 2.60

Sự khác biệt lớn giữa ROAS trung bình và trung vị (4.73 so với 2.60) cho thấy có một số chiến dịch hoặc ngày có hiệu suất cực kỳ cao, kéo ROAS trung bình lên. Điều này chỉ ra rằng **chất lượng** của chi tiêu quan trọng hơn **số lượng** chi tiêu.

## 3. Phân Tích Hiệu Quả Theo Kênh và Chiến Dịch

Hiệu suất khác nhau giữa các kênh và chiến dịch là một yếu tố phi thời gian gây nhiễu lớn cho mô hình dự báo đơn giản.

### 3.1. Hiệu Quả Theo Kênh (Channel)

| Kênh | Chi phí Marketing (VNĐ) | Doanh thu (VNĐ) | ROAS | CPL (VNĐ/Lead) | Tỷ lệ Chuyển đổi (Đơn/Lead) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FB** | 1.314.129.481 | 3.101.689.000 | **2.36** | 154.367 | 72.18% |
| **Google** | 132.545.235 | 3.120.762.000 | **23.54** | 178.152 | 84.26% |
| **Tiktok** | 350.299 | 1.956.000 | **5.58** | 87.574 | 72.82% |

*   **Google** có ROAS vượt trội (**23.54**) so với FB (**2.36**), mặc dù CPL (Chi phí trên mỗi Lead) cao hơn. Điều này cho thấy chất lượng Lead từ Google cao hơn đáng kể, dẫn đến tỷ lệ chuyển đổi (Conversion Rate) cao hơn.
*   **Tiktok** có CPL thấp nhất, nhưng tổng chi phí và doanh thu còn rất nhỏ.

### 3.2. Hiệu Quả Theo Chiến Dịch (Campaign)

Chiến dịch **CVS** chiếm phần lớn doanh thu (2.42 tỷ VNĐ) với ROAS là 2.42. Tuy nhiên, các chiến dịch nhỏ hơn như **Guu-Discovery** có ROAS cao hơn (3.06).

**Kết luận:** Nếu trong tháng tới, doanh nghiệp quyết định chuyển phần lớn ngân sách từ FB sang Google (hoặc ngược lại), mô hình dự báo chuỗi thời gian đơn giản sẽ không thể nắm bắt được sự thay đổi đột ngột về hiệu suất này.

## 4. Phân Tích Hiệu Suất Nhân Sự

Hiệu suất của Marketer và Sales là yếu tố con người, ảnh hưởng trực tiếp đến việc chuyển đổi Lead thành Doanh thu.

### 4.1. Hiệu Suất Marketer

| Marketer | Doanh thu (VNĐ) | Chi phí Marketing (VNĐ) | ROAS |
| :--- | :--- | :--- | :--- |
| **NgocNgo** | 1.251.666.000 | 479.175.063 | **2.61** |
| **GiangPhan** | 510.523.600 | 234.168.267 | **2.18** |
| **DucVu** | 492.454.100 | 207.650.866 | **2.37** |

Sự chênh lệch về ROAS giữa các Marketer (từ 2.18 đến 2.61) cho thấy **chất lượng quản lý chiến dịch** của từng người có tác động đến hiệu quả chi tiêu. Nếu một Marketer có ROAS cao nghỉ việc hoặc một Marketer có ROAS thấp được giao ngân sách lớn hơn, dự báo sẽ bị sai lệch.

### 4.2. Hiệu Suất Sales

| Sales | Tổng tiền (VNĐ) | Tương tác TB/Lead |
| :--- | :--- | :--- |
| **ThuyTran** | 2.685.044.000 | 1.00 |
| **ChiLe12** | 116.389.000 | 2.60 |
| **HuongDinh** | 114.383.000 | 4.71 |

Sales **ThuyTran** xử lý phần lớn doanh thu và có số lần tương tác trung bình rất thấp (1.00), cho thấy đây có thể là đội ngũ xử lý các đơn hàng chốt ngay (Dathang) hoặc các Lead chất lượng cao. Hiệu suất của đội ngũ Sales, đặc biệt là **ThuyTran**, là một biến số cực kỳ nhạy cảm.

## 5. Kết Luận và Khuyến Nghị Cải Thiện Mô Hình

Các yếu tố phi thời gian có thể ảnh hưởng đến độ chính xác của dự báo doanh thu trong tháng tới bao gồm:

| Yếu tố | Ảnh hưởng đến Dự báo | Khuyến nghị Cải thiện Mô hình |
| :--- | :--- | :--- |
| **Chi phí Marketing** | Mối tương quan 0.60 cho thấy chi phí là biến giải thích quan trọng. Nếu ngân sách tháng tới thay đổi, dự báo sẽ sai. | **Tích hợp:** Sử dụng **Chi phí Marketing** dự kiến của tháng tới làm biến ngoại sinh (Exogenous Variable) trong mô hình. |
| **Kênh Quảng cáo** | ROAS giữa các kênh chênh lệch rất lớn (Google 23.54 vs FB 2.36). Thay đổi phân bổ ngân sách sẽ làm sai lệch dự báo. | **Tích hợp:** Tạo các biến giả (Dummy Variables) cho Kênh hoặc sử dụng **ROAS trung bình theo Kênh** làm đặc trưng. |
| **Hiệu suất Nhân sự** | Sự khác biệt về ROAS của Marketer và hiệu suất chuyển đổi của Sales. | **Tích hợp:** Sử dụng **ROAS trung bình của Marketer** hoặc **Tỷ lệ chuyển đổi của Sales** làm đặc trưng. |
| **Sự kiện Bất thường** | Các chiến dịch khuyến mãi lớn, sự kiện ra mắt sản phẩm mới, hoặc các ngày lễ lớn. | **Tích hợp:** Tạo biến giả cho các ngày có sự kiện đặc biệt. |

Để có dự báo chính xác hơn, mô hình cần được nâng cấp để không chỉ dựa vào dữ liệu lịch sử mà còn dựa vào **kế hoạch chi tiêu Marketing** và **phân bổ kênh** dự kiến cho tháng tới.
