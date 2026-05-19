"""Une bibliothèque veut tracer ses livres proprement dans ses logs.

Implémente la classe `Book` :
- `__init__(self, isbn: str, title: str)` stocke `isbn` et `title`.
- `__repr__` renvoie EXACTEMENT : Book(isbn='978-2', title='Dune')
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        ...

    def __repr__(self) -> str:
        ...
