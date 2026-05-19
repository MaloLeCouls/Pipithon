"""Choix de design :
- new_board utilise une list comprehension `[[] for _ in range(lanes)]`
  qui crée `lanes` listes DISTINCTES. `[[]] * lanes` créerait `lanes`
  références vers UNE SEULE liste : assigner à une voie polluerait toutes
  les autres (aliasing) — c'est le piège du chapitre.
- assign mute la voie ciblée en place (append) : sémantique d'un board.
"""


def new_board(lanes: int) -> list[list[str]]:
    return [[] for _ in range(lanes)]


def assign(board: list[list[str]], lane: int, task: str) -> None:
    board[lane].append(task)
