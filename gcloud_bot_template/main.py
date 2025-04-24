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

from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "봇 작동 중!"

def run():
    port = int(os.environ.get("PORT", 8080))  # Cloud Run에서 반드시 필요
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
