# 🛡️ CyberNewsBot

**CyberNewsBot** is a Python-based Discord bot that delivers the **top 3 daily cybersecurity news headlines** directly into a designated channel in your Discord server. It also includes a web server to keep it running 24/7 using Replit + UptimeRobot.

> Built with ❤️ by [Jacore Baptiste](https://www.linkedin.com/in/your-profile) as part of the Year Up program to support peer learning and awareness in the cybersecurity community.

---

## 🚀 Features

- 📬 Posts **top 3 cybersecurity headlines** daily from The Hacker News
- 🕘 Posts automatically every morning at 9 AM UTC
- 🛠️ Slash command (`/news`) to fetch headlines on-demand (coming next)
- 💡 Future: GPT-powered summaries, threat level alerts, multi-feed support
- 🔄 24/7 uptime using Flask + UptimeRobot + Replit

---

## 📸 Screenshot

> _Example of daily post:_

```
🛡️ Top 3 Cybersecurity Headlines Today:

🔹 [Critical Cisco ASA Vulnerability Exploited in the Wild](https://example.com/article1)
🔹 [Google Patches Chrome Zero-Day Under Active Attack](https://example.com/article2)
🔹 [New Phishing Campaign Mimics Microsoft MFA Screens](https://example.com/article3)
```

---

## 🧰 Tech Stack

- **Python 3**
- `discord.py` – Discord bot framework
- `feedparser` – Parse RSS feeds
- `APScheduler` – Schedule daily jobs
- `Flask` – Lightweight web server for uptime pings
- **Replit** – Cloud code hosting
- **UptimeRobot** – Keeps Replit container alive

---

## 🛠️ Installation & Setup

1. Clone this repo or fork it:
   ```bash
   git clone https://github.com/your-username/cybernewsbot.git
   cd cybernewsbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your environment variables:
   - `DISCORD_TOKEN` – Your bot token
   - `DISCORD_CHANNEL_ID` – The ID of the channel to post in

4. Run the bot:
   ```bash
   python main.py
   ```

---

## 🧠 How It Works

- Fetches latest headlines from [The Hacker News](https://thehackernews.com) via RSS
- Formats them with markdown and links
- Posts them into your specified Discord channel
- Keeps Flask server running so Replit can be pinged
- UptimeRobot hits the Flask route every 5 minutes to prevent timeout

---

## 🛡️ Coming Soon

- `/news` slash command for manual fetch
- GPT-4 summaries of each article
- Multi-source support (BleepingComputer, CISA, Google News)
- “Threat Level of the Day” indicator

---

## 📬 Contact

Built by **Jacore Baptiste**  
🌐 [LinkedIn](https://www.linkedin.com/in/your-profile)  
📧 Email: your.email@example.com

---

## ⭐️ Show Some Love

If this bot helped you or inspired your own project:

⭐️ Star this repo  
🔀 Fork it  
📢 Share with your friends or Year Up peers  

---

> “Security is everyone’s responsibility — staying informed is the first line of defense.”
