from data.student import student
from notifications.templates import GOOD_MORNING_TEMPLATE


def build_good_morning_message():

    return GOOD_MORNING_TEMPLATE.format(
        name=student["name"],
        goal=student["goal"],
        topic=student["today_topic"],
        questions=student["questions"],
        quiz_time=student["quiz_time"],
        streak=student["streak"]
    )