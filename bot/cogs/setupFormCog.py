import discord
from discord.ext import commands
from modules.button_template import SetButton
from modules.modal_template import SetModal
from discord.ui import View


class SetupFormCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="setup")
    async def setup_form(self,ctx):
        view = setupView()
        
        # view = View()
        # self.add_item(button)

        await ctx.send("下のボタンを選択してください", view = view)


class setupView(View):
    def __init__(self):
        super().__init__()
        admissionbutton = SetButton(label="入会届",style=discord.ButtonStyle.primary,modal=SetModal("入会届"))
        obogbutton = SetButton(label="OBOG届",style=discord.ButtonStyle.gray,modal=SetModal("OBOG届"))
        self.add_item(admissionbutton)
        self.add_item(obogbutton)


def setup(bot):
    bot.add_cog(SetupFormCog(bot))
    