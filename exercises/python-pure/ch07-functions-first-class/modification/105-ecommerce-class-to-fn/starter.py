"""Cette « classe » est un objet stateless : son __init__ stocke un taux,
sa méthode apply l'utilise. C'est une fonction déguisée.

Refactor :
1. Crée une fonction `discount(price: float, rate: float) -> float` qui calcule
   `price * (1 - rate)`.
2. Crée `make_discount(rate: float)` qui renvoie une fonction spécialisée via
   `functools.partial(discount, rate=rate)`.

Les tests de forme vérifient que la classe `PercentageDiscount` a DISPARU.
"""
from __future__ import annotations


class PercentageDiscount:
    def __init__(self, rate: float) -> None:
        self.rate = rate

    def apply(self, price: float) -> float:
        return price * (1 - self.rate)
