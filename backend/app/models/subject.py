from pydantic import BaseModel


class Subject(BaseModel):
    subject_name: str
    difficulty: str