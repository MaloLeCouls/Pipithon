"""Fix : déclare `__slots__ = ("split",)` sur la sous-classe.

C'est l'un des plus gros pièges du chapitre 11. Si tu hérites d'une
classe slotted et que tu ne déclares pas tes propres slots, Python
ajoute silencieusement un `__dict__` — toute l'économie mémoire est
perdue pour les instances de la sous-classe.

Convention vLLM/Mistral : déclarer `__slots__ = ()` sur les classes
sans nouvel attribut, juste pour empêcher le `__dict__` de revenir.
"""
from __future__ import annotations


class Sample:
    __slots__ = ("label", "features")

    def __init__(self, label: str, features: list[float]) -> None:
        self.label = label
        self.features = features


class TaggedSample(Sample):
    __slots__ = ("split",)

    def __init__(self, label: str, features: list[float], split: str) -> None:
        super().__init__(label, features)
        self.split = split
