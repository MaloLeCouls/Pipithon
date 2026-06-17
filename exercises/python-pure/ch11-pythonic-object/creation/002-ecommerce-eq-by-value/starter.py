"""Un `Coupon` doit s'égaler par valeur (code), pas par identité.

Contrat :

- Classe `Coupon(code: str, discount_rate: float)`.
- `__eq__(self, other)` :
  - si `other` n'est pas un `Coupon` → renvoie `NotImplemented`,
  - sinon True si `self.code == other.code` ET `self.discount_rate == other.discount_rate`.

Notes :
- Renvoyer `NotImplemented` (pas False) permet à Python d'essayer
  `other.__eq__(self)` — c'est la convention.
- Ne pas implémenter `__hash__` : il devient automatiquement None
  quand on définit `__eq__`, et donc l'objet n'est plus hashable.
  C'est volontaire (cf. exo 003).
"""
from __future__ import annotations


class Coupon:
    def __init__(self, code: str, discount_rate: float) -> None:
        self.code = code
        self.discount_rate = discount_rate

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("À implémenter")
