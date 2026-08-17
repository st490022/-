import pandas as pd
from fetch_weather import fetch_weather
from predict import build_and_predict
from write_firebase import write_forecast

def main():
    print("1. 擷取 CWA 天氣資料...")
    weather_info = fetch_weather()

    print("2. 訓練 Prophet 模型並生成預測...")
    history_df = pd.DataFrame() 
    forecast_df = build_and_predict(history_df, weather_info)

    # 計算未來最新預測數值並分級
    latest_yhat = forecast_df.iloc[-1]["yhat"]
    if latest_yhat > 100:
        level = "high"
    elif latest_yhat > 50:
        level = "medium"
    else:
        level = "low"

    print(f"3. 寫入 Firebase (當前預測等級: {level})...")
    write_forecast(forecast_df, level)
    print("AI 預測與雲端更新順利完成！")

if __name__ == "__main__":
    main()
