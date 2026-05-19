"""Choix de design :
- List comprehension : intention déclarative ('les prix > seuil'), une
  seule expression, pas d'état mutable intermédiaire.
- Nouvelle liste renvoyée : la fonction est pure, l'entrée n'est pas touchée.
"""


def expensive_prices(prices: list[int], threshold: int) -> list[int]:
    return [p for p in prices if p > threshold]
