"""Tu valides les métadonnées d'un colis. La règle métier : c'est OK si
c'est une « table clé/valeur ». L'implé actuelle exige `dict` strict,
ce qui refuse les `MappingProxyType` (renvoyés par `types.MappingProxyType`,
utilisés pour exposer des configs immutables) ET `OrderedDict`. Faux
positifs de refus.

Refactore pour accepter n'importe quel `Mapping` (cf. `collections.abc`).
"""
from __future__ import annotations


def is_valid_metadata(meta: object) -> bool:
    # Anti-pattern : check sur le type concret, rejette les sous-types
    # structurellement valides (MappingProxyType, OrderedDict, ...).
    return isinstance(meta, dict)
