"""Choix de design :
- *args, **kwargs : transparent à toute signature.
- Pas besoin d'inspecter — on délègue tel quel à fn.
"""
from __future__ import annotations

TRACES: list[str] = []


def trace(fn):
    def wrapper(*args, **kwargs):
        TRACES.append(fn.__name__)
        return fn(*args, **kwargs)
    return wrapper
