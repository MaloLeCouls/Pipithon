"""Choix de design :
- wrapper transparent (*args, **kwargs).
- log AFTER call : on a besoin du résultat.
- args[0] = Logits (premier argument positionnel d'un sampler).
"""
from __future__ import annotations

SAMPLE_LOG: list[tuple[int, int]] = []


def log_sampler(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        SAMPLE_LOG.append((result, len(args[0])))
        return result
    return wrapper
