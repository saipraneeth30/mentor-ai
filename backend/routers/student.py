from fastapi import APIRouter

from backend.schemas.student import StudentRegistration
from backend.services.student_service import StudentService

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/register")
async def register_student(student: StudentRegistration):
    return StudentService.register_student(student)


@router.get("/dashboard")
async def get_dashboard():
    return StudentService.get_dashboard()


@router.get("/progress")
async def get_progress():
    return StudentService.get_progress()

@router.get("/settings")
async def get_settings():
    return StudentService.get_settings()