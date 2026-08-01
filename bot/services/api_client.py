import httpx


class APIClient:

    BASE_URL = "http://127.0.0.1:8000"

    @classmethod
    async def post(cls, endpoint: str, json: dict):

        async with httpx.AsyncClient(timeout=10.0) as client:

            response = await client.post(
                f"{cls.BASE_URL}{endpoint}",
                json=json
            )

            response.raise_for_status()

            return response.json()