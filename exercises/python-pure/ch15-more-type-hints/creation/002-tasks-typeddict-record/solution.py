"""Choix de design :
- `TypedDict` : à runtime = `dict`, mais mypy traque les clés/types.
- `make_task` renvoie un dict literal qui matche la forme — mypy
  vérifie tout d'un coup.
- `is_urgent` lit avec `["..."]` (mypy connaît le type de chaque clé).
"""
from __future__ import annotations

from typing import TypedDict


class TaskRecord(TypedDict):
    title: str
    priority: int
    done: bool


def make_task(title: str, priority: int) -> TaskRecord:
    return {"title": title, "priority": priority, "done": False}


def is_urgent(task: TaskRecord) -> bool:
    return task["priority"] >= 3 and not task["done"]
