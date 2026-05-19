"""Choix de design :
- enumerate(tasks, 1) fournit directement (rang, tâche) : plus d'indice
  manuel, plus de tasks[i], plus de désynchronisation possible entre i et
  l'élément. La comprehension exprime la transformation en une ligne.
- C'est le refactor que tout reviewer attend sur `range(len(...))`.
"""


def numbered(tasks: list[str]) -> list[str]:
    return [f"{rank}. {task}" for rank, task in enumerate(tasks, 1)]
