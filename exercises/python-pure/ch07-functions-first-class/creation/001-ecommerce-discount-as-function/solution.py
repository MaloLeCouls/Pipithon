"""Choix de design :
- apply_discount ne sait rien des stratégies : il les utilise. C'est l'essence
  des fonctions « first-class » : passées comme n'importe quelle autre valeur.
- flat_5 retourne max(..., 0) pour éviter un prix négatif (cas limite métier).
"""
from __future__ import annotations

from collections.abc import Callable


def half_off(price: float) -> float:
    return price * 0.5


def flat_5(price: float) -> float:
    return max(price - 5, 0)


def apply_discount(price: float, discount_fn: Callable[[float], float]) -> float:
    return discount_fn(price)
