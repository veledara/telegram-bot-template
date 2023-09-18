import telebot as tb
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    tg_token: str

    admins: list

    db_path: str

    db_name: str

    bot: Optional[tb.TeleBot] = None

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
