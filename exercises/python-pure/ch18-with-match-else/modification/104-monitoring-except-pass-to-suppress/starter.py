"""`silence_alerts(dashboard, names)` cherche à désactiver des alertes
nommées. Certaines peuvent être absentes : on les saute. Aujourd'hui c'est
écrit avec un `try/except KeyError: pass` pour chaque nom. Le chapitre 18
dit : ça se factorise en `contextlib.suppress`.

Refactor :
- Pour chaque nom, utilise `with suppress(KeyError): dashboard.disable(name)`.
- Plus aucun `try/except KeyError: pass` dans le code source.
- Comportement identique : les noms absents sont ignorés silencieusement."""
from __future__ import annotations

from collections.abc import Iterable


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
        try:
            dashboard.disable(name)
        except KeyError:
            pass
