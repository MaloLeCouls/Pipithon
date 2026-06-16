"""Choix de design :
- Generator function — le client itère et envoie une relance par Loan, sans
  qu'on matérialise jamais la liste complète.
- On yield le Loan entier : l'appelant a besoin de l'isbn ET de la date
  pour rédiger la relance. Renvoyer juste l'isbn perdrait de l'info.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def iter_overdue(loans: Iterable[Loan], today: int) -> Iterator[Loan]:
    for loan in loans:
        if loan.due_date < today:
            yield loan
