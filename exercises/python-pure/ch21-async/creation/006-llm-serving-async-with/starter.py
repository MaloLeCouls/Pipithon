"""Une session de génération sur ton inference server doit :
- préparer un id de session avant de sampler,
- garantir le close même si l'utilisateur lève une exception en plein milieu.

C'est exactement le pattern `async with` — équivalent async de `with`.

Contrat :

- Classe `InferenceSession(name: str)` :
  - attribut `events: list[str]` — log d'événements (pour les tests).
  - `async __aenter__`  : ajoute `f"open:{self.name}"` dans `events`, renvoie `self`.
  - `async __aexit__(exc_type, exc, tb)` : ajoute `f"close:{self.name}"` dans
    `events` (TOUJOURS, même si exception). Renvoie False / None pour laisser
    remonter les exceptions.
- `async def generate(session: InferenceSession, prompt: str) -> str` :
  ajoute `f"gen:{prompt}"` dans `session.events` et renvoie `prompt.upper()`.
"""
from __future__ import annotations


class InferenceSession:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events: list[str] = []

    async def __aenter__(self) -> "InferenceSession":
        raise NotImplementedError("À implémenter")

    async def __aexit__(self, exc_type, exc, tb) -> bool | None:
        raise NotImplementedError("À implémenter")


async def generate(session: InferenceSession, prompt: str) -> str:
    raise NotImplementedError("À implémenter")
