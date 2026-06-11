"""Choix de design :
- Default = None ; allocation d'une liste fraîche dans le corps.
- Préserve la signature (mêmes noms, mêmes types) pour ne casser aucun appelant.
"""
from __future__ import annotations


def dispatch(package: str, log: list[str] | None = None) -> list[str]:
    if log is None:
        log = []
    log.append(package)
    return log
