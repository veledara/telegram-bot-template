import messages as ms
from settings import bot
from db import db_f
from keyboards import menu_markup


@bot.message_handler(commands=["start"])
def handle_start_command(message) -> None:
    # Если пользователь новый - регистрируем его
    if not db_f.user_exist(message.chat.id):
        db_f.create_user(message.chat.id, message.from_user.username)
        bot.send_message(message.chat.id, ms.WELCOME_MESSAGE, reply_markup=menu_markup)
    else:
        bot.send_message(
            message.chat.id, ms.ALREADY_REGISTERED_MESSAGE, reply_markup=menu_markup
        )
        db_f.insert_step(ms.MENU_STEP, message.chat.id)
