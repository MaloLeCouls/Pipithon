"""Choix de design :
- `base | promo` crée un nouveau dict ; sur clé commune, l'opérande de
  DROITE (promo) écrase — exactement la sémantique 'la promo prime'.
- `|` (PEP 584) est plus lisible que {**base, **promo} et n'altère pas
  les opérandes (contrairement à base.update(promo)).
"""


def apply_promo(
    base: dict[str, float], promo: dict[str, float]
) -> dict[str, float]:
    return base | promo
