def get_mentor_notification(student):

    # Student missed 2 days
    if student.get("days_absent", 0) >= 2:
        return "restart"

    # Student is weak in Trees
    elif student.get("weak_topic") == "Trees":
        return "weak_topic"

    # Student has a good streak
    elif student.get("streak", 0) >= 7:
        return "streak"

    # Default notification
    return "daily"