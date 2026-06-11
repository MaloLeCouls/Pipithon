"""Cette fonction filtre les tâches assignées à un certain utilisateur.
Elle marche, mais c'est de la prose : boucle + condition + append.

Refactor : utilise une comprehension. Plus court, plus déclaratif.
Le test de forme exige que `append` ne soit plus appelé.
"""
from __future__ import annotations


def assigned_to(tasks: list[dict], user: str) -> list[dict]:
    out = []
    for t in tasks:
        if t["assignee"] == user:
            out.append(t)
    return out
