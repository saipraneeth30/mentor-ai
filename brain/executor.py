from brain.actions import Action
from brain.contracts.ai_response import AIResponse
from agents.teacher.teacher_agent import TeacherAgent
from agents.quiz.quiz_agent import QuizAgent


class Executor:
    """
    Executes actions using registered AI agents.
    """

    def __init__(self):

        self.agents = {

            Action.TEACH: TeacherAgent(),

            Action.GENERATE_QUIZ: QuizAgent(),

        }

    def execute(self, user_id: int, action: Action, message: str):

        # Greeting

        if action == Action.GREET:
            return AIResponse(
                response_type="greeting",
                title="Greeting",
                content="Hello! 👋 How can I help you today.",
                metadata={},
                actions=[],
                suggestions=[]
            )

        if action == Action.ASK_AI:
            return AIResponse(
                response_type="general",
                title="AI Assistant",
                content="General AI Assistant Coming Soon.",
                metadata={},
                actions=[],
                suggestions=[]
            )

        # Lookup agent

        agent = self.agents.get(action)

        if agent is None:
            return "Unknown Action."

        # Execute agent

        return agent.handle(message)