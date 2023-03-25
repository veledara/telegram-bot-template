import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.db_functions import lsc


def clear_table(table_name: str) -> None:
    with lsc:
        lsc.cursor.execute(f"DELETE FROM {table_name};")


if __name__ == "__main__":
    clear_table("users")
