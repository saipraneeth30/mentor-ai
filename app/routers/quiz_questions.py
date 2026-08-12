from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    QuizQuestionCreate,
    QuizQuestionUpdate,
    QuizQuestionResponse
)

from app.repositories.quiz_question_repository import (
    create_question,
    get_questions,
    get_question_by_id,
    update_question,
    delete_question
)

router = APIRouter(
    prefix="/quiz-questions",
    tags=["Quiz Questions"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=QuizQuestionResponse)
def add_question(
    question: QuizQuestionCreate,
    db: Session = Depends(get_db)
):
    return create_question(db, question)


@router.get("", response_model=List[QuizQuestionResponse])
def list_questions(
    db: Session = Depends(get_db)
):
    return get_questions(db)


@router.get("/{question_id}", response_model=QuizQuestionResponse)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = get_question_by_id(db, question_id)

    if question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return question


@router.put("/{question_id}", response_model=QuizQuestionResponse)
def edit_question(
    question_id: int,
    question: QuizQuestionUpdate,
    db: Session = Depends(get_db)
):
    updated_question = update_question(
        db,
        question_id,
        question
    )

    if updated_question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return updated_question


@router.delete("/{question_id}")
def remove_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    deleted_question = delete_question(
        db,
        question_id
    )

    if deleted_question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return {
        "message": "Question deleted successfully"
    }