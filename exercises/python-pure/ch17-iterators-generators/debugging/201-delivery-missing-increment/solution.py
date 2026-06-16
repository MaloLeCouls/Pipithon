"""Choix de design (correctif) :
- Le contrat de `__next__` : produire l'élément courant ET faire avancer
  l'état interne, pour que le prochain appel produise l'élément SUIVANT
  (et finisse par lever `StopIteration`).
- Une seule ligne ajoutée : `self._i += 1` AVANT le return, dans la
  branche où on retourne un élément.
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
        pkg = self._packages[self._i]
        self._i += 1
        return pkg
