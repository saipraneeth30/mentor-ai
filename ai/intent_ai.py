from ai.ollama_client import ask_ai
from brain.intents import Intent
from brain.models import IntentResult


class AIIntentClassifier:
    """
    Uses Qwen to classify student intent when
    the rule-based classifier is not confident.
    """

    def classify(self, message: str) -> IntentResult:

        prompt = f"""
You are an intent classification system.

Available intents:

- STUDY
- QUIZ
- GENERAL_CHAT

Rules:

Return ONLY one word.

Examples:

Explain Binary Search
STUDY

Give me a quiz
QUIZ

Hello
GENERAL_CHAT

Message:
{message}
"""

        response = ask_ai(prompt).strip().upper()

        if response == "STUDY":
            return IntentResult(
                intent=Intent.STUDY,
                confidence=0.85,
                reason="AI classified the message."
            )

        elif response == "QUIZ":
            return IntentResult(
                intent=Intent.QUIZ,
                confidence=0.85,
                reason="AI classified the message."
            )

        elif response == "GENERAL_CHAT":
            return IntentResult(
                intent=Intent.GENERAL_CHAT,
                confidence=0.85,
                reason="AI classified the message."
            )

        return IntentResult(
            intent=Intent.UNKNOWN,
            confidence=0.10,
            reason="AI could not classify."
        )