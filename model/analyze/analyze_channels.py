import pandas as pd
import matplotlib.pyplot as plt

# Read data
file_path = 'data/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')

# Aggregate by Channel
channel_stats = df_mkt.groupby('Channel').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum',
    'Lead MKT': 'sum',
    'Đơn hàng': 'sum'
}).reset_index()

# Calculate efficiency metrics
channel_stats['ROAS'] = channel_stats['Doanh thu'] / channel_stats['Chi phí Marketing']
channel_stats['CPL'] = channel_stats['Chi phí Marketing'] / channel_stats['Lead MKT']
channel_stats['Conversion_Rate'] = channel_stats['Đơn hàng'] / channel_stats['Lead MKT']

print("Statistics by Channel:")
print(channel_stats)

# Aggregate by Campaign - Get top 10 campaigns by revenue
campaign_stats = df_mkt.groupby('Chiến dịch').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum'
}).sort_values('Doanh thu', ascending=False).head(10).reset_index()

# Calculate ROAS for top campaigns
campaign_stats['ROAS'] = campaign_stats['Doanh thu'] / campaign_stats['Chi phí Marketing']

print("\nTop 10 Campaigns by Revenue:")
print(campaign_stats)

# Plot ROAS by Channel
plt.figure(figsize=(10, 6))
plt.bar(channel_stats['Channel'], channel_stats['ROAS'], color='skyblue')
plt.title('ROAS by Advertising Channel')
plt.ylabel('ROAS (Revenue / Cost)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('model/analyze/img/roas_by_channel.png')

# Save results to CSV
channel_stats.to_csv('data/analyze/channel_efficiency.csv', index=False)
campaign_stats.to_csv('data/analyze/datatop_campaigns.csv', index=False)