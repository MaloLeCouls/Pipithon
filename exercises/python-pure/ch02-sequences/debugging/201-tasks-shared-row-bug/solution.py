"""Correction (une ligne) :
- Bug : `[[]] * lanes` duplique la RÉFÉRENCE d'une unique liste -> les
  `lanes` voies sont le même objet, assigner à l'une remplit toutes.
- Fix : `[[] for _ in range(lanes)]` crée des listes réellement distinctes.
assign() était correct, on n'y touche pas.
"""


def new_board(lanes: int) -> list[list[str]]:
    return [[] for _ in range(lanes)]


def assign(board: list[list[str]], lane: int, task: str) -> None:
    board[lane].append(task)
