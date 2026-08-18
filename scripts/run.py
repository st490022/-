from fetch_weather import fetch_weather
from fetch_tdx import fetch_tdx
from predict import run_prediction
from write_firebase import save_to_firebase

def main():
    print("🚀 開始執行全自動預測 Pipeline...")
    
    # Step 1: 抓取外部數據
    weather_data = fetch_weather()
    tdx_data = fetch_tdx()
    
    # Step 2: 整理歷史數據並交給 Prophet 模型預測
    # （這裡模擬載入訓練數據，實際可換成你的資料庫歷史數據）
    sample_history = [{'ds': '2026-08-18 10:00:00', 'y': 15}, {'ds': '2026-08-18 11:00:00', 'y': 25}]
    predictions = run_prediction(sample_history)
    
    # Step 3: 將 AI 結果存回 Firebase 供前端網頁顯示
    save_to_firebase(predictions)
    print("🎉 全套流程執行完成！")

if __name__ == "__main__":
    main()
