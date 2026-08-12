from brain.workflow import Workflow


class Orchestrator:
    """
    Entry point for the MentorAI Brain.
    """

    def __init__(self):
        self.workflow = Workflow()

    def process(self, user_id: int, message: str):
        return self.workflow.run(user_id, message)