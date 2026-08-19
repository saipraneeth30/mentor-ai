from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user

router = APIRouter()


@router.get("/attendance")
def get_attendance(
    current_user: dict = Depends(get_current_user)
):
    """
    Temporary attendance endpoint.
    Later we'll connect this to the database.
    """

    return {
        "attendance_percentage": 92,
        "present_classes": 46,
        "absent_classes": 4,
        "total_classes": 50
    }