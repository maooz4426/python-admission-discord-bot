import json
import requests
import datetime
import os

url = os.getenv("URL")

# class gas_post:
#     def __init__(self,name,hiragana):
class GasHandle():

    # def data_add(self,data,name, hiragana, nickname, admission_year, student_id, rainbow_id, faculty, department, phone, gmail):
         
     
    # def gas_post(self,interaction, name, hiragana, nickname, admission_year, student_id, rainbow_id, faculty, department, phone, gmail):
    def gas_post(interaction,data):
            print("post")
            #提出時間取得
            now = datetime.datetime.now()
            format_now = now.isoformat()

            headers = {"Content-Type": "application/json", }
        
            # データ辞書の作成
            payload = {
                 "uid":str(interaction.user.id),
                 "currentTime":format_now,
                 **data
            }

            # self.data = data
            # data = {
            #     "uid": str(interaction.user.id),  # ユーザーID
            #     "currentTime": format_now,  # 提出時間
            #     "name": name,  # 氏名
            #     "hiragana": hiragana,  # ふりがな
            #     "nickname": nickname,  # ニックネーム
            #     "admissionYear": admission_year,  # 入学年度
            #     "studentID": student_id,  # 学籍番号
            #     "rainbowID": rainbow_id,  # RAINBOW ID
            #     "faculty": faculty,  # 学部
            #     "department": department,  # 学科（コース）
            #     "phone": phone,  # 電話番号
            #     "gmail": gmail  # Gmailアドレス
            # }

            try:
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                response.raise_for_status()  # HTTPエラーをチェック
                print(json.dumps(payload)) #jsonの中身チェック
                print(response.text) #テキスト形式で取得
            except requests.RequestException as e:
                print(f"Request failed: {e}")