"""Un planificateur de routes utilise un lambda assigné à une variable.
PEP 8 dit non : si tu donnes un nom à un lambda, utilise un def.

Refactor : `next_hop` doit devenir une fonction `def` correctement nommée.
Les tests vérifient que `next_hop.__name__ == "next_hop"` (plus '<lambda>').
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Route:
    depot: str
    stops: list[str]


next_hop = lambda r: r.stops[0] if r.stops else r.depot  # noqa: E731
