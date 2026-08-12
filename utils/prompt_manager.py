from utils.prompt_loader import load_prompt


class PromptManager:
    """
    Loads a prompt template and renders it by replacing placeholders.
    """

    def render(self, prompt_name: str, **kwargs) -> str:
        prompt = load_prompt(prompt_name)

        for key, value in kwargs.items():
            placeholder = "{{" + key + "}}"
            prompt = prompt.replace(placeholder, str(value))

        return prompt