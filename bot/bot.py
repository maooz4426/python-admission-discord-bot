import discord
from discord.ext import commands
from discord.ui import button
# from views.button import SetButtonView
import os


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

#起動するとターミナルに表示される
@bot.event
async def on_ready():
    print("Hello")

#cogを読み込み
bot.load_extension("cogs.setupFormCog")

# cclient = discord.Client()
bot.run(os.getenv("TOKEN"))
# client.run(os.getenv("TOKEN"))
