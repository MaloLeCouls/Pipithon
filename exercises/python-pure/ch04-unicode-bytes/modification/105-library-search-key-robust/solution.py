"""Choix de design :
- NFKD décompose lettre + diacritique ; on filtre les marques
  combinantes (unicodedata.combining(c) != 0) -> tout accent saute,
  pas seulement 4 cas codés en dur. casefold() ensuite pour la casse
  (gère 'ß'->'ss'). Clé stable, insensible accents+casse, sans table.
- find() ne change pas : il délègue toute la robustesse à search_key.
"""

import unicodedata


def search_key(s: str) -> str:
    decomposed = unicodedata.normalize("NFKD", s)
    no_marks = "".join(c for c in decomposed if not unicodedata.combining(c))
    return no_marks.casefold()


def find(titles: list[str], query: str) -> list[str]:
    q = search_key(query)
    return [t for t in titles if q in search_key(t)]
