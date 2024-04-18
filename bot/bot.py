import discord
import os

bot = discord.Bot(
    intents = discord.Intents.all(),
    activity = discord.Game("起動中")
)

@bot.event
async def on_ready():
    print("Hello")#起動するとターミナルに表示される
  
# cclient = discord.Client()
bot.run(os.getenv("TOKEN"))
# client.run(os.getenv("TOKEN"))
