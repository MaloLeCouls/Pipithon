"""Choix de design :
- `__eq__` aligné sur les MÊMES champs que `__hash__` : isbn + title.
- `NotImplemented` pour les comparaisons avec d'autres types.
- L'invariant `a == b ⇒ hash(a) == hash(b)` est restauré.
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn and self.title == other.title

    def __hash__(self) -> int:
        return hash((self.isbn, self.title))
