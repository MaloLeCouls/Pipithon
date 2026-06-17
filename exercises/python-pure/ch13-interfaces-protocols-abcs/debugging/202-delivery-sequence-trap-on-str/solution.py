"""Fix : exclure explicitement `str` (et `bytes`, par hygiène) du check.
On garde `Sequence` pour autoriser list/tuple/deque/range, et on coupe
le piège textuel à la source.
"""
from __future__ import annotations

from collections.abc import Sequence


def route(addresses: object) -> str:
    if isinstance(addresses, (str, bytes)) or not isinstance(addresses, Sequence):
        raise TypeError("addresses must be a sequence (not a str)")
    return " -> ".join(str(a) for a in addresses)
