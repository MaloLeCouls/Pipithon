"""Une API de tâches veut tracer qui appelle quoi.

Implémente :
- une liste-module `AUDIT_LOG: list[str]` (publique, importable).
- un décorateur `audit` qui :
    * append le nom de la fonction décorée à `AUDIT_LOG` à chaque appel,
    * préserve la valeur de retour de la fonction décorée.

Tu peux ensuite décorer n'importe quelle fonction : `@audit`.
"""
from __future__ import annotations

AUDIT_LOG: list[str] = []


def audit(fn):
    ...
