"""Choix de design :
- copy.deepcopy : descend partout, isole tout. Robuste à l'évolution du schéma
  (ajout d'un 4e niveau).
- Alternative manuelle : {a: [{**b, "reviews": list(b["reviews"])} for b in bs]
  for a, bs in catalog.items()}. Plus rapide en CPU mais fragile : oublier une
  liste mutable plus tard = bug silencieux.
"""
from __future__ import annotations

import copy


def clone_catalog(catalog: dict[str, list[dict]]) -> dict[str, list[dict]]:
    return copy.deepcopy(catalog)
