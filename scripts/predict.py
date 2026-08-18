import pandas as pd
from prophet import Prophet

def run_prediction(historical_data):
    # 1. 建立符合 Prophet 格式的 DataFrame (必須包含 ds 與 y)
    df = pd.DataFrame(historical_data) # 需包含 'ds' (時間) 與 'y' (人數)
    
    # 2. 初始化與訓練模型
    model = Prophet(daily_seasonality=True, weekly_seasonality=True)
    model.fit(df)
    
    # 3. 預測未來 24 小時
    future = model.make_future_dataframe(periods=24, freq='h')
    forecast = model.predict(future)
    
    # 回傳預測結果 (包含時間 ds 與 預測值 yhat)
    results = forecast[['ds', 'yhat']].tail(24).to_dict(orient='records')
    return results
