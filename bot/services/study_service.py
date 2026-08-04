from urllib.parse import quote

from bot.services.api_client import APIClient


class StudyService:

    @staticmethod
    async def get_topic(subject: str, topic: str):

        subject = quote(subject)
        topic = quote(topic)

        return await APIClient.get(
            f"/study/topic?subject={subject}&topic={topic}"
        )