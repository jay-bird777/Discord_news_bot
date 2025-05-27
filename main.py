import discord
import feedparser
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import os
from flask import Flask
from threading import Thread

# 🔐 Load bot token and channel ID from Replit secrets
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# 📡 Discord client setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler()

# 📰 News fetch function
def get_cyber_news():
    feed = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")
    top_articles = feed.entries[:3]  # Only get top 3
    news = "**🛡️ Top 3 Cybersecurity Headlines Today:**\n\n"
    for article in top_articles:
        news += f"🔹 [{article.title}]({article.link})\n"
    return news

# ⏰ Scheduled daily post at 9AM UTC
@scheduler.scheduled_job("cron", hour=9)
async def daily_news():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        news_message = get_cyber_news()
        await channel.send(news_message)

# 🤖 Bot ready event + test post
@client.event
async def on_ready():
    print(f"🤖 Bot is running as {client.user}")
    scheduler.start()

    try:
        channel = client.get_channel(CHANNEL_ID)
        print(f"🔍 Checking channel: {CHANNEL_ID} → {channel}")

        if channel:
            news_message = get_cyber_news()
            await channel.send(news_message)
            print("✅ News sent to channel.")
        else:
            print("❌ Channel not found. Check bot permissions and channel ID.")
    except Exception as e:
        print(f"❌ Error during on_ready: {e}")

# 🌐 Flask web server for UptimeRobot pings
app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=3000)

# 🚀 Start Flask server in background thread
Thread(target=run_web).start()

# 🧠 Start the Discord bot
client.run(TOKEN)