"""Cette fonction prétend que `coupon` est un str, mais elle accepte None
par défaut. L'annotation ment.

Refactor : annonce `str | None` (PEP 604) pour `coupon`.
"""
from __future__ import annotations


def apply(price: float, coupon: str = None) -> float:  # type: ignore[assignment]
    if coupon is None:
        return price
    return price * 0.9
