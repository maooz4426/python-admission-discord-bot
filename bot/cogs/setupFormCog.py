import discord
from discord.ext import commands
from modules.buttonHandle import SetButtonToModal,SetButtonToView
from modules.modalHandle import SetForm
from discord.ui import View
from modules.viewHandle import SetModalView,SetButtonView

class SetupFormCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #!setupでボタンを表示する
    @commands.command(name="setup")
    async def setup_form(self,ctx):
        user = ctx.author.mention
        view = SetButtonView(user)
        
        await ctx.send("下のボタンを選択してください", view = view)

#4つのボタンをセットアップ
# class setupView(View):
#     def __init__(self):
#         super().__init__()
#         admission_form = SetForm("入会届")
#         admision_view = SetupModalView("入会届",modal=admission_form.SetModal1(admission_form),style=discord.ButtonStyle.primary)
#         obog_view = SetupModalView("OBOG届",SetForm("OBOG届"),style=discord.ButtonStyle.primary)
#         admissionbutton = SetButtonToView(label="入会届",style=discord.ButtonStyle.primary,view=admision_view,comment = "入会届を入力してください")
#         obogbutton = SetButtonToView(label="OBOG届",style=discord.ButtonStyle.gray,view=obog_view,comment = "obog届を入力してください")
#         self.add_item(admissionbutton)
#         self.add_item(obogbutton)

#モーダル表示のview
# class SetupModalView(View):
#     def __init__(self,label,modal,style):
#     # def __init__(self,label,modal,style):
#         super().__init__()
#         button = SetButtonToModal(label=label,modal=modal,style=style)
#         # button = SetButtonToModal(label=label,modal=modal,style=style)
        
#         self.add_item(button)

def setup(bot):
    bot.add_cog(SetupFormCog(bot))
    