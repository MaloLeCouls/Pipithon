"""Choix de design : annotations standard. price/rate/retour en float.
"""
from __future__ import annotations


def apply_discount(price: float, rate: float) -> float:
    return price * (1 - rate)
