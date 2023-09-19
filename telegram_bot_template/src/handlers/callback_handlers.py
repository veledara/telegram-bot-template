from settings import bot
from functions import check_user_permissions
from db import db_adm_f
import messages as ms
import keyboards as kb


@bot.callback_query_handler(func=lambda call: call.data == "hide")
def hide_callback(call) -> None:
    # Проверяем все разрешения
    if not check_user_permissions(call.message):
        return

    if call.data == "hide":
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        except Exception as e:
            pass
            # обработать
    else:
        pass


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_callback(call) -> None:
    # Проверяем все разрешения
    if not check_user_permissions(call.message):
        return
    callback_action[call.data](call.message)


def admin_statistics_action(message):
    bot.send_message(
        message.chat.id,
        f"{ms.USER_COUNT_MESSAGE}: <b>{db_adm_f.admin_user_count_check()}</b>\n"
        + f"{ms.NEW_USERS_COUNT_MESSAGE}: <b>{db_adm_f.admin_count_new_members()}</b>\n\n"
        + f"{ms.WHO_IS_ON_WHAT_STEP_MESSAGE}: \n<b>{db_adm_f.who_is_on_what_step()}</b>\n",
        reply_markup=kb.hide_inline_markup,
        parse_mode="HTML",
    )


def admin_ban_action(message):
    pass


def admin_adv_action(message):
    pass


callback_action = {
    ms.ADMIN_STATISTICS: admin_statistics_action,
    ms.ADMIN_BAN_USER: admin_ban_action,
    ms.ADMIN_ADV: admin_adv_action,
}
