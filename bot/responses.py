from brain.orchestrator import Orchestrator

# Create a single orchestrator instance
orchestrator = Orchestrator()


def get_response(user_id: int, message: str):
    """
    Process the user's message through MentorAI.
    """

    result = orchestrator.process(user_id, message)

    return result["response"]