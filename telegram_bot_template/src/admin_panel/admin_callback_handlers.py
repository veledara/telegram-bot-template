import src.messages as ms
import src.admin_panel.admIn_db_functions as adm_db
from src.settings import bot
from src.functions import check_user_permissions
from src.keyboards import hide_inline_markup
from telebot.types import Message


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_callback(call) -> None:
    # Проверяем все разрешения
    if not check_user_permissions(call.message):
        return
    callback_action[call.data](call.message)


def admin_statistics_action(message: Message):
    bot.send_message(
        message.chat.id,
        f"{ms.USER_COUNT_MESSAGE}: <b>{adm_db.admin_user_count_check()}</b>\n"
        + f"{ms.NEW_USERS_COUNT_MESSAGE}: <b>{adm_db.admin_count_new_members()}</b>\n\n"
        + f"{ms.WHO_IS_ON_WHAT_STEP_MESSAGE}: \n<b>{adm_db.who_is_on_what_step()}</b>\n",
        reply_markup=hide_inline_markup,
        parse_mode="HTML",
    )


def admin_ban_action(message: Message):
    pass


def admin_adv_action(message: Message):
    pass


callback_action = {
    ms.ADMIN_STATISTICS: admin_statistics_action,
    ms.ADMIN_BAN_USER: admin_ban_action,
    ms.ADMIN_ADV: admin_adv_action,
}
