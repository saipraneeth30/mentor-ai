from pathlib import Path


def load_prompt(prompt_name: str) -> str:
    prompt_path = Path("prompts") / f"{prompt_name}.md"

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()