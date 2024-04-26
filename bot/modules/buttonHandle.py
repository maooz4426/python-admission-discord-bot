from typing import Any
import discord
from discord.ui import Button,View
from .gas import GasHandle
import config
import asyncio
import re
# from .modalHandle import SetForm


def SetButtonStyle(form):
    if form.title == "入会届":
        return config.admission_button_style
    elif form.title == "情報変更届":
        return config.change_button_style
    elif form.title == "OBOG届":
        return config.obog_button_style


#ボタンを押したらボタン(View）が表示される
class SetButtonToView(Button):
    def __init__(self,label,style,comment,user):
        super().__init__(label = label, style=style)
        self.user = user
        self.title = label
        # self.view = viewとすると目的のviewが開かない、セッターを準備しろとエラーが出る
        # self.view2 = view
        self.style = style
        self.comment = user+comment
        # self.form = form

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value  # セッターを通じて値を設定可能に

    async def callback(self,interaction:discord.Interaction):

        # await interaction.response.send_message(content="ボタンを準備しています")
        
        # temp_message.delete()
        #15分作業可能にするため
        await interaction.response.defer(ephemeral=True)
        #ボタン準備のための表示
        temp = await interaction.followup.send(content="ボタンを準備しています…", ephemeral=True)
        from .modalHandle import SetForm
        from .viewHandle import SetModalView

        #formをここで作成する
        self.form = SetForm(self.user,self.title)

        #情報変更届の場合はdataの中身をセット
        if self.form.title == "情報変更届":
            uid = re.sub("[<@>]","",self.user)

            get_data = GasHandle.gas_get(uid)

            print("getdata")
            # print(get_data)
            from .modalHandle import SetForm
            self.form.setdata(get_data)

        #modal1をここで作成する
        self.modal = self.form.SetModal1(self.form)
        # Modal 用の View をここで作成する（モーダル遷移ボタンを表示）
        self.view = SetModalView(user=self.user, label=self.title + "(1/1)", modal=self.modal, style=self.style, form=self.form)

        # self.view = SetButtonToModal(user=self.user,label=self.title,modal=self.modal,style=self.style,form=self.form)
        
        # message = await interaction.response.send_message(self.comment, view=self.view,ephemeral=True)
        # await temp_message.delete()
        # await interaction.delete_original_response()

        #遅らせた後にメッセージを送るのでfollowupを使う
        message = await interaction.followup.send(content=self.comment, view=self.view,ephemeral=True)
        #ボタン準備メッセージを削除
        await temp.delete()

        #modalを作る前に使うために上に書くのでコメントアウト
        # if self.form.title == "情報変更届":
        #     uid = re.sub("[<@>]","",self.user)

        #     get_data = GasHandle.gas_get(uid)

        #     print("getdata")
        #     # print(get_data)
        #     from .modalHandle import SetForm
        #     self.form.setdata(get_data)
            # print(self.form.data.get("name"))
            

        config.last_messageID = message



#ボタンを押したらモーダルを表示する
class SetButtonToModal(Button):
    def __init__(self,user, label, modal,style,form):
        super().__init__(label=label, style=style)
        self.user = user
        self.modal = modal
        self.form = form
        # self.interaciton = interaction

    #ボタンのコールバック関数
    #モーダル表示する
    async def callback(self,interaction:discord.Interaction):

        
        await interaction.response.send_modal(self.modal)
        # await interaction.response.defer()

#ボタンを押したらgasにpostリクエストを送る
class SetFinishButton(Button):
    def __init__(self,user,form,label,style):
        # self.label = str(label) + "を完了する"
        super().__init__(label=label+"を完了" ,style=style)
        self.form = form
        self.user = user

    async def callback(self, interaction: discord.Interaction):
        GasHandle.gas_post(interaction=interaction,data=self.form.data,title=self.form.title)

        last_message = config.last_messageID
        # await last_message.delete_original_response()

        # message = await interaction.response.send_message(self.user+f"{self.label}の送信が完了しました",ephemeral=True)

        
        
        await interaction.response.edit_message(content=self.user+f"{self.label}の送信が完了しました", view = None)
        await asyncio.sleep(20)
        await last_message.delete()

        # await last_message.delete_original_response()