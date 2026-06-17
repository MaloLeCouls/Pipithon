"""Quand tu traites des millions de `Sample` (ou de blocs KVCache, plus
tard), chaque `__dict__` par instance coûte des MB inutiles. `__slots__`
remplace le dict par un layout fixe : économie mémoire ET vérification
des attributs autorisés.

Contrat :

- Classe `Sample`.
- Déclare `__slots__ = ("label", "features")`.
- `__init__(self, label: str, features: list[float])` stocke les deux.
- N'AJOUTE PAS d'autres attributs ailleurs.

Conséquences :
- `s.label`, `s.features` marchent.
- `s.metadata = {}` doit lever `AttributeError` (pas dans slots).
- `s.__dict__` doit lever `AttributeError` (n'existe pas).
"""
from __future__ import annotations


class Sample:
    # À implémenter (slots + init).
    ...
