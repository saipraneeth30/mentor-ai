from brain.orchestrator import Orchestrator

orchestrator = Orchestrator()

message = input("Ask MentorAI: ")

print("\nThinking...\n")

result = orchestrator.process(message)

print("=" * 50)
print("MENTOR AI RESULT")
print("=" * 50)

print(f"Intent     : {result['intent']}")
print(f"Confidence : {result['confidence']:.2f}")
print(f"Reason     : {result['reason']}")
print(f"Action     : {result['action']}")

print("\nResponse:\n")
print(result["response"])