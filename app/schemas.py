from pydantic import BaseModel
from datetime import datetime, date
from typing import Any, List


class DashboardResponse(BaseModel):
    student: Any
    progress: List[Any]
    learning_plans: List[Any]
    quiz_attempts: List[Any]
    achievements: List[Any]
    notifications: List[Any]
    recommendations: List[Any]
class StudentCreate(BaseModel):
    full_name: str
    email: str
    phone_number: str
    password: str
    role: str = "student"

class StudentResponse(BaseModel):
    student_id: int
    full_name: str
    email: str
    phone_number: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
class StudentUpdate(BaseModel):
    full_name: str
    email: str
    phone_number: str
    password: str
    status: str
    role: str
class SubjectCreate(BaseModel):
    subject_name: str
    description: str


class SubjectResponse(BaseModel):
    subject_id: int
    subject_name: str
    description: str

    class Config:
        from_attributes = True


class SubjectUpdate(BaseModel):
    subject_name: str
    description: str
class SubjectCreate(BaseModel):
    subject_name: str
    description: str


class SubjectResponse(BaseModel):
    subject_id: int
    subject_name: str
    description: str

    class Config:
        from_attributes = True


class SubjectUpdate(BaseModel):
    subject_name: str
    description: str
class TopicCreate(BaseModel):
    topic_name: str
    description: str
    subject_id: int


class TopicResponse(BaseModel):
    topic_id: int
    topic_name: str
    description: str
    subject_id: int

    class Config:
        from_attributes = True


class TopicUpdate(BaseModel):
    topic_name: str
    description: str
    subject_id: int
# ==========================
# Progress Schemas
# ==========================

class ProgressCreate(BaseModel):
    student_id: int
    topic_id: int
    completion_percentage: int
    status: str


class ProgressUpdate(BaseModel):
    completion_percentage: int
    status: str


class ProgressResponse(BaseModel):
    progress_id: int
    student_id: int
    topic_id: int
    completion_percentage: int
    status: str

    class Config:
        from_attributes = True
# ==========================
# Learning Plan Schemas
# ==========================

from datetime import date


class LearningPlanCreate(BaseModel):
    student_id: int
    subject_id: int
    goal: str
    start_date: date
    end_date: date
    status: str


class LearningPlanUpdate(BaseModel):
    goal: str
    start_date: date
    end_date: date
    status: str


class LearningPlanResponse(BaseModel):
    plan_id: int
    student_id: int
    subject_id: int
    goal: str
    start_date: date
    end_date: date
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
class QuizCreate(BaseModel):
    subject_id: int
    quiz_name: str
    total_questions: int


class QuizUpdate(BaseModel):
    quiz_name: str
    total_questions: int


class QuizResponse(BaseModel):
    quiz_id: int
    subject_id: int
    quiz_name: str
    total_questions: int
    created_at: datetime

    class Config:
        from_attributes = True
class QuizQuestionCreate(BaseModel):
    quiz_id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str


class QuizQuestionUpdate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str


class QuizQuestionResponse(BaseModel):
    question_id: int
    quiz_id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str

    class Config:
        from_attributes = True
class QuizAttemptCreate(BaseModel):
    student_id: int
    quiz_id: int
    score: int


class QuizAttemptUpdate(BaseModel):
    score: int


class QuizAttemptResponse(BaseModel):
    attempt_id: int
    student_id: int
    quiz_id: int
    score: int
    attempted_at: datetime

    class Config:
        from_attributes = True
class AchievementCreate(BaseModel):
    student_id: int
    achievement_name: str
    description: str


class AchievementUpdate(BaseModel):
    achievement_name: str
    description: str


class AchievementResponse(BaseModel):
    achievement_id: int
    student_id: int
    achievement_name: str
    description: str
    earned_date: datetime

    class Config:
        from_attributes = True
class NotificationCreate(BaseModel):
    student_id: int
    title: str
    message: str
    notification_type: str


class NotificationUpdate(BaseModel):
    title: str
    message: str
    notification_type: str
    is_read: bool


class NotificationResponse(BaseModel):
    notification_id: int
    student_id: int
    title: str
    message: str
    notification_type: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
class RecommendationCreate(BaseModel):
    student_id: int
    subject_id: int
    topic_id: int | None = None
    recommendation_text: str
    priority: str


class RecommendationUpdate(BaseModel):
    topic_id: int | None = None
    recommendation_text: str
    priority: str


class RecommendationResponse(BaseModel):
    recommendation_id: int
    student_id: int
    subject_id: int
    topic_id: int | None
    recommendation_text: str
    priority: str
    created_at: datetime

    class Config:
        from_attributes = True
from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str