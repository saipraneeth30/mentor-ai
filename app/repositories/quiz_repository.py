from sqlalchemy.orm import Session
from app.models import Quiz


def create_quiz(db: Session, quiz):
    db_quiz = Quiz(
        subject_id=quiz.subject_id,
        quiz_name=quiz.quiz_name,
        total_questions=quiz.total_questions
    )

    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def get_quizzes(db: Session):
    return db.query(Quiz).all()


def get_quiz_by_id(db: Session, quiz_id: int):
    return (
        db.query(Quiz)
        .filter(Quiz.quiz_id == quiz_id)
        .first()
    )


def update_quiz(db: Session, quiz_id: int, quiz):
    db_quiz = get_quiz_by_id(db, quiz_id)

    if db_quiz is None:
        return None

    db_quiz.quiz_name = quiz.quiz_name
    db_quiz.total_questions = quiz.total_questions

    db.commit()
    db.refresh(db_quiz)

    return db_quiz


def delete_quiz(db: Session, quiz_id: int):
    db_quiz = get_quiz_by_id(db, quiz_id)

    if db_quiz is None:
        return None

    db.delete(db_quiz)
    db.commit()

    return db_quiz