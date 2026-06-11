"""Bug : copy.copy fait une copie superficielle. Le dict racine est dupliqué,
mais les listes internes restent les mêmes objets.

Fix chirurgical : copy.deepcopy.
"""
from __future__ import annotations

import copy


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    return copy.deepcopy(cat)
