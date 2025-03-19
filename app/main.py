# main.py: Главный файл сервера

from typing import Union

from fastapi import FastAPI
from app.database import database
from app.routes import teachers

# экземпляр класса FastAPI (сам сервер)
app = FastAPI()

# в ивенте "startup" вызываем функцию инициализации БД
@app.on_event("startup")
def on_startup():
    database.create_db_and_tables()

# здесь подключаются все роутеры
# (файлы с CRUD-операциями сущностей)
# для каждой отдельной сущности (пользователь, учитель, критерий) создается свой роутер и подключаются здесь
app.include_router(teachers.router)

