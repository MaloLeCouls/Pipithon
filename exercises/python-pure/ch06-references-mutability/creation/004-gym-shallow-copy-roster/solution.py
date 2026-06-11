"""Choix de design :
- `list(roster)` crée une nouvelle liste avec les mêmes éléments.
- Équivalent : `roster[:]` ou `copy.copy(roster)`. Tous sont O(n) et corrects ;
  on choisit `list(...)` qui est le plus lisible.
- Les Member partagés sont voulus : on snapshote l'appartenance, pas les
  membres eux-mêmes.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Member:
    member_id: int
    name: str


def snapshot(roster: list[Member]) -> list[Member]:
    return list(roster)
