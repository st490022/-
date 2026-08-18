import os
import json
import firebase_admin
from firebase_admin import credentials, db

def save_to_firebase(prediction_results):
    if not firebase_admin._apps:
        # 從環境變數讀取 Firebase Service Account JSON
        cred_json = json.loads(os.getenv("FIREBASE_SERVICE_ACCOUNT"))
        cred = credentials.Certificate(cred_json)
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv("FIREBASE_DB_URL")
        })
    
    ref = db.reference('/predictions')
    ref.set(prediction_results)
    print("✅ 成功將 AI 預測數據更新至 Firebase！")
