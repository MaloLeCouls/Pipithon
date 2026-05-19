"""Choix de design :
- defaultdict(list) supprime le boilerplate `if zone not in d: d[zone]=[]`.
  L'accès d[zone] crée la liste à la volée -> on append directement.
- On renvoie dict(grouped) pour livrer un dict ordinaire (pas de création
  surprise de clés côté appelant) ; l'ordre d'insertion est préservé (3.7+).
"""

from collections import defaultdict


def group_by_zone(packages: list[dict]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for pkg in packages:
        grouped[pkg["zone"]].append(pkg["tracking"])
    return dict(grouped)
