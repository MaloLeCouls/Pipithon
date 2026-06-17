"""Fix : attributs read-only via `@property` sur les sous-jacents
`_isbn`/`_title`. Toute tentative de mutation lève AttributeError —
l'objet redevient « immutable de facto » et stable comme clé.

Règle d'or chapitre 11 : « hashable ⇒ immutable, en pratique ».
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
        return (self._isbn, self._title) == (other._isbn, other._title)

    def __hash__(self) -> int:
        return hash((self._isbn, self._title))
