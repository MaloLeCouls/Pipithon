"""Fix : `alert.get("unit", "ms")` fournit un défaut pour la clé
optionnelle. `NotRequired` signale à mypy qu'on doit le lire avec
prudence ; `.get()` est l'API qui matérialise cette prudence.
"""
from __future__ import annotations

from typing import NotRequired, TypedDict


class Alert(TypedDict):
    name: str
    value: float
    unit: NotRequired[str]


def format_alert(alert: Alert) -> str:
    unit = alert.get("unit", "ms")
    return f"{alert['name']}={alert['value']}{unit}"
