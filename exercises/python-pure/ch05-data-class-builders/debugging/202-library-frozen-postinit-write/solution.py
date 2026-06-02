"""Correction :
- Bug : `self.isbn_norm = ...` dans __post_init__ passe par
  __setattr__, qui leve FrozenInstanceError parce que la classe
  est frozen=True. Frozen interdit TOUTE affectation normale, y
  compris pendant la construction.
- Fix : `object.__setattr__(self, 'isbn_norm', ...)` court-circuite
  le __setattr__ frozen. C'est l'idiome documente pour initialiser
  un champ derive sur une dataclass frozen.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:
    isbn: str
    title: str
    isbn_norm: str = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "isbn_norm", self.isbn.replace("-", "").upper())
