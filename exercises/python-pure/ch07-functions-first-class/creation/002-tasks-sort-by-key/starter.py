"""Une API de tâches reçoit une liste de tickets, chacun avec un attribut
`priority` (int, plus petit = plus urgent).

Implémente `by_priority(tasks: list[Task]) -> list[Task]` qui renvoie une
nouvelle liste triée par priorité CROISSANTE, sans muter l'entrée.

Utilise sorted(...) + une key (lambda ou fonction nommée).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int


def by_priority(tasks: list[Task]) -> list[Task]:
    ...
