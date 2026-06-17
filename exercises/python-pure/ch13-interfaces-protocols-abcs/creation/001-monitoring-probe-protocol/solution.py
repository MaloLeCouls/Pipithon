"""Choix de design :
- `Protocol` (`typing`) : duck typing statique. Aucune classe n'a besoin
  d'hériter de `Probe` — il suffit qu'elle ait `read() -> float`.
- `sample` est typée pour `Probe` ; mypy --strict accepte n'importe
  quelle classe structurellement compatible. À runtime, Python ne vérifie
  rien (pas de `@runtime_checkable` ici — exo 003 le drille).
"""
from __future__ import annotations

from typing import Protocol


class Probe(Protocol):
    def read(self) -> float: ...


def sample(p: Probe) -> float:
    return p.read()
