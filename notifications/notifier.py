from config.settings import CHANNEL_ID
from notifications.message_builder import build_good_morning_message
from notifications.reminder_rules import get_notification_type


async def send_notification(client):

    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("❌ Channel not found!")
        return

    # Temporary student data (Mock Data)
    student = {
        "name": "Prasanna",
        "goal": "GATE CSE",
        "today_topic": "Recursion",
        "questions": 5,
        "quiz_time": "7:00 PM",
        "streak": 6
    }

    notification_type = get_notification_type(student)

    print(f"Notification Type: {notification_type}")

    # 🌞 Good Morning Notification
    if notification_type == "good_morning":

        message = build_good_morning_message()

        await channel.send(message)

        print("✅ Good Morning Notification Sent!")

    # ⏰ Quiz Notification
    elif notification_type == "quiz":

        await channel.send(
            f"""
⏰ **Quiz Time!**

📘 Today's Topic:
**{student['today_topic']}**

Good Luck! 🚀
"""
        )

        print("✅ Quiz Notification Sent!")

    # 🌙 Study Check Notification
    elif notification_type == "study_check":

        await channel.send(
            """
🌙 **Study Check**

📚 Did you complete today's study goal?

✅ If yes, Great Job! 🎉

❌ If not, don't worry.

💪 Every expert was once a beginner.

🚀 Keep learning and never give up!
"""
        )

        print("✅ Study Check Notification Sent!")

    # 😴 No Notification
    else:

        print("😴 No notification to send.")