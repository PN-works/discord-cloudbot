import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Discord 이벤트 예시
@bot.event
async def on_ready():
    print(f"✅ 봇 작동 시작: {bot.user}")

# Flask 부분
app = Flask(__name__)

@app.route('/')
def home():
    return "봇 작동 중!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
