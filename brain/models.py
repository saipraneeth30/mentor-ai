from dataclasses import dataclass

from brain.intents import Intent


@dataclass
class IntentResult:
    intent: Intent
    confidence: float
    reason: str