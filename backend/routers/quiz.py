from fastapi import APIRouter

from backend.services.quiz_service import QuizService

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.get("/start")
async def start_quiz(
    subject: str,
    difficulty: str
):

    return QuizService.start_quiz(
        subject,
        difficulty
    )