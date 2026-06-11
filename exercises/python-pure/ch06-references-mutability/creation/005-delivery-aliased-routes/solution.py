"""Choix de design :
- `is` est exigé : deux routes peuvent être ==  sans être le même objet.
- O(n²) est acceptable ici (n petit). Pour des routes nombreuses, on grouperait
  par id() puis on émettrait les paires par groupe.
"""
from __future__ import annotations


def aliased_pairs(routes: list[list[str]]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for i in range(len(routes)):
        for j in range(i + 1, len(routes)):
            if routes[i] is routes[j]:
                pairs.append((i, j))
    return pairs
