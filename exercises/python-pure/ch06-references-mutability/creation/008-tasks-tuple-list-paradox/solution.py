"""Choix de design :
- On reconstruit un tuple avec une liste FRAÎCHE : ticket[1] + new_tags crée
  une nouvelle liste sans toucher la liste d'origine.
- Le tuple lui-même est donc remplacé, pas muté (impossible de toute façon).
"""
from __future__ import annotations


def add_tags_safely(
    ticket: tuple[int, list[str]], new_tags: list[str]
) -> tuple[int, list[str]]:
    return (ticket[0], ticket[1] + new_tags)
