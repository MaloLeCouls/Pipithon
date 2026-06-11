"""Un fabricant de meubles maintient un catalogue par section.
On veut pouvoir cloner le catalogue, modifier le clone (ex. pour simuler
des promotions), SANS toucher à l'original.

BUG : la fonction `clone_catalog` utilise un mauvais outil. Le clone et
l'original partagent les listes internes.

Corrige.
"""
from __future__ import annotations

import copy


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    return copy.copy(cat)
