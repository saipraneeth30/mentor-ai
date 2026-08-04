from pydantic import BaseModel


class DashboardResponse(BaseModel):
    goal: str
    study_streak: int
    study_hours: int
    quiz_accuracy: int
    current_subject: str