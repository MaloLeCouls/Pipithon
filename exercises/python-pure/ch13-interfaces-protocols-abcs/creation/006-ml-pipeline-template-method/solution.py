"""Choix de design :
- Template Method : `run` orchestre, `_transform` est le seul hook abstrait.
- Les sous-classes restent triviales (override d'une méthode unique).
- `_load`/`_dump` sont concrètes : factorisation par défaut, surchargeable
  si besoin par une sous-classe.
"""
from __future__ import annotations

import abc


class Pipeline(abc.ABC):
    def _load(self, p: str) -> str:
        return f"loaded:{p}"

    def _dump(self, p: str) -> str:
        return f"dumped:{p}"

    @abc.abstractmethod
    def _transform(self, p: str) -> str: ...

    def run(self, payload: str) -> str:
        loaded = self._load(payload)
        transformed = self._transform(loaded)
        return self._dump(transformed)


class UpperPipeline(Pipeline):
    def _transform(self, p: str) -> str:
        return p.upper()
