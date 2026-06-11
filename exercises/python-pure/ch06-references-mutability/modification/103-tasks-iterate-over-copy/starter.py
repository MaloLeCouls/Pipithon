"""Cette fonction relance les tâches urgentes : pour chaque tâche dont la
priorité est `urgent`, elle ajoute UNE tâche de relance (titre suffixé par
" (relance)", elle aussi urgente).

Bug : on itère SUR `tasks` ET on append DANS `tasks`. Les relances étant
urgentes elles aussi, elles re-déclenchent la condition -> boucle infinie.

Refactor : itère sur une snapshot pour découpler l'itération de la mutation.
Le résultat doit contenir UNE seule relance par tâche d'origine.
"""
from __future__ import annotations


def double_urgent(tasks: list[dict]) -> list[dict]:
    for t in tasks:
        if t["priority"] == "urgent":
            tasks.append({"title": t["title"] + " (relance)", "priority": "urgent"})
    return tasks
