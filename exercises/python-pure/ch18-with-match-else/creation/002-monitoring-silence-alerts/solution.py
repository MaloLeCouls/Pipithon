"""Choix de design :
- On capture l'état AVANT l'enter (dans `__init__` ou en haut de `__enter__`,
  ici on choisit `__enter__` pour minimiser la fenêtre de course).
- Pattern « save / set / restore » — typique des context managers à
  drapeau (cf. `unittest.mock.patch`, `logging.disabled`).
"""
from __future__ import annotations


class Dashboard:
    def __init__(self, silenced: bool = False) -> None:
        self.silenced = silenced


class AlertSilencer:
    def __init__(self, dashboard: Dashboard) -> None:
        self.dashboard = dashboard
        self._previous: bool = False

    def __enter__(self) -> Dashboard:
        self._previous = self.dashboard.silenced
        self.dashboard.silenced = True
        return self.dashboard

    def __exit__(self, exc_type, exc, tb) -> None:
        self.dashboard.silenced = self._previous
