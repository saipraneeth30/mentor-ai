def calculate_progress(completed_items: int, total_items: int) -> float:
    """
    Calculate progress percentage.

    Args:
        completed_items: Number of completed items.
        total_items: Total number of items.

    Returns:
        Progress percentage between 0 and 100.
    """

    if total_items <= 0:
        raise ValueError("total_items must be greater than 0")

    if completed_items < 0:
        raise ValueError("completed_items cannot be negative")

    if completed_items > total_items:
        raise ValueError(
            "completed_items cannot be greater than total_items"
        )

    progress = (completed_items / total_items) * 100

    return round(progress, 2)