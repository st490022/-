Python
import os
import requests

def fetch_weather(location="南投縣"):
    api_key = os.environ.get("CWA_API_KEY")
    if not api_key:
        raise ValueError("未設定 CWA_API_KEY 環境變數")
        
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-005"
    params = {
        "Authorization": api_key,
        "locationName": location,
        "format": "JSON"
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    
    # 預設範例結構，後續可依需求擷取具體降雨機率與溫度
    return {"rain_prob": 20.0, "temp": 26.5}

儲存：按右上角 Commit changes... 儲存。
8.scripts/predict.py（Prophet 模型時間序列預測）
點擊：Add file ➔ Create new file
檔名輸入：scripts/predict.py
程式碼內容：
Python
import pandas as pd
from prophet import Prophet

def build_and_predict(history_df, weather_info=None, periods=12):
    # 若無歷史數據，預設建立基礎序列
    if history_df.empty:
        history_df = pd.DataFrame({
            "ds": pd.date_range(end=pd.Timestamp.now(), periods=24, freq="h"),
            "y": [10] * 24,
            "rain_prob": [20.0] * 24
        })
    else:
        if weather_info and "rain_prob" in weather_info:
            history_df["rain_prob"] = weather_info["rain_prob"]

    m = Prophet(
        yearly_seasonality=False,
        weekly_seasonality=True,
        daily_seasonality=True
    )
    
    if "rain_prob" in history_df.columns:
        m.add_regressor("rain_prob")

    m.fit(history_df)

    future = m.make_future_dataframe(periods=periods, freq="5min")
    if "rain_prob" in history_df.columns:
        future["rain_prob"] = weather_info.get("rain_prob", 0.0) if weather_info else 0.0

    forecast = m.predict(future)
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

