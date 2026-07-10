from brain.intents import Intent


class Router:

    def route(self, intent: Intent):

        if intent == Intent.STUDY:
            return "Teacher Agent"

        elif intent == Intent.QUIZ:
            return "Quiz Agent"

        elif intent == Intent.GENERAL_CHAT:
            return "Greeting Handler"

        return "AI Intent Analyzer"