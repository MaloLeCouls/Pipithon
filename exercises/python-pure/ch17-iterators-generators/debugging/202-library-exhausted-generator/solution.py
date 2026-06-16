"""Choix de design (correctif) :
- Un Iterator est à USAGE UNIQUE. Quand on a besoin de le parcourir deux
  fois, soit on le matérialise (`list(...)`), soit on le filtre deux fois
  (re-création).
- Ici, materialiser en `list` est le bon choix : on a déjà besoin de la
  liste des isbns, et `len(...)` remplace `sum(1 for _ in ...)` qui devient
  inutilement bavard.
"""
from __future__ import annotations

from collections.abc import Iterable


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def overdue_summary(loans: Iterable[Loan], today: int) -> tuple[int, list[str]]:
    overdue = [loan for loan in loans if loan.due_date < today]
    return len(overdue), [loan.isbn for loan in overdue]
