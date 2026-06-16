"""Le module bibliothèque expose `overdue_summary(loans, today)` qui retourne
le couple `(count, isbns)` des emprunts en retard. Sur certains datasets,
`count` est correct mais `isbns` est vide — alors qu'on a bien des emprunts
en retard. Le bug est silencieux : aucune exception levée.

Trouve la cause et corrige le code. Le comportement attendu : `count` ET
`isbns` doivent être cohérents (même nombre, mêmes éléments).
"""
from __future__ import annotations

from collections.abc import Iterable


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def overdue_summary(loans: Iterable[Loan], today: int) -> tuple[int, list[str]]:
    # BUG : `overdue` est une generator expression — paresseuse, à usage
    # unique. Le `sum(1 for _ in overdue)` la consomme entièrement. La ligne
    # suivante itère sur le même objet, déjà épuisé : la liste sort vide.
    overdue = (loan for loan in loans if loan.due_date < today)
    count = sum(1 for _ in overdue)
    isbns = [loan.isbn for loan in overdue]
    return count, isbns
