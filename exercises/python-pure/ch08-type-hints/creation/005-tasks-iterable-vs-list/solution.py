"""Choix de design :
- Iterable[dict] en paramètre : le code n'a besoin que de l'itération.
  Demander list[dict] serait trop restrictif (rejetterait tuple, set, generator).
- int en retour : précis, garantissable.
"""
from __future__ import annotations

from collections.abc import Iterable


def count_at_priority(tasks: Iterable[dict], priority: int) -> int:
    return sum(1 for t in tasks if t["priority"] == priority)
