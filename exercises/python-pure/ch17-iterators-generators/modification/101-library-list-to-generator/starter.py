"""La bibliothèque a écrit `overdue_isbns(loans, today)` qui RETOURNE UNE
LISTE. C'est OK sur 100 emprunts, mais sur 1 million la mémoire saute et
le premier `isbn` n'apparaît qu'à la fin du parcours.

Refactor : convertis-la en **générateur** (mot-clé `yield`). Le comportement
observable doit rester identique (mêmes isbns, dans le même ordre), mais
le retour doit être un Iterator paresseux."""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Loan:
    def __init__(self, isbn: str, due_date: int) -> None:
        self.isbn = isbn
        self.due_date = due_date


def overdue_isbns(loans: Iterable[Loan], today: int) -> Iterator[str]:
    result: list[str] = []
    for loan in loans:
        if loan.due_date < today:
            result.append(loan.isbn)
    return result  # type: ignore[return-value]
