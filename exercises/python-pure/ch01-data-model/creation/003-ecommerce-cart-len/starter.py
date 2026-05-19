"""Un site e-commerce veut écrire `len(cart)` plutôt que `cart.count()`.

Implémente la classe `Cart` :
- `__init__` crée un panier vide.
- `add(self, sku: str)` ajoute un article (un SKU) au panier.
- `__len__` renvoie le nombre d'articles dans le panier.
"""


class Cart:
    def __init__(self) -> None:
        ...

    def add(self, sku: str) -> None:
        ...

    def __len__(self) -> int:
        ...
