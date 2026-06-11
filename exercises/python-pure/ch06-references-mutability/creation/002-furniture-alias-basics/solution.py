"""Choix de design :
- Une assignation `view = catalog` crée une référence partagée, pas une copie.
- L'append via view est visible via catalog (même objet).
- Une réassignation `view = ["NEW"]` change *où* view pointe, sans toucher
  l'objet d'origine — catalog reste intact.
"""
from __future__ import annotations


def mutation_is_shared(catalog: list[str]) -> bool:
    view = catalog
    view.append("EXTRA")
    return "EXTRA" in catalog


def rebind_is_isolated(catalog: list[str]) -> bool:
    snapshot = list(catalog)
    view = catalog
    view = ["NEW"]
    _ = view  # used to keep ruff happy; rebinding is the point
    return catalog == snapshot
