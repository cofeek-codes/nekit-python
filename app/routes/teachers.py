from typing import Annotated, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import database

from app.database.models import Teacher, TeacherUpdate, TeacherCreate, TeacherPublic



router = APIRouter(
    prefix="/teachers",
    tags=["teachers"]
    )

@router.get("/all", tags=["teachers"], response_model=list[TeacherPublic])
async def read_all_teachers(
    session: database.SessionDep,
) -> list[TeacherPublic]:
    teachers = session.exec(select(Teacher)).all()
    return teachers



@router.get("/{teacher_id}", tags=["teachers"], response_model=TeacherPublic)
async def read_teacher(teacher_id: int, session: database.SessionDep):
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
          raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")
    return teacher

@router.post('/create', response_model=TeacherPublic)
async def create_teacher(teacher: TeacherCreate, session: database.SessionDep):
    teacher_valid = Teacher.model_validate(teacher)
    session.add(teacher_valid)
    session.commit()
    session.refresh(teacher_valid)
    return teacher_valid

@router.patch('/update/{teacher_id}', response_model=TeacherPublic)
async def update_teacher(teacher_id: int, teacher: TeacherUpdate, session: database.SessionDep):
    teacher_to_update = session.get(Teacher, teacher_id)
    if not teacher_to_update:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")
    teacher_data = teacher.model_dump(exclude_unset=True)
    teacher_to_update.sqlmodel_update(teacher_data)
    session.add(teacher_to_update)
    session.commit()
    session.refresh(teacher_to_update)
    return teacher_to_update

@router.delete("/delete/{teacher_id}")
def delete_hero(teacher_id: int, session: database.SessionDep):
    teacher_to_delete = session.get(Teacher, teacher_id)
    if not teacher_to_delete:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")
    session.delete(teacher_to_delete)
    session.commit()
    return {"ok": True}
