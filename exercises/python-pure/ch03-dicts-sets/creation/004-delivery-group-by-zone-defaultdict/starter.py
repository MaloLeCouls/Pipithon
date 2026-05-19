"""Un dépôt veut grouper ses colis par zone de livraison.

Chaque colis est un dict {"tracking": str, "zone": str}.

Implémente `group_by_zone(packages: list[dict]) -> dict[str, list[str]]` :
- renvoie {zone: [tracking, ...]} dans l'ordre de rencontre,
- utilise collections.defaultdict (pas de test `if k in d`).
"""

import collections  # noqa: F401


def group_by_zone(packages: list[dict]) -> dict[str, list[str]]:
    ...
