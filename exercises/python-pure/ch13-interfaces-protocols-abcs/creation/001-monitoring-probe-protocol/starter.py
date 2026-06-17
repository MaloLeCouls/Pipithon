"""`Protocol` (PEP 544) = typage structurel : une classe satisfait le
Protocol si elle a les bonnes méthodes, sans avoir à en hériter.

Contrat :

- Déclare `Probe(Protocol)` avec UNE méthode :
  `def read(self) -> float: ...`.
- Écris `sample(p: Probe) -> float` qui renvoie `p.read()`.

Le test passera N'IMPORTE QUEL objet ayant `read() -> float` (instance d'une
classe arbitraire, dataclass, etc.) — pas besoin d'hériter de `Probe`.
"""
from __future__ import annotations

from typing import Protocol


class Probe(Protocol):
    ...


def sample(p: Probe) -> float:
    raise NotImplementedError("À implémenter")
