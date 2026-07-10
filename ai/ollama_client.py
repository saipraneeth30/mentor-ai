import ollama


def ask_ai(prompt: str) -> str:
    """
    Sends a prompt to the local Qwen model
    and returns the generated response.
    """

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]