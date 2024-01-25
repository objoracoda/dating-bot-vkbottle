from loader import bot, photo_uploader

from vkbottle.bot import Message, rules
from vkbottle import PhotoMessageUploader

from vkbottle import Keyboard, KeyboardButtonColor, Text


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