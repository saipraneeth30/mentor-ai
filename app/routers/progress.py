from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.auth.oauth2 import get_current_user
from app.auth.roles import require_admin
from app.dependencies import get_db

from app.models import Progress

from app.schemas import (
    ProgressCreate,
    ProgressResponse,
    ProgressUpdate
)

from app.repositories.progress_repository import (
    create_progress,
    get_progress,
    get_progress_by_id,
    update_progress,
    delete_progress
)


router = APIRouter(
    prefix="/progress",
    tags=["Progress"],
    dependencies=[Depends(get_current_user)]
)


# ==========================
# Create Progress - Admin Only
# ==========================
@router.post("", response_model=ProgressResponse)
def add_progress(
    progress: ProgressCreate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    return create_progress(db, progress)


# ==========================
# Get All Progress
# ==========================
@router.get("", response_model=List[ProgressResponse])
def list_progress(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Admin can see all progress
    if current_user["role"] == "admin":
        return get_progress(db)

    # Student can see only their own progress
    return db.query(Progress).filter(
        Progress.student_id == current_user["student_id"]
    ).all()


# ==========================
# Get Progress By ID
# ==========================
@router.get("/{progress_id}", response_model=ProgressResponse)
def get_progress_record(
    progress_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    progress = get_progress_by_id(db, progress_id)

    if progress is None:
        raise HTTPException(
            status_code=404,
            detail="Progress not found"
        )

    # Student can only access their own progress
    if (
        current_user["role"] != "admin"
        and progress.student_id != current_user["student_id"]
    ):
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return progress


# ==========================
# Update Progress
# ==========================
@router.put("/{progress_id}", response_model=ProgressResponse)
def edit_progress(
    progress_id: int,
    progress: ProgressUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    existing_progress = get_progress_by_id(
        db,
        progress_id
    )

    if existing_progress is None:
        raise HTTPException(
            status_code=404,
            detail="Progress not found"
        )

    # Student can only update their own progress
    if (
        current_user["role"] != "admin"
        and existing_progress.student_id != current_user["student_id"]
    ):
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return update_progress(
        db,
        progress_id,
        progress
    )


# ==========================
# Delete Progress - Admin Only
# ==========================
@router.delete("/{progress_id}")
def remove_progress(
    progress_id: int,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    deleted_progress = delete_progress(
        db,
        progress_id
    )

    if deleted_progress is None:
        raise HTTPException(
            status_code=404,
            detail="Progress not found"
        )

    return {
        "message": "Progress deleted successfully"
    }