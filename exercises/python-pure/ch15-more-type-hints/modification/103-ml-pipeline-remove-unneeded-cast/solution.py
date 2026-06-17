"""Choix de design :
- `isinstance(value, int)` narrowe `value` à `int` côté mypy. Pas besoin
  d'un `cast` qui dit la même chose.
- `cast` est un aveu de l'absence d'évidence ; ici l'évidence est là.
"""
from __future__ import annotations


def extract_int(value: object) -> int:
    if isinstance(value, int):
        return value
    raise TypeError(f"expected int, got {type(value).__name__}")
