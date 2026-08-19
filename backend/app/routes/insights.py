from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.insights_service import (
    get_student_insights
)

router = APIRouter(
    prefix="/insights",
    tags=["AI Learning Insights"]
)


@router.get("/students/{student_id}")
def student_insights(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = get_student_insights(
        db,
        student_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result