# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio
import random
from config import Config
from pyrogram import Client, idle, filters
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# Create Bot Client
VJBot = Client(
    "VJ-Forward-Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=120,
    plugins=dict(root="plugins")
)

# 🔥 Positive Emojis List
positive_emojis = [
    "🔥", "🚀", "😎", "💪", "✨",
    "🎉", "🥳", "⚡", "😃", "🫶"
]

# ✅ /start Command Handler
@VJBot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    random_emoji = random.choice(positive_emojis)
    
    await message.reply_text(
        f"🚀 Welcome To Advance Forward Bot {random_emoji}\n\n"
        "Send me any message and I will forward it automatically!"
    )

async def main():
    await VJBot.start()
    await restart_forwards(VJBot)
    print("Bot Started Successfully ✅")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
