def get_response(message: str) -> str:
    """
    Returns a response based on the user's message.
    """

    message = message.lower().strip()

    if message == "hello":
        return "Hello! 👋 I am MentorAI."

    elif message == "hi":
        return "Hi! 😊"

    elif "how are you" in message:
        return "I'm doing great! Ready to help you study. 📚"

    return (
        "I'm still learning. "
        "Soon I'll be able to teach you using my AI brain! 🤖"
    )