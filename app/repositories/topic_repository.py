from sqlalchemy.orm import Session
from app.models import Topic


def create_topic(db: Session, topic):
    db_topic = Topic(
        topic_name=topic.topic_name,
        description=topic.description,
        subject_id=topic.subject_id
    )

    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)

    return db_topic


def get_topics(db: Session):
    return db.query(Topic).all()


def get_topic_by_id(db: Session, topic_id: int):
    return db.query(Topic).filter(
        Topic.topic_id == topic_id
    ).first()


def update_topic(db: Session, topic_id: int, topic):
    db_topic = get_topic_by_id(db, topic_id)

    if db_topic is None:
        return None

    db_topic.topic_name = topic.topic_name
    db_topic.description = topic.description
    db_topic.subject_id = topic.subject_id

    db.commit()
    db.refresh(db_topic)

    return db_topic


def delete_topic(db: Session, topic_id: int):
    db_topic = get_topic_by_id(db, topic_id)

    if db_topic is None:
        return None

    db.delete(db_topic)
    db.commit()

    return db_topic