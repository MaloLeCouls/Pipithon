"""`first_assignee_or_unassigned(tasks, status)` doit retourner le premier
`assignee` parmi les tâches du statut demandé, ou la chaîne `"unassigned"`
si aucune tâche ne match.

Quelqu'un a lu en diagonale la sémantique du `for/else` : « le else
s'exécute si la liste est vide ». C'est faux — le else s'exécute si la
boucle finit SANS `break`. Du coup la fonction retourne `"unassigned"`
même quand on a trouvé.

Trouve le bug, corrige."""
from __future__ import annotations


class Task:
    def __init__(self, task_id: str, status: str, assignee: str) -> None:
        self.task_id = task_id
        self.status = status
        self.assignee = assignee


def first_assignee_or_unassigned(tasks: list[Task], status: str) -> str:
    for t in tasks:
        if t.status == status:
            result = t.assignee  # on capture, sans `break` ni `return`
    else:
        # BUG : on tombe TOUJOURS ici (la boucle finit sans break, qu'on
        # ait matché ou non). result peut ne pas exister.
        return "unassigned"
    return result
