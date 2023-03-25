import src.messages as ms
from src.settings import bot
from src.db_functions import user_exist


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


def check_user_permissions(message) -> bool:
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, ms.NOT_REGISTERED_MESSAGE)
        return False
    return True
