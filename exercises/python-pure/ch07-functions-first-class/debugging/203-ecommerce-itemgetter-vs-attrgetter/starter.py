"""On veut trier des Order (dataclass) par total décroissant.
L'auteur a tapé `itemgetter` au lieu de `attrgetter` — TypeError au sort.

Corrige : import + nom utilisé.
"""
from __future__ import annotations

from dataclasses import dataclass
from operator import itemgetter


@dataclass
class Order:
    id: str
    total: float


def top_orders(orders: list[Order]) -> list[Order]:
    return sorted(orders, key=itemgetter("total"), reverse=True)
