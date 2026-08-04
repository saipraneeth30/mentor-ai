from pydantic import BaseModel


class SettingsResponse(BaseModel):
    goal: str
    level: str
    daily_study_hours: int
    preferred_study_time: str
    target_exam: str