from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP,
    ForeignKey,
    Date,
    Boolean,
    Index
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(15))
    password_hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    status = Column(String(20), default="ACTIVE")
    role = Column(
    String(20),
    nullable=False,
    default="student"
)


class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    topics = relationship(
        "Topic",
        back_populates="subject",
        cascade="all, delete"
    )


class Topic(Base):
    __tablename__ = "topics"

    topic_id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(100), nullable=False)
    description = Column(Text)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.subject_id"),
        nullable=False
    )

    subject = relationship(
        "Subject",
        back_populates="topics"
    )


class Progress(Base):
    __tablename__ = "progress"

    progress_id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    topic_id = Column(
        Integer,
        ForeignKey("topics.topic_id"),
        nullable=False
    )

    completion_percentage = Column(Integer, default=0)

    status = Column(
        String(20),
        default="NOT_STARTED"
    )

    last_updated = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    student = relationship("Student")
    topic = relationship("Topic")
class LearningPlan(Base):
    __tablename__ = "learning_plans"

    plan_id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.subject_id"),
        nullable=False
    )

    goal = Column(Text, nullable=False)

    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)

    status = Column(String(20), default="ACTIVE")

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    student = relationship("Student")
    subject = relationship("Subject")
class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(Integer, primary_key=True, index=True)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.subject_id"),
        nullable=False
    )

    quiz_name = Column(String(100), nullable=False)

    total_questions = Column(Integer, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    subject = relationship("Subject")
class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    question_id = Column(Integer, primary_key=True, index=True)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.quiz_id"),
        nullable=False
    )

    question = Column(Text, nullable=False)

    option_a = Column(String(255), nullable=False)
    option_b = Column(String(255), nullable=False)
    option_c = Column(String(255), nullable=False)
    option_d = Column(String(255), nullable=False)

    correct_answer = Column(String(1), nullable=False)

    quiz = relationship("Quiz")
class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    attempt_id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.quiz_id"),
        nullable=False
    )

    score = Column(Integer, nullable=False)

    attempted_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    student = relationship("Student")
    quiz = relationship("Quiz")
class Achievement(Base):
    __tablename__ = "achievements"

    achievement_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    achievement_name = Column(
        String(100),
        nullable=False
    )

    description = Column(Text)

    earned_date = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    student = relationship("Student")
class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    title = Column(String(100), nullable=False)

    message = Column(Text, nullable=False)

    notification_type = Column(
        String(30),
        default="GENERAL"
    )

    is_read = Column(Boolean, default=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    student = relationship("Student")
class Recommendation(Base):
    __tablename__ = "recommendations"

    recommendation_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.subject_id"),
        nullable=False
    )

    topic_id = Column(
        Integer,
        ForeignKey("topics.topic_id"),
        nullable=True
    )

    recommendation_text = Column(
        Text,
        nullable=False
    )

    priority = Column(
        String(20),
        default="MEDIUM"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    student = relationship("Student")
    subject = relationship("Subject")
    topic = relationship("Topic")

    __table_args__ = (
        Index(
            "ix_recommendations_student_subject_topic",
            "student_id",
            "subject_id",
            "topic_id"
        ),
    )