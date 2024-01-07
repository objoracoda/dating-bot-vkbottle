from loader import bot

from vkbottle.bot import Message, rules
from vkbottle import PhotoMessageUploader

from vkbottle import Keyboard, KeyboardButtonColor, Text

from vkbottle import BaseStateGroup
from vkbottle import CtxStorage

import requests

ctx = CtxStorage()

photo_uploader = PhotoMessageUploader(bot.api)


@bot.on.private_message(text="👤 Профиль")
async def handler(message):
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Создать Анкету!"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()

    await message.answer(message="Смотри сколько кнопок!!",keyboard=keyboard)


@bot.on.message(text="Начать")
async def start(message):
    photo = await photo_uploader.upload(
        file_source="reg.jpg",
        peer_id=message.peer_id,
    )
    caption = (
        "Я Бот Для Знакомств! 🫦\n\n"
        "Для начала, давай узнаем друг-друга получше 👀\n\n"
        "Помоги мне составить твою анкету 👇")
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Создать Анкету!"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()

    await message.answer(caption,keyboard=keyboard,attachment=photo)
    #await message.answer(caption)