"""Choix de design :
- Attributs read-only via `@property` : empêche `book.isbn = "..."`
  d'arriver. Sans ça, on pourrait muter un livre stocké dans un set —
  le hash deviendrait obsolète, set corrompu.
- `__hash__` = `hash((isbn, title))` : un hash de tuple des champs
  identifiants. C'est le pattern standard.
- `__eq__` cohérent avec `__hash__` (mêmes champs).
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self._isbn = isbn
        self._title = title

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def title(self) -> str:
        return self._title

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._isbn == other._isbn and self._title == other._title

    def __hash__(self) -> int:
        return hash((self._isbn, self._title))
