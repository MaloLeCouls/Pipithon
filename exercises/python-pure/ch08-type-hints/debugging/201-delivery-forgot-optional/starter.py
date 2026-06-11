"""On affiche le nom du chauffeur d'une route, en majuscules.
BUG : l'annotation dit `driver: str` mais l'appelant peut passer None
(les routes non assignées). AttributeError.

Corrige :
- annotation : `str | None`
- guard : renvoie 'unassigned' si None
- le reste du comportement inchangé.
"""
from __future__ import annotations


def driver_label(driver: str) -> str:
    return driver.upper()
