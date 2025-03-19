# database/database.py: файл конфигурации базы данных

from typing import Annotated

from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends

# конфигурация БД
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

# инициализация БД
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)


# инициализация сущностей (таблиц)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# получение и экспорт сессии
def get_session():
    with Session(engine) as session:
        yield session

# ВАЖНО! эта переменная используется в endpoint'ах для взаимодействия с БД
SessionDep = Annotated[Session, Depends(get_session)]
