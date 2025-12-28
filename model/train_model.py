import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import joblib

# Đọc dữ liệu đã tiền xử lý
df = pd.read_csv('data/preprocessed_finance_data.csv', index_col='Date')

# Xác định features và target
# Dự báo 'Doanh thu'
features = ['day_of_week', 'day_of_month', 'month', 'revenue_lag_1', 'revenue_lag_2', 
            'revenue_lag_3', 'revenue_lag_4', 'revenue_lag_5', 'revenue_lag_6', 
            'revenue_lag_7', 'revenue_rolling_mean_7']
target = 'Doanh thu'

X = df[features]
y = df[target]

# Chia dữ liệu huấn luyện và kiểm tra (80/20)
split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# Khởi tạo và huấn luyện mô hình
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")

# Lưu mô hình
joblib.dump(model, 'model/finance_forecast_model.pkl')
print("Save model.")
