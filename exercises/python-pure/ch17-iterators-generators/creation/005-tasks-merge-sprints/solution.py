"""Choix de design :
- `itertools.chain(*sprints)` : C-implémenté, paresseux, idiomatique. Aucune
  copie ; un seul passage sur chaque sprint, dans l'ordre des arguments.
- On retourne directement le `chain` (lui-même un Iterator) : pas besoin de
  `yield from` ici (mais ça marcherait aussi).
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from itertools import chain


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def merge_sprints(*sprints: Iterable[Task]) -> Iterator[Task]:
    return chain(*sprints)
