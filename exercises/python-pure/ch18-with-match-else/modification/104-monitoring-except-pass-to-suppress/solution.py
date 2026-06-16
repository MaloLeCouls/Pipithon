"""Choix de design :
- `contextlib.suppress(KeyError)` est l'équivalent déclaratif de
  `try: ... except KeyError: pass` — borné au bloc `with`, donc pas de
  risque d'élargir accidentellement le `try` plus tard.
- Visuellement : on lit « ignore les KeyError » au-dessus de l'appel
  qui peut en lever ; l'intention est explicite.
"""
from __future__ import annotations

from collections.abc import Iterable
from contextlib import suppress


class Dashboard:
    def __init__(self) -> None:
        self._alerts: dict[str, bool] = {}

    def enable(self, name: str) -> None:
        self._alerts[name] = True

    def disable(self, name: str) -> None:
        if name not in self._alerts:
            raise KeyError(name)
        self._alerts[name] = False

    def is_enabled(self, name: str) -> bool:
        return self._alerts.get(name, False)


def silence_alerts(dashboard: Dashboard, names: Iterable[str]) -> None:
    for name in names:
        with suppress(KeyError):
            dashboard.disable(name)
