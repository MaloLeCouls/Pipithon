"""Cette fonction n'itère qu'une fois sur `tasks` — elle n'a aucune raison
d'exiger une `list`.

Refactor : remplace `list[dict]` par `Iterable[dict]`. Le test vérifie
qu'un generator passe désormais.
"""
from __future__ import annotations


def titles(tasks: list[dict]) -> list[str]:
    return [t["title"] for t in tasks]
