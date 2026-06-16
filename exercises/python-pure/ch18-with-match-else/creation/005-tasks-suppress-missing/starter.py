"""Une API de tâches reçoit une liste d'ids à supprimer. Certains n'existent
peut-être pas — c'est OK, on les ignore silencieusement. Pas besoin d'un
`try/except KeyError: pass` à chaque pop.

Implémente `bulk_close(tasks, task_ids)` :
- `tasks` : `dict[str, Task]` (mappé par id).
- `task_ids` : `Iterable[str]` — peut contenir des ids absents.
- pour chaque id : retire-le de `tasks`. Si l'id est absent, **ignore
  silencieusement** (zéro exception remontée).

Utilise `contextlib.suppress` — c'est tout l'intérêt du chapitre.
"""
from __future__ import annotations

from collections.abc import Iterable


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def bulk_close(tasks: dict[str, Task], task_ids: Iterable[str]) -> None:
    raise NotImplementedError("À implémenter")
