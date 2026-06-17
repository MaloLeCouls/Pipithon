"""Fix : remplacer `List[int]` par `list[int]` builtin (PEP 585).
Plus moderne, pas d'import nécessaire, get_type_hints résout direct.

Alternative équivalente : `from typing import List` puis garder
`List[int]`. Recommandation moderne (Python 3.9+) : préférer le builtin.
"""
from __future__ import annotations

from typing import get_type_hints


class BatchBuffer:
    items: list[int]

    def __init__(self, items: list[int]) -> None:
        self.items = items


def inspect_buffer_hints() -> dict[str, type]:
    return get_type_hints(BatchBuffer)
