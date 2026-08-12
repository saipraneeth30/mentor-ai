from sqlalchemy.orm import Session
from app.models import QuizAttempt


def create_attempt(db: Session, attempt):
    db_attempt = QuizAttempt(
        student_id=attempt.student_id,
        quiz_id=attempt.quiz_id,
        score=attempt.score
    )

    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)

    return db_attempt


def get_attempts(db: Session):
    return db.query(QuizAttempt).all()
def get_attempts_by_student(
    db: Session,
    student_id: int
):
    return (
        db.query(QuizAttempt)
        .filter(
            QuizAttempt.student_id == student_id
        )
        .all()
    )

def get_attempt_by_id(db: Session, attempt_id: int):
    return (
        db.query(QuizAttempt)
        .filter(QuizAttempt.attempt_id == attempt_id)
        .first()
    )


def update_attempt(db: Session, attempt_id: int, attempt):
    db_attempt = get_attempt_by_id(db, attempt_id)

    if db_attempt is None:
        return None

    db_attempt.score = attempt.score

    db.commit()
    db.refresh(db_attempt)

    return db_attempt


def delete_attempt(db: Session, attempt_id: int):
    db_attempt = get_attempt_by_id(db, attempt_id)

    if db_attempt is None:
        return None

    db.delete(db_attempt)
    db.commit()

    return db_attempt