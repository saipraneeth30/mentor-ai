from pydantic import BaseModel


class StudyResponse(BaseModel):
    subject: str
    topic: str
    content: str