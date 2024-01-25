from vkbottle import Keyboard, KeyboardButtonColor, Text

kb_match_react = (
        Keyboard(one_time=True, inline=False)
        .add(Text("❤️"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("💔"), color=KeyboardButtonColor.PRIMARY)
    ).get_json()