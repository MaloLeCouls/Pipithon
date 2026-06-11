"""Bug : le défaut `log=[]` est une seule liste, créée à la définition de la
fonction, et partagée entre toutes les invocations qui acceptent le défaut.

Fix chirurgical : default = None ; if None alors liste fraîche.
"""
from __future__ import annotations


def log_trip(package: str, log: list[str] | None = None) -> list[str]:
    if log is None:
        log = []
    log.append(package)
    return log
