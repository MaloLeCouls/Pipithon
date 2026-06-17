"""`Sample` est slotted (gros gain mémoire). On crée une sous-classe
`TaggedSample` qui n'ajoute qu'un attribut `split`. Surprise : les
instances de `TaggedSample` ont un `__dict__` — le gain mémoire de
slots est perdu pour toute la sous-classe.

Indices :
- `__slots__` n'est PAS hérité — il faut le re-déclarer.
- Sur une sous-classe SANS slots, Python ajoute `__dict__` (et le gain
  est annulé).
- Fix : déclare `__slots__ = (\"split\",)` sur `TaggedSample`.

NB : si la sous-classe n'a aucun nouvel attribut, mettre
`__slots__ = ()` (tuple vide) suffit à garder le bénéfice.
"""
from __future__ import annotations


class Sample:
    __slots__ = ("label", "features")

    def __init__(self, label: str, features: list[float]) -> None:
        self.label = label
        self.features = features


class TaggedSample(Sample):
    # BUG : pas de __slots__ -> __dict__ réapparaît sur TaggedSample.
    def __init__(self, label: str, features: list[float], split: str) -> None:
        super().__init__(label, features)
        self.split = split
