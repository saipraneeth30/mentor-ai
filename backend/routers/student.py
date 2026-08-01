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