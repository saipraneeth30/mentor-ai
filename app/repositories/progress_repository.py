from sqlalchemy.orm import Session
from app.models import Progress


def create_progress(db: Session, progress):
    db_progress = Progress(
        student_id=progress.student_id,
        topic_id=progress.topic_id,
        completion_percentage=progress.completion_percentage,
        status=progress.status
    )

    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)

    return db_progress


def get_progress(db: Session):
    return db.query(Progress).all()

def get_progress_by_student(
    db: Session,
    student_id: int
):
    return (
        db.query(Progress)
        .filter(
            Progress.student_id == student_id
        )
        .all()
    )


def get_progress_by_id(db: Session, progress_id: int):
    return (
        db.query(Progress)
        .filter(Progress.progress_id == progress_id)
        .first()
    )


def update_progress(
    db: Session,
    progress_id: int,
    progress
):
    db_progress = get_progress_by_id(
        db,
        progress_id
    )

    if db_progress is None:
        return None

    db_progress.completion_percentage = (
        progress.completion_percentage
    )

    db_progress.status = progress.status

    db.commit()
    db.refresh(db_progress)

    return db_progress


def delete_progress(
    db: Session,
    progress_id: int
):
    db_progress = get_progress_by_id(
        db,
        progress_id
    )

    if db_progress is None:
        return None

    db.delete(db_progress)
    db.commit()

    return db_progress