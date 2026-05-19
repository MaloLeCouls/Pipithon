"""Corrections (chirurgie minimale) :
- Bug 1 : __init__ ne stockait pas price -> ajout de self.price = price.
- Bug 2 : __repr__ n'entourait pas ref de guillemets -> !r sur self.ref
  (robuste même si ref contient une apostrophe).
Aucune autre ligne touchée.
"""


class Chair:
    def __init__(self, ref, price):
        self.ref = ref
        self.price = price

    def __repr__(self):
        return f"Chair(ref={self.ref!r}, price={self.price})"
