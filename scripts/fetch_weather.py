import os
import requests

def fetch_weather():
    api_key = os.getenv("CWA_API_KEY", "YOUR_CWA_API_KEY") 
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-005"
    params = {"Authorization": api_key, "locationName": "南投縣", "format": "JSON"}

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ 氣象 API 擷取失敗，啟用備用資料: {e}")
        return {
            "records": {"locations": [{"location": [{"locationName": "南投縣", "weatherElement": [
                {"elementName": "PoP12h", "time": [{"elementValue": [{"value": "10"}]}]},
                {"elementName": "T", "time": [{"elementValue": [{"value": "26"}]}]}
            ]}]}]}
        }
