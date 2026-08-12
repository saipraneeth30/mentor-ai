from brain.intent_classifier import IntentClassifier
from brain.action_planner import ActionPlanner
from brain.executor import Executor
from brain.context_manager import ContextManager
from brain.topic_extractor import TopicExtractor


class Workflow:
    """
    Executes the complete MentorAI AI workflow.

    Pipeline:
    User Message
        ↓
    Intent Detection
        ↓
    Topic Extraction
        ↓
    Context Update
        ↓
    Action Planning
        ↓
    Agent Execution
        ↓
    Return Response
    """

    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.action_planner = ActionPlanner()
        self.executor = Executor()
        self.context = ContextManager()
        self.topic_extractor = TopicExtractor()

    def run(self, user_id: int, message: str):

        # -----------------------------
        # Step 1 : Detect Intent
        # -----------------------------
        intent_result = self.intent_classifier.classify(message)

        # Store Intent
        self.context.set(
            user_id,
            "last_intent",
            intent_result.intent.value
        )

        # -----------------------------
        # Step 2 : Extract Topic
        # -----------------------------
        topic = self.topic_extractor.extract(message)

        if topic:
            self.context.set(
                user_id,
                "current_topic",
                topic
            )

        # -----------------------------
        # Step 3 : Plan Action
        # -----------------------------
        action = self.action_planner.plan(intent_result.intent)

        # Store Action
        self.context.set(
            user_id,
            "last_action",
            action.value
        )

        # -----------------------------
        # Step 4 : Store User Message
        # -----------------------------
        self.context.set(
            user_id,
            "last_message",
            message
        )

        # -----------------------------
        # Step 5 : Execute Agent
        # -----------------------------
        response = self.executor.execute(
            user_id,
            action,
            message
        )

        # -----------------------------
        # Step 6 : Return Result
        # -----------------------------
        return {
            "intent": intent_result.intent.value,
            "confidence": intent_result.confidence,
            "reason": intent_result.reason,
            "action": action.value,
            "response": response,
        }