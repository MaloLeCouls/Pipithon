"""On déploie en pleine prod : on veut suspendre les alertes du dashboard
*juste* le temps d'une fenêtre de maintenance, sans laisser le drapeau
collé au cas où le code lèverait.

Implémente `AlertSilencer(dashboard)` :
- `dashboard` a un attribut booléen `silenced`.
- `__enter__` met `dashboard.silenced = True` et retourne le dashboard.
- `__exit__` restore l'ancienne valeur (avant le with), exception ou pas.
"""
from __future__ import annotations


class Dashboard:
    def __init__(self, silenced: bool = False) -> None:
        self.silenced = silenced


class AlertSilencer:
    def __init__(self, dashboard: Dashboard) -> None:
        raise NotImplementedError("À implémenter")

    def __enter__(self) -> Dashboard:
        raise NotImplementedError("À implémenter")

    def __exit__(self, exc_type, exc, tb) -> None:
        raise NotImplementedError("À implémenter")
