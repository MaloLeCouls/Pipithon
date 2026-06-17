"""Choix de design :
- `TypedDict` documente la forme attendue ; mypy refuse les clés
  manquantes ou de mauvais type.
- Runtime : zero différence — un TypedDict EST un dict.
"""
from __future__ import annotations

from typing import TypedDict


class TaskRecord(TypedDict):
    title: str
    priority: int
    done: bool


def process(task: TaskRecord) -> str:
    return f"{task['title']} (P{task['priority']})"
