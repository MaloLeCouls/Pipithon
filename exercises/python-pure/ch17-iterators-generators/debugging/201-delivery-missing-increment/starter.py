"""`PackageStream` est un iterator écrit à la main. Il « marche » sur le
papier — mais la moindre `for ... in stream` se transforme en boucle
infinie (et il faut tuer le process). Trouve pourquoi.

Indices :
- `__iter__` retourne `self` (correct).
- `__next__` retourne le bon élément (correct).
- Quelque chose manque dans `__next__`.
"""
from __future__ import annotations


class Package:
    def __init__(self, tracking_id: str, status: str) -> None:
        self.tracking_id = tracking_id
        self.status = status


class PackageStream:
    def __init__(self, packages: list[Package]) -> None:
        self._packages = packages
        self._i = 0

    def __iter__(self) -> "PackageStream":
        return self

    def __next__(self) -> Package:
        if self._i >= len(self._packages):
            raise StopIteration
        # BUG : on retourne l'élément courant... mais on n'avance jamais.
        return self._packages[self._i]
