from app.repositories.interfaces.student_repository import StudentRepository


def get_student_repository() -> StudentRepository:
    """
    Placeholder dependency.

    The Database Team will later return the real
    SQLAlchemy repository implementation.
    """
    raise NotImplementedError(
        "StudentRepository implementation not provided yet."
    )