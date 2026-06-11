"""Choix de design (canonique 3 étages) :
- Niveau 1 : timed(label) — accepte les paramètres.
- Niveau 2 : decorator(fn) — accepte la fonction à décorer.
- Niveau 3 : wrapper(*args, **kwargs) — l'enveloppe d'exécution.
Chaque niveau capture le précédent en closure.
"""
from __future__ import annotations

TIMINGS: list[tuple[str, object]] = []


def timed(label: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            TIMINGS.append((label, result))
            return result
        return wrapper
    return decorator
