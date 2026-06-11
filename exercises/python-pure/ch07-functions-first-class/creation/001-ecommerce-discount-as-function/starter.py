"""Une plateforme e-commerce applique plusieurs stratégies de remise.
Plutôt que de coder un if-else, on passe la stratégie EN ARGUMENT.

Implémente :
- `half_off(price)` -> prix * 0.5
- `flat_5(price)` -> max(price - 5, 0)
- `apply_discount(price, discount_fn)` -> discount_fn(price)
"""
from __future__ import annotations

from collections.abc import Callable


def half_off(price: float) -> float:
    ...


def flat_5(price: float) -> float:
    ...


def apply_discount(price: float, discount_fn: Callable[[float], float]) -> float:
    ...
