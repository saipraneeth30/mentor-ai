from brain.intents import Intent
from brain.models import IntentResult
from ai.intent_ai import AIIntentClassifier

from brain.keywords import (
    STUDY_KEYWORDS,
    QUIZ_KEYWORDS,
    GREETING_KEYWORDS,
)


class IntentClassifier:
    """
    Classifies the student's message into an intent.

    Version 1:
    - Rule-based classification.
    - Unknown messages will later be classified by Qwen (Hybrid AI).
    """

    def __init__(self):
        self.ai_classifier = AIIntentClassifier()

    def classify(self, message: str) -> IntentResult:
        """
        Analyze the message and return the detected intent.
        """

        message = message.lower().strip()

        # ---------- Study ----------
        for keyword in STUDY_KEYWORDS:
            if keyword in message:
                return IntentResult(
                    intent=Intent.STUDY,
                    confidence=0.98,
                    reason=f"Detected study keyword: '{keyword}'."
                )

        # ---------- Quiz ----------
        for keyword in QUIZ_KEYWORDS:
            if keyword in message:
                return IntentResult(
                    intent=Intent.QUIZ,
                    confidence=0.98,
                    reason=f"Detected quiz keyword: '{keyword}'."
                )

        # ---------- Greeting ----------
        for keyword in GREETING_KEYWORDS:
            if keyword in message:
                return IntentResult(
                    intent=Intent.GENERAL_CHAT,
                    confidence=1.00,
                    reason=f"Detected greeting keyword: '{keyword}'."
                )

        return self.ai_classifier.classify(message)