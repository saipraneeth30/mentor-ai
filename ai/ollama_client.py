from ollama import Client

client = Client(host="http://127.0.0.1:11434")


def ask_ai(prompt: str) -> str:
    response = client.chat(
        model="qwen3:0.6b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]