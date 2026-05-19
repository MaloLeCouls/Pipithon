"""Un site e-commerce a une grille de prix `base` {sku: price} et une
grille promo `promo` {sku: price} qui doit ÉCRASER la base pour les SKU
concernés.

Implémente `apply_promo(base: dict[str, float], promo: dict[str, float])
-> dict[str, float]` :
- renvoie un NOUVEAU dict = base, surchargé par promo,
- ne modifie ni `base` ni `promo`,
- utilise l'opérateur de fusion |.

Piège signalé : en cas de SKU commun, c'est le prix de `promo` qui gagne.
L'ordre des opérandes est donc crucial.
"""


def apply_promo(
    base: dict[str, float], promo: dict[str, float]
) -> dict[str, float]:
    ...
