"""Tu factures les tokens consommés via une classe `Cost`. `__format__`
devrait permettre `f"{cost:.4f}"` pour afficher 4 décimales. Mais
l'appel pète tout de suite avec `RecursionError`.

Indices :
- Dans `__format__`, écrire `f"{self:spec}"` ré-appelle... `self.__format__(spec)`.
  Récursion infinie.
- Fix : formate l'ATTRIBUT NUMÉRIQUE, pas `self`. `format(self.amount, spec)`
  délègue à `float.__format__` qui sait gérer `.4f`.
"""
from __future__ import annotations


class Cost:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __format__(self, spec: str) -> str:
        # BUG : f"{self:spec}" relance self.__format__ -> RecursionError.
        return f"{self:{spec}}€" if spec else f"{self.amount}€"
