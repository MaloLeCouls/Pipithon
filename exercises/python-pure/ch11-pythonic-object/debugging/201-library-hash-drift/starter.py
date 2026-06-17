"""Bug observé : un `Book` est ajouté à un set ; on mute son `title` ;
soudain `book in set` est False. Pire : aucune exception, le set est
silencieusement cassé.

Indices :
- `__hash__` repose sur `title`.
- Modifier `title` change `hash(book)` — mais le set garde l'ancien
  bucket. L'objet est inaccessible.
- Fix : interdire la mutation. Rends `isbn` et `title` **read-only**
  via `@property` (les sous-jacents en `_isbn`/`_title`).
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.isbn, self.title) == (other.isbn, other.title)

    def __hash__(self) -> int:
        return hash((self.isbn, self.title))
