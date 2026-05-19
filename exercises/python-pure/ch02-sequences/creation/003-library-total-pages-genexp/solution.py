"""Choix de design :
- Generator expression dans sum() : pas d'allocation d'une liste
  temporaire ; sur un gros catalogue, ça compte (lazy, O(1) mémoire).
- sum() gère nativement le cas vide en renvoyant 0.
"""


def total_pages(books: list[dict]) -> int:
    return sum(book["pages"] for book in books)
