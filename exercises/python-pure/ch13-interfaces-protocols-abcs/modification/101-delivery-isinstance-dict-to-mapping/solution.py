"""Choix de design :
- `Mapping` (de `collections.abc`) est l'ABC racine : couvre dict,
  MappingProxyType, OrderedDict, defaultdict, et toute classe enregistrée
  comme Mapping.
- C'est l'application directe du conseil Fluent Python : « code against
  the ABC, not the concrete type ».
"""
from __future__ import annotations

from collections.abc import Mapping


def is_valid_metadata(meta: object) -> bool:
    return isinstance(meta, Mapping)
