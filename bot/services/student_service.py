from bot.services.api_client import APIClient


class StudentService:

    @staticmethod
    async def register_student(student_data: dict):
        return await APIClient.post(
            "/students/register",
            json=student_data
        )

    @staticmethod
    async def get_dashboard():
        return await APIClient.get(
            "/students/dashboard"
        )

    @staticmethod
    async def get_progress():
        return await APIClient.get(
            "/students/progress"
        )

    @staticmethod
    async def get_settings():
        return await APIClient.get(
            "/students/settings"
        )