from brain.intents import Intent
from brain.actions import Action


class ActionPlanner:
    """
    Decides what MentorAI should do
    based on the detected intent.
    """

    def plan(self, intent: Intent) -> Action:

        if intent == Intent.STUDY:
            return Action.TEACH

        elif intent == Intent.QUIZ:
            return Action.GENERATE_QUIZ

        elif intent == Intent.GENERAL_CHAT:
            return Action.GREET

        return Action.ASK_AI