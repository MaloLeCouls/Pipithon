"""Bug : annotation = commentaire pour mypy, pas runtime. Le piège du défaut
mutable est INDÉPENDANT du typage.

Fix : pattern sentinelle (None default, instanciation à l'intérieur).
"""
from __future__ import annotations


def accumulate(feature: int, acc: list[int] | None = None) -> list[int]:
    if acc is None:
        acc = []
    acc.append(feature)
    return acc
