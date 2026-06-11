"""Choix de design :
- @functools.cache (3.9+) memoize sur tous les arguments. text est hashable
  (str), donc compatible.
- CALLS[0] compte les MISS (appels non cachés). Les HIT renvoient le résultat
  sans re-exécuter le corps -> CALLS[0] inchangé.
"""
from __future__ import annotations

import functools

from pymistral import BPETokenizer

CALLS: list[int] = [0]


@functools.cache
def tokenize_len(text: str) -> int:
    CALLS[0] += 1
    return len(BPETokenizer().encode(text))
