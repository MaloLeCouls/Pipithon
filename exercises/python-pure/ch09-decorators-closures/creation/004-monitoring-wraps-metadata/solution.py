"""Choix de design :
- @functools.wraps(fn) copie __name__, __qualname__, __doc__, __wrapped__,
  __module__, __dict__. Sans ça, debug et introspection sont perdus.
- wrapper.__calls__ persiste sur l'objet renvoyé.
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
