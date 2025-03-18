from typing import Annotated, Union
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database import database

from app.database.models import Item



router = APIRouter(
    prefix="/items",
    tags=["items"]
    )

@router.get("/all", tags=["items"])
async def read_all_items(
    session: database.SessionDep,
) -> list[Item]:
    items = session.exec(select(Item)).all()
    return items



@router.get("/{item_id}", tags=["items"])
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
