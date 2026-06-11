"""Le « test ferme la doc » du chapitre 8, façon Fluent Python.

Reproduis `show_count(count, singular, plural='')` :
- 1, 'token'       -> '1 token'
- 0, 'token'       -> '0 tokens'    (pluriel par défaut = singular + 's')
- 3, 'token'       -> '3 tokens'
- 5, 'mouse', 'mice' -> '5 mice'    (pluriel explicite)

Le checkpoint exige :
- signature COMPLÈTEMENT annotée,
- mypy --strict propre (validateur),
- pas de Any, pas d'annotation manquante.
"""
from __future__ import annotations


def show_count(count, singular, plural=""):
    ...
