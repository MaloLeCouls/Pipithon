"""Choix de design :
- `def` au lieu de lambda nommé : __name__ correct, doc possible, debug plus
  clair (le traceback affichera "next_hop" au lieu de "<lambda>").
- Aucun changement de signature.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Route:
    depot: str
    stops: list[str]


def next_hop(r: Route) -> str:
    return r.stops[0] if r.stops else r.depot
