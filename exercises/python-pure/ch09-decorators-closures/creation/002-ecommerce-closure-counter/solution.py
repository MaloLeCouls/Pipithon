"""Choix de design :
- nonlocal indispensable : sans, `count += 1` ferait de count une variable
  locale et lèverait UnboundLocalError à la lecture.
- Closure : la fonction interne « se souvient » de count entre les appels.
"""
from __future__ import annotations

from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    count = start
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter
