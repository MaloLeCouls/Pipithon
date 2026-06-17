"""Choix de design :
- `abc.ABC` + `@abstractmethod` : impossible d'instancier une classe qui
  n'override pas TOUTES les abstractmethods. Erreur précoce, claire.
- Plus de `raise NotImplementedError` : les corps abstraits restent vides
  (`...`).
- `CompleteTokenizer` reste valide (override des deux abstraites).
- `IncompleteTokenizer` ne peut plus être instancié : TypeError au
  premier `IncompleteTokenizer()`.
"""
from __future__ import annotations

import abc


class BaseTokenizer(abc.ABC):
    @abc.abstractmethod
    def encode(self, text: str) -> list[int]: ...

    @abc.abstractmethod
    def decode(self, ids: list[int]) -> str: ...


class CompleteTokenizer(BaseTokenizer):
    def encode(self, text: str) -> list[int]:
        return [ord(c) for c in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(chr(i) for i in ids)


class IncompleteTokenizer(BaseTokenizer):
    def decode(self, ids: list[int]) -> str:
        return "x" * len(ids)
