"""Choix de design :
- copy.deepcopy descend récursivement : dict copié, listes copiées, str copiées
  (les str sont immutables donc l'optimisation interne les partage — c'est OK).
- Alternative manuelle : {k: list(v) for k, v in cat.items()} — mais deepcopy
  est plus robuste si on étend le catalogue à 3 niveaux plus tard.
"""
from __future__ import annotations

import copy


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    return copy.deepcopy(cat)
