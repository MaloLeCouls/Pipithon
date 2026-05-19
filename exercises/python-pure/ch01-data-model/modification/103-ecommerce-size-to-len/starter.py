"""Ce panier expose size() et empty(). C'est du non-pythonique.

Refactor :
1. Remplace size() par __len__.
2. Supprime size() ET empty() : `len(cart)` et `if cart:` doivent suffire.
3. add() inchangé. N'ajoute PAS __bool__ (le fallback sur __len__ suffit).
"""


class Cart:
    def __init__(self):
        self.items = []

    def add(self, sku):
        self.items.append(sku)

    def size(self):
        return len(self.items)

    def empty(self):
        return self.size() == 0
