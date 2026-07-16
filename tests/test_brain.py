from brain.brain import MentorBrain

brain = MentorBrain()

while True:
    message = input("\nYou: ")

    intent, destination = brain.process(message)

    print(f"\nIntent      : {intent.value}")
    print(f"Destination : {destination}")