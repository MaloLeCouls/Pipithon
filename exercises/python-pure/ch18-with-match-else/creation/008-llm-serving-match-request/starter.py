"""Le serveur d'inférence reçoit un flux d'évènements hétérogènes : tokens,
fins de génération avec différentes raisons, heartbeats. On veut router
chacun vers une string descriptive — c'est *exactement* le job de
`match`/`case`.

Implémente `route_event(event)` qui retourne :
- `StreamToken(token_id=tid, text=t)`  -> `f"stream:{tid}:{t}"`
- `FinishReason(reason="stop")`        -> `"done:ok"`
- `FinishReason(reason="length")`      -> `"done:max-tokens"`
- `FinishReason(reason=other)`         -> `f"done:{other}"`
- `Heartbeat()`                        -> `"alive"`
- tout le reste                        -> `"unknown"`

⚠️ Utilise un seul `match event:` avec 6 `case`. Pas de `isinstance`."""
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
    raise NotImplementedError("À implémenter")
