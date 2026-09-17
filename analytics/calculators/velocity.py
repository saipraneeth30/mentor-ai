def calculate_velocity(progress_change: float, time_period: float) -> float:
    """
    Calculate learning velocity.

    Learning velocity represents how much progress
    a student makes per unit of time.

    Args:
        progress_change: Amount of progress made.
        time_period: Amount of time taken.

    Returns:
        Learning velocity.
    """

    if progress_change < 0:
        raise ValueError("progress_change cannot be negative")

    if time_period <= 0:
        raise ValueError("time_period must be greater than 0")

    velocity = progress_change / time_period

    return round(velocity, 2)