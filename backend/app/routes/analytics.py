from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.analytics_service import (
    get_student_analytics
)

router = APIRouter(
    prefix="/analytics",
    tags=["Learning Analytics"]
)


@router.get("/students/{student_id}")
def student_analytics(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = get_student_analytics(
        db,
        student_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result