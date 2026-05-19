"""Une salle de sport veut la liste des formules distinctes proposées,
normalisées (minuscules, sans espaces superflus), sans doublon.

Les membres sont des dicts {"name": str, "tier": str} ; `tier` peut être
"Gold", " gold ", "PREMIUM", etc.

Implémente `distinct_tiers(members: list[dict]) -> set[str]` :
- normalise chaque tier (strip + lower),
- renvoie l'ensemble des tiers distincts,
- via une set comprehension.
"""


def distinct_tiers(members: list[dict]) -> set[str]:
    ...
