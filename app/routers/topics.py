from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.dependencies import get_db
from app.auth.oauth2 import get_current_user
from app.auth.roles import require_admin

from app.schemas import (
    TopicCreate,
    TopicResponse,
    TopicUpdate
)

from app.repositories.topic_repository import (
    create_topic,
    get_topics,
    get_topic_by_id,
    update_topic,
    delete_topic
)


router = APIRouter(
    prefix="/topics",
    tags=["Topics"],
    dependencies=[Depends(get_current_user)]
)


# ==========================
# Create Topic - Admin Only
# ==========================
@router.post("", response_model=TopicResponse)
def add_topic(
    topic: TopicCreate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    return create_topic(db, topic)


# ==========================
# Get All Topics
# ==========================
@router.get("", response_model=List[TopicResponse])
def list_topics(
    db: Session = Depends(get_db)
):
    return get_topics(db)


# ==========================
# Get Topic By ID
# ==========================
@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(
    topic_id: int,
    db: Session = Depends(get_db)
):
    topic = get_topic_by_id(db, topic_id)

    if topic is None:
        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )

    return topic


# ==========================
# Update Topic - Admin Only
# ==========================
@router.put("/{topic_id}", response_model=TopicResponse)
def edit_topic(
    topic_id: int,
    topic: TopicUpdate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    updated_topic = update_topic(
        db,
        topic_id,
        topic
    )

    if updated_topic is None:
        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )

    return updated_topic


# ==========================
# Delete Topic - Admin Only
# ==========================
@router.delete("/{topic_id}")
def remove_topic(
    topic_id: int,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db)
):
    deleted_topic = delete_topic(
        db,
        topic_id
    )

    if deleted_topic is None:
        raise HTTPException(
            status_code=404,
            detail="Topic not found"
        )

    return {
        "message": "Topic deleted successfully"
    }