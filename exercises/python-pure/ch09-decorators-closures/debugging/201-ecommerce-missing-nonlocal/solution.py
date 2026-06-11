"""Bug : `count += 1` rend `count` locale -> UnboundLocalError à la lecture.
Fix : `nonlocal count` dans le corps interne.
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
