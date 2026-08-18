import os
import requests

CLIENT_ID = os.environ.get("TDX_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TDX_CLIENT_SECRET")

def get_tdx_token():
    auth_url = "https://tdx.transportdata.tw/auth/realms/TDX/protocol/openid-connect/token"
    payload = {
        'content-type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(auth_url, data=payload)
    return response.json().get('access_token')

# 使用 Token 抓取資料（範例：公車即時動態或停車場資料）
token = get_tdx_token()
headers = {'authorization': f'Bearer {token}'}
# api_url = "https://tdx.transportdata.tw/api/basic/v2/Bus/RealTimeByFrequency/Streaming/..."
# data = requests.get(api_url, headers=headers).json()
