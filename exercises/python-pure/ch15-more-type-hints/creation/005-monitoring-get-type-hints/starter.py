"""`get_type_hints(fn)` lit les annotations d'une fn et RÉSOUT les
forward refs / stringifications (`from __future__ import annotations`).

Contrat :

- `record_metric(name: str, value: float) -> str` est fournie ; juste un
  stub avec annotations.
- Écris `param_types(fn) -> dict[str, type]` qui :
  - utilise `get_type_hints(fn)`,
  - retire la clé `"return"` si présente,
  - renvoie le reste tel quel (déjà sous forme `{name: type}`).
"""
from __future__ import annotations

from typing import get_type_hints


def record_metric(name: str, value: float) -> str:
    return f"{name}={value}"


def param_types(fn: object) -> dict[str, type]:
    raise NotImplementedError("À implémenter")
