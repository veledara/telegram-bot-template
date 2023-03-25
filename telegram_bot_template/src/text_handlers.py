import messages as ms
from src.settings import bot
from src.db_functions import check_step, user_exist
from telebot.types import Message


@bot.message_handler(content_types=["text", "photo"])
def conversation(message: Message) -> None:
    # Проверяем все разрешения
    if not check_user_permissions(message):
        return
    step_action[check_step(message.chat.id)](message)


def menu_step_action(message: Message):
    if message.text == ms.FIRST_BUTTON:
        bot.send_message(message.chat.id, "first button text")
    elif message.text == ms.SECOND_BUTTON:
        bot.send_message(message.chat.id, "second button text")
    elif message.text == ms.THIRD_BUTTON:
        bot.send_message(message.chat.id, "third button text")
    else:
        pass


def second_step_action(message: Message):
    pass


def third_step_action(message: Message):
    pass


step_action = {
    ms.MENU_STEP: menu_step_action,
    ms.SECOND_STEP: second_step_action,
    ms.THIRD_STEP: third_step_action,
}


def check_user_permissions(message: Message) -> bool:
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, ms.NOT_REGISTERED_MESSAGE)
        return False
    return True
