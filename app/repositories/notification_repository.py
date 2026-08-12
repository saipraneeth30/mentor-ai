from sqlalchemy.orm import Session
from app.models import Notification


def create_notification(db: Session, notification):
    db_notification = Notification(
        student_id=notification.student_id,
        title=notification.title,
        message=notification.message,
        notification_type=notification.notification_type
    )

    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    return db_notification


def get_notifications(db: Session):
    return db.query(Notification).all()


def get_notification_by_id(db: Session, notification_id: int):
    return (
        db.query(Notification)
        .filter(Notification.notification_id == notification_id)
        .first()
    )


def update_notification(
    db: Session,
    notification_id: int,
    notification
):
    db_notification = get_notification_by_id(
        db,
        notification_id
    )

    if db_notification is None:
        return None

    db_notification.title = notification.title
    db_notification.message = notification.message
    db_notification.notification_type = notification.notification_type
    db_notification.is_read = notification.is_read

    db.commit()
    db.refresh(db_notification)

    return db_notification


def delete_notification(
    db: Session,
    notification_id: int
):
    db_notification = get_notification_by_id(
        db,
        notification_id
    )

    if db_notification is None:
        return None

    db.delete(db_notification)
    db.commit()

    return db_notification