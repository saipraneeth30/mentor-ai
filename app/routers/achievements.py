from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    AchievementCreate,
    AchievementUpdate,
    AchievementResponse
)

from app.repositories.achievement_repository import (
    create_achievement,
    get_achievements,
    get_achievement_by_id,
    update_achievement,
    delete_achievement
)

router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=AchievementResponse)
def add_achievement(
    achievement: AchievementCreate,
    db: Session = Depends(get_db)
):
    return create_achievement(db, achievement)


@router.get("", response_model=List[AchievementResponse])
def list_achievements(
    db: Session = Depends(get_db)
):
    return get_achievements(db)


@router.get("/{achievement_id}", response_model=AchievementResponse)
def get_achievement(
    achievement_id: int,
    db: Session = Depends(get_db)
):
    achievement = get_achievement_by_id(db, achievement_id)

    if achievement is None:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found"
        )

    return achievement


@router.put("/{achievement_id}", response_model=AchievementResponse)
def edit_achievement(
    achievement_id: int,
    achievement: AchievementUpdate,
    db: Session = Depends(get_db)
):
    updated = update_achievement(
        db,
        achievement_id,
        achievement
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found"
        )

    return updated


@router.delete("/{achievement_id}")
def remove_achievement(
    achievement_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_achievement(
        db,
        achievement_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found"
        )

    return {
        "message": "Achievement deleted successfully"
    }