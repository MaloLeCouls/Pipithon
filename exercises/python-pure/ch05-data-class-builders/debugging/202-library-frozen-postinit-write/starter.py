"""Book est immutable (frozen=True) et calcule une cle normalisee
(isbn sans tirets, en majuscules) au moment de la construction.

Aujourd'hui Book(...) leve FrozenInstanceError. Corrige sans
retirer frozen=True : l'immutabilite est voulue (Book est utilise
comme cle de dict ailleurs).
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:
    isbn: str
    title: str
    isbn_norm: str = field(init=False)

    def __post_init__(self) -> None:
        self.isbn_norm = self.isbn.replace("-", "").upper()
