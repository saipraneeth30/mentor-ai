from sqlalchemy.orm import Session
from app.models import LearningPlan


def create_learning_plan(db: Session, plan):
    db_plan = LearningPlan(
        student_id=plan.student_id,
        subject_id=plan.subject_id,
        goal=plan.goal,
        start_date=plan.start_date,
        end_date=plan.end_date,
        status=plan.status
    )

    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)

    return db_plan


def get_learning_plans(db: Session):
    return db.query(LearningPlan).all()


def get_learning_plan_by_id(db: Session, plan_id: int):
    return (
        db.query(LearningPlan)
        .filter(LearningPlan.plan_id == plan_id)
        .first()
    )


def update_learning_plan(db: Session, plan_id: int, plan):
    db_plan = get_learning_plan_by_id(db, plan_id)

    if db_plan is None:
        return None

    db_plan.goal = plan.goal
    db_plan.start_date = plan.start_date
    db_plan.end_date = plan.end_date
    db_plan.status = plan.status

    db.commit()
    db.refresh(db_plan)

    return db_plan


def delete_learning_plan(db: Session, plan_id: int):
    db_plan = get_learning_plan_by_id(db, plan_id)

    if db_plan is None:
        return None

    db.delete(db_plan)
    db.commit()

    return db_plan