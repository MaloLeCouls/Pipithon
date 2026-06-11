"""Choix de design :
- copy.deepcopy(session.members) duplique la liste ET ses Member.
- Le trainer est passé tel quel : référence partagée volontaire.
- Le slot est une str (immutable), pas besoin de précautions.
"""
from __future__ import annotations

import copy
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
    return Session(
        slot=session.slot,
        trainer=session.trainer,  # partagé volontairement
        members=copy.deepcopy(session.members),  # isolé
    )
