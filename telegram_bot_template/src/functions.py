from settings import bot
from db import db_f
from messages import NOT_REGISTERED_MESSAGE


def check_user_permissions(message) -> bool:
    if not db_f.user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return False
    return True
