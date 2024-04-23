
from discord.ui import Modal,InputText,Select,View
from discord import InputTextStyle,SelectOption
import discord
from .gas import GasHandle
from .button import SetButtonToModal
# このインポートを関数内に移動
# from .view import SetupModalView, SetupFinishView



class SetForm:
    #送るデータを辞書型配列として初期化
    def __init__(self,title):
        self.title = title
        # self.uid = str(interaction.user.id)
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

    #モーダルのテンプレート１
    class SetModal1(Modal):

        def __init__(self,form):
            super().__init__(title=form.title)
            
            self.title = form.title
            self.data = form.data
            self.nextmodal = form.SetModal2(form)

            # 名前入力
            self.name = InputText(label="氏名", style=InputTextStyle.short)
            self.add_item(self.name)
            
            # ふりがな入力
            self.hiragana = InputText(label="氏名（ふりがな）", style=InputTextStyle.short)
            self.add_item(self.hiragana)
            
            # ニックネーム入力
            self.nickname = InputText(label="ニックネーム", style=InputTextStyle.short)
            self.add_item(self.nickname)

            # 入学年度
            self.admission_year = InputText(label="入学年度", style=InputTextStyle.short)
            self.add_item(self.admission_year)
            
            # 学籍番号
            self.student_id = InputText(label="学籍番号", style=InputTextStyle.short)
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
            from .view import SetModalView

            # 追加入力をさせるためのボタン表示の準備
            view = SetModalView(self.title,self.nextmodal,discord.ButtonStyle.primary)
            
            # 説明とボタンを表示
            await interaction.response.send_message(f"{self.title}の続きを入力してください",view = view)
            
            
    #モーダルのテンプレート２
    class SetModal2(Modal):
            
        def __init__(self,form):
            super().__init__(title=form.title)
            self.form = form
            self.title = form.title
            self.data = form.data

            # RAINBOW ID
            self.rainbow_id = InputText(label="RAINBOW ID", style=InputTextStyle.short)
            self.add_item(self.rainbow_id)
                    
            # 学部
            self.faculty = InputText(label="学部", style=InputTextStyle.short)
            self.add_item(self.faculty)
                    
            # 学科（コース）
            self.department = InputText(label="学科（コース）", style=InputTextStyle.short)
            self.add_item(self.department)
                    
            # 携帯電話番号
            self.phone = InputText(label="携帯電話番号", style=InputTextStyle.short)
            self.add_item(self.phone)
                    
            # Gmailアドレス
            self.gmail = InputText(label="Gmailアドレス", style=InputTextStyle.short)
            self.add_item(self.gmail)

        #コールバック関数を設定
        async def callback(self,interaction:discord.Interaction):
            self.data["rainbow_id"] = self.rainbow_id.value
            self.data["faculty"] = self.faculty.value
            self.data["department"] = self.department.value
            self.data["phone"] = self.phone.value
            self.data["gmail"] = self.gmail.value

            # 循環インポートを避けるためにここでインポート
            from .view import SetupFinishView

            #完了ボタンを表示するためViewを作成
            view = SetupFinishView(form = self.form,label=self.title,style=discord.ButtonStyle.primary)

            await interaction.response.send_message("ボタンを押して完了してください！",view=view)

                # GasHandle.gas_post(interaction, name, hiragana, nickname, admission_year,student_id)
                # await interaction.response.send_message(f"{self.title}を送信しました")
                # rainbow_id = self.rainbow_id.value
                # faculty = self.faculty.value
                # department = self.department.value
                # phone = self.phone.value
                # gmail = self.gmail.value

            #gasにpostリクエスト送信
            # gas_post(interaction, name, hiragana, nickname, admission_year, student_id, rainbow_id, faculty, department, phone, gmail)
            # GasHandle.gas_post(interaction, name, hiragana, nickname, admission_year,student_id)
            # await interaction.response.send_message(f"{self.title}を送信しました")

    # class SetModal2(Modal):
    #         def __init__(self,title):
    #             super().__init__(title=title)

    #             self.title = title
    #             # RAINBOW ID
    #             self.rainbow_id = InputText(label="RAINBOW ID", style=InputTextStyle.short)
    #             self.add_item(self.rainbow_id)
                
    #             # 学部
    #             self.faculty = InputText(label="学部", style=InputTextStyle.short)
    #             self.add_item(self.faculty)
                
    #             # 学科（コース）
    #             self.department = InputText(label="学科（コース）", style=InputTextStyle.short)
    #             self.add_item(self.department)
                
    #             # 携帯電話番号
    #             self.phone = InputText(label="携帯電話番号", style=InputTextStyle.short)
    #             self.add_item(self.phone)
                
    #             # Gmailアドレス
    #             self.gmail = InputText(label="Gmailアドレス", style=InputTextStyle.short)
    #             self.add_item(self.gmail)

    #         async def callback(self,interaction):
    #             rainbow_id = self.rainbow_id.value
    #             aculty = self.faculty.value
    #             department = self.department.value
    #             phone = self.phone.value
    #             gmail = self.gmail.value

    #             await interaction.response.send_message(f"{self.title}を送信")