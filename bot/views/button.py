import discord
from discord.ui import button,View

class SetButtonView(View):
    @button(label="入会届",style=discord.ButtonStyle.primary)
    async def button_callback(self,button,interaction):
        await interaction.response.send_message("You clicked the button!")

    