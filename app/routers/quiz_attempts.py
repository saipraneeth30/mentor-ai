from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    QuizAttemptCreate,
    QuizAttemptUpdate,
    QuizAttemptResponse
)

from app.repositories.quiz_attempt_repository import (
    create_attempt,
    get_attempts,
    get_attempt_by_id,
    update_attempt,
    delete_attempt
)

router = APIRouter(
    prefix="/quiz-attempts",
    tags=["Quiz Attempts"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=QuizAttemptResponse)
def add_attempt(
    attempt: QuizAttemptCreate,
    db: Session = Depends(get_db)
):
    return create_attempt(db, attempt)


@router.get("", response_model=List[QuizAttemptResponse])
def list_attempts(
    db: Session = Depends(get_db)
):
    return get_attempts(db)


@router.get("/{attempt_id}", response_model=QuizAttemptResponse)
def get_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):
    attempt = get_attempt_by_id(db, attempt_id)

    if attempt is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz Attempt not found"
        )

    return attempt


@router.put("/{attempt_id}", response_model=QuizAttemptResponse)
def edit_attempt(
    attempt_id: int,
    attempt: QuizAttemptUpdate,
    db: Session = Depends(get_db)
):
    updated_attempt = update_attempt(
        db,
        attempt_id,
        attempt
    )

    if updated_attempt is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz Attempt not found"
        )

    return updated_attempt


@router.delete("/{attempt_id}")
def remove_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):
    deleted_attempt = delete_attempt(
        db,
        attempt_id
    )

    if deleted_attempt is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz Attempt not found"
        )

    return {
        "message": "Quiz Attempt deleted successfully"
    }