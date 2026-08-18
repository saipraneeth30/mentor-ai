from datetime import datetime


def get_notification_type(student):
    """
    🎯 Decide which notification MentorAI should send
    based on the current time.
    """

    current_hour = datetime.now().hour

    # 🌅 5:00 AM → Good Morning Notification
    if current_hour == 5:
        print("🌅 Time: 5:00 AM")
        print("📨 Sending Good Morning Notification...")
        return "good_morning"

    # ⏰ 7:00 PM → Quiz Reminder
    elif current_hour == 19:
        print("⏰ Time: 7:00 PM")
        print("📝 Sending Quiz Reminder...")
        return "quiz"

    # 🌙 9:00 PM → Study Completion Check
    elif current_hour == 21:
        print("🌙 Time: 9:00 PM")
        print("📚 Sending Study Check Notification...")
        return "study_check"

    # 😴 No Notification
    else:
        print("😴 No notification scheduled at this time.")
        return "none"