"""Choix de design :
- `str | None` reflète la vraie sémantique du paramètre.
- Le comportement reste identique.
"""
from __future__ import annotations


def apply(price: float, coupon: str | None = None) -> float:
    if coupon is None:
        return price
    return price * 0.9
