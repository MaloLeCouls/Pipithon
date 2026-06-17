"""Choix de design :
- `__repr__` avec `!r` sur le titre : roundtrip eval-friendly.
- `__str__` plus compact : préfixe `P` + numéro de priorité.
- Si on n'avait défini que `__repr__`, `str(task)` aurait fallback dessus.
"""
from __future__ import annotations


class Task:
    def __init__(self, title: str, priority: int) -> None:
        self.title = title
        self.priority = priority

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, priority={self.priority})"

    def __str__(self) -> str:
        return f"{self.title} (P{self.priority})"
