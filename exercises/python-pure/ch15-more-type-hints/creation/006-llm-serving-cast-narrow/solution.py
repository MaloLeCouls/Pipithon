"""Choix de design :
- `cast(int, blob["count"])` : promet à mypy que la valeur est un `int`.
  À runtime, retourne EXACTEMENT la valeur d'origine.
- Convention : `cast` est légitime ici parce que le contrat API garantit
  le type. Si on n'avait pas cette garantie, il faudrait `isinstance` +
  branche d'erreur.
"""
from __future__ import annotations

from typing import cast


def parse_count(blob: dict[str, object]) -> int:
    return cast(int, blob["count"])
