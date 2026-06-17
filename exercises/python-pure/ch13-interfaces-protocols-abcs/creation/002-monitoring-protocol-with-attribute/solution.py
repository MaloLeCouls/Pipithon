"""Choix de design :
- `name: str` dans le corps de `Named(Protocol)` : suffit pour exiger
  l'attribut. mypy l'enforce statiquement.
- `label` est un one-liner ; le boulot pédago est dans la déclaration du
  Protocol.
"""
from __future__ import annotations

from typing import Protocol


class Named(Protocol):
    name: str


def label(m: Named) -> str:
    return f"metric:{m.name}"
