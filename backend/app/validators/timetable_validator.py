from app.exceptions.base_exception import BusinessException


class TimetableValidator:

    VALID_DIFFICULTIES = [
        "Easy",
        "Medium",
        "Hard"
    ]

    @staticmethod
    def validate_difficulty(level: str):

        if level not in TimetableValidator.VALID_DIFFICULTIES:
            raise BusinessException(
                "Invalid difficulty level."
            )