"""Choix de design :
- Itérer une snapshot via list comprehension (ne dépend pas de tasks pendant
  qu'on le construit) puis extend en une passe.
- Pythonique : sépare clairement la production des relances de leur insertion.
"""
from __future__ import annotations


def double_urgent(tasks: list[dict]) -> list[dict]:
    relances = [
        {"title": t["title"] + " (relance)", "priority": "urgent"}
        for t in tasks
        if t["priority"] == "urgent"
    ]
    tasks.extend(relances)
    return tasks
