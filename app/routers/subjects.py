from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.dependencies import get_db
from app.auth.oauth2 import get_current_user
from app.auth.roles import require_admin

from app.schemas import (
    SubjectCreate,
    SubjectResponse,
    SubjectUpdate,
)

from app.repositories.subject_repository import (
    create_subject,
    get_subjects,
    get_subject_by_id,
    update_subject,
    delete_subject,
)

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
    dependencies=[Depends(get_current_user)]   # All routes require login
)


# ==========================
# Create Subject (Admin Only)
# ==========================
@router.post("", response_model=SubjectResponse)
def add_subject(
    subject: SubjectCreate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    return create_subject(db, subject)


# ==========================
# Get All Subjects
# ==========================
@router.get("", response_model=List[SubjectResponse])
def list_subjects(
    db: Session = Depends(get_db)
):
    return get_subjects(db)


# ==========================
# Get Subject By ID
# ==========================
@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    subject = get_subject_by_id(db, subject_id)

    if subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return subject


# ==========================
# Update Subject (Admin Only)
# ==========================
@router.put("/{subject_id}", response_model=SubjectResponse)
def edit_subject(
    subject_id: int,
    subject: SubjectUpdate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    updated_subject = update_subject(db, subject_id, subject)

    if updated_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return updated_subject


# ==========================
# Delete Subject (Admin Only)
# ==========================
@router.delete("/{subject_id}")
def remove_subject(
    subject_id: int,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    deleted_subject = delete_subject(db, subject_id)

    if deleted_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return {
        "message": "Subject deleted successfully"
    }