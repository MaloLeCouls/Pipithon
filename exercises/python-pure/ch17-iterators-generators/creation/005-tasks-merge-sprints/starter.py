"""Une API de gestion de tâches veut un flux paresseux qui *concatène* les
tâches de plusieurs sprints (vue agrégée sans dupliquer les données en RAM).

Implémente `merge_sprints(*sprints) -> Iterator[Task]` :
- chaque `sprint` est un itérable de `Task` (attribut `task_id: str`).
- yield chaque Task dans l'ordre des sprints, puis dans l'ordre interne
  de chaque sprint.

Indication : `itertools.chain` est fait pour ça. Pas de boucle imbriquée
écrite à la main si tu peux l'éviter.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def merge_sprints(*sprints: Iterable[Task]) -> Iterator[Task]:
    raise NotImplementedError("À implémenter")
