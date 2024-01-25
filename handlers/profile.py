from loader import bot, db, photo_uploader

from vkbottle.bot import Message, rules
from vkbottle import Keyboard, KeyboardButtonColor, Text

from keyboards.default import kb_profile

@bot.on.private_message(text="👤 Профиль")
async def handler(message):
    data = db.get_user_data(message.from_id)
    
    photo = await photo_uploader.upload(
        file_source=data[5],
        peer_id=message.peer_id,
    )
    caption = (
        f'{data[2].title()}, {data[3]}\n'
        f'{data[6].title()}\n\n'
        f'{data[4]}\n\n')
    await message.answer(message=caption,attachment=photo,keyboard=kb_profile)