"""Checkpoint chapitre 18 — Reproduire l'exemple canonique `LookingGlass`
de Fluent Python, en l'adaptant au domaine `monitoring` : un context
manager `LogMirror` qui INVERSE tout ce qui est imprimé pendant son bloc,
et qui AVALE `ZeroDivisionError` en imprimant "RECOVERED" à sa place.

Tu dois écrire **deux versions équivalentes** :

1. **Forme classe** `LogMirror` :
   - `__enter__` :
       * sauve `sys.stdout.write` original dans `self._original_write`.
       * remplace `sys.stdout.write` par une version qui inverse chaque
         chaîne reçue (reverse via slicing `text[::-1]`).
       * retourne la string `"MIRROR"` (à binder via `as`).
   - `__exit__(exc_type, exc, tb)` :
       * restore `sys.stdout.write` au write original (TOUJOURS).
       * Si `exc_type` est `ZeroDivisionError` :
           - imprime `"RECOVERED"` via le write original.
           - retourne `True` pour avaler l'exception.
       * Sinon : ne retourne rien (laisse l'exception remonter, ou pas
         d'exception du tout).

2. **Forme `@contextmanager`** `log_mirror()` :
   - mêmes effets, mêmes valeurs ; sucre syntaxique sur try/except/finally.
"""
from __future__ import annotations

import sys
from collections.abc import Iterator
from contextlib import contextmanager


class LogMirror:
    def __enter__(self) -> str:
        raise NotImplementedError("À implémenter")

    def __exit__(self, exc_type, exc, tb):
        raise NotImplementedError("À implémenter")


@contextmanager
def log_mirror() -> Iterator[str]:
    raise NotImplementedError("À implémenter")
    yield "MIRROR"  # pragma: no cover
