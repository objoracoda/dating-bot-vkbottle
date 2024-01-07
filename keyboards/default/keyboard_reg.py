from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_self_gender = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Я Парень"), color=KeyboardButtonColor.PRIMARY)
        .add(Text("Я Девушка"), color=KeyboardButtonColor.PRIMARY)
    ).get_json()


kb_find_gender = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Парни"), color=KeyboardButtonColor.PRIMARY)
        .add(Text("Девушки"), color=KeyboardButtonColor.PRIMARY)
    ).get_json()

kb_city = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Москва"), color=KeyboardButtonColor.PRIMARY)
    ).get_json()

kb_show_profile = (
        Keyboard(one_time=True, inline=False)
        .add(Text("👤 Профиль"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()