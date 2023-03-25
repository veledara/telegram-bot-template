from src.messages import NOT_REGISTERED_MESSAGE
from telebot.types import Message
from src.db_functions import user_exist
from src.settings import bot


def check_user_permissions(message: Message) -> bool:
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return False
    return True
