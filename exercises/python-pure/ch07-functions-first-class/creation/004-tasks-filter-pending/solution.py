"""Choix de design :
- Comprehension de filtre : lisible, locale, expressive.
- filter() est valide mais demande un cast list() pour matérialiser ; deux
  fois moins direct qu'une comprehension.
"""
from __future__ import annotations


def pending(tasks: list[dict]) -> list[dict]:
    return [t for t in tasks if t["status"] != "done"]
