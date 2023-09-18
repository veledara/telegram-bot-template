from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, DateTime, literal
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import settings
import datetime
import messages as ms


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
    join_time = Column("join_name", DateTime, default=datetime.datetime.now())
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
                join_time=datetime.datetime.now(),
                tg_username=tg_username,
            )
            session.add(new_user)


db_f = DBFunctions()

if __name__ == "__main__":
    pass
