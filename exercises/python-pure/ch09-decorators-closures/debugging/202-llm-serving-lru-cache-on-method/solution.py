"""Bug : @functools.cache sur une méthode garde une référence à `self` dans
sa table -> chaque instance survit aussi longtemps que le cache.

Fix : sortir le calcul en fonction libre, la méthode délègue. Pas de self
dans la signature cachée.
"""
from __future__ import annotations

import functools


@functools.cache
def _count_chars(text: str) -> int:
    return len(text)


class TokenCounter:
    def count_chars(self, text: str) -> int:
        return _count_chars(text)
