from settings import bot
from functions import check_user_permissions
from db import db_f
import messages as ms


@bot.message_handler(content_types=["text", "photo"])
def conversation(message) -> None:
    # Проверяем все разрешения
    if not check_user_permissions(message):
        return
    step_action[db_f.check_step(message.chat.id)](message)


def menu_step_action(message):
    if message.text == ms.FIRST_BUTTON:
        bot.send_message(message.chat.id, "first button text")
    elif message.text == ms.SECOND_BUTTON:
        bot.send_message(message.chat.id, "second button text")
    elif message.text == ms.THIRD_BUTTON:
        bot.send_message(message.chat.id, "third button text")
    else:
        pass


def second_step_action(message):
    pass


def third_step_action(message):
    pass


step_action = {
    ms.MENU_STEP: menu_step_action,
    ms.SECOND_STEP: second_step_action,
    ms.THIRD_STEP: third_step_action,
}
