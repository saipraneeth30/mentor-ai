from sqlalchemy.orm import Session
from app.models import Student
from app.models import Student, Subject
from app.models import Student, Subject


def create_student(db: Session, student):
    db_student = Student(
        full_name=student.full_name,
        email=student.email,
        phone_number=student.phone_number,
        password_hash=student.password
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
    db_student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if db_student is None:
        return None

    db_student.full_name = student.full_name
    db_student.email = student.email
    db_student.phone_number = student.phone_number
    db_student.password_hash = student.password
    db_student.status = student.status

    db.commit()
    db.refresh(db_student)

    return db_student
def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student
def create_subject(db: Session, subject):
    db_subject = Subject(
        subject_name=subject.subject_name,
        description=subject.description
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return db_subject
def get_subjects(db: Session):
    return db.query(Subject).all()
def get_subject_by_id(db: Session, subject_id: int):
    return (
        db.query(Subject)
        .filter(Subject.subject_id == subject_id)
        .first()
    )
def update_subject(db: Session, subject_id: int, subject):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db_subject.subject_name = subject.subject_name
    db_subject.description = subject.description

    db.commit()
    db.refresh(db_subject)

    return db_subject
def delete_subject(db: Session, subject_id: int):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db.delete(db_subject)
    db.commit()

    return db_subject
def create_subject(db: Session, subject):
    db_subject = Subject(
        subject_name=subject.subject_name,
        description=subject.description
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return db_subject
def get_subjects(db: Session):
    return db.query(Subject).all()
def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(
        Subject.subject_id == subject_id
    ).first()
def create_subject(db: Session, subject):
    db_subject = Subject(
        subject_name=subject.subject_name,
        description=subject.description
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return db_subject
def get_subjects(db: Session):
    return db.query(Subject).all()
def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(
        Subject.subject_id == subject_id
    ).first()
def update_subject(db: Session, subject_id: int, subject):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db_subject.subject_name = subject.subject_name
    db_subject.description = subject.description

    db.commit()
    db.refresh(db_subject)

    return db_subject
def delete_subject(db: Session, subject_id: int):
    db_subject = get_subject_by_id(db, subject_id)

    if db_subject is None:
        return None

    db.delete(db_subject)
    db.commit()

    return db_subject