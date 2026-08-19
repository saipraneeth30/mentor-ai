from app.agents.timetable_agent import TimetableAgent
from app.database.models import (
    StudentDB,
    SubjectDB,
    TimetableDB,
    StudentProfileDB
)

agent = TimetableAgent()


# -----------------------------
# Generate Timetable (Old API)
# -----------------------------
def create_timetable(student):
    return {
        "message": "Use generate_student_timetable() instead."
    }


# -----------------------------
# Save Student
# -----------------------------
def save_student(db, student):

    db_student = StudentDB(
        name=student.name,
        department=student.department,
        semester=student.semester,
        study_hours=student.study_hours
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# -----------------------------
# Get All Students
# -----------------------------
def get_all_students(db):

    return db.query(StudentDB).all()


# -----------------------------
# Get Student By ID
# -----------------------------
def get_student_by_id(db, student_id):

    return db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()


# -----------------------------
# Update Student
# -----------------------------
def update_student(db, student_id, student):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db_student.name = student.name
    db_student.department = student.department
    db_student.semester = student.semester
    db_student.study_hours = student.study_hours

    db.commit()
    db.refresh(db_student)

    return db_student


# -----------------------------
# Delete Student
# -----------------------------
def delete_student(db, student_id):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }


# -----------------------------
# Add Subject
# -----------------------------
def add_subject(db, student_id, subject):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db_subject = SubjectDB(
        student_id=student_id,
        subject_name=subject.subject_name,
        difficulty=subject.difficulty
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return db_subject


# -----------------------------
# Get Student Subjects
# -----------------------------
def get_student_subjects(db, student_id):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    return db_student.subjects


# -----------------------------
# Generate Weekly AI Timetable
# -----------------------------
def generate_student_timetable(db, student_id):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return {
            "error": "Student not found"
        }

    profile = db.query(StudentProfileDB).filter(
        StudentProfileDB.student_id == student_id
    ).first()

    if profile is None:
        return {
            "error": "Student profile not found"
        }

    # Remove previous timetable
    db.query(TimetableDB).filter(
        TimetableDB.student_id == student_id
    ).delete()

    # Generate Weekly Schedule
    weekly_schedule = agent.generate_weekly_schedule(
        db_student.subjects,
        profile,
        db_student.study_hours
    )

    # Save only subject sessions
    for day, sessions in weekly_schedule.items():

        for session in sessions:

            if "subject" not in session:
                continue

            db_timetable = TimetableDB(
                student_id=student_id,
                subject=session["subject"],
                duration=session["duration"]
            )

            db.add(db_timetable)

    db.commit()

    return {
        "student": db_student.name,
        "goal": profile.goal,
        "preferred_study_time": profile.preferred_study_time,
        "study_hours": db_student.study_hours,
        "weekly_schedule": weekly_schedule
    }


# -----------------------------
# Get Saved Timetables
# -----------------------------
def get_saved_timetables(db, student_id):

    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    return db_student.timetables
# -----------------------------
# Mark Timetable as Completed
# -----------------------------
def complete_timetable(db, timetable_id):

    timetable = db.query(TimetableDB).filter(
        TimetableDB.id == timetable_id
    ).first()

    if timetable is None:
        return {
            "error": "Timetable not found"
        }

    timetable.completed = True

    db.commit()
    db.refresh(timetable)

    return {
        "message": "Study session marked as completed",
        "timetable_id": timetable.id,
        "subject": timetable.subject,
        "completed": timetable.completed
    }


# -----------------------------
# Get Student Progress
# -----------------------------
def get_student_progress(db, student_id):

    total = db.query(TimetableDB).filter(
        TimetableDB.student_id == student_id
    ).count()

    completed = db.query(TimetableDB).filter(
        TimetableDB.student_id == student_id,
        TimetableDB.completed == True
    ).count()

    pending = total - completed

    percentage = 0

    if total > 0:
        percentage = round((completed / total) * 100, 2)

    return {
        "student_id": student_id,
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage
    }