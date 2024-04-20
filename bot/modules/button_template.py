from discord.ui import Button,View

class SetButton(Button):
    # def __init__(self,style,label,modal):
    #     # super().__init__()

    #     self.modal = modal

    #     button = Button(label=label,style=style)
        
    #     #ボタンのコールバック関数を設定
    #     button.callback =  self.button_callback


    #     # self.add_item(button)

    # async def button_callback(self,interaction):
        
    #     await interaction.response.send_modal(self.modal)
    def __init__(self, label, modal,style, *args, **kwargs):
        super().__init__(label=label, style=style,*args, **kwargs)
        self.modal = modal

    async def callback(self, interaction):
        await interaction.response.send_modal(self.modal)