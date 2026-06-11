"""Choix de design :
- Protocol Encoder : duck typing statique. BPETokenizer continue de marcher,
  mais n'importe quel autre objet `.encode(text) -> list[Token]` aussi.
- Iterable[str] en entrée (Liskov : accepte large) ; list[list[Token]] en retour.
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from pymistral import Token


class Encoder(Protocol):
    def encode(self, text: str) -> list[Token]: ...


def encode_all(texts: Iterable[str], encoder: Encoder) -> list[list[Token]]:
    return [encoder.encode(t) for t in texts]
