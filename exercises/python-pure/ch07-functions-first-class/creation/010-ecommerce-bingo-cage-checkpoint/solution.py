"""Choix de design (canonique Fluent Python ch.7) :
- random.Random(seed).shuffle(...) : tirage REPRODUCTIBLE pour les tests.
- list(items) : copie défensive ; l'appelant peut muter sa source.
- pick() pop ; LookupError est l'exception canonique de Python pour
  « la collection est vide ».
- __call__ aliase pick : c'est l'astuce qui fait l'instance « appelable comme
  une fonction ».
"""
from __future__ import annotations

import random
from collections.abc import Iterable


class BingoCage:
    def __init__(self, items: Iterable[str], seed: int = 0) -> None:
        self._items = list(items)
        random.Random(seed).shuffle(self._items)

    def pick(self) -> str:
        try:
            return self._items.pop()
        except IndexError as exc:
            raise LookupError("empty BingoCage") from exc

    def __call__(self) -> str:
        return self.pick()
