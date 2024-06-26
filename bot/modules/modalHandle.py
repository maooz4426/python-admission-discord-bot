
from discord.ui import Modal,InputText
from discord import InputTextStyle
import discord

from .buttonHandle import SetButtonStyle
# このインポートを関数内に移動


class SetForm:
    #送るデータを辞書型配列として初期化
    def __init__(self,user,title):
        self.user = user
        self.title = title

        self.data = {
            "name": "",
            "hiragana": "",
            "nickname": "",
            "admission_year": "",
            "student_id": "",
            "rainbow_id": "",
            "faculty": "",
            "department": "",
            "phone": "",
            "gmail": ""
        }


    #getリクエスト送ったらデータ挿入する
    def setdata(self,response):

        # 新しい辞書にユーザーデータを格納する
        user_data = response.get('userData', {})  # userDataキーがなければ空の辞書を返す

        # 各フィールドを新しい辞書に格納する
        
        self.data["name"] = user_data.get('name')#self付け忘れてインスタンス変数に入れるの忘れないように
        self.data["hiragana"] = user_data.get('hiragana')
        self.data["nickname"] = user_data.get('nickname')
        self.data["admission_year"] = user_data.get('admission_year')
        self.data["student_id"] = user_data.get('student_id')
        self.data["rainbow_id"] = user_data.get('rainbow_id')
        self.data["faculty"] = user_data.get('faculty')
        self.data["department"] = user_data.get('department')
        self.data["phone"] = user_data.get('phone')
        self.data["gmail"] = user_data.get('gmail')
        
        print("dataをセットしました")

    #モーダルのテンプレート１
    class SetModal1(Modal):

        def __init__(self,form):
            super().__init__(title=form.title)

            self.form = form
            self.user = form.user
            
            self.title = form.title.replace("(1/1)","")
            self.data = form.data
            # print(form)
            self.nextmodal = form.SetModal2(form)

            # 名前入力
            self.name = InputText(label="氏名", style=InputTextStyle.short,value = self.data.get("name"))
            self.add_item(self.name)
            
            # ふりがな入力
            self.hiragana = InputText(label="ふりがな", style=InputTextStyle.short, value=self.data.get("hiragana"))
            self.add_item(self.hiragana)
            print(self.data.get("name"))
            # ニックネーム入力
            self.nickname = InputText(label="ニックネーム", style=InputTextStyle.short, value=self.data.get("nickname"))
            self.add_item(self.nickname)

            # 入学年度
            self.admission_year = InputText(label="入学年度", style=InputTextStyle.short, value=self.data.get("admission_year"))
            self.add_item(self.admission_year)
            
            # 学籍番号
            self.student_id = InputText(label="学籍番号", style=InputTextStyle.short, value=self.data.get("student_id"))
            self.add_item(self.student_id)

        #コールバック関数を設定
        async def callback(self,interaction:discord.Interaction):

            # 辞書にデータを入力
            self.data["name"] = self.name.value
            self.data["hiragana"] = self.hiragana.value
            self.data["nickname"] = self.nickname.value
            self.data["admission_year"] = self.admission_year.value
            self.data["student_id"] = self.student_id.value

            # 循環インポートを避けるためにここでインポート
            from .viewHandle import SetModalView

            # 追加入力をさせるためのボタン表示の準備
            view = SetModalView(self.user,self.title+"(2/2)",self.nextmodal,SetButtonStyle(self.form),form=self.form)
        

            #メッセージの中身とボタンを入れ替え
            await interaction.response.edit_message(content=self.user+f"{self.title}の続きを入力してください",view = view)
            
            # config.last_messageID = message
            
    #モーダルのテンプレート２
    class SetModal2(Modal):
            
        def __init__(self,form):
            super().__init__(title=form.title)
            self.form = form
            self.user = form.user
            self.title = form.title
            self.data = form.data

            # RAINBOW ID
            self.rainbow_id = InputText(label="RAINBOW ID", style=InputTextStyle.short, value=self.data.get("rainbow_id"))
            self.add_item(self.rainbow_id)
                    
            # 学部
            self.faculty = InputText(label="学部", style=InputTextStyle.short, value=self.data.get("faculty"))
            self.add_item(self.faculty)
                    
            # 学科（コース）
            self.department = InputText(label="学科（コース）", style=InputTextStyle.short, value=self.data.get("department"))
            self.add_item(self.department)
                    
            # 携帯電話番号
            self.phone = InputText(label="電話番号", style=InputTextStyle.short, value=self.data.get("phone"))
            self.add_item(self.phone)
                    
            # Gmailアドレス
            self.gmail = InputText(label="Gmailアドレス", style=InputTextStyle.short, value=self.data.get("gmail"))
            self.add_item(self.gmail)

        #コールバック関数を設定
        async def callback(self,interaction:discord.Interaction):
            self.data["rainbow_id"] = self.rainbow_id.value
            self.data["faculty"] = self.faculty.value
            self.data["department"] = self.department.value
            self.data["phone"] = self.phone.value
            self.data["gmail"] = self.gmail.value

            # 循環インポートを避けるためにここでインポート
            from .viewHandle import SetFinishView

            #完了ボタンを表示するためViewを作成
            view = SetFinishView(user=self.user,form = self.form,label=self.title,style=discord.ButtonStyle.primary)
            

            #動的に中身とボタンを変更
            await interaction.response.edit_message(content=self.user+"ボタンを押して完了してください！",view = view)

