"""Choix de design :
- On délègue à la liste interne : index négatif et IndexError sont déjà
  corrects et idiomatiques, inutile de les réimplémenter.
- On copie la liste reçue (list(dishes)) pour ne pas être couplé à une
  mutation externe du caller.
"""


class Menu:
    def __init__(self, dishes: list[str]) -> None:
        self._dishes = list(dishes)

    def __getitem__(self, index: int) -> str:
        return self._dishes[index]
