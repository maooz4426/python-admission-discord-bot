import discord
from discord.ext import commands
from discord.ui import button
from views.button import SetButtonView
import os

# bot = discord.Bot(
#     intents = discord.Intents.all(),
#     activity = discord.Game("起動中")
# )
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Hello")#起動するとターミナルに表示される


# class MyButton(discord.ui.Button):
#     def __init__(self, label: str, custom_id: str, style: discord.ButtonStyle):
#         super().__init__(label=label, style=style, custom_id=custom_id)
    
#     async def callback(self, interaction: discord.Interaction):
#         await interaction.response.send_message(f"{self.label} ボタンが押されました！", ephemeral=True)

# class MyView(discord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.add_item(MyButton(label="クリック", custom_id="click_button", style=discord.ButtonStyle.primary))

@bot.command(name="button")
async def button_command(ctx: commands.Context):
    view = SetButtonView()
    await ctx.send("下のボタンを押してください。", view=view)

# cclient = discord.Client()
bot.run(os.getenv("TOKEN"))
# client.run(os.getenv("TOKEN"))
