from fastapi import APIRouter, Depends

from app.utils.dependencies import (
    get_current_student,
    get_current_mentor,
    get_current_admin,
)

router = APIRouter(prefix="/roles", tags=["Role Based Access"])


@router.get("/student")
def student_dashboard(
    current_user: dict = Depends(get_current_student)
):
    return {
        "message": "Welcome Student!",
        "user": current_user
    }


@router.get("/mentor")
def mentor_dashboard(
    current_user: dict = Depends(get_current_mentor)
):
    return {
        "message": "Welcome Mentor!",
        "user": current_user
    }


@router.get("/admin")
def admin_dashboard(
    current_user: dict = Depends(get_current_admin)
):
    return {
        "message": "Welcome Admin!",
        "user": current_user
    }