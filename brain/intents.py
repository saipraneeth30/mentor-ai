from enum import Enum


class Intent(Enum):
    STUDY = "study"
    QUIZ = "quiz"
    GENERAL_CHAT = "general_chat"
    UNKNOWN = "unknown"