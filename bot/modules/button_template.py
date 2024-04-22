from typing import Any
import discord
from discord.ui import Button,View



#ボタンテンプレート
class SetButtonToView(Button):
    def __init__(self,label,view,style,comment):
        super().__init__(label = label, style=style)
        # self.ctx = ctx
        # self.view = view
        self.view2 = view
        self.comment = comment
        # self.button = button

    print("1button")

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value  # セッターを通じて値を設定可能に

    async def callback(self,interaction:discord.Interaction):
        # await self.ctx.send(self.comment,view = self.view())
        await interaction.response.send_message(self.comment, view=self.view2)

class SetButtonToModal(Button):
    def __init__(self, label, modal,style):
        super().__init__(label=label, style=style)
        self.modal = modal
        # self.interaciton = interaction

    #ボタンのコールバック関数
    #モーダル表示する
    async def callback(self,interaction:discord.Interaction):
        await interaction.response.send_modal(self.modal)