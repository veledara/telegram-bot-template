import src.messages as ms
from src.keyboards import administration_inline_markup
from src.settings import settings, bot
from src.db_functions import insert_step
from src.functions import check_user_permissions
from src.keyboards import menu_markup
from telebot.types import Message


@bot.message_handler(commands=["admin"])
def handle_admin_command(message: Message) -> None:
    # Проверка из трех этапов: зарегестирован ли пользователь, прочитал п.с. и забанен ли он?
    if not check_user_permissions(message):
        return
    if str(message.chat.id) in settings.admins:
        bot.send_message(
            message.chat.id,
            ms.WELCOME_ADMIN_MESSAGE,
            reply_markup=administration_inline_markup,
        )
    else:
        bot.send_message(
            message.chat.id, ms.NOT_ADMIN_MESSAGE, reply_markup=menu_markup
        )
    insert_step(ms.MENU_STEP, message.chat.id)
