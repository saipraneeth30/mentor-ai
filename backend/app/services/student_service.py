from app.repositories.interfaces.student_repository import StudentRepository
from app.utils.logger import get_logger

logger = get_logger(__name__)


class StudentService:

    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def create_student(self, student):

        logger.info("Creating a new student")

        return self.student_repository.create_student(student)

    def get_student(self, student_id: int):

        logger.info(f"Fetching student with ID {student_id}")

        return self.student_repository.get_student_by_id(student_id)

    def get_all_students(self):

        logger.info("Fetching all students")

        return self.student_repository.get_all_students()

    def update_student(self, student_id: int, student):

        logger.info(f"Updating student with ID {student_id}")

        return self.student_repository.update_student(student_id, student)

    def delete_student(self, student_id: int):

        logger.info(f"Deleting student with ID {student_id}")

        return self.student_repository.delete_student(student_id)