"""Choix de design :
- Plus de class attribute mutable : la liste est créée DANS `__init__`,
  donc chaque instance a la sienne propre.
- Pattern hyper classique du chapitre 11 — pendant Python du « mutable
  default argument » des fns.
"""
from __future__ import annotations


class Chair:
    def __init__(self, ref: str) -> None:
        self.ref = ref
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)
