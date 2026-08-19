from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import StudentDB, StudentProfileDB
from app.models.profile import (
    StudentProfileCreate,
    StudentProfileUpdate
)


# -----------------------------
# Create Student Profile
# -----------------------------
def create_profile(profile: StudentProfileCreate, db: Session):

    # Check if student exists
    student = db.query(StudentDB).filter(
        StudentDB.id == profile.student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Check if profile already exists
    existing_profile = db.query(StudentProfileDB).filter(
        StudentProfileDB.student_id == profile.student_id
    ).first()

    if existing_profile is not None:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists"
        )

    new_profile = StudentProfileDB(
        student_id=profile.student_id,
        goal=profile.goal,
        target_cgpa=profile.target_cgpa,
        weak_subjects=profile.weak_subjects,
        strong_subjects=profile.strong_subjects,
        preferred_study_time=profile.preferred_study_time,
        learning_style=profile.learning_style
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


# -----------------------------
# Get Student Profile
# -----------------------------
def get_profile(student_id: int, db: Session):

    profile = db.query(StudentProfileDB).filter(
        StudentProfileDB.student_id == student_id
    ).first()

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile


# -----------------------------
# Update Student Profile
# -----------------------------
def update_profile(
    student_id: int,
    profile: StudentProfileUpdate,
    db: Session
):

    existing_profile = db.query(StudentProfileDB).filter(
        StudentProfileDB.student_id == student_id
    ).first()

    if existing_profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    existing_profile.goal = profile.goal
    existing_profile.target_cgpa = profile.target_cgpa
    existing_profile.weak_subjects = profile.weak_subjects
    existing_profile.strong_subjects = profile.strong_subjects
    existing_profile.preferred_study_time = profile.preferred_study_time
    existing_profile.learning_style = profile.learning_style

    db.commit()
    db.refresh(existing_profile)

    return existing_profile