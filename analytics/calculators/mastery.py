def calculate_mastery(assessment_score: float, practice_score: float) -> float:
    """
    Calculate a student's mastery score.

    The mastery score is the average of the assessment
    and practice scores.

    Args:
        assessment_score: Assessment score between 0 and 100.
        practice_score: Practice score between 0 and 100.

    Returns:
        Mastery score between 0 and 100.
    """

    if not 0 <= assessment_score <= 100:
        raise ValueError(
            f"assessment_score must be between 0 and 100. Got: {assessment_score}"
        )

    if not 0 <= practice_score <= 100:
        raise ValueError(
            f"practice_score must be between 0 and 100. Got: {practice_score}"
        )

    mastery = (assessment_score + practice_score) / 2

    return round(mastery, 2)