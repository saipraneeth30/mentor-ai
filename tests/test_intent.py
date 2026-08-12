from brain.intent_classifier import IntentClassifier

classifier = IntentClassifier()

print("=" * 50)
print("MentorAI Intent Classifier")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    message = input("\nYou: ")

    if message.lower() == "exit":
        break

    result = classifier.classify(message)

    print("\n------------------------------")
    print(f"Intent      : {result.intent.value}")
    print(f"Confidence  : {result.confidence}")
    print(f"Reason      : {result.reason}")
    print("------------------------------")