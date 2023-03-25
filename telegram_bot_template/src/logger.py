import logging

# Получение пользовательского логгера и установка уровня логирования
bot_logger = logging.getLogger(__name__)
bot_logger.setLevel(logging.ERROR)
# Настройка обработчика и форматировщика в соответствии с нашими нуждами
bot_handler = logging.FileHandler(f"{__name__}.log", mode="w")
bot_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# добавление форматировщика к обработчику
bot_handler.setFormatter(bot_formatter)
# добавление обработчика к логгеру
bot_logger.addHandler(bot_handler)
