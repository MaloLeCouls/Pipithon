"""Une salle de sport veut « forker » une session de réservation pour la
planifier dans un autre créneau :

- la liste des `members` (mutable) doit être ISOLÉE (deep) — on ne veut pas
  que la mutation d'une session pollue l'autre,
- le `Trainer` (objet partagé entre sessions, supposé géré ailleurs) doit
  rester PARTAGÉ (shallow) — un seul coach physique.

Implémente `fork_session(session: Session) -> Session`.

Tout est dans le choix : que copies-tu en profondeur, et que partages-tu ?
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Member:
    member_id: int
    name: str


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name


@dataclass
class Session:
    slot: str
    trainer: Trainer
    members: list[Member] = field(default_factory=list)


def fork_session(session: Session) -> Session:
    ...
