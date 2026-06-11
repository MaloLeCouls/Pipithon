"""Cette fonction de calcul de remise utilise un dict de cache « fait main ».

Refactor :
- Remplace tout le mécanisme par `@functools.cache`.
- Supprime le dict _CACHE.
- Le test de forme vérifie qu'aucune variable contenant 'cache' n'est définie
  manuellement dans le module.
"""
from __future__ import annotations

_CACHE: dict = {}


def compute_total(price: int, rate: float) -> float:
    key = (price, rate)
    if key in _CACHE:
        return _CACHE[key]
    result = price * (1 - rate)
    _CACHE[key] = result
    return result
