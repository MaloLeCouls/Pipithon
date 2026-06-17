"""Choix de design :
- `__slots__` figé sur les seuls attributs métier. Layout fixe en mémoire,
  pas de `__dict__`, pas de fautes de frappe silencieuses.
- API publique inchangée : `LineItem(sku, qty, price).subtotal()` continue
  de marcher exactement comme avant.
"""
from __future__ import annotations


class LineItem:
    __slots__ = ("sku", "quantity", "unit_price")

    def __init__(self, sku: str, quantity: int, unit_price: float) -> None:
        self.sku = sku
        self.quantity = quantity
        self.unit_price = unit_price

    def subtotal(self) -> float:
        return self.quantity * self.unit_price
