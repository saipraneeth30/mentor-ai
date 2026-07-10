from brain.intents import Intent


class IntentClassifier:

    def classify(self, message: str) -> Intent:

        message = message.lower()

        # Study
        study_keywords = [
            "explain",
            "teach",
            "what is",
            "understand",
            "learn",
        ]

        # Quiz
        quiz_keywords = [
            "quiz",
            "test",
            "mcq",
            "questions",
        ]

        # Greeting
        greeting_keywords = [
            "hi",
            "hello",
            "good morning",
            "good evening",
            "hey",
        ]

        for keyword in study_keywords:
            if keyword in message:
                return Intent.STUDY

        for keyword in quiz_keywords:
            if keyword in message:
                return Intent.QUIZ

        for keyword in greeting_keywords:
            if keyword in message:
                return Intent.GENERAL_CHAT

        return Intent.UNKNOWN