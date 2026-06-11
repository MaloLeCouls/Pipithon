"""Un compteur de commandes, version closure. Premier appel : UnboundLocalError.

Corrige. UNE ligne à ajouter.
"""
from __future__ import annotations

from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    count = start

    def counter() -> int:
        count += 1
        return count

    return counter
