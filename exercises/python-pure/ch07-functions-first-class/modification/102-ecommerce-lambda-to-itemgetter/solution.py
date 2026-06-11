"""Choix de design :
- itemgetter('total') est l'équivalent stdlib du lambda. Plus rapide (en C),
  plus déclaratif.
- Idiomatique pour extraire un champ par nom.
"""
from __future__ import annotations

from operator import itemgetter


def top_orders(orders: list[dict]) -> list[dict]:
    return sorted(orders, key=itemgetter("total"), reverse=True)
