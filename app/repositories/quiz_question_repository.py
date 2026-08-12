from sqlalchemy.orm import Session
from app.models import QuizQuestion


def create_question(db: Session, question):
    db_question = QuizQuestion(
        quiz_id=question.quiz_id,
        question=question.question,
        option_a=question.option_a,
        option_b=question.option_b,
        option_c=question.option_c,
        option_d=question.option_d,
        correct_answer=question.correct_answer
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def get_questions(db: Session):
    return db.query(QuizQuestion).all()


def get_question_by_id(db: Session, question_id: int):
    return db.query(QuizQuestion).filter(
        QuizQuestion.question_id == question_id
    ).first()


def update_question(db: Session, question_id: int, question):
    db_question = get_question_by_id(db, question_id)

    if db_question is None:
        return None

    db_question.question = question.question
    db_question.option_a = question.option_a
    db_question.option_b = question.option_b
    db_question.option_c = question.option_c
    db_question.option_d = question.option_d
    db_question.correct_answer = question.correct_answer

    db.commit()
    db.refresh(db_question)

    return db_question


def delete_question(db: Session, question_id: int):
    db_question = get_question_by_id(db, question_id)

    if db_question is None:
        return None

    db.delete(db_question)
    db.commit()

    return db_question