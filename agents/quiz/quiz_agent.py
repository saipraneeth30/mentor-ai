from ai.ollama_client import ask_ai
from utils.prompt_loader import load_prompt
from agents.base_agent import BaseAgent
from brain.contracts.ai_response import AIResponse


class QuizAgent(BaseAgent):

    def handle(self, message: str) -> AIResponse:

        quiz = self.generate_quiz(message)

        return AIResponse(
            response_type="quiz",
            title="Quiz",
            content=quiz,
            metadata={
                "source": "quiz_agent"
            },
            actions=[
                "submit"
            ],
            suggestions=[]
        )

    def generate_quiz(self, topic: str):

        print("[Quiz] Loading prompt...")

        prompt = load_prompt("quiz")

        print("[Quiz] Replacing placeholder...")

        prompt = prompt.replace("{{message}}", topic)

        print("[Quiz] Calling Ollama...")

        response = ask_ai(prompt)

        return response