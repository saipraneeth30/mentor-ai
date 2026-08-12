from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    NotificationCreate,
    NotificationUpdate,
    NotificationResponse
)

from app.repositories.notification_repository import (
    create_notification,
    get_notifications,
    get_notification_by_id,
    update_notification,
    delete_notification
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=NotificationResponse)
def add_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    return create_notification(db, notification)


@router.get("", response_model=List[NotificationResponse])
def list_notifications(
    db: Session = Depends(get_db)
):
    return get_notifications(db)


@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = get_notification_by_id(
        db,
        notification_id
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


@router.put("/{notification_id}", response_model=NotificationResponse)
def edit_notification(
    notification_id: int,
    notification: NotificationUpdate,
    db: Session = Depends(get_db)
):
    updated_notification = update_notification(
        db,
        notification_id,
        notification
    )

    if updated_notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return updated_notification


@router.delete("/{notification_id}")
def remove_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    deleted_notification = delete_notification(
        db,
        notification_id
    )

    if deleted_notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification deleted successfully"
    }