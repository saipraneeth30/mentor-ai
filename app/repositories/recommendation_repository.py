from sqlalchemy.orm import Session

from app.models import Recommendation


def create_recommendation(
    db: Session,
    recommendation
):
    db_recommendation = Recommendation(
        student_id=recommendation.student_id,
        subject_id=recommendation.subject_id,
        topic_id=getattr(
            recommendation,
            "topic_id",
            None
        ),
        recommendation_text=recommendation.recommendation_text,
        priority=recommendation.priority
    )

    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)

    return db_recommendation


def get_recommendations(
    db: Session
):
    return (
        db.query(Recommendation)
        .order_by(
            Recommendation.created_at.desc()
        )
        .all()
    )


def get_recommendations_by_student(
    db: Session,
    student_id: int
):
    return (
        db.query(Recommendation)
        .filter(
            Recommendation.student_id == student_id
        )
        .order_by(
            Recommendation.created_at.desc()
        )
        .all()
    )


def get_recommendation_by_id(
    db: Session,
    recommendation_id: int
):
    return (
        db.query(Recommendation)
        .filter(
            Recommendation.recommendation_id
            == recommendation_id
        )
        .first()
    )


def get_existing_recommendation(
    db: Session,
    student_id: int,
    subject_id: int,
    topic_id,
    recommendation_text: str
):
    return (
        db.query(Recommendation)
        .filter(
            Recommendation.student_id == student_id,
            Recommendation.subject_id == subject_id,
            Recommendation.topic_id == topic_id,
            Recommendation.recommendation_text
            == recommendation_text
        )
        .first()
    )


def update_recommendation(
    db: Session,
    recommendation_id: int,
    recommendation
):
    db_recommendation = get_recommendation_by_id(
        db,
        recommendation_id
    )

    if db_recommendation is None:
        return None

    db_recommendation.recommendation_text = (
        recommendation.recommendation_text
    )

    db_recommendation.priority = (
        recommendation.priority
    )

    if hasattr(recommendation, "topic_id"):
        db_recommendation.topic_id = (
            recommendation.topic_id
        )

    db.commit()
    db.refresh(db_recommendation)

    return db_recommendation


def delete_recommendation(
    db: Session,
    recommendation_id: int
):
    db_recommendation = get_recommendation_by_id(
        db,
        recommendation_id
    )

    if db_recommendation is None:
        return None

    db.delete(db_recommendation)
    db.commit()

    return db_recommendation