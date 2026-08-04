from pydantic import BaseModel


class ProgressResponse(BaseModel):
    study_streak: int
    study_hours: int
    completed_topics: int
    quiz_accuracy: int
    goal_progress: int
    achievement: str