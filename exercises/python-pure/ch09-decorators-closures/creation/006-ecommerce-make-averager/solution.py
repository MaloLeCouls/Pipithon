"""Choix de design (canonique Fluent Python ch.9) :
- total et count sont des variables LIBRES dans la closure.
- nonlocal indispensable pour les RÉ-ASSIGNER (total += ..., count += ...).
- Pas de structure exposée : pas d'attribut, pas d'instance — juste la
  fonction renvoyée.
"""
from __future__ import annotations

from collections.abc import Callable


def make_averager() -> Callable[[float], float]:
    total = 0.0
    count = 0
    def averager(new_value: float) -> float:
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return averager
