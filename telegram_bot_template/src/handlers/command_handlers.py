import messages as ms
from settings import settings, bot
from db import db_f
import keyboards as kb
from functions import check_user_permissions


@bot.message_handler(commands=["start"])
def handle_start_command(message) -> None:
    # Если пользователь новый - регистрируем его
    if not db_f.user_exist(message.chat.id):
        db_f.create_user(message.chat.id, message.from_user.username)
        bot.send_message(
            message.chat.id, ms.WELCOME_MESSAGE, reply_markup=kb.menu_markup
        )
    else:
        bot.send_message(
            message.chat.id, ms.ALREADY_REGISTERED_MESSAGE, reply_markup=kb.menu_markup
        )
        db_f.insert_step(ms.MENU_STEP, message.chat.id)


@bot.message_handler(commands=["admin"])
def handle_admin_command(message) -> None:
    # Проверка из трех этапов: зарегестирован ли пользователь, прочитал п.с. и забанен ли он?
    if not check_user_permissions(message):
        return
    if str(message.chat.id) in settings.admins:
        bot.send_message(
            message.chat.id,
            ms.WELCOME_ADMIN_MESSAGE,
            reply_markup=kb.administration_inline_markup,
        )
    else:
        bot.send_message(
            message.chat.id, ms.NOT_ADMIN_MESSAGE, reply_markup=kb.menu_markup
        )
    db_f.insert_step(ms.MENU_STEP, message.chat.id)
