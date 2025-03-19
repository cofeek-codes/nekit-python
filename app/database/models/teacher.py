from sqlmodel import SQLModel, Field

class TeacherBase(SQLModel):
    name: str = Field(index=True)
    subject: str = Field(index=True)
    lessons_amount: int = Field(index=True)
    grade_point_avg: float = Field(index=True)
    teacher_courses_amount: int = Field(index=True)
    positive_rewiews_amount: float = Field(index=True)
    
class Teacher(TeacherBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(TeacherBase):
    name: str | None = None
    subject: str | None = None
    lessons_amount: int | None = None
    grade_point_avg: float | None = None
    teacher_courses_amount: int | None = None
    positive_rewiews_amount: float | None = None
        
class TeacherPublic(TeacherBase):
    id: int
