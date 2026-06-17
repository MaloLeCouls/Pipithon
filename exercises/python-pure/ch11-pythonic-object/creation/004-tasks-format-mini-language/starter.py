"""`__format__` est appelé par `format(obj, spec)` et f-string `{obj:spec}`.
Tu définis ton propre mini-langage de format.

Contrat — classe `Task(title: str, status: str)` :

- `__format__(self, spec: str) -> str` :
  - `""` (vide) → `f"{title} [{status}]"`,
  - `"short"` → `title`,
  - `"full"` → `f"{title} ({status.upper()})"`,
  - autre → `ValueError(f"Unknown format spec: {spec}")`.

- `__str__` peut renvoyer `format(self, "")` (ou être implémenté directement).
"""
from __future__ import annotations


class Task:
    def __init__(self, title: str, status: str) -> None:
        self.title = title
        self.status = status

    def __format__(self, spec: str) -> str:
        raise NotImplementedError("À implémenter")

    def __str__(self) -> str:
        return format(self, "")
