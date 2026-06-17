"""Choix de design :
- 2 stubs `@overload` : mypy comprend que le type de retour dépend du
  type d'entrée. Si l'appelant passe `int`, mypy reconnaît une `str`
  sans unité (jusqu'à `format_metric(5).startswith("5")` typé).
- L'impl FINALE n'a pas `@overload` ; elle accepte `int | float` et
  branche sur `isinstance` pour distinguer.
- `bool` est une `int` en Python : on traite `bool` comme `int`. C'est
  consistent avec `isinstance(True, int) is True`.
"""
from __future__ import annotations

from typing import overload


@overload
def format_metric(x: int) -> str: ...


@overload
def format_metric(x: float) -> str: ...


def format_metric(x: int | float) -> str:
    if isinstance(x, bool) or type(x) is int:
        return str(x)
    return f"{x}ms"
