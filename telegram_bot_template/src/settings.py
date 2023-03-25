import telebot as tb
from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    tg_token: str

    admins: list

    bot: Optional[tb.TeleBot]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = tb.TeleBot(self.tg_token)
        print(self.bot.get_me())

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
bot = settings.bot
