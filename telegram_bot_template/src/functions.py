from messages import NOT_REGISTERED_MESSAGE
from db import db_f
from settings import bot


def check_user_permissions(message) -> bool:
    if not db_f.user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return False
    return True
