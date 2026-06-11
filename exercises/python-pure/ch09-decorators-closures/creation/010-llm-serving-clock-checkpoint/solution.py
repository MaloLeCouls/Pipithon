"""Choix de design (canonique Fluent Python ch.9) :
- clock(fmt) : 3 niveaux + @functools.wraps.
- _TICK déterministe : pas de time.perf_counter() ici (rend les tests
  reproductibles). En production on remplacerait par perf_counter avant/après.
- make_averager : closure (total, count) + nonlocal — pattern exact du livre.
"""
from __future__ import annotations

import functools
from collections.abc import Callable

CLOCK_LOG: list[str] = []
_TICK = 0


def clock(fmt: str):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            global _TICK
            _TICK += 1
            start = _TICK
            result = fn(*args, **kwargs)
            _TICK += 1
            elapsed = _TICK - start
            CLOCK_LOG.append(fmt.format(name=fn.__name__, elapsed=elapsed, result=result))
            return result
        return wrapper
    return decorator


def make_averager() -> Callable[[float], float]:
    total = 0.0
    count = 0
    def averager(new_value: float) -> float:
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return averager
