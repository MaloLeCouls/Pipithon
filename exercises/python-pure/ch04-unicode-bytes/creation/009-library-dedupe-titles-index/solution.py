"""Choix de design :
- canonical_key = NFC puis casefold : NFC réconcilie composé/décomposé,
  casefold neutralise la casse (y compris 'ß'/'SS'). C'est la clé de
  regroupement ; on ne l'expose pas, on garde la 1re graphie réelle.
- dedupe : un set de clés vues + une liste pour l'ordre — O(n), et le
  représentant affiché reste la graphie d'origine (on ne montre pas la
  forme casefoldée à l'utilisateur).
"""

import unicodedata


def canonical_key(title: str) -> str:
    return unicodedata.normalize("NFC", title).casefold()


def dedupe(titles: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for t in titles:
        k = canonical_key(t)
        if k not in seen:
            seen.add(k)
            out.append(t)
    return out
