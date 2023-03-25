import src.messages as ms
from src.settings import settings, bot
from src.db_functions import user_exist, insert_step, check_step, create_user
from src.keyboards import menu_markup


@bot.message_handler(commands=["start"])
def handle_start_command(message) -> None:
    # Если пользователь новый - регистрируем его
    if not user_exist(message.chat.id):
        create_user(message.chat.id, message.from_user.username)
        bot.send_message(
            message.chat.id, ms.WELCOME_MESSAGE, reply_markup=menu_markup
        )
    else:
        bot.send_message(
            message.chat.id, ms.ALREADY_REGISTERED_MESSAGE, reply_markup=menu_markup
        )
        insert_step(ms.MENU, message.chat.id)
