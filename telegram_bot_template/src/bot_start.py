import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.command_handlers import *
from src.admin_panel.admin_command_handler import *
from src.text_handlers import *
from src.callback_handlers import *
from src.admin_panel.admin_callback_handlers import *


if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)
