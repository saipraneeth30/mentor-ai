from sqlalchemy.orm import Session
from app.models import Achievement


def create_achievement(db: Session, achievement):
    db_achievement = Achievement(
        student_id=achievement.student_id,
        achievement_name=achievement.achievement_name,
        description=achievement.description
    )

    db.add(db_achievement)
    db.commit()
    db.refresh(db_achievement)

    return db_achievement


def get_achievements(db: Session):
    return db.query(Achievement).all()


def get_achievement_by_id(db: Session, achievement_id: int):
    return (
        db.query(Achievement)
        .filter(Achievement.achievement_id == achievement_id)
        .first()
    )


def update_achievement(db: Session, achievement_id: int, achievement):
    db_achievement = get_achievement_by_id(db, achievement_id)

    if db_achievement is None:
        return None

    db_achievement.achievement_name = achievement.achievement_name
    db_achievement.description = achievement.description

    db.commit()
    db.refresh(db_achievement)

    return db_achievement


def delete_achievement(db: Session, achievement_id: int):
    db_achievement = get_achievement_by_id(db, achievement_id)

    if db_achievement is None:
        return None

    db.delete(db_achievement)
    db.commit()

    return db_achievement