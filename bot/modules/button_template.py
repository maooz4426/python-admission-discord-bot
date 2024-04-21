from discord.ui import Button,View

#ボタンテンプレート
class SetButton(Button):
    def __init__(self, label, modal,style):
        super().__init__(label=label, style=style)
        self.modal = modal

    #ボタンのコールバック関数
    #モーダル表示する
    async def callback(self, interaction):
        await interaction.response.send_modal(self.modal)