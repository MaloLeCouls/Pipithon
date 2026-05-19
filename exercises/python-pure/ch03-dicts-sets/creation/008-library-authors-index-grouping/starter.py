"""Une bibliothèque veut un index {auteur: {titres uniques}}.

Chaque entrée est un dict {"author": str, "title": str}. Le catalogue
peut contenir des doublons (même auteur + même titre plusieurs fois).

Implémente `index_by_author(books: list[dict]) -> dict[str, set[str]]` :
- groupe les titres par auteur, SANS doublon (set),
- utilise collections.defaultdict,
- renvoie un dict ordinaire.
"""

import collections  # noqa: F401


def index_by_author(books: list[dict]) -> dict[str, set[str]]:
    ...
