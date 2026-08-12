import re


class TopicExtractor:
    """
    Extracts the study topic from a user's message.

    Version 1:
    Rule-based extraction.

    Future:
    AI-powered topic extraction.
    """

    def extract(self, message: str) -> str | None:

        message = message.strip()

        patterns = [

            r"explain\s+(.*)",
            r"teach\s+(.*)",
            r"what is\s+(.*)",
            r"learn\s+(.*)",
            r"understand\s+(.*)",

        ]

        for pattern in patterns:

            match = re.search(pattern, message, re.IGNORECASE)

            if match:
                return match.group(1).strip()

        return None