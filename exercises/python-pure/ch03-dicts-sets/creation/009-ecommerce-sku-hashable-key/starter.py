"""Un entrepôt indexe son stock par référence produit. La référence
combine un `code` et une `variant` (ex. couleur).

Implémente la classe `Sku` :
- `__init__(self, code: str, variant: str)`.
- Deux Sku sont égaux ssi `code` ET `variant` sont égaux.
- Un Sku doit pouvoir servir de clé de dict et d'élément de set,
  de façon cohérente avec cette égalité.
- `__repr__` : Sku(code='A1', variant='red').

Ensuite, implémente `build_stock(rows: list[tuple]) -> dict`:
- `rows` est une liste de ((code, variant), qty),
- renvoie un dict {Sku: qty_total} (les quantités du même Sku s'additionnent).
"""


class Sku:
    def __init__(self, code: str, variant: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


def build_stock(rows: list[tuple]) -> dict:
    ...
