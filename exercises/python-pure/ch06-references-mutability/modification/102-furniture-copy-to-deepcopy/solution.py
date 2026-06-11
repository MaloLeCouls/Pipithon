"""Choix de design :
- copy.deepcopy descend récursivement : dict copié, listes copiées.
- L'API ne change pas.
"""
from __future__ import annotations

import copy


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    return copy.deepcopy(cat)
