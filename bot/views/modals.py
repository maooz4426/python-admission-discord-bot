import discord
from discord.ui import Modal, InputText
from gas.gas_post import gas_post

class SetModal(Modal):
    def __init__(self,title):
        super().__init__(title = title)

        self.name = InputText(label="名前",style = discord.InputTextStyle.short)
        self.add_item(self.name)

        self.hiragana = InputText(label="ふりがな",style=discord.InputTextStyle.short)
        self.add_item(self.hiragana)

    async def callback(self,interaction:discord.interactions) -> None:

        name = self.name.value
        hiragana = self.hiragana.value

        gas_post(name,hiragana)
        print("postしました")
        await interaction.response.send_message(f"名前: {name}, ふりがな: {hiragana}を登録しました", ephemeral=True)

