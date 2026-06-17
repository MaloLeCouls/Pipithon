"""Cette fn `process` prend un `dict[str, Any]` — c'est exactement
ce que `TypedDict` est fait pour remplacer.

Refactore :
- Déclare `TaskRecord(TypedDict)` avec `title: str`, `priority: int`,
  `done: bool`.
- Type `process(task: TaskRecord) -> str`.
- Comportement runtime inchangé.
"""
from __future__ import annotations

from typing import Any


def process(task: dict[str, Any]) -> str:
    return f"{task['title']} (P{task['priority']})"
