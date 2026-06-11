"""Ce code livre, mais il a le bug classique du défaut mutable :
la liste `log` est partagée entre TOUS les appels qui ne fournissent pas
explicitement un journal.

Refactor :
1. Remplace le défaut `log=[]` par le pattern sentinelle None.
2. Garde le comportement : on append toujours le nom du colis au log et on
   renvoie le log.
3. Les tests vérifient à la fois le comportement ET la forme (plus de défaut
   mutable dans la signature).
"""
from __future__ import annotations


def dispatch(package: str, log: list[str] = []) -> list[str]:  # noqa: B006
    log.append(package)
    return log
