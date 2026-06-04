"""Une bibliothèque trace ses livres dans ses logs : sans `__repr__`, chaque
ligne ressemble à `<Book object at 0x7f3e9c00>` — inutile pour débugger.

`__repr__` est la méthode appelée par `repr(obj)` (et par le REPL, les
exceptions, les logs). Elle **renvoie** une `str` — elle ne l'affiche pas.
La chaîne doit être *non ambiguë* : un dev qui la lit doit pouvoir
reconstruire l'objet. Convention idiomatique : ressembler à l'appel
constructeur.

Implémente la classe `Book` :
- `__init__(self, isbn: str, title: str)` stocke `isbn` et `title`.
- `__repr__` **renvoie** EXACTEMENT, pour `Book("978-2", "Dune")` :
  Book(isbn='978-2', title='Dune')
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        ...

    def __repr__(self) -> str:
        ...
