"""Choix de design :
- `cls(...)` (pas `Book(...)`) : préserve le polymorphisme. Une sous-classe
  appelant `Sub.from_csv_line(line)` reçoit un `Sub`, pas un `Book`.
- `split(',', 1)` : ne casse que sur le PREMIER `,` — sinon les titres
  avec virgules seraient massacrés.
- C'est le pattern le plus commun de `classmethod` : « constructeur
  alternatif » (cf. `dict.fromkeys`, `datetime.fromisoformat`).
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    @classmethod
    def from_csv_line(cls, line: str) -> "Book":
        isbn, title = line.split(",", 1)
        return cls(isbn, title)
