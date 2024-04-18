#https://guide.pycord.dev/interactions/ui-components/buttons
import discord
from discord.ui import button,View
from .modals import SetModal

class SetButtonView(View):
    def __init__(self,label):
        self.button_name = label
    
    @button(label = "入会届", style=discord.ButtonStyle.primary)
    async def button_callback(self,button,interaction):
        modal = SetModal(title = "入会届")
        await interaction.response.send_modal(modal)

    