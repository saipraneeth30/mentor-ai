from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    QuizCreate,
    QuizUpdate,
    QuizResponse
)

from app.repositories.quiz_repository import (
    create_quiz,
    get_quizzes,
    get_quiz_by_id,
    update_quiz,
    delete_quiz
)

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=QuizResponse)
def add_quiz(
    quiz: QuizCreate,
    db: Session = Depends(get_db)
):
    return create_quiz(db, quiz)


@router.get("", response_model=List[QuizResponse])
def list_quizzes(db: Session = Depends(get_db)):
    return get_quizzes(db)


@router.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz(
    quiz_id: int,
    db: Session = Depends(get_db)
):
    quiz = get_quiz_by_id(db, quiz_id)

    if quiz is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    return quiz


@router.put("/{quiz_id}", response_model=QuizResponse)
def edit_quiz(
    quiz_id: int,
    quiz: QuizUpdate,
    db: Session = Depends(get_db)
):
    updated_quiz = update_quiz(
        db,
        quiz_id,
        quiz
    )

    if updated_quiz is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    return updated_quiz


@router.delete("/{quiz_id}")
def remove_quiz(
    quiz_id: int,
    db: Session = Depends(get_db)
):
    deleted_quiz = delete_quiz(db, quiz_id)

    if deleted_quiz is None:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    return {
        "message": "Quiz deleted successfully"
    }