
from discord.ui import Modal,InputText
from discord import InputTextStyle
from .gas_post import gas_post


class SetModal(Modal):
    def __init__(self,title):
        super().__init__(title=title)

        self.title = title

        self.name = InputText(label="名前",style=InputTextStyle.short)

        self.hiragana = InputText(label="ふりがな",style=InputTextStyle.short)

        self.add_item(self.name)
        self.add_item(self.hiragana)

    async def callback(self,interaction):

        name = self.name.value
        hiragana = self.hiragana.value

        gas_post(name,hiragana)

        await interaction.response.send_message(f"{self.title}を送信しました")