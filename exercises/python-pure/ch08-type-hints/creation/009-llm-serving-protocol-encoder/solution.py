"""Choix de design :
- Protocol décrit une INTERFACE par structure (« a une méthode encode »).
- @runtime_checkable autorise isinstance(obj, Encoder) au runtime.
- BPETokenizer satisfait Encoder par sa simple présence d'une méthode encode
  retournant list[Token] — pas besoin d'héritage explicite.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from pymistral import Token


@runtime_checkable
class Encoder(Protocol):
    def encode(self, text: str) -> list[Token]: ...


def count_tokens(text: str, encoder: Encoder) -> int:
    return len(encoder.encode(text))
