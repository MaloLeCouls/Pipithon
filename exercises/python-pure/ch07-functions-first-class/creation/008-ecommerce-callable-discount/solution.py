"""Choix de design :
- __call__ rend l'instance appelable : `d(price)` -> `d.__call__(price)`.
- Stocker `rate` à __init__ est le pattern naturel pour une fonction
  partiellement appliquée mais stateful.
- Alternative équivalente : functools.partial sur une fonction nue ; ici
  l'avantage de la classe est qu'elle peut s'étendre (méthodes, attributs).
"""
from __future__ import annotations


class PercentageDiscount:
    def __init__(self, rate: float) -> None:
        self.rate = rate

    def __call__(self, price: float) -> float:
        return price * (1 - self.rate)
