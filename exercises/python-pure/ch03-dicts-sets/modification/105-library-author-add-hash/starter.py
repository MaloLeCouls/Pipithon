"""`Author` définit __eq__ mais pas __hash__ : il est donc non-hashable
(impossible en set/dict). Du coup `distinct` déduplique en O(n²) avec une
liste — ça marche mais c'est le symptôme du problème.

Refactor :
1. Ajoute __hash__ à Author, cohérent avec __eq__ (mêmes champs).
2. Réécris `distinct` pour dédupliquer via un set, en gardant l'ordre
   de première apparition.
Comportement (liste d'auteurs distincts, même ordre) strictement préservé.
"""


class Author:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Author):
            return NotImplemented
        return (self.first, self.last) == (other.first, other.last)

    def __repr__(self) -> str:
        return f"Author({self.first!r}, {self.last!r})"


def distinct(authors: list[Author]) -> list[Author]:
    out: list[Author] = []
    for a in authors:
        if a not in out:  # O(n) à chaque tour -> O(n^2)
            out.append(a)
    return out
