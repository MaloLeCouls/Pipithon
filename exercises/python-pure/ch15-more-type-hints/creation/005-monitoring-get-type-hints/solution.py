"""Choix de design :
- `get_type_hints` : résout les annotations stringifiées (lazy evaluation
  due à PEP 563). C'est l'API officielle de runtime introspection.
- `fn.__annotations__` brut donnerait `{"name": "str", "value": "float", ...}`
  avec des STRINGS — pas utilisable directement.
- On retire `"return"` pour ne renvoyer que les params.
"""
from __future__ import annotations

from typing import get_type_hints


def record_metric(name: str, value: float) -> str:
    return f"{name}={value}"


def param_types(fn: object) -> dict[str, type]:
    hints = get_type_hints(fn)
    hints.pop("return", None)
    return hints
