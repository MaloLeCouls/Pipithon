"""Choix de design :
- discount est nu, réutilisable, testable indépendamment du taux.
- make_discount produit une fonction spécialisée via partial — c'est
  l'équivalent fonctionnel d'une classe avec un seul paramètre d'init.
- Plus simple à composer (passer à map/filter/sorted-key).
"""
from __future__ import annotations

from collections.abc import Callable
from functools import partial


def discount(price: float, rate: float) -> float:
    return price * (1 - rate)


def make_discount(rate: float) -> Callable[[float], float]:
    return partial(discount, rate=rate)
