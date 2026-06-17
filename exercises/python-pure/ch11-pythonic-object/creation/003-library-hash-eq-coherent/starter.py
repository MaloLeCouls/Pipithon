"""Tu veux utiliser des `Book` comme clés de set/dict (déduplication
de catalogue, par exemple). Pour ça : `__hash__` + `__eq__` cohérents.

Contrat :

- Classe `Book(isbn: str, title: str)`.
- Attributs READ-ONLY exposés via `@property` (les sous-jacents sont
  stockés en `_isbn`/`_title`).
- `__eq__` : True si même `isbn` ET même `title`. NotImplemented sinon.
- `__hash__` : `hash((self.isbn, self.title))`.

Règle d'or : si `a == b` alors `hash(a) == hash(b)`. C'est ce qui rend
le set/dict cohérent.
"""
from __future__ import annotations


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self._isbn = isbn
        self._title = title

    @property
    def isbn(self) -> str:
        raise NotImplementedError("À implémenter")

    @property
    def title(self) -> str:
        raise NotImplementedError("À implémenter")

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("À implémenter")

    def __hash__(self) -> int:
        raise NotImplementedError("À implémenter")
