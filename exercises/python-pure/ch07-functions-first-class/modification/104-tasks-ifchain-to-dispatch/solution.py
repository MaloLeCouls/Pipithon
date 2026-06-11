"""Choix de design :
- Dict de fonctions construit au niveau module (évalué une fois, pas à chaque
  appel).
- Lookup O(1), ajout d'une action = ajout d'une entrée, sans toucher au
  dispatcher.
- KeyError native du dict : pas besoin de la lever à la main.
"""
from __future__ import annotations

from collections.abc import Callable

_ACTIONS: dict[str, Callable[[dict], str]] = {
    "close": lambda t: f"closed:{t['title']}",
    "reopen": lambda t: f"reopened:{t['title']}",
    "tag": lambda t: f"tagged:{t['title']}",
}


def apply_action(task: dict, action: str) -> str:
    return _ACTIONS[action](task)
