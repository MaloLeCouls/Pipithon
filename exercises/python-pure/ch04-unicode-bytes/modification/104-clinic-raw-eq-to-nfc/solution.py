"""Choix de design :
- Normaliser les DEUX opérandes en NFC avant == : sans ça, 'é' (U+00E9)
  et 'e'+◌́ (U+0301) sont jugés différents alors que c'est le même nom.
  Quand les formes coïncident déjà, NFC est idempotent -> aucune
  régression de comportement.
"""

import unicodedata


def is_match(name_a: str, name_b: str) -> bool:
    n = unicodedata.normalize
    return n("NFC", name_a) == n("NFC", name_b)
