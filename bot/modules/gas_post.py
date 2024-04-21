import json
import requests
import datetime
import os

url = os.getenv("URL")

# class gas_post:
#     def __init__(self,name,hiragana):
def gas_post(name,hiragana):

        print("post")
        #提出時間取得
        now = datetime.datetime.now()
        format_now = now.isoformat()

        headers = {"Content-Type": "application/json", }
        data={
            "currentTime":format_now,
            "name":name,
            "hiragana":hiragana

        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            response.raise_for_status()  # HTTPエラーをチェック
            print(json.dumps(data))
            print(response.text)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
