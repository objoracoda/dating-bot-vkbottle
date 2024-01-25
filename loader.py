import asyncio

from vkbottle.bot import Bot
from utils.database_api import Database

from vkbottle import PhotoMessageUploader

from data import config

bot = Bot(token=config.BOT_TOKEN)

db = Database('data/database.db')

photo_uploader = PhotoMessageUploader(bot.api)