"""Une pipeline ML accumule des features dans une liste passée en paramètre.
L'auteur a typé `list[int]` et mis `=[]` en pensant que les hints
empêcheraient le piège du défaut mutable.

BUG : les hints ne sont QUE des annotations — Python évalue `[]` une seule
fois à la définition, comme avant. Toutes les invocations partagent la liste.

Corrige :
- annonce `list[int] | None = None`,
- instancie une liste fraîche si None,
- append la feature et retourne la liste.
"""
from __future__ import annotations


def accumulate(feature: int, acc: list[int] = []) -> list[int]:  # noqa: B006
    acc.append(feature)
    return acc
