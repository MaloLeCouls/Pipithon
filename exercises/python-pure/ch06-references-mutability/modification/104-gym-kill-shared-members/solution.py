"""Choix de design :
- list(roster) crée une copie superficielle par session : nouveau contenant,
  mêmes Member.
- C'est suffisant : le besoin métier est d'isoler les *appartenances*, pas
  d'avoir des copies indépendantes de chaque membre.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Member:
    member_id: int
    name: str


@dataclass
class Session:
    slot: str
    roster: list[Member] = field(default_factory=list)


def schedule(slots: list[str], roster: list[Member]) -> list[Session]:
    return [Session(slot=s, roster=list(roster)) for s in slots]
