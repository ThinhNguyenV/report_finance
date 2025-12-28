import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
file_path = '/home/ubuntu/upload/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')

# Làm sạch dữ liệu: loại bỏ các hàng có chi phí hoặc doanh thu bằng 0 để xem tương quan thực tế
df_clean = df_mkt[(df_mkt['Chi phí Marketing'] > 0) & (df_mkt['Doanh thu'] > 0)].copy()

# Tính toán hệ số tương quan
correlation = df_clean[['Chi phí Marketing', 'Doanh thu', 'Lead MKT', 'Đơn hàng']].corr()

print("Hệ số tương quan giữa các biến chính:")
print(correlation)

# Vẽ biểu đồ phân tán (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.regplot(x='Chi phí Marketing', y='Doanh thu', data=df_clean, scatter_kws={'alpha':0.5})
plt.title('Tương quan giữa Chi phí Marketing và Doanh thu')
plt.xlabel('Chi phí Marketing (VNĐ)')
plt.ylabel('Doanh thu (VNĐ)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('/home/ubuntu/correlation_mkt_revenue.png')

# Tính ROAS (Return on Ad Spend) trung bình
df_clean['ROAS'] = df_clean['Doanh thu'] / df_clean['Chi phí Marketing']
print(f"\nROAS trung bình: {df_clean['ROAS'].mean():.2f}")
print(f"ROAS trung vị: {df_clean['ROAS'].median():.2f}")

# Lưu kết quả
df_clean.to_csv('/home/ubuntu/mkt_efficiency_analysis.csv', index=False)
