from brain.intent_classifier import IntentClassifier
from brain.action_planner import ActionPlanner
from brain.executor import Executor


class Orchestrator:
    """
    Coordinates the complete MentorAI workflow.
    """

    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.action_planner = ActionPlanner()
        self.executor = Executor()

    def process(self, message: str):

        # Step 1: Detect Intent
        intent_result = self.intent_classifier.classify(message)

        # Step 2: Decide Action
        action = self.action_planner.plan(intent_result.intent)

        # Step 3: Execute Action
        agent = self.executor.execute(action)

        return {
            "intent": intent_result.intent.value,
            "confidence": intent_result.confidence,
            "reason": intent_result.reason,
            "action": action.value,
            "agent": agent,
        }