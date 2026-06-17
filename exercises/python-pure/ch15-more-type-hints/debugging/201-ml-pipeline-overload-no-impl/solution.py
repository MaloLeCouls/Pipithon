"""Fix : enlever `@overload` de l'impl finale. Les stubs `@overload`
décrivent les signatures ; la fn non décorée fournit le corps réel.
"""
from __future__ import annotations

from typing import overload


@overload
def normalize(x: int) -> float: ...


@overload
def normalize(x: list[int]) -> list[float]: ...


def normalize(x: int | list[int]) -> float | list[float]:
    if isinstance(x, int):
        return float(x)
    return [float(i) for i in x]
