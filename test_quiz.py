from agents.quiz.quiz_agent import QuizAgent

quiz_agent = QuizAgent()

topic = input("Enter Topic: ")

print("\nGenerating Quiz...\n")

quiz = quiz_agent.generate_quiz(topic)

print("=" * 50)
print("QUIZ")
print("=" * 50)

print(quiz)