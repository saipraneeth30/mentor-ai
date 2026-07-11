from brain.intents import Intent
from brain.models import IntentResult


class IntentClassifier:

    def classify(self, message: str) -> IntentResult:

        message = message.lower().strip()

        study_keywords = [
            "explain",
            "teach",
            "learn",
            "what is",
            "understand",
        ]

        quiz_keywords = [
            "quiz",
            "mcq",
            "test",
            "question",
        ]

        greeting_keywords = [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good evening",
        ]

        for keyword in study_keywords:
            if keyword in message:
                return IntentResult(
                    intent=Intent.STUDY,
                    confidence=0.98,
                    reason=f"Detected study keyword '{keyword}'."
                )

        for keyword in quiz_keywords:
            if keyword in message:
                return IntentResult(
                    intent=Intent.QUIZ,
                    confidence=0.98,
                    reason=f"Detected quiz keyword '{keyword}'."
                )

        for keyword in greeting_keywords:
            if keyword in message:
                return IntentResult(
                    intent=Intent.GENERAL_CHAT,
                    confidence=1.0,
                    reason=f"Detected greeting '{keyword}'."
                )

        return IntentResult(
            intent=Intent.UNKNOWN,
            confidence=0.20,
            reason="No rule matched. Needs AI classification."
        )