"""Choix de design :
- `__aenter__`/`__aexit__` async : seules méthodes nécessaires. Pas besoin
  d'un `try/finally` dans le bloc `async with` : Python garantit
  l'appel de `__aexit__` même si une exception est levée.
- `__aexit__` renvoie None (équivaut à False) : on ne **swallow** rien,
  l'exception remonte normalement à l'appelant.
- `generate` est juste une coroutine helper ; elle n'a pas à gérer
  l'ouverture/fermeture — c'est le rôle du context manager.
"""
from __future__ import annotations


class InferenceSession:
    def __init__(self, name: str) -> None:
        self.name = name
        self.events: list[str] = []

    async def __aenter__(self) -> "InferenceSession":
        self.events.append(f"open:{self.name}")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool | None:
        self.events.append(f"close:{self.name}")
        return None


async def generate(session: InferenceSession, prompt: str) -> str:
    session.events.append(f"gen:{prompt}")
    return prompt.upper()
