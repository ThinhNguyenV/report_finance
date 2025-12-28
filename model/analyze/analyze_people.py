import pandas as pd

# Đọc dữ liệu
file_path = '/home/ubuntu/upload/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')
df_sales = pd.read_excel(file_path, sheet_name='Sales')

# Hiệu suất Marketer (từ bảng MKT)
marketer_stats = df_mkt.groupby('MKTer').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum',
    'Lead MKT': 'sum'
}).reset_index()
marketer_stats['ROAS'] = marketer_stats['Doanh thu'] / marketer_stats['Chi phí Marketing']
marketer_stats = marketer_stats.sort_values('Doanh thu', ascending=False)

print("Hiệu suất Marketer (Top 5 theo Doanh thu):")
print(marketer_stats.head())

# Hiệu suất Sales (từ bảng Sales)
# Lưu ý: Cần kiểm tra tên cột chính xác trong bảng Sales
sales_stats = df_sales.groupby('Sales').agg({
    'Tổng tiền': 'sum',
    'Số lần tương tác': 'mean'
}).reset_index()
sales_stats = sales_stats.sort_values('Tổng tiền', ascending=False)

print("\nHiệu suất Sales (Top 5 theo Doanh thu):")
print(sales_stats.head())

# Lưu kết quả
marketer_stats.to_csv('/home/ubuntu/marketer_performance.csv', index=False)
sales_stats.to_csv('/home/ubuntu/sales_performance.csv', index=False)
