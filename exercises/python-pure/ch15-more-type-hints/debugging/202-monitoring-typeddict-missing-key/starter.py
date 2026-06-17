"""La fn `format_alert` reçoit un dict typé `Alert`. `unit` est
`NotRequired`. Pourtant le code accède `alert["unit"]` direct — KeyError
quand le client ne fournit pas la clé.

Fix : remplace `alert["unit"]` par `alert.get("unit", "ms")` (défaut).
"""
from __future__ import annotations

from typing import NotRequired, TypedDict


class Alert(TypedDict):
    name: str
    value: float
    unit: NotRequired[str]


def format_alert(alert: Alert) -> str:
    # BUG : si `unit` absente -> KeyError.
    return f"{alert['name']}={alert['value']}{alert['unit']}"
