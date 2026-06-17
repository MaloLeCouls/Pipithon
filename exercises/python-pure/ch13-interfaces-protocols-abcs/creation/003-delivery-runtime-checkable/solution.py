"""Choix de design :
- `@runtime_checkable` active la mécanique `__class_getitem__` de Protocol
  pour qu'`isinstance` reconnaisse les classes structurellement compatibles.
- Sans ce décorateur : `TypeError: Instance and class checks can only be
  used with @runtime_checkable protocols`.
- À retenir : on contrôle juste la PRÉSENCE des méthodes, pas leur type.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Trackable(Protocol):
    def track(self) -> str: ...


def is_trackable(obj: object) -> bool:
    return isinstance(obj, Trackable)
