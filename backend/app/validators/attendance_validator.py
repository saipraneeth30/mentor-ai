from app.exceptions.base_exception import BusinessException


class AttendanceValidator:

    @staticmethod
    def validate_percentage(percentage: float):

        if percentage < 0 or percentage > 100:
            raise BusinessException(
                "Attendance percentage must be between 0 and 100."
            )