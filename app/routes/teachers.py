# routes/teachers.py: файл endpoint'ов сущности "Учитель"

from typing import Annotated, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import database

from app.database.models import Teacher, TeacherUpdate, TeacherCreate, TeacherPublic

# Создание роутера
router = APIRouter(
    # превикс добовляет этот элемент пути ко всем endpoint'ам (/teachers/all)
    prefix="/teachers",
    tags=["teachers"]
)

@router.get("/all", tags=["teachers"], response_model=list[TeacherPublic])
async def read_all_teachers(
    session: database.SessionDep,
) -> list[TeacherPublic]:
    """get all endpoint - возвращает вообще всех записи в таблице"""
    teachers = session.exec(select(Teacher)).all()
    return teachers

@router.get("/{teacher_id}", tags=["teachers"], response_model=TeacherPublic)
async def read_teacher(teacher_id: int, session: database.SessionDep):
    """
    Возвращает запись с указанным id

    Parameters
    ----------
    teacher_id : int
        id записи
    session : SessionDep
        Сессия, необходимая для взаимодействия с БД

    Raises
    ------
    HTTPException : ошибка с кодом 404, если записи с таким id нет
    """
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")
    return teacher

@router.post('/create', response_model=TeacherPublic)
async def create_teacher(teacher: TeacherCreate, session: database.SessionDep):
    """
    Создает запись

    Parameters
    ----------
    teacher : TeacherCreate
        данные для новой записи
    session : SessionDep
        Сессия, необходимая для взаимодействия с БД

    Raises
    ------
    HTTPException : ошибка с кодом 404, если записи с таким id нет
    """
    teacher_valid = Teacher.model_validate(teacher)
    session.add(teacher_valid)
    session.commit()
    session.refresh(teacher_valid)
    return teacher_valid

@router.patch('/update/{teacher_id}', response_model=TeacherPublic)
async def update_teacher(teacher_id: int, teacher: TeacherUpdate, session: database.SessionDep):
    """
    Обновляет запись

    Parameters
    ----------
    teacher : TeacherUpdate
        обновленные данные
    session : SessionDep
        Сессия, необходимая для взаимодействия с БД

    Raises
    ------
    HTTPException : ошибка с кодом 404, если записи с таким id нет
    """
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
def delete_teacher(teacher_id: int, session: database.SessionDep):
    """
    Удаляет запись

    Parameters
    ----------
    teacher_id : int
        id записи
    session : SessionDep
        Сессия, необходимая для взаимодействия с БД

    Raises
    ------
    HTTPException : ошибка с кодом 404, если записи с таким id нет
    """
    teacher_to_delete = session.get(Teacher, teacher_id)
    if not teacher_to_delete:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")
    session.delete(teacher_to_delete)
    session.commit()
    return {"ok": True}
