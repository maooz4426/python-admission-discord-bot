import json
import requests
import datetime
import os
from .roleHandle import RoleHandle

url = os.getenv("URL")

# class gas_post:
#     def __init__(self,name,hiragana):
class GasHandle():

    # def data_add(self,data,name, hiragana, nickname, admission_year, student_id, rainbow_id, faculty, department, phone, gmail):
         
     
    # def gas_post(self,interaction, name, hiragana, nickname, admission_year, student_id, rainbow_id, faculty, department, phone, gmail):
    #postリクエストを送るためのメソッド
    def gas_post(interaction,data,title):
            print("post")
            print(title)
            #提出時間取得
            now = datetime.datetime.now()
            format_now = now.isoformat()

            headers = {"Content-Type": "application/json", }

            if title == "入会届":
                sheet = "admissionSheet"
            elif title == "OBOG届":
                sheet = "obogSheet"
            else:
                role = interaction.user.roles
                print(role)
                sheet = RoleHandle(interaction).setSheetNameByRole(role)

        
            # データ辞書の作成
            payload = {
                "sheet":sheet,
                "form":title,
                "uid":str(interaction.user.id),
                "currentTime":format_now,
                 **data
            }

            try:
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                response.raise_for_status()  # HTTPエラーをチェック
                print(json.dumps(payload)) #jsonの中身チェック
                
            except requests.RequestException as e:
                print(f"Request failed: {e}")

    def gas_get(user):
        print("get")

        #  headers = {"Contents-Type":"application/json"}

        payload = {
            "uid":user,
        }
        print(payload["uid"])

        try:
            response = requests.get(url,params=payload)
            print(response.text) #テキスト形式で取得
            response.raise_for_status()
            print(json.dumps(payload))
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed:{e}")