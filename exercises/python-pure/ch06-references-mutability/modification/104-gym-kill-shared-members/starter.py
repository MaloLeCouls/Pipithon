"""Cette fonction crée N sessions de réservation pour des créneaux différents.
Bug d'aliasing : toutes les sessions reçoivent le MÊME objet `roster` ; ajouter
un membre à une session pollue les N-1 autres.

Refactor : isole les rosters. Chaque session doit avoir sa propre liste.
La copie superficielle suffit (les Member peuvent rester partagés).
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
    return [Session(slot=s, roster=roster) for s in slots]
