from typing import Any
import discord
from discord.ui import Button,View
from .gas import GasHandle
import config
import asyncio
import re
# from .modalHandle import SetForm



#ボタンを押したらボタン(View）が表示される
class SetButtonToView(Button):
    def __init__(self,label,view,style,comment,user,form):
        super().__init__(label = label, style=style)
        self.user = user
        
        # self.view = viewとすると目的のviewが開かない、セッターを準備しろとエラーが出る
        self.view2 = view
        self.style = style
        self.comment = user+comment
        self.form = form
        # print(self.form.get("name"))
        # self.button = button

    # print("1button")

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value  # セッターを通じて値を設定可能に

    async def callback(self,interaction:discord.Interaction):
        # await self.ctx.send(self.comment,view = self.view())
        message = await interaction.response.send_message(self.comment, view=self.view2,ephemeral=True)
        if self.form.title == "情報変更届":
            uid = re.sub("[<@>]","",self.user)

            get_data = GasHandle.gas_get(uid)

            print("getdata")
            # print(get_data)
            from .modalHandle import SetForm
            self.form.setdata(get_data)
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
        GasHandle.gas_post(interaction=interaction,data=self.form.data)

        last_message = config.last_messageID
        # await last_message.delete_original_response()

        # message = await interaction.response.send_message(self.user+f"{self.label}の送信が完了しました",ephemeral=True)

        
        
        await interaction.response.edit_message(content=self.user+f"{self.label}の送信が完了しました", view = None)
        await asyncio.sleep(20)
        await last_message.delete_original_response()