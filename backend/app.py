from fastapi import FastAPI

from backend.routers.student import router as student_router
from backend.routers.health import router as health_router
app = FastAPI(
    title="MentorAI Backend",
    version="1.0.0",
    description="Backend API for MentorAI"
)

app.include_router(student_router)
app.include_router(health_router)

@app.get("/")
async def home():
    return {
        "message": "MentorAI Backend is Running 🚀"
    }