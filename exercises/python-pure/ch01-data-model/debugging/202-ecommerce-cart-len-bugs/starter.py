"""Ce panier a 2 bugs. Les tests les exposent.
Corrige en chirurgie, sans réécrire from scratch.
"""


class Cart:
    def __init__(self):
        self.items = []

    def add(self, sku):
        self.items = [sku]

    def __len__(self):
        return len(self.items) + 1
