"""Une plateforme de streaming veut recommander des films selon un critère
arbitraire : « durée < 2 h », « genre = comedy », etc.

Implémente `recommend(movies: list[Movie], criteria: Callable[[Movie], bool])
-> list[Movie]` qui renvoie les films satisfaisant `criteria`, dans l'ordre
d'entrée.

Le point clé : `recommend` ne sait RIEN du critère ; elle l'applique, c'est tout.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    duration_min: int
    genre: str


def recommend(movies: list[Movie], criteria: Callable[[Movie], bool]) -> list[Movie]:
    ...
