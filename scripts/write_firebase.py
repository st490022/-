import os
import json
import firebase_admin
from firebase_admin import credentials, db

def save_to_firebase(prediction_results):
    env_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    db_url = os.getenv("FIREBASE_DB_URL")
    
    # 檢查環境變數是否存在
    if not env_json:
        print("⚠️ 未檢測到 FIREBASE_SERVICE_ACCOUNT 環境變數，跳過 Firebase 寫入步驟（本地/測試模式）")
        print("預測數據範例：", prediction_results[:2])
        return

    if not firebase_admin._apps:
        try:
            cred_json = json.loads(env_json)
            cred = credentials.Certificate(cred_json)
            firebase_admin.initialize_app(cred, {
                'databaseURL': db_url
            })
        except Exception as e:
            print(f"⚠️ Firebase 初始化失敗: {e}")
            return
    
    try:
        ref = db.reference('/predictions')
        ref.set(prediction_results)
        print("✅ 成功將 AI 預測數據更新至 Firebase！")
    except Exception as e:
        print(f"⚠️ Firebase 寫入失敗: {e}")
