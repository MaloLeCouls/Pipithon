"""Une bibliothèque maintient un index ISBN -> Book *qui ne doit pas
empêcher le garbage collector* de récupérer un Book non référencé ailleurs.

Implémente `build_index(books: list[Book]) -> weakref.WeakValueDictionary`
qui renvoie un index pondéré : si on supprime la liste `books`, l'index doit
se vider tout seul.

`Book` n'utilise pas `__slots__` (les weakrefs nécessitent un __dict__ ou
`__weakref__` dans __slots__).
"""
from __future__ import annotations

import weakref


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title


def build_index(books: list[Book]) -> weakref.WeakValueDictionary[str, Book]:
    ...
