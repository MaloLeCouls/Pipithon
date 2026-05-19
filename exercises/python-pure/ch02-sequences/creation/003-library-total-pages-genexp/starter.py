"""Une bibliothèque veut le total de pages de tous ses livres.

Chaque livre est un dict {"title": str, "pages": int}.

Implémente `total_pages(books: list[dict]) -> int` :
- somme des pages de tous les livres,
- en utilisant une generator expression passée à sum() (pas de liste
  intermédiaire, pas de boucle + accumulateur).
"""


def total_pages(books: list[dict]) -> int:
    ...
