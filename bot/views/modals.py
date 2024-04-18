import discord
from discord.ui import Modal, InputText

class SetModal(Modal):
    def __init__(self,title):
        super().__init__(title = title)

        self.name = InputText(label="名前",style = discord.InputTextStyle.short)
        self.add_item(self.name)

        self.hiragana = InputText(label="ふりがな",style=discord.InputTextStyle.short)
        self.add_item(self.hiragana)

  