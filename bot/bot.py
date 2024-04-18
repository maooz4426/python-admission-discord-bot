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

@bot.command(name="button")
async def button_command(ctx: commands.Context):
    view = SetButtonView()
    await ctx.send("下のボタンを押してください。", view=view)


# cclient = discord.Client()
bot.run(os.getenv("TOKEN"))
# client.run(os.getenv("TOKEN"))
