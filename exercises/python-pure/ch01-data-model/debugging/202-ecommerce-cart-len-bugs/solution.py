"""Corrections (chirurgie minimale) :
- Bug 1 : add() faisait self.items = [sku] (réassignation) -> il écrasait
  tout le panier. Remplacé par self.items.append(sku).
- Bug 2 : __len__ retournait len(...) + 1 (off-by-one) -> on retire le +1.
"""


class Cart:
    def __init__(self):
        self.items = []

    def add(self, sku):
        self.items.append(sku)

    def __len__(self):
        return len(self.items)
