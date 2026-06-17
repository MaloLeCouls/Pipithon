"""Fix : aligner `BadProbe.read` sur la signature du Protocol — `(self) -> float`.

Leçon du chapitre : `@runtime_checkable` est un filet, pas un mur.
mypy --strict, lui, attrape la divergence de signature au build — c'est
pour ça qu'on combine TOUJOURS Protocol + mypy quand on veut un contrat
ferme.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Probe(Protocol):
    def read(self) -> float: ...


class BadProbe:
    def read(self) -> float:
        return 42.0


def sample(p: Probe) -> float:
    return p.read()
