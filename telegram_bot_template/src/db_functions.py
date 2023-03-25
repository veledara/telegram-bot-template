import sqlite3 as sql
import threading
import time
import uuid
from src.messages import MENU_STEP


class LockableSqliteConnection(object):
    def __init__(self, db):
        self.lock = threading.Lock()
        self.connection = sql.connect(db, uri=True, check_same_thread=False)
        self.cursor = None

    def __enter__(self):
        self.lock.acquire()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, type, value, traceback):
        self.connection.commit()
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        self.lock.release()


db = r"telegram_bot_template\databases\telegram_bot_template_database.db"
lsc = LockableSqliteConnection(db)


# Фукнция, генерирующая айди проблемы и совета
def generate_id() -> str:
    return str(uuid.uuid4())


# Фукнция, возвращающая шаг, на котором сейчас находится пользователь
def check_step(user_id: str) -> str:
    with lsc:
        lsc.cursor.execute(f"SELECT step FROM users WHERE id = '{user_id}'")
        result = lsc.cursor.fetchall()[0][0]
    return result


# Фукнция, меняющая шаг, на котором сейчас находится пользователь
def insert_step(n: str, user_id: str) -> None:
    with lsc:
        lsc.cursor.execute(f"UPDATE users SET step = '{n}' WHERE id = '{user_id}'")


# Фукнция, проверяющая есть ли пользователь в базе данных
def user_exist(user_id: str) -> bool:
    with lsc:
        lsc.cursor.execute(f"SELECT id FROM users WHERE id = '{user_id}'")
        exist = lsc.cursor.fetchone()
    return exist


# Фукнция, создающая пользователя в базе данных
def create_user(user_id: str, tg_username: str) -> None:
    with lsc:
        now = int(time.time())
        lsc.cursor.execute(
            f"INSERT INTO users (id, step, tg_username, join_time) VALUES('{user_id}', '{MENU_STEP}', '{tg_username}', '{now}')"
        )
