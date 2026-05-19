"""Un outil de gestion de tâches affiche ses sprints dans des logs.

Implémente la classe `Sprint` :
- `__init__(self, name: str, tasks: list[str])`.
- `__len__` : nombre de tickets du sprint.
- `__repr__` au format : Sprint('S1', 3 tasks)
  (au singulier OU pluriel peu importe, garde "tasks" ; le chiffre = len).

Piège signalé : un sprint sans tâche doit donner Sprint('S0', 0 tasks),
sans lever d'erreur.
"""


class Sprint:
    def __init__(self, name: str, tasks: list[str]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def __repr__(self) -> str:
        ...
