"""Contrat indépendant du moteur ; aucun adaptateur réseau n'est implémenté."""
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class AIRequest:
    prompt: str
    context: tuple[str, ...] = ()


@dataclass(frozen=True)
class AIResponse:
    text: str
    provider: str
    model: str


class AIProvider(Protocol):
    def generate(self, request: AIRequest) -> AIResponse:
        """Produire une proposition IA, sans la qualifier de preuve."""
        ...
