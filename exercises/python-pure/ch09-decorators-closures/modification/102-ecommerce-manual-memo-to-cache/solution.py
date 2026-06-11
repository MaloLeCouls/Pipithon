"""Choix de design :
- @functools.cache : un dict interne géré par functools, expose cache_info et
  cache_clear. Plus de boilerplate.
"""
from __future__ import annotations

import functools


@functools.cache
def compute_total(price: int, rate: float) -> float:
    return price * (1 - rate)
