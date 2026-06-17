"""Le code passe le check `isinstance(bp, Probe)` (True) puis explose
sur `sample(bp)` avec « missing required positional argument: 'source' ».

Comment c'est possible ?

Indices :
- `@runtime_checkable` ne vérifie QUE l'existence de `read`, pas sa
  signature.
- `BadProbe.read` exige un `source: str` que l'appelant ne fournit pas.
- Le fix : aligner `BadProbe.read` sur le contrat `(self) -> float`.

NB : un fix LOOPHOLE serait de donner un défaut à `source` (`source: str = "cpu"`).
On préfère ici **supprimer** le param pour rester aligné sur le Protocol.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Probe(Protocol):
    def read(self) -> float: ...


class BadProbe:
    # BUG : la signature attendue est `read(self) -> float`. Ici on exige
    # un `source` que l'appelant ne fournit pas.
    def read(self, source: str) -> float:
        return float(len(source))


def sample(p: Probe) -> float:
    return p.read()
