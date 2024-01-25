from loader import bot, db, photo_uploader

from vkbottle.bot import Message, rules
from vkbottle import Keyboard, KeyboardButtonColor, Text

from keyboards.default import kb_match_react
from states import states_match, ctx

import random

@bot.on.private_message(text="Показать Лайки")
async def handler(message):
    try:
        ctx.set("MATCH_LAST_ID",db.get_likes_data(message.peer_id).split(';'))
        MATCH_LAST_ID = ctx.get("MATCH_LAST_ID")
        ctx.set("REC_USER",random.choice(MATCH_LAST_ID))
        REC_USER = ctx.get("REC_USER")
        user_data = db.get_user_data(REC_USER)
        photo = await photo_uploader.upload(
                file_source=user_data[5],
                peer_id=message.peer_id,
            )
        caption = (
                f'{user_data[2].title()}, {user_data[3]}\n'
                f'{user_data[6].title()}\n\n'
                f'{user_data[4]}\n\n')
        await message.answer(message=caption,attachment=photo,keyboard=kb_match_react)
        MATCH_LAST_ID.remove(REC_USER)
        ctx.set("MATCH_LAST_ID",MATCH_LAST_ID)
        await bot.state_dispenser.set(message.peer_id, states_match.STATE_MATCH_REACTION)
    except IndexError:
        await message.answer('Лайков пока нет!')

@bot.on.private_message(state=states_match.STATE_MATCH_REACTION)
async def handler(message):
    try:
        if message.text == '❤️':
            REC_USER = ctx.get("REC_USER")
            #user_data = db.get_user_data(REC_USER)
            await message.answer('Это Match! Можете начинать общаться 😜\nhttps://vk.com/id'+str(message.peer_id))
            #await bot.api.messages.send(peer_id=message.peer_id, random_id=0, message='Это Match! Можете начинать общаться 😜\nhttps://vk.com/id'+str(user_data[1]))
            MATCH_LAST_ID = ctx.get("MATCH_LAST_ID")
            ctx.set("REC_USER",random.choice(MATCH_LAST_ID))
            REC_USER = ctx.get("REC_USER")
            user_data = db.get_user_data(REC_USER)
            photo = await photo_uploader.upload(
                    file_source=user_data[5],
                    peer_id=message.peer_id,
                )
            caption = (
                    f'{user_data[2].title()}, {user_data[3]}\n'
                    f'{user_data[6].title()}\n\n'
                    f'{user_data[4]}\n\n')
            await message.answer(message=caption,attachment=photo,keyboard=kb_match_react)
            MATCH_LAST_ID.remove(REC_USER)
            ctx.set("MATCH_LAST_ID",MATCH_LAST_ID)
            await bot.state_dispenser.set(message.peer_id, states_match.STATE_MATCH_REACTION)
        if message.text == '💔':
            MATCH_LAST_ID = ctx.get("MATCH_LAST_ID")
            ctx.set("REC_USER",random.choice(MATCH_LAST_ID))
            REC_USER = ctx.get("REC_USER")
            user_data = db.get_user_data(REC_USER)
            photo = await photo_uploader.upload(
                    file_source=user_data[5],
                    peer_id=message.peer_id,
                )
            caption = (
                    f'{user_data[2].title()}, {user_data[3]}\n'
                    f'{user_data[6].title()}\n\n'
                    f'{user_data[4]}\n\n')
            await message.answer(message=caption,attachment=photo,keyboard=kb_match_react)
            MATCH_LAST_ID.remove(REC_USER)
            ctx.set("MATCH_LAST_ID",MATCH_LAST_ID)
            await bot.state_dispenser.set(message.peer_id, states_match.STATE_MATCH_REACTION)
    except IndexError:
        db.clear_likes(message.peer_id)
        await message.answer('Лайки кончились! Будем ждать, пока ты кому-то понравишься')