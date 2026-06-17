"""Une `Pipeline` ML a TOUJOURS le même squelette : load → transform → dump.
Seule la transformation diffère selon le pipeline (tokenize, normalize,
embed, ...). On factorise ça avec un Template Method.

Contrat :

- ABC `Pipeline(abc.ABC)` :
  - méthode CONCRÈTE `run(self, payload: str) -> str` qui appelle dans
    l'ordre `_load(payload)`, `_transform(...)`, `_dump(...)` et renvoie
    le résultat de `_dump`.
  - méthodes CONCRÈTES `_load(self, p: str) -> str` (renvoie `f"loaded:{p}"`)
    et `_dump(self, p: str) -> str` (renvoie `f"dumped:{p}"`).
  - méthode ABSTRAITE `_transform(self, p: str) -> str`.

- Sous-classe `UpperPipeline(Pipeline)` qui implémente
  `_transform(p) -> str = p.upper()`.
"""
from __future__ import annotations

import abc


class Pipeline(abc.ABC):
    def _load(self, p: str) -> str:
        return f"loaded:{p}"

    def _dump(self, p: str) -> str:
        return f"dumped:{p}"

    # À implémenter (méthode abstraite + méthode concrète run).
    ...


class UpperPipeline(Pipeline):
    ...
