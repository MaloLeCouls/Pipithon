"""Choix de design :
- Check `isinstance` AVANT d'accéder à `.code` : sans ça, comparer un
  `Coupon` à un `int` lèverait `AttributeError` au lieu de `False`.
- `NotImplemented` (singleton, pas `False`) : Python essaie alors
  `other.__eq__(self)` ; si lui aussi renvoie `NotImplemented`, Python
  conclut False. C'est la convention pour les opérateurs binaires.
"""
from __future__ import annotations


class Coupon:
    def __init__(self, code: str, discount_rate: float) -> None:
        self.code = code
        self.discount_rate = discount_rate

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coupon):
            return NotImplemented
        return self.code == other.code and self.discount_rate == other.discount_rate
