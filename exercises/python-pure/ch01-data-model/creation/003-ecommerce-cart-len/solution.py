"""Choix de design :
- Stockage interne dans une list : ordre d'ajout préservé, doublons permis
  (un panier peut contenir deux fois le même SKU).
- __len__ délègue à len(self._items) : une seule source de vérité.
"""


class Cart:
    def __init__(self) -> None:
        self._items: list[str] = []

    def add(self, sku: str) -> None:
        self._items.append(sku)

    def __len__(self) -> int:
        return len(self._items)
