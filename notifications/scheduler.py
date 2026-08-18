from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from notifications.notifier import send_notification


scheduler = AsyncIOScheduler()


def start_scheduler(client):

    print("==========================================")
    print("📅 Scheduler Started")
    print("==========================================")

    # 🌅 Good Morning at 5:00 AM
    scheduler.add_job(
        send_notification,
        CronTrigger(hour=5, minute=0),
        args=[client]
    )

    # ⏰ Quiz Reminder at 7:00 PM
    scheduler.add_job(
        send_notification,
        CronTrigger(hour=19, minute=0),
        args=[client]
    )

    # 🌙 Study Check at 9:00 PM
    scheduler.add_job(
        send_notification,
        CronTrigger(hour=21, minute=0),
        args=[client]
    )

    scheduler.start()

    print("✅ Automatic Notifications Enabled!")