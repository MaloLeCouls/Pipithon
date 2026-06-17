"""Pour vérifier *à runtime* qu'un objet respecte un Protocol, il faut le
décorer avec `@runtime_checkable`.

⚠️ Piège du chapitre : `@runtime_checkable` ne vérifie que la PRÉSENCE
des méthodes, pas leur signature (cf. exo de debugging 203).

Contrat :

- Déclare `Trackable(Protocol)` (décoré `@runtime_checkable`) avec
  `def track(self) -> str: ...`.
- Écris `is_trackable(obj: object) -> bool` qui renvoie
  `isinstance(obj, Trackable)`.
"""
from __future__ import annotations

from typing import Protocol


class Trackable(Protocol):
    ...


def is_trackable(obj: object) -> bool:
    raise NotImplementedError("À implémenter")
