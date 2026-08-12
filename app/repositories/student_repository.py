from sqlalchemy.orm import Session
from app.models import Student
from app.auth.hashing import hash_password


def create_student(db: Session, student):
    db_student = Student(
    full_name=student.full_name,
    email=student.email,
    phone_number=student.phone_number,
    password_hash=hash_password(student.password),
    role=student.role
)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(
        Student.student_id == student_id
    ).first()


def update_student(db: Session, student_id: int, student):
    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db_student.full_name = student.full_name
    db_student.email = student.email
    db_student.phone_number = student.phone_number

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student_by_id(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student