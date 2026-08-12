from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.auth.oauth2 import get_current_user

from app.models import (
    Student,
    Subject,
    Topic,
    Progress,
    LearningPlan,
    QuizAttempt,
    Achievement,
    Notification,
    Recommendation,
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
    dependencies=[Depends(get_current_user)]
)


@router.get("")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    # --------------------------------
    # Get logged-in student
    # --------------------------------
    student = (
        db.query(Student)
        .filter(
            Student.student_id == current_user["student_id"]
        )
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # --------------------------------
    # Get student's progress
    # --------------------------------
    progress = (
        db.query(Progress)
        .filter(
            Progress.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Calculate overall progress
    # --------------------------------
    if progress:
        overall_progress = round(
            sum(
                p.completion_percentage
                for p in progress
            ) / len(progress),
            2
        )
    else:
        overall_progress = 0

    # --------------------------------
    # Calculate subject-wise progress
    # --------------------------------
    subjects = db.query(Subject).all()

    subject_progress = []

    for subject in subjects:

        topics = (
            db.query(Topic)
            .filter(
                Topic.subject_id == subject.subject_id
            )
            .all()
        )

        topic_ids = [
            topic.topic_id
            for topic in topics
        ]

        topic_progress = [
            p for p in progress
            if p.topic_id in topic_ids
        ]

        if topic_progress:
            average_progress = (
                sum(
                    p.completion_percentage
                    for p in topic_progress
                ) / len(topic_progress)
            )
        else:
            average_progress = 0

        subject_progress.append({
            "subject_id": subject.subject_id,
            "subject_name": subject.subject_name,
            "progress_percentage": round(
                average_progress,
                2
            )
        })

    # --------------------------------
    # Get learning plans
    # --------------------------------
    learning_plans = (
        db.query(LearningPlan)
        .filter(
            LearningPlan.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Get quiz attempts
    # --------------------------------
    quiz_attempts = (
        db.query(QuizAttempt)
        .filter(
            QuizAttempt.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Calculate quiz performance
    # --------------------------------
    if quiz_attempts:

        total_attempts = len(quiz_attempts)

        average_score = round(
            sum(
                attempt.score
                for attempt in quiz_attempts
            ) / total_attempts,
            2
        )

        highest_score = max(
            attempt.score
            for attempt in quiz_attempts
        )

    else:

        total_attempts = 0
        average_score = 0
        highest_score = 0

    quiz_performance = {
        "total_attempts": total_attempts,
        "average_score": average_score,
        "highest_score": highest_score
    }

    # --------------------------------
    # Get achievements
    # --------------------------------
    achievements = (
        db.query(Achievement)
        .filter(
            Achievement.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Get notifications
    # --------------------------------
    notifications = (
        db.query(Notification)
        .filter(
            Notification.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Get recommendations
    # --------------------------------
    recommendations = (
        db.query(Recommendation)
        .filter(
            Recommendation.student_id == student.student_id
        )
        .all()
    )

    # --------------------------------
    # Dashboard response
    # --------------------------------
    return {
        "student": {
            "student_id": student.student_id,
            "full_name": student.full_name,
            "email": student.email,
            "status": student.status
        },

        "overall_progress": overall_progress,

        "subject_progress": subject_progress,

        "progress": progress,

        "learning_plans": learning_plans,

        "quiz_performance": quiz_performance,

        "quiz_attempts": quiz_attempts,

        "achievements": achievements,

        "notifications": notifications,

        "recommendations": recommendations
    }