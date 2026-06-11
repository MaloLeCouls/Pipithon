"""Bug : itemgetter('total')(order) ferait order['total'] — un dataclass n'a
pas __getitem__ par défaut.

Fix : attrgetter('total')(order) -> order.total.
"""
from __future__ import annotations

from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Order:
    id: str
    total: float


def top_orders(orders: list[Order]) -> list[Order]:
    return sorted(orders, key=attrgetter("total"), reverse=True)
