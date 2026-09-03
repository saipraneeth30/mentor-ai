def calculate_attendance(attended_days: int, total_days: int) -> float:
    """
    Calculate attendance percentage.

    Args:
        attended_days: Number of days attended.
        total_days: Total number of days.

    Returns:
        Attendance percentage between 0 and 100.
    """

    if total_days <= 0:
        raise ValueError("total_days must be greater than 0")

    if attended_days < 0:
        raise ValueError("attended_days cannot be negative")

    if attended_days > total_days:
        raise ValueError(
            "attended_days cannot be greater than total_days"
        )

    attendance = (attended_days / total_days) * 100

    return round(attendance, 2)