"""Tri par 'total' décroissant. Le lambda fait le job mais il y a une version
plus directe dans la stdlib.

Refactor : remplace le lambda par operator.itemgetter.
Le test de forme exige : plus aucun Lambda dans le code.
"""
from __future__ import annotations


def top_orders(orders: list[dict]) -> list[dict]:
    return sorted(orders, key=lambda x: x["total"], reverse=True)
