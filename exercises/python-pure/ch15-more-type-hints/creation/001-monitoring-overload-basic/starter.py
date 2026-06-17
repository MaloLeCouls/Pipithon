"""`@overload` permet de déclarer plusieurs signatures cohérentes pour
une seule fonction — utile quand le type de RETOUR dépend du type du
PARAMÈTRE.

Contrat :

- `format_metric(x)` :
  - si `x: int` → renvoie `str(x)` (pas d'unité).
  - si `x: float` → renvoie `f"{x}ms"`.
  - Pour mypy, déclare DEUX stubs `@overload` (l'un avec `int`, l'autre
    avec `float`), puis l'implé finale (sans `@overload`) qui prend
    `int | float`.

NB : les stubs `@overload` ont un corps `...`. L'impl finale fait le boulot.
"""
from __future__ import annotations

from typing import overload


@overload
def format_metric(x: int) -> str: ...


@overload
def format_metric(x: float) -> str: ...


def format_metric(x: int | float) -> str:
    raise NotImplementedError("À implémenter")
