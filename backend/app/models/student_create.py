from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    department: str
    semester: int
    study_hours: int