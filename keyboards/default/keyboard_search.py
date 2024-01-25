from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_search_react = (
        Keyboard(one_time=True, inline=False)
        .add(Text("❤️"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("💔"), color=KeyboardButtonColor.PRIMARY)
        .add(Text("💤"), color=KeyboardButtonColor.SECONDARY)
    ).get_json()
