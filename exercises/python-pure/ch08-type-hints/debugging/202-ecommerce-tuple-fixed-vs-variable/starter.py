"""Cette fonction calcule la somme d'une suite de prix.
L'annotation actuelle prétend que `prices` est un tuple de longueur 1
(tuple[int] = (int,)) — mais l'appelant lui passe (10, 20, 30).

Le test de signature vérifie qu'on a bien `tuple[int, ...]` désormais.

Corrige l'annotation. Le corps est correct.
"""
from __future__ import annotations


def total(prices: tuple[int]) -> int:
    return sum(prices)
