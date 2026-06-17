"""Choix de design :
- `!r` sur `ref` : force `repr(self.ref)`, ce qui guillemete la str.
- Sans `!r`, on aurait `Chair(ref=A1, price=99)` qui n'est pas du Python
  valide.
- Roundtrip : `eval(repr(Chair("A1", 99)))` reconstruit un Chair équivalent.
"""
from __future__ import annotations


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        self.ref = ref
        self.price = price

    def __repr__(self) -> str:
        return f"Chair(ref={self.ref!r}, price={self.price})"
