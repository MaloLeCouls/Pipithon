"""Choix de design :
- Comprehension équivalente, plus expressive.
- Pas de filter() : la comprehension est plus lisible pour un filtre simple.
"""
from __future__ import annotations


def assigned_to(tasks: list[dict], user: str) -> list[dict]:
    return [t for t in tasks if t["assignee"] == user]
