import os
import logging
from telegram import Bot,Update
import pickle
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import asyncio


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TELEGRAM_BOT_CREDENTIALS_FILE = os.path.join(CURRENT_DIRECTORY,"telegram_bot_credentials")
TELEGRAM_IDS_FILE = os.path.join(CURRENT_DIRECTORY,"telegram_ids")

with open(TELEGRAM_BOT_CREDENTIALS_FILE, "rb") as f:
    access_token = pickle.load(f)
with open(TELEGRAM_IDS_FILE,"rb") as f:
	MY_TELEGRAM_ID = pickle.load(f)     
      
# print(access_token)

async def main():
	bot = Bot(token=access_token)
	await bot.send_message(chat_id=MY_TELEGRAM_ID, text="Hello, Automated Telegram Bot")
	# await bot.send_photo(chat_id=MY_TELEGRAM_ID, photo=img)

if __name__ == '__main__':
    asyncio.run(main())



