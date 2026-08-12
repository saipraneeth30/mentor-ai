from agents.teacher.teacher_agent import TeacherAgent


teacher = TeacherAgent()

message = input("Ask MentorAI: ")

print("\nThinking...\n")

response = teacher.teach(message)

print(response)