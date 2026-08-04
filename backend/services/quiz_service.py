from backend.schemas.quiz import QuizQuestion, QuizResponse


class QuizService:

    @staticmethod
    def start_quiz(subject: str, difficulty: str):

        questions = [

            QuizQuestion(
                question="What is the time complexity of Binary Search?",
                options=[
                    "O(n)",
                    "O(log n)",
                    "O(n²)",
                    "O(1)"
                ],
                correct_answer="O(log n)"
            ),

            QuizQuestion(
                question="Which data structure uses FIFO?",
                options=[
                    "Stack",
                    "Queue",
                    "Tree",
                    "Graph"
                ],
                correct_answer="Queue"
            )

        ]

        quiz = QuizResponse(
            subject=subject,
            difficulty=difficulty,
            questions=questions
        )

        return {
            "success": True,
            "quiz": quiz.model_dump()
        }