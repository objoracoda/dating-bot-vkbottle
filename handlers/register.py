from loader import bot

from vkbottle.bot import Message, rules
from vkbottle import PhotoMessageUploader

from vkbottle import Keyboard, KeyboardButtonColor, Text
from states import states_reg, ctx
from keyboards.default import kb_self_gender, kb_find_gender, kb_city, kb_show_profile

from loader import db

import requests


@bot.on.private_message(lev="Создать Анкету!")
async def handler(message):
    user_data = await bot.api.users.get(message.from_id)
    kb_self_name = (
        Keyboard(one_time=True, inline=False)
        .add(Text(f"{user_data[0].first_name}"), color=KeyboardButtonColor.PRIMARY)
    ).get_json()
    await bot.state_dispenser.set(message.peer_id, states_reg.NAME)
    await message.answer("Отлично, составим новую Анкету!\n\nКак тебя зовут?", keyboard=kb_self_name)


@bot.on.private_message(state=states_reg.NAME)
async def handler(message):
    ctx.set("name",message.text)
    name = message.text
    await bot.state_dispenser.set(message.peer_id, states_reg.AGE)
    return f'{name}, сколько тебе лет?'


@bot.on.private_message(state=states_reg.AGE)
async def handler(message):
    ctx.set("age",message.text)
    await bot.state_dispenser.set(message.peer_id, states_reg.GENDER)
    await message.answer('Определимся с твоим полом 👀', keyboard=kb_self_gender)


@bot.on.private_message(state=states_reg.GENDER)
async def handler(message):
    ctx.set("gender",message.text)
    await bot.state_dispenser.set(message.peer_id, states_reg.PHOTO)
    return 'Фотку 👀!'


@bot.on.private_message(rules.AttachmentTypeRule(["photo"]),state=states_reg.PHOTO)
async def handler(message):
    url = (message.attachments[0].photo.sizes[-5].url)
    response = requests.get(url)
    if response.status_code == 200: 
        with open(f'./media/users/{message.from_id}.jpg', 'wb') as f:
            f.write(response.content)
        ctx.set("photo",f'./media/users/{message.from_id}.jpg')
        name = ctx.get("name")
        #age = ctx.get("age")
        #gender = ctx.get("gender")
        #await message.answer(f"{name},{age},{gender}")
        #await bot.state_dispenser.delete(message.peer_id)
        await message.answer(f"{name}, расскажи немного о себе!\n\nА исскуственный интеллект поможет подобрать тебе пару, на основе твоей анкеты 😉")
        await bot.state_dispenser.set(message.peer_id, states_reg.CONTENT)


@bot.on.private_message(state=states_reg.CONTENT)
async def handler(message):
    ctx.set("content",message.text)
    await message.answer("Кого будем искать?", keyboard=kb_find_gender)
    await bot.state_dispenser.set(message.peer_id, states_reg.FIND_GENDER)


@bot.on.private_message(state=states_reg.FIND_GENDER)
async def handler(message):
    if message.text == 'Парни':
        ctx.set("find_gender",'male')
        await bot.state_dispenser.set(message.peer_id, states_reg.FIND_GENDER)

    if message.text == 'Девушки':
        ctx.set("find_gender",'female')
    else:
        message.answer('Не понимаю тебя!')
    await message.answer("Из какого ты города?", keyboard=kb_city)
    await bot.state_dispenser.set(message.peer_id, states_reg.CITY)


@bot.on.private_message(state=states_reg.CITY)
async def handler(message):
    ctx.set("city",message.text)
    await message.answer("Анкета создана! Давай посмотрим на твой профиль 👀", keyboard=kb_show_profile)
    db.add_user(message.from_id,
        ctx.get('name'),
        ctx.get('age'),
        ctx.get('gender'),
        ctx.get('photo'),
        ctx.get('content'),
        ctx.get('find_gender'),
        ctx.get('city'),
        'done')
    await bot.state_dispenser.delete(message.peer_id)