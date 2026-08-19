from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.recommendation_service import get_recommendations

router = APIRouter(
    prefix="/recommendations",
    tags=["AI Recommendations"]
)


@router.get("/{student_id}")
def recommendations(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = get_recommendations(
        db,
        student_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result