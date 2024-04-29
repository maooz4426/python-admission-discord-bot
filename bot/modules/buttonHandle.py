from typing import Any
import discord
from discord.ui import Button,View
from .gas import GasHandle
import config
import asyncio
import re
import os
from .roleHandle import RoleHandle
# from .modalHandle import SetForm


def SetButtonStyle(form):
    if form.title == "入会届":
        return config.admission_button_style
    elif form.title == "情報変更届":
        return config.change_button_style
    elif form.title == "OBOG届":
        return config.obog_button_style
    
def formalizeUid(user):
    uid = re.sub("[<@>]","",user)

    return uid


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
        if self.form.title == "情報変更届" or self.form.title=="退会届":
            uid = formalizeUid(self.user)

            get_data = GasHandle.gas_get(uid)

            print("getdata")
            # print(get_data)
            from .modalHandle import SetForm
            self.form.setdata(get_data)

        # elif self.form.title == "退会届":
        #     uid = formalizeUid(self.user)

        #     get_data = GasHandle.gas_get(uid)
        #     print("getdata")

        #退会届は別ボタンを実装する
        if self.form.title == "退会届":

            #ユーザーネームを取得して表示
            userName = self.form.data.get("name")

            from .viewHandle import SetDeleteView
            #viewを表示
            view = SetDeleteView(user = self.user,form = self.form,label = self.title,style=self.style)

            #遅らせた後にメッセージを送るのでfollowupを使う
            self.comment += userName + "さんの情報が削除されます"
            message = await interaction.followup.send(content=self.comment, view=view,ephemeral=True)

        
        else:
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
        await interaction.response.defer()
        GasHandle.gas_post(interaction=interaction,data=self.form.data,title=self.form.title)
        print(self.user)

        #ロール付与
        await RoleHandle(interaction).giveRole(title = self.form.title)
        # role = discord.utils.get(interaction.guild.roles, name="サークル会員")
        # print(role)
        # member = interaction.user
        # await member.add_roles(role)
        # uid = re.sub("[<@>]","",self.user)
        # user_member = interaction.guild.get_member(user_id = uid)
        # role = discord.utils.get(interaction.guild.roles, name=os.getenv("CIRCLE_MEMBER_ROLE_ID"))
        # user_member.add_roles(role)


        # last_message = config.last_messageID
        # await last_message.delete_original_response()

        # message = await interaction.response.send_message(self.user+f"{self.label}の送信が完了しました",ephemeral=True)
        
        #defer()してメッセージを送る時、interaction.edit_original_response または interaction.followup.sendしか使えない
        last_message = await interaction.edit_original_response(content=self.user+f"{self.label}の送信が完了しました", view = None)
        await asyncio.sleep(20)
        await last_message.delete()

        # await last_message.delete_original_response()

#退会用ボタン
class SetDeleteButton(Button):
    def __init__(self,user,form,label,style):
        super().__init__(label = label + "送信",style=style)
        self.form = form
        self.user = user


    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        GasHandle.gas_post_delete(interaction,data = self.form.data,title = self.form.title)

        last_message=await interaction.edit_original_response(content=self.user+f"{self.label}の送信が完了しました", view = None)
        await asyncio.sleep(20)
        await last_message.delete()

