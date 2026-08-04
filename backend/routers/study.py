from fastapi import APIRouter

from backend.services.study_service import StudyService

router = APIRouter(
    prefix="/study",
    tags=["Study"]
)


@router.get("/topic")
async def get_topic(
    subject: str,
    topic: str
):

    return StudyService.get_topic(
        subject,
        topic
    )