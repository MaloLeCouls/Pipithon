"""Cette classe `Book` définit `__hash__` mais PAS `__eq__`. Conséquence :
`a == b` utilise l'identité (`object.__eq__`), donc deux Book avec le
même contenu ne sont PAS égaux, ALORS QUE leur hash matche.

Résultat : le set/dict est incohérent. C'est un bug subtil.

Refactore : ajoute `__eq__` cohérent avec `__hash__` (par valeur sur
isbn + title).
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __hash__(self) -> int:
        return hash((self.isbn, self.title))
