"""On tokenize les mêmes prompts plusieurs fois ; cache le coût.

Implémente :
- `CALLS: list[int]` (compteur, position 0 = nombre d'appels « réels »).
- `tokenize_len(text: str) -> int` qui :
    * est décorée par `@functools.cache`,
    * incrémente CALLS[0] à chaque appel non caché,
    * renvoie len(BPETokenizer().encode(text)).

Les tests appellent plusieurs fois avec les mêmes textes ; CALLS[0] ne doit
augmenter qu'aux premiers appels (cache hits ne comptent pas).
"""
from __future__ import annotations

CALLS: list[int] = [0]


def tokenize_len(text: str) -> int:
    ...
