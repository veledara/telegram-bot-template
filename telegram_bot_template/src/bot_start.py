from handlers.command_handlers import *
from handlers.text_handlers import *
from handlers.callback_handlers import *


if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)
