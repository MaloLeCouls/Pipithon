"""Choix de design :
- __len__ remplace size() : tout l'écosystème Python (len(), `if x:`,
  asserts) marche sans connaître d'API maison.
- On NE définit PAS __bool__ : en son absence, Python utilise __len__
  (0 -> False). empty() devient donc `not cart`, gratuitement et idiomatique.
"""


class Cart:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, sku: str) -> None:
        self.items.append(sku)

    def __len__(self) -> int:
        return len(self.items)
