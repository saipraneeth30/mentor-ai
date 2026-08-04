from urllib.parse import quote

from bot.services.api_client import APIClient


class QuizService:

    @staticmethod
    async def start_quiz(subject: str, difficulty: str):

        subject = quote(subject)
        difficulty = quote(difficulty)

        return await APIClient.get(
            f"/quiz/start?subject={subject}&difficulty={difficulty}"
        )