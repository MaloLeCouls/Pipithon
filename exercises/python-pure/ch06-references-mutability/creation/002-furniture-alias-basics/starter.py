"""Un entrepôt de meubles a un catalogue (liste de références).
Démontre la sémantique d'alias en Python en implémentant deux fonctions :

- `mutation_is_shared(catalog)` -> bool
  Crée un alias `view = catalog`, ajoute "EXTRA" via `view`, et renvoie True
  si la mutation est visible depuis `catalog`.

- `rebind_is_isolated(catalog)` -> bool
  Crée un alias `view = catalog`, réassigne `view = ["NEW"]`, et renvoie True
  si `catalog` n'a PAS été affecté par cette réassignation.
"""
from __future__ import annotations


def mutation_is_shared(catalog: list[str]) -> bool:
    ...


def rebind_is_isolated(catalog: list[str]) -> bool:
    ...
