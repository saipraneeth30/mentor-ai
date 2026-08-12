from ai.ollama_client import ask_ai
from utils.prompt_loader import load_prompt
from agents.base_agent import BaseAgent
from brain.contracts.ai_response import AIResponse


class TeacherAgent(BaseAgent):

    def handle(self, message: str) -> AIResponse:

        response = self.teach(message)

        return AIResponse(
            response_type="lesson",
            title="Lesson",
            content=response,
            metadata={
                "source": "teacher_agent"
            },
            actions=[
                "quiz"
            ],
            suggestions=[]
        )

    def teach(self, message: str):

        print("[1] Loading prompt...")

        prompt = load_prompt("teacher")

        print("[2] Replacing placeholder...")

        prompt = prompt.replace("{{message}}", message)

        print("[3] Calling Ollama...")

        response = ask_ai(prompt)

        return response