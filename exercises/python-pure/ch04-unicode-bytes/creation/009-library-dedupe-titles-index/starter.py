"""Une bibliothèque agrège des catalogues de plusieurs pays. Le même
livre arrive avec des graphies différentes au sens binaire ("Café" vs
"Café" décomposé, "DUNE" vs "dune") mais c'est le même titre.

Implémente :

1. `canonical_key(title: str) -> str`
   une clé stable pour regrouper les graphies équivalentes.

2. `dedupe(titles: list[str]) -> list[str]`
   renvoie les titres distincts au sens de canonical_key, en gardant la
   PREMIÈRE graphie rencontrée, dans l'ordre d'apparition.
"""


def canonical_key(title: str) -> str:
    ...


def dedupe(titles: list[str]) -> list[str]:
    ...
