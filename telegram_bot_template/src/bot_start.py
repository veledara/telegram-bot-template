from handlers.command_handlers import *
# from admin_panel.admin_command_handler import *
from handlers.text_handlers import *
from handlers.callback_handlers import *
# from admin_panel.admin_callback_handlers import *


if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)
