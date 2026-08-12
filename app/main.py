from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
from app.auth import auth

from app.routers import (
    students,
    subjects,
    topics,
    progress,
    learning_plans,
    quizzes,
    quiz_questions,
    quiz_attempts,
    achievements,
    notifications,
    recommendations,
    dashboard
)

app = FastAPI(
    title="MentorAI API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to MentorAI API"
    }


app.include_router(students.router)
app.include_router(subjects.router)
app.include_router(topics.router)
app.include_router(progress.router)
app.include_router(learning_plans.router)
app.include_router(quizzes.router)
app.include_router(quiz_questions.router)
app.include_router(quiz_attempts.router)
app.include_router(achievements.router)
app.include_router(notifications.router)
app.include_router(recommendations.router)
app.include_router(dashboard.router)

app.include_router(auth.router)