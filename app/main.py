from typing import Union

from fastapi import FastAPI
from app.database import database
from app.routes import teachers


app = FastAPI()


@app.on_event("startup")
def on_startup():
    database.create_db_and_tables()


app.include_router(teachers.router)

