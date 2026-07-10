from brain.intent_classifier import IntentClassifier
from brain.router import Router


class MentorBrain:

    def __init__(self):

        self.classifier = IntentClassifier()
        self.router = Router()

    def process(self, message: str):

        intent = self.classifier.classify(message)

        destination = self.router.route(intent)

        return intent, destination