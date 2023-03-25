import src.messages as ms
from src.settings import bot
from src.db_functions import user_exist, insert_step, create_user
from src.keyboards import menu_markup
from telebot.types import Message


@bot.message_handler(commands=["start"])
def handle_start_command(message: Message) -> None:
    # Если пользователь новый - регистрируем его
    if not user_exist(message.chat.id):
        create_user(message.chat.id, message.from_user.username)
        bot.send_message(message.chat.id, ms.WELCOME_MESSAGE, reply_markup=menu_markup)
    else:
        bot.send_message(
            message.chat.id, ms.ALREADY_REGISTERED_MESSAGE, reply_markup=menu_markup
        )
        insert_step(ms.MENU_STEP, message.chat.id)
