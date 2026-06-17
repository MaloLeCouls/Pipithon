"""Un Protocol peut exiger un ATTRIBUT, pas seulement des méthodes.

Contrat :

- Déclare `Named(Protocol)` avec un attribut `name: str` (juste l'annotation).
- Écris `label(m: Named) -> str` qui renvoie `f"metric:{m.name}"`.

Tu vas tester avec dataclass, named tuple, classe à la main — tout marche
tant que `m.name: str` est lisible.
"""
from __future__ import annotations

from typing import Protocol


class Named(Protocol):
    ...


def label(m: Named) -> str:
    raise NotImplementedError("À implémenter")
