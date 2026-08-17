import os
import json
import firebase_admin
from firebase_admin import credentials, db

def write_forecast(forecast_df, current_level):
    if not firebase_admin._apps:
        cred_json = os.environ.get("FIREBASE_CREDENTIALS")
        if not cred_json:
            raise ValueError("未設定 FIREBASE_CREDENTIALS 環境變數")
            
        cred_dict = json.loads(cred_json)
        cred = credentials.Certificate(cred_dict)
        # 替換為你的 Firebase 資料庫 URL
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://dtrl-182a4-default-rtdb.asia-southeast1.firebasedatabase.app/"
        })

    # 更新擁擠度分級狀態供 ESP32 讀取
    db.reference("prediction/level").set(current_level)

    # 寫入時間序列預測數據供前端儀表板繪圖
    data = {}
    for _, row in forecast_df.iterrows():
        key = row["ds"].strftime("%Y%m%d%H%M")
        data[key] = {
            "predicted": round(float(row["yhat"]), 1),
            "lower": round(float(row["yhat_lower"]), 1),
            "upper": round(float(row["yhat_upper"]), 1)
        }
    db.reference("crowd_forecast").set(data)
