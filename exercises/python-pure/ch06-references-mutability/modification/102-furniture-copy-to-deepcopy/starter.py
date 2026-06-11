"""Ce code copie un catalogue de meubles, mais la copie est superficielle :
muter le clone affecte l'original. Le tests le démontrent (et échouent).

Refactor : passe à `copy.deepcopy` pour isoler le clone.

Garde la signature et le nom de la fonction.
"""
from __future__ import annotations

import copy


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    return copy.copy(cat)
