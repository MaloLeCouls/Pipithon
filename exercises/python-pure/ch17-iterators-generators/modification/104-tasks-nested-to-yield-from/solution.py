"""Choix de design :
- `yield from sprint` est strictement plus expressif que `for t in sprint:
  yield t` : il propage `send`/`throw`/`close` au sous-iterator. Pour un
  Iterable simple ça ne change rien, mais c'est l'idiome du chapitre 17.
- La boucle externe reste : `yield from` délègue à UN sous-iterable à la fois.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def all_tasks(*sprints: Iterable[Task]) -> Iterator[Task]:
    for sprint in sprints:
        yield from sprint
