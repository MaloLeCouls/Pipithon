"""Choix de design :
- __repr__ s'appuie sur len(self) : une seule source de vérité, impossible
  que le compte affiché diverge du compte réel.
- list(tasks) découple de la liste du caller ; le cas vide tombe juste
  naturellement (len == 0), aucun garde-fou spécial nécessaire.
"""


class Sprint:
    def __init__(self, name: str, tasks: list[str]) -> None:
        self.name = name
        self._tasks = list(tasks)

    def __len__(self) -> int:
        return len(self._tasks)

    def __repr__(self) -> str:
        return f"Sprint({self.name!r}, {len(self)} tasks)"
