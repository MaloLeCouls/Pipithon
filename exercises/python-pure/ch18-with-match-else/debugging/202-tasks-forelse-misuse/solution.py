"""Choix de design (correctif) :
- `for/else` se lit « else = la boucle a fini sans break ». Pour le
  pattern *find-or-default*, on `return` dans la boucle dès qu'on trouve ;
  si on n'a jamais return, le else s'exécute et renvoie le défaut.
"""
from __future__ import annotations


class Task:
    def __init__(self, task_id: str, status: str, assignee: str) -> None:
        self.task_id = task_id
        self.status = status
        self.assignee = assignee


def first_assignee_or_unassigned(tasks: list[Task], status: str) -> str:
    for t in tasks:
        if t.status == status:
            return t.assignee
    else:
        return "unassigned"
