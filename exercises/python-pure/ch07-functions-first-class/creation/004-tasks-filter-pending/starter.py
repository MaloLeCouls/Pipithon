"""Filtre les tâches en cours : tout ce qui n'est pas 'done'.

Implémente `pending(tasks: list[dict]) -> list[dict]` qui renvoie une nouvelle
liste contenant uniquement les tâches dont `status != 'done'`.

Utilise une comprehension (idiomatique) plutôt que filter() — sauf si tu as
une raison forte de l'éviter.
"""
from __future__ import annotations


def pending(tasks: list[dict]) -> list[dict]:
    ...
