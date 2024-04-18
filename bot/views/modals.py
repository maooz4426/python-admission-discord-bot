import discord
from discord.ui import Modal, InputText

class MyModal(Modal):
    def __init__(self,title):
        super().__init__(title == title)
        self.add_item(InputText(label="name",style = discord.InputTextStyle.short))