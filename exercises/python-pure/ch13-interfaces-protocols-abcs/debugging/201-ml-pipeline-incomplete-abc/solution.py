"""Fix : implémenter `decode`. L'inverse symétrique d'`encode` (qui
renvoie des longueurs de mots) : reconstruire des mots de la bonne
longueur — ici on choisit `"x" * n` (placeholder, c'est le pattern
qui compte).
"""
from __future__ import annotations

import abc


class BaseTokenizer(abc.ABC):
    @abc.abstractmethod
    def encode(self, text: str) -> list[int]: ...

    @abc.abstractmethod
    def decode(self, ids: list[int]) -> str: ...


class WordTokenizer(BaseTokenizer):
    def encode(self, text: str) -> list[int]:
        return [len(w) for w in text.split()]

    def decode(self, ids: list[int]) -> str:
        return " ".join("x" * n for n in ids)
