"""Choix de design :
- stops : list[dict[str, int]] — mypy --strict refuse les generics non paramétrés.
- Une version plus stricte typerait `dict[str, int]` en TypedDict — hors scope ici.
- total_distance renvoie float pour rester simple (coercion via float()).
"""
from __future__ import annotations


def total_distance(stops: list[dict[str, int]]) -> float:
    return float(sum(s["km"] for s in stops))


def average_per_stop(stops: list[dict[str, int]]) -> float:
    if not stops:
        return 0.0
    return total_distance(stops) / len(stops)
