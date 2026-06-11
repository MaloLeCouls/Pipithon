"""Choix de design (canonique 3 niveaux) :
- tag(label) — niveau 1, accepte les args du décorateur.
- decorator(fn) — niveau 2, accepte la fn à décorer.
- wrapper(*args, **kwargs) — niveau 3, l'enveloppe d'exécution.
"""
from __future__ import annotations

TAGGED: list[tuple[str, object]] = []


def tag(label: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            TAGGED.append((label, result))
            return result
        return wrapper
    return decorator
