from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_profile = (
        Keyboard(one_time=True, inline=False)
        .add(Text("🚀 Вперед"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("🌹 Подписка"), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("👤 Новая Анкета"), color=KeyboardButtonColor.SECONDARY)
    ).get_json()
