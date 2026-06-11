"""Choix de design :
- wrapper accepte *args, **kwargs : transparent quelle que soit la signature.
- AUDIT_LOG est partagé au niveau module ; suffisant ici (le suivant exo
  introduira functools.wraps pour préserver les métadonnées).
"""
from __future__ import annotations

AUDIT_LOG: list[str] = []


def audit(fn):
    def wrapper(*args, **kwargs):
        AUDIT_LOG.append(fn.__name__)
        return fn(*args, **kwargs)
    return wrapper
