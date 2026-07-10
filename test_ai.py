from ai.ollama_client import ask_ai

question = input("Ask MentorAI: ")

answer = ask_ai(question)

print("\nMentorAI:\n")
print(answer)