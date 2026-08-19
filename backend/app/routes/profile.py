from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.profile import (
    StudentProfileCreate,
    StudentProfileResponse,
    StudentProfileUpdate
)
from app.services.profile_service import (
    create_profile,
    get_profile,
    update_profile
)

router = APIRouter(
    prefix="/profile",
    tags=["Student Profile"]
)


@router.post("/", response_model=StudentProfileResponse)
def create_student_profile(
    profile: StudentProfileCreate,
    db: Session = Depends(get_db)
):
    return create_profile(profile, db)


@router.get("/{student_id}", response_model=StudentProfileResponse)
def get_student_profile(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_profile(student_id, db)


@router.put("/{student_id}", response_model=StudentProfileResponse)
def update_student_profile(
    student_id: int,
    profile: StudentProfileUpdate,
    db: Session = Depends(get_db)
):
    return update_profile(student_id, profile, db)