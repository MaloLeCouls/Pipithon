"""Choix de design :
- defaultdict(set) : .add() crée le set au besoin et déduplique tout
  seul -> ni `if author in d`, ni filtrage de doublons à la main.
- dict(index) en sortie : un dict normal, pas de création de clé
  fantôme côté appelant.
"""

from collections import defaultdict


def index_by_author(books: list[dict]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for book in books:
        index[book["author"]].add(book["title"])
    return dict(index)
