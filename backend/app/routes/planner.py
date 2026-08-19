from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.student_create import StudentCreate
from app.models.subject import Subject

from app.database.session import get_db

from app.services.planner_service import (
    create_timetable,
    save_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
    add_subject,
    get_student_subjects,
    generate_student_timetable,
    get_saved_timetables,
    complete_timetable,
    get_student_progress
)

router = APIRouter()


# -----------------------------
# Create Student
# -----------------------------
@router.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    return save_student(db, student)


# -----------------------------
# Add Subject
# -----------------------------
@router.post("/students/{student_id}/subjects")
def create_subject(
    student_id: int,
    subject: Subject,
    db: Session = Depends(get_db)
):

    new_subject = add_subject(db, student_id, subject)

    if new_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return new_subject


# -----------------------------
# Get Student Subjects
# -----------------------------
@router.get("/students/{student_id}/subjects")
def get_subjects(
    student_id: int,
    db: Session = Depends(get_db)
):

    subjects = get_student_subjects(db, student_id)

    if subjects is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return subjects


# -----------------------------
# Generate Weekly Timetable
# -----------------------------
@router.post("/students/{student_id}/generate-timetable")
def generate_db_timetable(
    student_id: int,
    db: Session = Depends(get_db)
):

    timetable = generate_student_timetable(db, student_id)

    if timetable is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return timetable


# -----------------------------
# Get Saved Timetables
# -----------------------------
@router.get("/students/{student_id}/timetables")
def get_timetables(
    student_id: int,
    db: Session = Depends(get_db)
):

    timetables = get_saved_timetables(db, student_id)

    if timetables is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return timetables


# -----------------------------
# Complete Study Session
# -----------------------------
@router.put("/timetable/{timetable_id}/complete")
def complete_session(
    timetable_id: int,
    db: Session = Depends(get_db)
):

    return complete_timetable(
        db,
        timetable_id
    )


# -----------------------------
# Student Progress
# -----------------------------
@router.get("/students/{student_id}/progress")
def student_progress(
    student_id: int,
    db: Session = Depends(get_db)
):

    return get_student_progress(
        db,
        student_id
    )


# -----------------------------
# Old Timetable API
# -----------------------------
@router.post("/generate-timetable")
def generate_timetable(
    student: Student,
    db: Session = Depends(get_db)
):

    save_student(db, student)

    timetable = create_timetable(student)

    return {
        "student": student.name,
        "study_hours": student.study_hours,
        "timetable": timetable
    }


# -----------------------------
# Get All Students
# -----------------------------
@router.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    return get_all_students(db)


# -----------------------------
# Get Student By ID
# -----------------------------
@router.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# -----------------------------
# Update Student
# -----------------------------
@router.put("/students/{student_id}")
def edit_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    updated_student = update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# -----------------------------
# Delete Student
# -----------------------------
@router.delete("/students/{student_id}")
def remove_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    deleted_student = delete_student(
        db,
        student_id
    )

    if deleted_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return deleted_student