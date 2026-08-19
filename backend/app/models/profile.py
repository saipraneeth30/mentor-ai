from pydantic import BaseModel


class StudentProfileCreate(BaseModel):
    student_id: int
    goal: str
    target_cgpa: float
    weak_subjects: str
    strong_subjects: str
    preferred_study_time: str
    learning_style: str


class StudentProfileResponse(BaseModel):
    id: int
    student_id: int
    goal: str
    target_cgpa: float
    weak_subjects: str
    strong_subjects: str
    preferred_study_time: str
    learning_style: str

    class Config:
        from_attributes = True


class StudentProfileUpdate(BaseModel):
    goal: str
    target_cgpa: float
    weak_subjects: str
    strong_subjects: str
    preferred_study_time: str
    learning_style: str