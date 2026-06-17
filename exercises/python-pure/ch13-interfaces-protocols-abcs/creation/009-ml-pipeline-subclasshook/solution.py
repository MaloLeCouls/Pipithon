"""Choix de design :
- `cls is TokenizerABC` : on ne répond QUE pour notre ABC. Si une
  sous-classe hérite (rare mais légal), on délègue au mécanisme par défaut.
- `any('tokenize' in B.__dict__ for B in C.__mro__)` : on scanne l'arbre
  d'héritage de la classe candidate — pareil que `Iterable.__subclasshook__`.
- Retour `NotImplemented` (pas False) : permet aux autres mécanismes (ABC
  register, héritage explicite) de répondre si besoin.
"""
from __future__ import annotations

import abc


class TokenizerABC(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C: type) -> bool | type(NotImplemented):  # type: ignore[valid-type]
        if cls is TokenizerABC:
            if any("tokenize" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
