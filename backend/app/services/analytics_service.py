from app.database.models import (
    StudentDB,
    TimetableDB
)


def get_student_analytics(db, student_id):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if student is None:
        return None

    analytics = []

    subjects = set()

    timetables = db.query(TimetableDB).filter(
        TimetableDB.student_id == student_id
    ).all()

    for timetable in timetables:
        subjects.add(timetable.subject)

    for subject in subjects:

        total_sessions = db.query(TimetableDB).filter(
            TimetableDB.student_id == student_id,
            TimetableDB.subject == subject
        ).count()

        completed_sessions = db.query(TimetableDB).filter(
            TimetableDB.student_id == student_id,
            TimetableDB.subject == subject,
            TimetableDB.completed == True
        ).count()

        pending_sessions = total_sessions - completed_sessions

        if total_sessions == 0:
            completion_percentage = 0
        else:
            completion_percentage = round(
                (completed_sessions / total_sessions) * 100,
                2
            )

        analytics.append({
            "subject": subject,
            "total_sessions": total_sessions,
            "completed_sessions": completed_sessions,
            "pending_sessions": pending_sessions,
            "completion_percentage": completion_percentage
        })

    return {
        "student": student.name,
        "analytics": analytics
    }