"""Choix de design :
- Generator function : `yield` au lieu d'`append`, plus de variable accumulator.
  Mémoire O(1) ; premier `isbn` disponible dès la 1re itération.
- L'appelant qui voulait une liste reste libre de faire `list(overdue_isbns(...))`.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def overdue_isbns(loans: Iterable[Loan], today: int) -> Iterator[str]:
    for loan in loans:
        if loan.due_date < today:
            yield loan.isbn
