"""Ce code marche mais n'est pas pythonique : getters triviaux, pas de __repr__.

Refactor :
1. Supprime get_ref et get_price ; expose `ref` et `price` directement.
2. Ajoute __repr__ -> Chair(ref='A1', price=99).
3. Ne casse aucun comportement (les valeurs restent accessibles).
"""


class Chair:
    def __init__(self, ref, price):
        self.ref = ref
        self.price = price

    def get_ref(self):
        return self.ref

    def get_price(self):
        return self.price
