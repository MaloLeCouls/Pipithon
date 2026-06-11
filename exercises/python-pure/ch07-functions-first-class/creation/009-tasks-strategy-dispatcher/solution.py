"""Choix de design :
- Closure simple : la fonction renvoyée capture `strategies`.
- strategies[name] est un lookup O(1) ; lève KeyError si name est absent —
  c'est le comportement attendu, on ne le masque pas.
- Préférable à un if/elif/else : ajouter une stratégie = ajouter une entrée
  au dict, pas modifier le dispatcher.
"""
from __future__ import annotations

from collections.abc import Callable


def make_dispatcher(
    strategies: dict[str, Callable[[dict], str]],
) -> Callable[[str, dict], str]:
    def dispatch(name: str, task: dict) -> str:
        return strategies[name](task)
    return dispatch
