from brain.actions import Action


class Executor:
    """
    Executes the action by selecting
    the appropriate agent.

    Version 1:
    Returns the agent name.
    Later it will execute the real agent.
    """

    def execute(self, action: Action) -> str:

        if action == Action.TEACH:
            return "Teacher Agent"

        elif action == Action.GENERATE_QUIZ:
            return "Quiz Agent"

        elif action == Action.GREET:
            return "Greeting Handler"

        elif action == Action.ASK_AI:
            return "AI Assistant"

        return "Unknown Agent"