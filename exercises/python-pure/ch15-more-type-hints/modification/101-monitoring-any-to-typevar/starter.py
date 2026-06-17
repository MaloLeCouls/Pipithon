"""Cette fn `first` rend `Any` — c'est le typage de la défaite.
mypy ne sait rien des appels en aval (`first([1,2]) + 1` n'est pas
vérifié).

Refactore en utilisant un `TypeVar` pour préserver le type d'entrée.
"""
from __future__ import annotations

from typing import Any


def first(items: list[Any]) -> Any:
    return items[0]
