"""Une boutique veut afficher les plus grosses commandes en premier.

Implémente `top_orders(orders: list[dict]) -> list[dict]` qui renvoie les
commandes triées par 'total' DÉCROISSANT.

Utilise `operator.itemgetter` plutôt qu'un lambda. C'est l'usage canonique
quand on extrait un champ par nom.
"""
from __future__ import annotations


def top_orders(orders: list[dict]) -> list[dict]:
    ...
