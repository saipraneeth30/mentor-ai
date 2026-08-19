from app.exceptions.base_exception import BusinessException


class ProfileValidator:

    VALID_GOALS = [
        "Placement",
        "GATE",
        "Higher Studies"
    ]

    @staticmethod
    def validate_goal(goal: str):

        if goal not in ProfileValidator.VALID_GOALS:
            raise BusinessException(
                "Invalid learning goal."
            )

    @staticmethod
    def validate_target_cgpa(cgpa: float):

        if cgpa < 0 or cgpa > 10:
            raise BusinessException(
                "Target CGPA must be between 0 and 10."
            )