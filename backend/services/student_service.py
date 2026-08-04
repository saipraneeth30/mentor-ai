from backend.schemas.student import StudentRegistration
from backend.schemas.dashboard import DashboardResponse
from backend.schemas.progress import ProgressResponse
from backend.schemas.settings import SettingsResponse


class StudentService:

    @staticmethod
    def register_student(student: StudentRegistration):

        return {
            "success": True,
            "message": "Student Registered Successfully",
            "student": student.model_dump()
        }

    @staticmethod
    def get_dashboard():

        dashboard = DashboardResponse(
            goal="GATE CSE 2027",
            study_streak=5,
            study_hours=20,
            quiz_accuracy=82,
            current_subject="Data Structures"
        )

        return {
            "success": True,
            "dashboard": dashboard.model_dump()
        }

    @staticmethod
    def get_progress():

        progress = ProgressResponse(
            study_streak=5,
            study_hours=24,
            completed_topics=18,
            quiz_accuracy=82,
            goal_progress=34,
            achievement="🥇 Consistent Learner"
        )

        return {
            "success": True,
            "progress": progress.model_dump()
        }

    @staticmethod
    def get_settings():

        settings = SettingsResponse(
            goal="GATE CSE 2027",
            level="Beginner",
            daily_study_hours=4,
            preferred_study_time="Evening",
            target_exam="February 2027"
        )

        return {
            "success": True,
            "settings": settings.model_dump()
        }