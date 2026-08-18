import os
import requests

def fetch_tdx():
    client_id = os.getenv("TDX_CLIENT_ID", "YOUR_CLIENT_ID")
    client_secret = os.getenv("TDX_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
    
    # 取得 Access Token
    auth_url = "https://tdx.transportdata.tw/auth/realms/TDX/protocol/openid-connect/token"
    auth_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    try:
        res = requests.post(auth_url, data=auth_data, timeout=10)
        token = res.json().get("access_token")
        headers = {"authorization": f"Bearer {token}"}
        
        # 抓取資料（範例：觀光景點人流或觀光數據）
        data_url = "https://tdx.transportdata.tw/api/basic/v2/Tourism/ScenicSpot/NantouCounty?$top=10&$format=JSON"
        response = requests.get(data_url, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        print(f"⚠️ TDX API 連線失敗: {e}")
        return []
