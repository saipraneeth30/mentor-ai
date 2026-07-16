from enum import Enum


class Action(Enum):
    """
    Represents what MentorAI should do
    after understanding the student's intent.
    """

    TEACH = "teach"

    GENERATE_QUIZ = "generate_quiz"

    GREET = "greet"

    ASK_AI = "ask_ai"

    UNKNOWN = "unknown"