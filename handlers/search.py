from loader import bot, db, photo_uploader

from vkbottle.bot import Message, rules
from vkbottle import Keyboard, KeyboardButtonColor, Text

from keyboards.default import kb_search_react
from keyboards.inline import kb_show_likes

from states import states_search, ctx

import random

STATE_LAST_ID = []

@bot.on.private_message(text="🚀 Вперед")
async def handler(message):
    data_user = db.get_user_data(message.from_id)
    ctx.set("STATE_LAST_ID",db.get_users_recommend(message.from_id,data_user[6],data_user[3],data_user[8]))
    try:
        STATE_LAST_ID = ctx.get("STATE_LAST_ID")
        ctx.set("REC_USER",random.choice(STATE_LAST_ID))
        REC_USER = ctx.get("REC_USER")
        photo = await photo_uploader.upload(
            file_source=REC_USER[5],
            peer_id=message.peer_id,
        )
        caption = (
            f'{REC_USER[2].title()}, {REC_USER[3]}\n'
            f'{REC_USER[6].title()}\n\n'
            f'{REC_USER[4]}\n\n')
        await message.answer(message=caption,attachment=photo,keyboard=kb_search_react)
        STATE_LAST_ID.remove(REC_USER)
        ctx.set("STATE_LAST_ID",STATE_LAST_ID)
        await bot.state_dispenser.set(message.peer_id, states_search.STATE_SEARCH_REACTION)
    except IndexError:
        await message.answer('Из твоего Города никого нет!\n\nУкажи другой город, чтобы искать там!')


@bot.on.private_message(state=states_search.STATE_SEARCH_REACTION)
async def handler(message):
    try:
        if message.text == '❤️':
            REC_USER = ctx.get("REC_USER")
            try:
                if str(message.peer_id) not in REC_USER[9]:
                    likes = REC_USER[9]+';'+str(message.peer_id)
                    db.update_likes(REC_USER[1],likes)
                    await message.answer('Твоя анкета кому-то понравилась!',keyboard=kb_show_likes)
                    #await bot.api.messages.send(peer_id=message.peer_id, random_id=0, message='Твоя анкета кому-то понравилась!')
            except TypeError:
                likes = str(message.peer_id)
                db.update_likes(REC_USER[1],likes)
                await message.answer('Твоя анкета кому-то понравилась!',keyboard=kb_show_likes)
            STATE_LAST_ID = ctx.get("STATE_LAST_ID")
            ctx.set("REC_USER",random.choice(STATE_LAST_ID))
            REC_USER = ctx.get("REC_USER")
            photo = await photo_uploader.upload(
                file_source=REC_USER[5],
                peer_id=message.peer_id,
            )
            caption = (
                f'{REC_USER[2].title()}, {REC_USER[3]}\n'
                f'{REC_USER[6].title()}\n\n'
                f'{REC_USER[4]}\n\n')
            STATE_LAST_ID.remove(REC_USER)
            ctx.set("STATE_LAST_ID",STATE_LAST_ID)
            await message.answer(message=caption,attachment=photo,keyboard=kb_search_react)
            await bot.state_dispenser.set(message.peer_id, states_search.STATE_SEARCH_REACTION)
        if message.text == '💔':
            STATE_LAST_ID = ctx.get("STATE_LAST_ID")
            ctx.set("REC_USER",random.choice(STATE_LAST_ID))
            REC_USER = ctx.get("REC_USER")
            photo = await photo_uploader.upload(
                file_source=REC_USER[5],
                peer_id=message.peer_id,
            )
            caption = (
                f'{REC_USER[2].title()}, {REC_USER[3]}\n'
                f'{REC_USER[6].title()}\n\n'
                f'{REC_USER[4]}\n\n')
            STATE_LAST_ID.remove(REC_USER)
            ctx.set("STATE_LAST_ID",STATE_LAST_ID)
            await message.answer(message=caption,attachment=photo,keyboard=kb_search_react)
            await bot.state_dispenser.set(message.peer_id, states_search.STATE_SEARCH_REACTION)
        if message.text == '💤':
            await message.answer("Будем искать анкеты в другой раз 👀\n\nПодождем пока кто-нибудь тебя лайкнет!")
            await bot.state_dispenser.delete(message.peer_id)

    except IndexError:
        return 'Закончились Анкеты!'
