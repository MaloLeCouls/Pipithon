"""Choix de design (canonique Fluent Python ch.8) :
- 3 paramètres entièrement annotés (int, str, str).
- Retour str, pas de branche silencieuse non typée.
- plural par défaut '' (sentinelle non-mutable, autorisée car str immutable).
"""
from __future__ import annotations


def show_count(count: int, singular: str, plural: str = "") -> str:
    if count == 1:
        return f"1 {singular}"
    count_str = str(count)
    if not plural:
        plural = singular + "s"
    return f"{count_str} {plural}"
