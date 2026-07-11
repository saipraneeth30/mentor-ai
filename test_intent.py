from brain.intent_classifier import IntentClassifier

classifier = IntentClassifier()

while True:
    message = input("\nYou: ")

    result = classifier.classify(message)

    print("\nIntent     :", result.intent.value)
    print("Confidence :", result.confidence)
    print("Reason     :", result.reason)