from app.database.models import StudentDB, TimetableDB


def get_student_insights(db, student_id):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if student is None:
        return None

    timetables = db.query(TimetableDB).filter(
        TimetableDB.student_id == student_id
    ).all()

    if not timetables:
        return {
            "student": student.name,
            "message": "No timetable found."
        }

    subject_stats = {}

    for timetable in timetables:

        subject = timetable.subject

        if subject not in subject_stats:
            subject_stats[subject] = {
                "total": 0,
                "completed": 0
            }

        subject_stats[subject]["total"] += 1

        if timetable.completed:
            subject_stats[subject]["completed"] += 1

    best_subject = None
    weakest_subject = None

    highest = -1
    lowest = 101

    for subject, data in subject_stats.items():

        percentage = (
            data["completed"] / data["total"]
        ) * 100

        if percentage > highest:
            highest = percentage
            best_subject = subject

        if percentage < lowest:
            lowest = percentage
            weakest_subject = subject

    total_sessions = len(timetables)

    completed_sessions = sum(
        1 for timetable in timetables
        if timetable.completed
    )

    overall_completion = round(
        (completed_sessions / total_sessions) * 100,
        2
    )

    if overall_completion >= 80:
        consistency = "Excellent"
    elif overall_completion >= 60:
        consistency = "Good"
    elif overall_completion >= 40:
        consistency = "Average"
    else:
        consistency = "Poor"

    if overall_completion >= 70:
        goal_status = "On Track"
    else:
        goal_status = "Needs Improvement"

    insights = [
        f"Your best performing subject is {best_subject}.",
        f"You should spend more time on {weakest_subject}.",
        f"You have completed {overall_completion}% of your study plan.",
        f"Your study consistency is {consistency}.",
        f"Goal Status: {goal_status}."
    ]

    return {
        "student": student.name,
        "best_subject": best_subject,
        "weakest_subject": weakest_subject,
        "overall_completion": overall_completion,
        "consistency": consistency,
        "goal_status": goal_status,
        "insights": insights
    }