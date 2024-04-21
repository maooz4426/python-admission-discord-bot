import json
import requests
import datetime
import os

url = os.getenv("URL")

# class gas_post:
#     def __init__(self,name,hiragana):
def gas_post(interaction,name,hiragana):

        print("post")
        #提出時間取得
        now = datetime.datetime.now()
        format_now = now.isoformat()

        headers = {"Content-Type": "application/json", }
        data={
            "uid":str(interaction.user.id),#str型にして、科学的表記法を回避
            "currentTime":format_now,
            "name":name,
            "hiragana":hiragana

        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            response.raise_for_status()  # HTTPエラーをチェック
            print(json.dumps(data)) #jsonの中身チェック
            print(response.text) #テキスト形式で取得
        except requests.RequestException as e:
            print(f"Request failed: {e}")
