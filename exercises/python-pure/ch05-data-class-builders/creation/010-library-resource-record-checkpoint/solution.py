"""Choix de design (la synthèse du chapitre 5) :
- Ordre des champs : obligatoires sans défaut d'abord, puis optionnels
  (contrainte dataclass).
- authors/subjects = field(default_factory=list) : une liste neuve par
  instance, pas d'état partagé.
- _normalized = field(init=False, repr=False, default="") : champ dérivé,
  ni saisi ni affiché, rempli en __post_init__ — l'invariant vit dans la
  classe, pas chez l'appelant.
- __post_init__ valide l'identifiant : un record invalide n'existe pas.
"""

from dataclasses import dataclass, field


@dataclass
class Resource:
    identifier: str
    title: str
    authors: list[str] = field(default_factory=list)
    subjects: list[str] = field(default_factory=list)
    description: str | None = None
    _normalized: str = field(init=False, repr=False, default="")

    def __post_init__(self) -> None:
        if not self.identifier.strip():
            raise ValueError("identifier requis")
        self._normalized = self.title.strip().lower()
