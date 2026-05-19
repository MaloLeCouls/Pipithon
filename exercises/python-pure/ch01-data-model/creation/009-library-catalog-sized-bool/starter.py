"""Une bibliothèque modélise son catalogue.

Implémente DEUX classes :

1. `Book`
   - `__init__(self, isbn: str, title: str)`.
   - `__repr__` : Book(isbn='978-2', title='Dune').

2. `Catalog`
   - `__init__(self, books: list[Book])`.
   - `__len__` : nombre de livres.
   - `__getitem__(self, index: int)` : le Book à cette position.
   - `__repr__` : Catalog(2 books).
   - On doit pouvoir écrire `if catalog:` pour savoir s'il contient des livres.
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Catalog:
    def __init__(self, books: list[Book]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, index: int) -> Book:
        ...

    def __repr__(self) -> str:
        ...
