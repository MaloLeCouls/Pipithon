"""Choix de design :
- __bool__ renvoie explicitement un bool via la comparaison `> 0`
  (et non `bool(self.remaining_days)`, qui serait vrai pour des jours négatifs).
- Pas de __len__ ici : la vérité de l'objet est sémantique (valable ou non),
  pas une histoire de taille.
"""


class Subscription:
    def __init__(self, remaining_days: int) -> None:
        self.remaining_days = remaining_days

    def __bool__(self) -> bool:
        return self.remaining_days > 0
