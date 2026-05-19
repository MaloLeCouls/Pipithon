"""Ce board a 1 bug retors. Les tests l'exposent.
Corrige en chirurgie (une ligne suffit), sans réécrire from scratch.
"""


def new_board(lanes: int) -> list[list[str]]:
    return [[]] * lanes


def assign(board: list[list[str]], lane: int, task: str) -> None:
    board[lane].append(task)
