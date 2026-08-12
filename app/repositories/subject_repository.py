from sqlalchemy.orm import Session
from app.models import Subject

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models import Subject

def create_subject(db, subject):
    db_subject = Subject(
        subject_name=subject.subject_name,
        description=subject.description
    )

    db.add(db_subject)

    try:
        db.commit()
        db.refresh(db_subject)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Subject already exists"
        )

    return db_subject


def get_subjects(db: Session):
    return db.query(Subject).all()


def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(
        Subject.subject_id == subject_id
    ).first()


def update_subject(db: Session, subject_id: int, subject):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db_subject.subject_name = subject.subject_name
    db_subject.description = subject.description

    db.commit()
    db.refresh(db_subject)

    return db_subject


def delete_subject(db: Session, subject_id: int):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db.delete(db_subject)
    db.commit()

    return db_subject