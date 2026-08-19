from sqlalchemy import func

from app.database.models import StudentDB, SubjectDB, TimetableDB
from app.utils.logger import get_logger

logger = get_logger(__name__)


# ------------------------------------------------
# Existing FastAPI Route Support
# ------------------------------------------------
def get_dashboard(db):

    total_students = db.query(StudentDB).count()

    total_subjects = db.query(SubjectDB).count()

    total_timetables = db.query(TimetableDB).count()

    average_study_hours = db.query(
        func.avg(StudentDB.study_hours)
    ).scalar()

    if average_study_hours is None:
        average_study_hours = 0
    else:
        average_study_hours = round(average_study_hours, 2)

    most_studied_subject = (
        db.query(
            SubjectDB.subject_name,
            func.count(SubjectDB.id).label("total")
        )
        .group_by(SubjectDB.subject_name)
        .order_by(func.count(SubjectDB.id).desc())
        .first()
    )

    subject_name = (
        most_studied_subject.subject_name
        if most_studied_subject
        else "No Subjects"
    )

    return {
        "total_students": total_students,
        "total_subjects": total_subjects,
        "total_timetables": total_timetables,
        "average_study_hours": average_study_hours,
        "most_studied_subject": subject_name
    }


# ------------------------------------------------
# New Business Layer
# ------------------------------------------------
class DashboardService:

    def get_dashboard_summary(
        self,
        student_name,
        attendance_percentage,
        progress_percentage,
        recommendation_count
    ):

        productivity_score = round(
            (attendance_percentage + progress_percentage) / 2,
            2
        )

        return {
            "student": student_name,
            "attendance_percentage": attendance_percentage,
            "progress_percentage": progress_percentage,
            "recommendations": recommendation_count,
            "productivity_score": productivity_score
        }