"""Le « test ferme la doc » du chapitre 7, façon Fluent Python.

Reproduis le canonique `BingoCage` : un objet callable qui pop un élément
de sa liste à chaque appel, dans un ordre déterministe (graine fournie).

Implémente `class BingoCage` :
- `__init__(self, items: Iterable[str], seed: int = 0)` :
    * stocke une COPIE des items (ne tient pas la liste de l'appelant),
    * mélange-la avec random.Random(seed).shuffle(...) pour avoir un ordre
      déterministe testable.
- `__call__(self) -> str` :
    * pop et retourne un item ;
    * lève LookupError("empty BingoCage") si vide.
- `pick(self) -> str` : alias de __call__ (commodité).
"""
from __future__ import annotations

from collections.abc import Iterable


class BingoCage:
    def __init__(self, items: Iterable[str], seed: int = 0) -> None:
        ...

    def pick(self) -> str:
        ...

    def __call__(self) -> str:
        ...
