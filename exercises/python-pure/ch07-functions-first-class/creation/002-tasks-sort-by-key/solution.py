"""Choix de design :
- sorted(...) renvoie une nouvelle liste : l'entrée n'est pas mutée.
- key=lambda t: t.priority est l'usage canonique de lambda (court, jetable).
- Pour une version plus structurée : operator.attrgetter('priority'), drillée
  dans un exo ultérieur.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int


def by_priority(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda t: t.priority)
