"""Tu charges un catalogue depuis un CSV. Plutôt qu'une fn `parse_book`
externe, expose un **constructeur alternatif** via `@classmethod`.

Contrat :

- Classe `Book(isbn: str, title: str)`.
- `Book.from_csv_line(cls, line: str)` (`@classmethod`) :
  - parse `line` au format `"978-001,Refactoring"`,
  - renvoie `cls(isbn, title)`.
- `cls(...)` est crucial : si on sous-classe `Book` en `RareBook`,
  `RareBook.from_csv_line(...)` renvoie bien un `RareBook`, pas un `Book`.
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    @classmethod
    def from_csv_line(cls, line: str) -> "Book":
        raise NotImplementedError("À implémenter")
