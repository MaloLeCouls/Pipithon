"""Choix de design :
- defaultdict(list) : groups[d].append(...) crée la liste à la volée,
  le `if d not in groups` disparaît. dict(groups) en sortie : pas de
  defaultdict qui crée des clés fantômes chez l'appelant.
"""

from collections import defaultdict


def by_driver(packages: list[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for pkg in packages:
        groups[pkg["driver"]].append(pkg["tracking"])
    return dict(groups)
