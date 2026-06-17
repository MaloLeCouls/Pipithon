"""Choix de design :
- `match`/`if-elif` sur `spec` : le mini-langage est documenté en
  branchements explicites.
- `ValueError` sur spec inconnue : c'est ce que fait `int.__format__`
  quand le spec est mauvais — on s'aligne sur la stdlib.
- `__str__` réutilise `format(self, "")` : DRY.
"""
from __future__ import annotations


class Task:
    def __init__(self, title: str, status: str) -> None:
        self.title = title
        self.status = status

    def __format__(self, spec: str) -> str:
        if spec == "":
            return f"{self.title} [{self.status}]"
        if spec == "short":
            return self.title
        if spec == "full":
            return f"{self.title} ({self.status.upper()})"
        raise ValueError(f"Unknown format spec: {spec}")

    def __str__(self) -> str:
        return format(self, "")
