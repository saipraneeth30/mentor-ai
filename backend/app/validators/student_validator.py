from app.exceptions.base_exception import BusinessException


class StudentValidator:

    @staticmethod
    def validate_study_hours(study_hours: int):

        if study_hours < 1:
            raise BusinessException(
                "Study hours must be at least 1 hour."
            )

        if study_hours > 12:
            raise BusinessException(
                "Study hours cannot exceed 12 hours per day."
            )