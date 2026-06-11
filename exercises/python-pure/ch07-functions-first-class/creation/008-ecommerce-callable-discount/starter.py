"""Une politique de remise peut avoir un état (un taux configuré). Plutôt
qu'une closure, on utilise une CLASSE callable.

Implémente `class PercentageDiscount` :
- `__init__(self, rate: float)` stocke le taux (0..1).
- `__call__(self, price: float) -> float` renvoie `price * (1 - rate)`.

Une instance doit s'utiliser comme une fonction : `d = PercentageDiscount(0.2)` ;
`d(100)` doit renvoyer 80.
"""
from __future__ import annotations


class PercentageDiscount:
    def __init__(self, rate: float) -> None:
        ...

    def __call__(self, price: float) -> float:
        ...
