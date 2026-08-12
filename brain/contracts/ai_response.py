from dataclasses import dataclass, field
from typing import Any


@dataclass
class AIResponse:
    """
    Standard response object returned by every AI Agent.

    This object acts as the communication contract
    between the AI Brain and the remaining MentorAI modules.
    """

    response_type: str
    title: str
    content: str

    metadata: dict[str, Any] = field(default_factory=dict)

    actions: list[str] = field(default_factory=list)

    suggestions: list[str] = field(default_factory=list)