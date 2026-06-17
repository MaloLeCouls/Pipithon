"""`TypedDict` permet d'annoter un dict comme un record (champs fixés
+ types). À runtime, c'est un dict normal — c'est PURE annotation
pour mypy. Très utilisé pour JSON API responses.

Contrat :

- Déclare `TaskRecord(TypedDict)` avec :
  - `title: str`
  - `priority: int`
  - `done: bool`
- Écris `make_task(title: str, priority: int) -> TaskRecord` qui renvoie
  un record avec `done=False`.
- Écris `is_urgent(task: TaskRecord) -> bool` qui renvoie
  `task["priority"] >= 3 and not task["done"]`.
"""
from __future__ import annotations

from typing import TypedDict


class TaskRecord(TypedDict):
    ...


def make_task(title: str, priority: int) -> TaskRecord:
    raise NotImplementedError("À implémenter")


def is_urgent(task: TaskRecord) -> bool:
    raise NotImplementedError("À implémenter")
