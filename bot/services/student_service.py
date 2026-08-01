from bot.services.api_client import APIClient


class StudentService:

    @staticmethod
    async def register_student(student_data: dict):

        return await APIClient.post(
            "/students/register",
            json=student_data
        )