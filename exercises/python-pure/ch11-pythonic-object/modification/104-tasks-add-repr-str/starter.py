"""Cette `Task` n'a ni `__repr__` ni `__str__` — debug et présentation
sont galère. Ajoute les deux.

Contrat solution :
- `__repr__(self)` = `f"Task(title='X', priority=2)"` (eval-friendly).
- `__str__(self)` = `f"X (P2)"` (lisible).
"""
from __future__ import annotations


class Task:
    def __init__(self, title: str, priority: int) -> None:
        self.title = title
        self.priority = priority
