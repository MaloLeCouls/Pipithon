"""Une flotte de livraison maintient plusieurs « routes » en mémoire.
Certaines, par erreur, pointent vers le même objet (alias).

Implémente `aliased_pairs(routes: list[list[str]]) -> list[tuple[int, int]]`
qui renvoie toutes les paires d'indices (i, j) avec i < j telles que
`routes[i] is routes[j]`.

Liste triée par ordre lexicographique (i, j) croissant.
"""
from __future__ import annotations


def aliased_pairs(routes: list[list[str]]) -> list[tuple[int, int]]:
    ...
