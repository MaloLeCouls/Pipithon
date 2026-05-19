"""Ce module construit une clé de recherche en minusculant et en
remplaçant quelques accents à la main. La table est forcément
incomplète (ñ, ø, ł... manquent), et lower() rate les plis durs.

Refactor (comportement accent-insensible PRÉSERVÉ et généralisé) :
1. `search_key(s)` : NFKD, retire les marques combinantes
   (unicodedata.combining(c)), puis casefold(). Plus de table d'accents.
2. `find(titles, query)` : intention inchangée — titres dont la clé
   contient la clé de la requête, ordre préservé.
"""

_ACCENTS = {"é": "e", "è": "e", "à": "a", "ç": "c"}


def search_key(s: str) -> str:
    s = s.lower()
    for k, v in _ACCENTS.items():
        s = s.replace(k, v)
    return s


def find(titles: list[str], query: str) -> list[str]:
    q = search_key(query)
    return [t for t in titles if q in search_key(t)]
