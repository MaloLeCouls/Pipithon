"""Choix de design :
- @functools.wraps(fn) recopie __name__, __qualname__, __doc__, __wrapped__,
  __module__, __dict__ depuis fn vers wrapper.
"""
from __future__ import annotations

import functools


def instrument(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        wrapper.__calls__ += 1
        return fn(*args, **kwargs)
    wrapper.__calls__ = 0
    return wrapper
