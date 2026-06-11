"""Un dispatcher de stratégies : tu lui donnes un dict {nom_stratégie:
fonction} et il te renvoie une fonction qui sait choisir la bonne par son nom.

Implémente `make_dispatcher(strategies: dict[str, Callable[[dict], str]])
-> Callable[[str, dict], str]` qui renvoie une fonction `dispatch(name, task)`.

- dispatch("triage", {"title": "x"}) doit appeler strategies["triage"]({"title": "x"}).
- Si `name` n'est pas dans le dict, lève KeyError.

Ce pattern est partout : preview du Strategy pattern du ch10 et des samplers
du framework pymistral (ch >= 8).
"""
from __future__ import annotations

from collections.abc import Callable


def make_dispatcher(
    strategies: dict[str, Callable[[dict], str]],
) -> Callable[[str, dict], str]:
    ...
