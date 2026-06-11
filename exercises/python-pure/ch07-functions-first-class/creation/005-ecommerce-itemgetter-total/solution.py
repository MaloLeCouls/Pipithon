"""Choix de design :
- operator.itemgetter('total') est une fonction préfabriquée qui fait
  `lambda x: x['total']` — mais en C, plus rapide, et plus déclarative.
- reverse=True pour ordre décroissant.
"""
from __future__ import annotations

from operator import itemgetter


def top_orders(orders: list[dict]) -> list[dict]:
    return sorted(orders, key=itemgetter("total"), reverse=True)
