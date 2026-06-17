"""Cette fn `route` est censée prendre une liste/tuple d'adresses et
les concaténer en route formatée. Bug observé : si on lui passe la
chaîne `"123 Main St"`, elle l'accepte ET produit `"1 -> 2 -> 3 -> ..."`
(itération sur les caractères, désastre).

Indices :
- `str` satisfait `collections.abc.Sequence` — d'où le passage du check.
- Soit on exclut explicitement `(str, bytes)`, soit on ne se base pas
  sur `Sequence` du tout pour ce cas.
"""
from __future__ import annotations

from collections.abc import Sequence


def route(addresses: object) -> str:
    if not isinstance(addresses, Sequence):
        raise TypeError("addresses must be a sequence")
    return " -> ".join(str(a) for a in addresses)
