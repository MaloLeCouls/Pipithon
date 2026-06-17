"""Fix : déléguer à `format(self.amount, spec)` — c'est `float.__format__`
qui consomme le spec. Aucune récursion.

Pattern général : dans un `__format__`, NE JAMAIS faire `f"{self:...}"`.
Toujours appeler `format(attribute, spec)` ou construire la str à la main.
"""
from __future__ import annotations


class Cost:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __format__(self, spec: str) -> str:
        if spec:
            return f"{format(self.amount, spec)}€"
        return f"{self.amount}€"
