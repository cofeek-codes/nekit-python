from sqlmodel import SQLModel, Field

class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    subject: str = Field(index=True)
    lessons_amount: int = Field(index=True)
    grade_point_avg: float = Field(index=True)
    teacher_courses_amount: int = Field(index=True)
    positive_rewiews_amount: float = Field(index=True)
    
