"""Ce décorateur marche, mais il efface l'identité de la fonction décorée :
`instrumented.__name__` vaut 'wrapper' au lieu du vrai nom.

Refactor : ajoute `@functools.wraps(fn)` sur le wrapper interne.
"""
from __future__ import annotations


def instrument(fn):
    def wrapper(*args, **kwargs):
        wrapper.__calls__ += 1
        return fn(*args, **kwargs)
    wrapper.__calls__ = 0
    return wrapper
