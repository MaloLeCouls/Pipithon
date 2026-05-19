"""Choix de design :
- casefold() est conçu pour la comparaison sans casse (plis agressifs :
  'ß'->'ss', 'ﬁ'->'fi', 'İ'...). lower() est pour l'affichage humain.
  Sur l'ASCII les deux coïncident -> aucune régression.
"""


def same_ci(a: str, b: str) -> bool:
    return a.casefold() == b.casefold()
