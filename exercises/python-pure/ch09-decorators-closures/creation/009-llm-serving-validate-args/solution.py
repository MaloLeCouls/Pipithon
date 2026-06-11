"""Choix de design :
- inspect.signature(fn) une seule fois à la décoration (économe en CPU).
- On localise le paramètre GenerationConfig par nom (la signature de fn doit
  l'avoir explicitement comme paramètre nommé `config`).
- bind() résout positional/keyword automatiquement.
"""
from __future__ import annotations

import inspect

from pymistral import GenerationConfig


def validate_temperature(fn):
    sig = inspect.signature(fn)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        cfg = bound.arguments.get("config")
        if isinstance(cfg, GenerationConfig) and cfg.temperature < 0.5:
            raise ValueError(f"temperature too low: {cfg.temperature}")
        return fn(*args, **kwargs)
    return wrapper
