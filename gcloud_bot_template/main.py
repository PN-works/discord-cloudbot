import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 작동 시작: {bot.user}")

@bot.command()
async def 핑(ctx):
    await ctx.send("퐁!")

TOKEN = os.getenv("DISCORD_TOKEN")
if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
