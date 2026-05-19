"""Choix de design :
- Set comprehension : normalisation + déduplication en une expression.
  Le set absorbe les variantes ('Gold', ' gold ') une fois normalisées
  -> une seule entrée 'gold', sans gestion manuelle de doublons.
"""


def distinct_tiers(members: list[dict]) -> set[str]:
    return {m["tier"].strip().lower() for m in members}
