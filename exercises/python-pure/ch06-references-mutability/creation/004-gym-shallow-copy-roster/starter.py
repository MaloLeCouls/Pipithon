"""Une salle de sport veut faire un snapshot de la liste de ses membres :
- la liste copiée ne doit plus être affectée par les ajouts/retraits
  ultérieurs (= contenant indépendant),
- mais les objets `Member` peuvent rester partagés (= contenus partagés).

C'est une copie *superficielle*.

Implémente `snapshot(roster: list[Member]) -> list[Member]`.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Member:
    member_id: int
    name: str


def snapshot(roster: list[Member]) -> list[Member]:
    ...
