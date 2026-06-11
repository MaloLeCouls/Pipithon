"""Une boutique veut un générateur de numéros de commande croissants.

Implémente `make_counter(start: int = 0)` qui renvoie une fonction sans
argument. À chaque appel, elle incrémente le compteur de 1 et renvoie sa
valeur (donc le 1er appel renvoie start+1).

Exemple :
    c = make_counter()
    c()  # 1
    c()  # 2
    c()  # 3
"""
from __future__ import annotations

from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    ...
