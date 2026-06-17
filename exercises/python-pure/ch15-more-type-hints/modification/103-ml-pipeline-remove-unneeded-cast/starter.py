"""Cette fn parse un payload mixte ; après un `isinstance(value, int)`,
mypy SAIT déjà que value est `int`. Le `cast(int, value)` est redondant
— pire, il masque les évolutions futures du code (si on enlève
l'isinstance, le cast ment).

Supprime le `cast` ; renvoie `value` directement (mypy le sait déjà
narrowed après l'isinstance).
"""
from __future__ import annotations

from typing import cast


def extract_int(value: object) -> int:
    if isinstance(value, int):
        # `cast` ici ne sert à rien : mypy a déjà narrowed `value` en `int`.
        return cast(int, value)
    raise TypeError(f"expected int, got {type(value).__name__}")
