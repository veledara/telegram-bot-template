import messages as ms
from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, DateTime, literal, func
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import settings
import datetime as dt


Base = declarative_base()
engine = create_engine(f"sqlite:///{settings.db_path + settings.db_name}")


class DBAdapter:
    @contextmanager
    def get_session(self):
        try:
            session = Session()
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            session.close()


class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True)
    step = Column("step", String)
    join_time = Column("join_name", DateTime, default=dt.datetime.now())
    tg_username = Column("tg_username", String)

    def __init__(self, user_id, step, join_time, tg_username):
        self.user_id = user_id
        self.step = step
        self.join_time = join_time
        self.tg_username = tg_username

    def __repr__(self):
        return f"{self.user_id} {self.tg_username} {self.step}"


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


class DBFunctions:
    def __init__(self) -> None:
        self._db_adapter = DBAdapter()

    def user_exist(self, user_id: str) -> bool:
        with self._db_adapter.get_session() as session:
            q = session.query(User).filter(User.user_id == user_id)
            is_user = session.query(literal(True)).filter(q.exists()).scalar()
            return is_user

    def check_step(self, user_id: str) -> str:
        with self._db_adapter.get_session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            return user.step

    def insert_step(self, new_step: str, user_id: str) -> None:
        with self._db_adapter.get_session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.step = new_step

    def create_user(self, user_id: str, tg_username: str) -> None:
        with self._db_adapter.get_session() as session:
            new_user = User(
                user_id=user_id,
                step=ms.MENU_STEP,
                join_time=dt.datetime.now(),
                tg_username=tg_username,
            )
            session.add(new_user)


class DBAdminFunctions:
    def __init__(self) -> None:
        self._db_adapter = DBAdapter()

    def admin_user_count_check(self) -> int:
        with self._db_adapter.get_session() as session:
            user_count = session.query(User).count()
            return user_count

    def admin_count_new_members(self) -> int:
        with self._db_adapter.get_session() as session:
            current_time = dt.datetime.now()
            yesterday = current_time - dt.timedelta(hours=24)
            new_members_count = (
                session.query(User).filter(User.join_time >= yesterday).count()
            )
            return new_members_count

    def who_is_on_what_step(self) -> str:
        with self._db_adapter.get_session() as session:
            step_counts = (
                session.query(User.step, func.count(User.user_id))
                .group_by(User.step)
                .all()
            )
            text = ""
            all_users_count = session.query(func.count()).scalar()
            for step, count in step_counts:
                percentage = (count / all_users_count) * 100
                text += f"{step} - {percentage:.2f}% - {count}\n"
            return text


db_f = DBFunctions()
db_adm_f = DBAdminFunctions()

if __name__ == "__main__":
    pass
