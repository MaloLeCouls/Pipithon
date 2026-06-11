"""Choix de design :
- `is` est l'opérateur Python pour l'identité (même cellule mémoire).
- `==` est l'opérateur d'égalité ; pour un @dataclass il compare champ à champ.
Aucune fonction utilitaire nécessaire : les opérateurs sont déjà nos primitives.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Package:
    tracking: str
    weight_kg: float


def same_object(a: Package, b: Package) -> bool:
    return a is b


def same_data(a: Package, b: Package) -> bool:
    return a == b
