"""La fonction `all_tasks(*sprints)` aplatit plusieurs sprints en un seul
flux de Tasks. Elle marche, mais avec une double boucle `for ... : for ... :
yield`. Le chapitre 17 introduit une syntaxe plus propre : `yield from`.

Refactor : remplace la boucle interne par `yield from sprint`. La boucle
externe sur `sprints` reste (un sprint à la fois, dans l'ordre). Le
comportement observable doit rester identique."""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def all_tasks(*sprints: Iterable[Task]) -> Iterator[Task]:
    for sprint in sprints:
        for task in sprint:
            yield task
