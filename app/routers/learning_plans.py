from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db

from app.schemas import (
    LearningPlanCreate,
    LearningPlanUpdate,
    LearningPlanResponse
)

from app.repositories.learning_plan_repository import (
    create_learning_plan,
    get_learning_plans,
    get_learning_plan_by_id,
    update_learning_plan,
    delete_learning_plan
)

router = APIRouter(
    prefix="/learning-plans",
    tags=["Learning Plans"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=LearningPlanResponse)
def add_learning_plan(
    plan: LearningPlanCreate,
    db: Session = Depends(get_db)
):
    return create_learning_plan(db, plan)


@router.get("", response_model=List[LearningPlanResponse])
def list_learning_plans(
    db: Session = Depends(get_db)
):
    return get_learning_plans(db)


@router.get("/{plan_id}", response_model=LearningPlanResponse)
def get_learning_plan(
    plan_id: int,
    db: Session = Depends(get_db)
):
    plan = get_learning_plan_by_id(db, plan_id)

    if plan is None:
        raise HTTPException(
            status_code=404,
            detail="Learning Plan not found"
        )

    return plan


@router.put("/{plan_id}", response_model=LearningPlanResponse)
def edit_learning_plan(
    plan_id: int,
    plan: LearningPlanUpdate,
    db: Session = Depends(get_db)
):
    updated_plan = update_learning_plan(
        db,
        plan_id,
        plan
    )

    if updated_plan is None:
        raise HTTPException(
            status_code=404,
            detail="Learning Plan not found"
        )

    return updated_plan


@router.delete("/{plan_id}")
def remove_learning_plan(
    plan_id: int,
    db: Session = Depends(get_db)
):
    deleted_plan = delete_learning_plan(
        db,
        plan_id
    )

    if deleted_plan is None:
        raise HTTPException(
            status_code=404,
            detail="Learning Plan not found"
        )

    return {
        "message": "Learning Plan deleted successfully"
    }