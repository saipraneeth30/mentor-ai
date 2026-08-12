from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.oauth2 import get_current_user

from app.schemas import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)

from app.dependencies import get_db

from app.repositories.student_repository import (
    create_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"],
    dependencies=[Depends(get_current_user)]
)


@router.post("")
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = create_student(db, student)

    return {
        "message": "Student Registered Successfully",
        "student_id": new_student.student_id,
        "name": new_student.full_name,
        "email": new_student.email
    }


@router.get("", response_model=List[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
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


@router.put("/{student_id}", response_model=StudentResponse)
def edit_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    updated_student = update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


@router.delete("/{student_id}")
def remove_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = delete_student(db, student_id)

    if deleted_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }