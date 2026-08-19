from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from app.database.connection import Base


class StudentDB(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    semester = Column(Integer)
    study_hours = Column(Integer)

    # One Student -> Many Subjects
    subjects = relationship(
        "SubjectDB",
        back_populates="student",
        cascade="all, delete"
    )

    # One Student -> Many Timetables
    timetables = relationship(
        "TimetableDB",
        back_populates="student",
        cascade="all, delete"
    )

    # One Student -> One Profile
    profile = relationship(
        "StudentProfileDB",
        back_populates="student",
        uselist=False,
        cascade="all, delete"
    )


class SubjectDB(Base):

    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    subject_name = Column(String)

    difficulty = Column(String)

    student = relationship(
        "StudentDB",
        back_populates="subjects"
    )


class TimetableDB(Base):

    __tablename__ = "timetables"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    subject = Column(String)

    duration = Column(String)

    # NEW COLUMN
    completed = Column(Boolean, default=False)

    student = relationship(
        "StudentDB",
        back_populates="timetables"
    )


class StudentProfileDB(Base):

    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True
    )

    goal = Column(String)

    target_cgpa = Column(Float)

    weak_subjects = Column(String)

    strong_subjects = Column(String)

    preferred_study_time = Column(String)

    learning_style = Column(String)

    student = relationship(
        "StudentDB",
        back_populates="profile"
    )