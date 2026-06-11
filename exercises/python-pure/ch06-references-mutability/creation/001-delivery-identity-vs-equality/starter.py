"""Une plateforme logistique veut distinguer deux questions :
1. « Ces deux variables désignent-elles le *même* colis physique ? » -> identité
2. « Ces deux colis ont-ils les *mêmes* données ? » -> égalité

Implémente :
- `same_object(a, b)` -> True ssi a et b désignent le même objet (is).
- `same_data(a, b)`  -> True ssi a et b ont les mêmes attributs (==).

La classe `Package` est déjà fournie, ne la modifie pas.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Package:
    tracking: str
    weight_kg: float


def same_object(a: Package, b: Package) -> bool:
    ...


def same_data(a: Package, b: Package) -> bool:
    ...
