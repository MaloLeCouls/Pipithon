"""Choix de design :
- 2 stubs `@overload` : mypy sait que int → str et list[int] → list[str].
- Une seule impl dispatche sur `isinstance` — pas de duplication.
- L'API publique est `decode` (un seul nom), plus clair pour l'appelant.
"""
from __future__ import annotations

from typing import overload

_VOCAB = ["<pad>", "the", "cat", "sat", "on", "mat"]


@overload
def decode(x: int) -> str: ...


@overload
def decode(x: list[int]) -> list[str]: ...


def decode(x: int | list[int]) -> str | list[str]:
    if isinstance(x, int):
        return _VOCAB[x]
    return [_VOCAB[i] for i in x]
