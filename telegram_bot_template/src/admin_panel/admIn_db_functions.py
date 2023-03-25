import time
from src.db_functions import lsc


def admin_user_count_check() -> str:
    with lsc:
        lsc.cursor.execute("SELECT COUNT(*) FROM users")
        count = lsc.cursor.fetchone()
    return count[0]


def admin_count_new_members() -> str:
    with lsc:
        now = int(time.time())
        yesterday = now - (24 * 60 * 60)
        lsc.cursor.execute(f"SELECT * FROM users WHERE join_time >= '{yesterday}'")
        new_members = lsc.cursor.fetchall()
        num_new_members = len(new_members)
    return num_new_members


def who_is_on_what_step() -> str:
    with lsc:
        text = ""
        lsc.cursor.execute("SELECT step, COUNT(*) FROM users GROUP BY step")
        step_counts = lsc.cursor.fetchall()
        lsc.cursor.execute("SELECT COUNT(*) FROM users")
        all_users_count = lsc.cursor.fetchone()[0]
        for step, count in step_counts:
            percentage = count / all_users_count
            text += (
                f"{step} - {(count/all_users_count)*100}% - {count}\n"
                if percentage.is_integer()
                else f"{step} - {(count/all_users_count)*100:.{4}}% - {count}\n"
            )
    return text
