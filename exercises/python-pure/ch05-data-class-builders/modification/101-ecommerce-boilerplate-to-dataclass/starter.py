"""Cette classe écrit __init__, __repr__ et __eq__ à la main.

Refactor en @dataclass :
- mêmes champs (product_id: str, price: float),
- même repr : Product(product_id='A1', price=9.9),
- même égalité (champ à champ),
- plus aucun de ces dunders écrit manuellement.
"""


class Product:
    def __init__(self, product_id, price):
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"Product(product_id={self.product_id!r}, price={self.price})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.product_id, self.price) == (other.product_id, other.price)
