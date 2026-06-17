"""Cette classe `Chair` a une liste `tags` au niveau CLASSE. Toutes les
instances partagent silencieusement la même liste : ajouter à l'une
ajoute à toutes. Bug en attente.

Refactore :
- Plus de `tags = []` au niveau classe.
- `__init__` initialise `self.tags = []` (ou la valeur passée).
- Chaque instance a sa propre liste.
"""
from __future__ import annotations


class Chair:
    tags: list[str] = []  # BUG : partagée entre toutes les instances.

    def __init__(self, ref: str) -> None:
        self.ref = ref

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)
