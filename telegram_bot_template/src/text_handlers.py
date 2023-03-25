import src.steps as st
from src.settings import bot
from src.db_functions import check_step



@bot.message_handler(content_types=["text", "photo"])
def conversation(message) -> None:
    # Проверяем все разрешения
    if not st.check_user_permissions(message):
        return
    st.step_action[check_step(message)](message)
