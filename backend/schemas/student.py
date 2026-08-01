from typing import Literal

from pydantic import BaseModel, Field


class StudentRegistration(BaseModel):
    goal: str = Field(
        min_length=3,
        max_length=100,
        description="Student's learning goal"
    )

    level: Literal[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    study_hours: int = Field(
        ge=1,
        le=16,
        description="Daily study hours"
    )

    preferred_time: Literal[
        "Morning",
        "Afternoon",
        "Evening",
        "Night"
    ]

    target_exam_date: str = Field(
        min_length=3,
        max_length=50,
        description="Target exam date"
    )