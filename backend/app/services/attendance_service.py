from app.repositories.interfaces.attendance_repository import AttendanceRepository
from app.validators.attendance_validator import AttendanceValidator
from app.utils.logger import get_logger
from app.exceptions.attendance_exceptions import AttendanceNotFoundException

logger = get_logger(__name__)


class AttendanceService:
    """
    Business Service for Attendance operations.
    """

    def __init__(self, attendance_repository: AttendanceRepository):
        self.attendance_repository = attendance_repository

    def mark_attendance(self, attendance):

        logger.info("Marking attendance")

        return self.attendance_repository.mark_attendance(
            attendance
        )

    def get_attendance(self, student_id: int):

        logger.info(
            f"Fetching attendance for student {student_id}"
        )

        attendance = self.attendance_repository.get_attendance(
            student_id
        )

        if attendance is None:
            raise AttendanceNotFoundException()

        return attendance

    def get_attendance_percentage(
        self,
        student_id: int
    ):

        logger.info(
            f"Calculating attendance percentage for {student_id}"
        )

        percentage = self.attendance_repository.get_attendance_percentage(
            student_id
        )

        AttendanceValidator.validate_percentage(
            percentage
        )

        return percentage