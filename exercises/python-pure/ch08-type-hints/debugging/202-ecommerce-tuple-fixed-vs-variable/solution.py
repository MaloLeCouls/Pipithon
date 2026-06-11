"""Bug : tuple[int] = un 1-uple. Ce qu'on veut, c'est tuple[int, ...]
(longueur variable, type uniforme).
"""
from __future__ import annotations


def total(prices: tuple[int, ...]) -> int:
    return sum(prices)
