"""Choix de design :
- __hash__ sur (first, last) : exactement les champs de __eq__. Contrat
  respecté (a == b => hash(a) == hash(b)) -> Author devient une clé/élément
  fiable. L'oublier casserait set/dict silencieusement (bug typique vu en
  review vLLM/transformers).
- distinct : un set `seen` donne l'appartenance en O(1) ; on garde une
  liste pour l'ordre de première apparition. O(n) au lieu de O(n^2).
"""


class Author:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Author):
            return NotImplemented
        return (self.first, self.last) == (other.first, other.last)

    def __hash__(self) -> int:
        return hash((self.first, self.last))

    def __repr__(self) -> str:
        return f"Author({self.first!r}, {self.last!r})"


def distinct(authors: list[Author]) -> list[Author]:
    seen: set[Author] = set()
    out: list[Author] = []
    for a in authors:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out
