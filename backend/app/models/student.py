from pydantic import BaseModel
from app.models.subject import Subject

class Student(BaseModel):
    name: str
    department: str
    semester: int
    study_hours: int
    subjects: list[Subject]