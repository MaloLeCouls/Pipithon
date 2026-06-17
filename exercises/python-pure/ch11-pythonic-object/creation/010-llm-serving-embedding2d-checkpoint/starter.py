"""Checkpoint chapitre 11 — Reproduire `Vector2d` de Fluent Python en
version `Embedding2d` pour l'inférence (toy 2d embedding, mais le
pattern monte à n'importe quelle dim).

Contrat — classe `Embedding2d(x: float, y: float)` :

1. `__slots__ = ("__x", "__y")` — économie mémoire + verrouillage.
2. Attributs READ-ONLY via `@property` : `e.x`, `e.y`.
3. `__iter__` : yield x, y (rend `tuple(e)`, `list(e)`, unpacking dispo).
4. `__repr__` : `f"Embedding2d({x!r}, {y!r})"`.
5. `__str__` : `f"({x}, {y})"`.
6. `__eq__` : `tuple(self) == tuple(other)` (uniquement pour Embedding2d).
7. `__hash__` : `hash((self.x, self.y))`.
8. `__abs__` : norme euclidienne `sqrt(x² + y²)`.
9. `__bool__` : `bool(abs(self))` (False si vecteur nul).
10. `__format__` :
    - `""`  → `f"({x}, {y})"` (= `__str__`),
    - `"p"` → `f"<{r}, {theta}>"` avec `r = abs(self)` et `theta = atan2(y, x)`.
11. `@classmethod from_pair(cls, pair: tuple[float, float])` : alt
    constructor depuis un tuple.

NB : `__x`/`__y` (double underscore) → name-mangled en `_Embedding2d__x`
et `_Embedding2d__y`. Les `@property` exposent juste `x`/`y` propres.
"""
from __future__ import annotations

import math
from collections.abc import Iterator


class Embedding2d:
    # À implémenter (slots, init, properties, dunders, frombytes).
    ...
