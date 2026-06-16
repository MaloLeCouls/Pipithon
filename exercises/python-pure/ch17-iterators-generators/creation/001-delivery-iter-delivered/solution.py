"""Choix de design :
- Generator function : `yield` dans le corps, retourne un Iterator sans
  builder de liste intermédiaire. Mémoire O(1) même sur 1M de colis.
- `Iterable[Package]` en entrée (pas `list`) : on accepte tout — un autre
  générateur, un set, une queue paresseuse.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Package:
    def __init__(self, tracking_id: str, status: str) -> None:
        self.tracking_id = tracking_id
        self.status = status


def iter_delivered(packages: Iterable[Package]) -> Iterator[str]:
    for pkg in packages:
        if pkg.status == "delivered":
            yield pkg.tracking_id
