from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user
from app.dependencies import get_db
from app.services.recommendation_service import generate_recommendations
from app.schemas import (
    RecommendationCreate,
    RecommendationUpdate,
    RecommendationResponse
)
from app.models import (
    Student,
    Progress,
    Topic,
    QuizAttempt
)

from app.services.ai_recommendation_service import (
    generate_ai_recommendation
)
from app.repositories.recommendation_repository import (
    create_recommendation,
    get_recommendations,
    get_recommendation_by_id,
    update_recommendation,
    delete_recommendation
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
    dependencies=[Depends(get_current_user)]
)


@router.post("", response_model=RecommendationResponse)
def add_recommendation(
    recommendation: RecommendationCreate,
    db: Session = Depends(get_db)
):
    return create_recommendation(db, recommendation)


@router.get("", response_model=List[RecommendationResponse])
def list_recommendations(
    db: Session = Depends(get_db)
):
    return get_recommendations(db)


@router.get("/{recommendation_id}", response_model=RecommendationResponse)
def get_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db)
):
    recommendation = get_recommendation_by_id(
        db,
        recommendation_id
    )

    if recommendation is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found"
        )

    return recommendation


@router.put("/{recommendation_id}", response_model=RecommendationResponse)
def edit_recommendation(
    recommendation_id: int,
    recommendation: RecommendationUpdate,
    db: Session = Depends(get_db)
):
    updated = update_recommendation(
        db,
        recommendation_id,
        recommendation
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found"
        )

    return updated


@router.delete("/{recommendation_id}")
def remove_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_recommendation(
        db,
        recommendation_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found"
        )

    return {
        "message": "Recommendation deleted successfully"
    }
@router.post("/generate")
def generate_student_recommendations(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    student_id = current_user["student_id"]

    recommendations = generate_recommendations(
        db,
        student_id
    )

    return {
        "message": "Recommendations generated successfully",
        "recommendations": recommendations
    }
@router.post("/ai-generate")
def generate_ai_student_recommendation(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    student_id = current_user["student_id"]

    # -------------------------------
    # Get student
    # -------------------------------
    student = (
        db.query(Student)
        .filter(
            Student.student_id == student_id
        )
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -------------------------------
    # Get progress
    # -------------------------------
    progress_records = (
        db.query(Progress)
        .filter(
            Progress.student_id == student_id
        )
        .all()
    )

    if progress_records:

        overall_progress = round(
            sum(
                p.completion_percentage
                for p in progress_records
            ) / len(progress_records),
            2
        )

    else:
        overall_progress = 0

    # -------------------------------
    # Find weak topics
    # -------------------------------
    weak_topics = []

    for progress in progress_records:

        if progress.completion_percentage >= 40:
            continue

        topic = (
            db.query(Topic)
            .filter(
                Topic.topic_id == progress.topic_id
            )
            .first()
        )

        if topic:

            weak_topics.append({
                "topic_id": topic.topic_id,
                "topic_name": topic.topic_name,
                "completion": progress.completion_percentage
            })

    # -------------------------------
    # Get quiz attempts
    # -------------------------------
    quiz_attempts = (
        db.query(QuizAttempt)
        .filter(
            QuizAttempt.student_id == student_id
        )
        .all()
    )

    if quiz_attempts:

        average_quiz_score = round(
            sum(
                attempt.score
                for attempt in quiz_attempts
            ) / len(quiz_attempts),
            2
        )

    else:
        average_quiz_score = None

    # -------------------------------
    # Generate AI recommendation
    # -------------------------------
    ai_recommendation = generate_ai_recommendation(
        student_name=student.full_name,
        overall_progress=overall_progress,
        weak_topics=weak_topics,
        average_quiz_score=average_quiz_score
    )

    return {
        "student_id": student_id,
        "student_name": student.full_name,
        "overall_progress": overall_progress,
        "average_quiz_score": average_quiz_score,
        "weak_topics": weak_topics,
        "ai_recommendation": ai_recommendation
    }