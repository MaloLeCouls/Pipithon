"""Choix de design :
- `match/case` : un seul site de dispatch, lecture descendante (l'ordre des
  `case` compte — les plus spécifiques d'abord).
- Class patterns avec capture (`StreamToken(token_id=tid, text=t)`) :
  on extrait les champs nommés en une ligne. C'est possible parce que
  `@dataclass` génère `__match_args__` automatiquement.
- Le `case _:` final attrape tout ce qui n'a pas matché. *Ne JAMAIS l'oublier*
  (sinon valeur de retour implicite = None côté Python).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StreamToken:
    token_id: int
    text: str


@dataclass
class FinishReason:
    reason: str


@dataclass
class Heartbeat:
    pass


def route_event(event: object) -> str:
    match event:
        case StreamToken(token_id=tid, text=t):
            return f"stream:{tid}:{t}"
        case FinishReason(reason="stop"):
            return "done:ok"
        case FinishReason(reason="length"):
            return "done:max-tokens"
        case FinishReason(reason=other):
            return f"done:{other}"
        case Heartbeat():
            return "alive"
        case _:
            return "unknown"
