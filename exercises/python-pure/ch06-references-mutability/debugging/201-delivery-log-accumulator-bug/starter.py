"""Le centre de tri ouvre un journal pour CHAQUE trajet de camion.
Sauf que tous les trajets partagent le même journal et finissent par avoir
toute l'histoire du dépôt dedans.

Corrige le bug. Une ligne suffit, pas de réécriture.
"""
from __future__ import annotations


def log_trip(package: str, log: list[str] = []) -> list[str]:  # noqa: B006
    log.append(package)
    return log
