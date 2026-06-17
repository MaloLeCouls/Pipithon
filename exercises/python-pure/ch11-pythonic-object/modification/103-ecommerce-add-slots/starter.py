"""Cette `LineItem` est utilisée par MILLIONS dans un export comptable.
Sans `__slots__`, chaque instance porte un `__dict__` complet — pour
3 attributs ça représente des MB inutiles à grande échelle.

Refactore :
- Ajoute `__slots__ = (\"sku\", \"quantity\", \"unit_price\")`.
- Comportement inchangé, mais plus de `__dict__` et plus d'attributs
  inattendus possibles.
"""
from __future__ import annotations


class LineItem:
    def __init__(self, sku: str, quantity: int, unit_price: float) -> None:
        self.sku = sku
        self.quantity = quantity
        self.unit_price = unit_price

    def subtotal(self) -> float:
        return self.quantity * self.unit_price
