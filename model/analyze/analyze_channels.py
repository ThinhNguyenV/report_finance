import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
file_path = '/home/ubuntu/upload/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')

# Tổng hợp theo Kênh (Channel)
channel_stats = df_mkt.groupby('Channel').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum',
    'Lead MKT': 'sum',
    'Đơn hàng': 'sum'
}).reset_index()

channel_stats['ROAS'] = channel_stats['Doanh thu'] / channel_stats['Chi phí Marketing']
channel_stats['CPL'] = channel_stats['Chi phí Marketing'] / channel_stats['Lead MKT']
channel_stats['Conversion_Rate'] = channel_stats['Đơn hàng'] / channel_stats['Lead MKT']

print("Thống kê theo Kênh:")
print(channel_stats)

# Tổng hợp theo Chiến dịch (Campaign) - Lấy top 10 chiến dịch theo doanh thu
campaign_stats = df_mkt.groupby('Chiến dịch').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum'
}).sort_values('Doanh thu', ascending=False).head(10).reset_index()

campaign_stats['ROAS'] = campaign_stats['Doanh thu'] / campaign_stats['Chi phí Marketing']

print("\nTop 10 Chiến dịch theo Doanh thu:")
print(campaign_stats)

# Vẽ biểu đồ ROAS theo Kênh
plt.figure(figsize=(10, 6))
plt.bar(channel_stats['Channel'], channel_stats['ROAS'], color='skyblue')
plt.title('ROAS theo Kênh Quảng cáo')
plt.ylabel('ROAS (Doanh thu / Chi phí)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('/home/ubuntu/roas_by_channel.png')

# Lưu kết quả
channel_stats.to_csv('/home/ubuntu/channel_efficiency.csv', index=False)
campaign_stats.to_csv('/home/ubuntu/top_campaigns.csv', index=False)
