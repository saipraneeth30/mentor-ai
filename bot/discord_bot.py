import discord

from notifications.notification_service import NotificationService
from notifications.scheduler import start_scheduler

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():

    print("=" * 50)
    print("MentorAI Bot is Online!")
    print(f"Logged in as: {client.user}")
    print("=" * 50)

    # Send one notification when the bot starts
    await NotificationService.send(client)

    # Start the scheduler
    start_scheduler(client)