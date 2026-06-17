"""Choix de design :
- `__slots__` = tuple des seuls attributs autorisés. Python alloue un
  layout fixe au lieu d'un dict par instance — gain de ~40-50 % de mémoire.
- Pas de `__dict__` → toute écriture hors slots = AttributeError. Ça
  attrape les fautes de frappe (`s.lable = ...` au lieu de `s.label`).
- Critique pour vLLM : KVCache, BlockTable, etc. utilisent slots partout.
"""
from __future__ import annotations


class Sample:
    __slots__ = ("label", "features")

    def __init__(self, label: str, features: list[float]) -> None:
        self.label = label
        self.features = features
