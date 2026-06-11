"""Cette classe mémoïse `count_chars` via @functools.cache sur la méthode.

BUG : `self` est dans la clé de cache. Chaque instance créée est retenue
indéfiniment par le cache global -> fuite mémoire.

Refactor :
- Extrais une fonction LIBRE `_count_chars(text)` cachée par @functools.cache.
- La méthode `count_chars` délègue à _count_chars : pas de self dans le cache.
- Garde l'API publique (TokenCounter().count_chars("abc") == 3).

Le test vérifie que des instances détruites sont libérables.
"""
from __future__ import annotations

import functools


class TokenCounter:
    @functools.cache
    def count_chars(self, text: str) -> int:
        return len(text)
