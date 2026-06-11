"""Cette fonction route une action sur une tâche par un long if/elif.
Chaque ajout d'action = une nouvelle branche à toucher (anti-pattern OSS).

Refactor : remplace par un dict {action: fonction}.
Le test de forme exige : plus de if/elif comparant `action`.

Le contrat :
- action="close"  -> renvoie f"closed:{task['title']}"
- action="reopen" -> renvoie f"reopened:{task['title']}"
- action="tag"    -> renvoie f"tagged:{task['title']}"
- action inconnue -> lève KeyError
"""
from __future__ import annotations


def apply_action(task: dict, action: str) -> str:
    if action == "close":
        return f"closed:{task['title']}"
    elif action == "reopen":
        return f"reopened:{task['title']}"
    elif action == "tag":
        return f"tagged:{task['title']}"
    else:
        raise KeyError(action)
