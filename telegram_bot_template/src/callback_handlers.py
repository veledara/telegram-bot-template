from src.settings import bot
from src.functions import check_user_permissions


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
