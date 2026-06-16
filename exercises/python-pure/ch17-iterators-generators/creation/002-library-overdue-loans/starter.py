"""Une bibliothèque veut un flux paresseux des emprunts en retard pour
envoyer des relances une par une (sans charger toute la table).

Implémente `iter_overdue(loans, today)` :
- `loans` : itérable de `Loan` (attributs `isbn: str`, `due_date: int`).
- `today` : int — la date courante (en jours depuis une époque arbitraire).
- yield chaque `Loan` dont `due_date < today`.

Générateur (mot-clé `yield`) — pas de liste construite.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def iter_overdue(loans: Iterable[Loan], today: int) -> Iterator[Loan]:
    raise NotImplementedError("À implémenter")
