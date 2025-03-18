from typing import Annotated, Union
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.database import database

from app.database.models import Teacher



router = APIRouter(
    prefix="/teachers",
    tags=["teachers"]
    )

@router.get("/all", tags=["teachers"])
async def read_all_teachers(
    session: database.SessionDep,
) -> list[Teacher]:
    teachers = session.exec(select(Teacher)).all()
    return teachers



@router.get("/{teacher_id}", tags=["teachers"])
async def read_teacher(teacher_id: int):
    teacher = session.get(Teacher, teacer_id)
    if not teacher:
          raise HTTPException(status_code=404, detail=f"Teacher with ${teacher_id} not found")
    return teacher
