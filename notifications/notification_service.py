from notifications.notifier import send_notification


class NotificationService:
    """
    Service layer for handling notification requests.
    """

    @staticmethod
    async def send(client):
        """
        Send a notification using the notifier.
        """
        await send_notification(client)