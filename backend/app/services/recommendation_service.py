from app.database.models import (
    StudentDB,
    StudentProfileDB
)

from app.utils.logger import get_logger

logger = get_logger(__name__)


# ------------------------------------------------
# Existing FastAPI Route Support
# ------------------------------------------------
def get_recommendations(db, student_id):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if student is None:
        return None

    profile = db.query(StudentProfileDB).filter(
        StudentProfileDB.student_id == student_id
    ).first()

    if profile is None:
        return {
            "student": student.name,
            "recommendations": [
                "Complete your student profile first."
            ]
        }

    service = RecommendationService()

    recommendations = service.generate_recommendations(
        profile=profile,
        attendance_percentage=80,
        progress_percentage=60
    )

    return {
        "student": student.name,
        "goal": profile.goal,
        "recommendations": recommendations
    }


# ------------------------------------------------
# Business Layer
# ------------------------------------------------
class RecommendationService:

    def generate_recommendations(
        self,
        profile,
        attendance_percentage,
        progress_percentage
    ):

        logger.info("Generating recommendations")

        recommendations = []

        if attendance_percentage < 75:
            recommendations.append(
                "Improve your attendance."
            )

        if progress_percentage < 50:
            recommendations.append(
                "Complete more timetable tasks."
            )

        weak_subjects = [
            subject.strip()
            for subject in profile.weak_subjects.split(",")
            if subject.strip()
        ]

        for subject in weak_subjects:
            recommendations.append(
                f"Spend extra time on {subject}."
            )

        goal = profile.goal.lower()

        if goal == "gate":
            recommendations.append(
                "Practice more aptitude and core subjects."
            )

        elif goal == "placement":
            recommendations.append(
                "Practice coding and aptitude daily."
            )

        elif goal == "higher studies":
            recommendations.append(
                "Focus on maintaining a high CGPA."
            )

        if (
            attendance_percentage >= 90
            and progress_percentage >= 90
        ):
            recommendations.append(
                "Excellent performance! Attempt mock tests."
            )

        return recommendations