# database/models/teacher.py: файл сущности "Учитель"

from sqlmodel import SQLModel, Field

# в классе "Base" указываются базовые поля таблицы
# в таком синтаксисе
#
#   name:    str =      Field(index=True)
#    ↑       ↑          ↑                
# имя поля тип поля    значение (класс "Field") оставляем без изменений

class TeacherBase(SQLModel):
    name: str = Field(index=True)
    subject: str = Field(index=True)
    lessons_amount: int = Field(index=True)
    grade_point_avg: float = Field(index=True)
    teacher_courses_amount: int = Field(index=True)
    positive_rewiews_amount: int = Field(index=True)

# основной класс
# наследует базовый с добавлением поля-идентификатора и установкой первичного ключа
class Teacher(TeacherBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
# create DTO класс
# ВАЖНО: наследует базоый класс
# содержит поля, которые вводит пользователь при создании класса
# сюда можно записать поля, которые можно занести пользователю, но они не будут возвращаться в GET-запросах
# например пароль
class TeacherCreate(TeacherBase):
    pass

# update DTO класс
# ВАЖНО: наследует базоый класс
# содержит поля, которые вводит пользователь при редактировании данных
# сюда можно записать поля, которые можно редактировать пользователю
# ВАЖНО: все поля должны быть опциональными
# т.е. иметь тип (тип) или None
class TeacherUpdate(TeacherBase):
    name: str | None = None
    subject: str | None = None
    lessons_amount: int | None = None
    grade_point_avg: float | None = None
    teacher_courses_amount: int | None = None
    positive_rewiews_amount: int | None = None

# ВАЖНО: наследует базоый класс
# содержит только поля, которые должны возвращаться в GET-запросах
class TeacherPublic(TeacherBase):
    # дописываем id, потому что в базовом классе его нет
    id: int
