from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_show_likes = (
        Keyboard(inline=True)
        .add(Text("Показать Лайки"), color=KeyboardButtonColor.POSITIVE)
).get_json()
