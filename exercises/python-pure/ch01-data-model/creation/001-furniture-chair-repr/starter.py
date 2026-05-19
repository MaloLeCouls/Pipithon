"""Une entreprise de meubles veut des objets lisibles dans ses logs.

Implémente la classe `Chair` :
- `__init__(self, ref: str, price: int)` stocke `ref` et `price`.
- `__repr__` renvoie EXACTEMENT : Chair(ref='A1', price=99)
  (guillemets autour de la ref, pas autour du prix).
"""


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        ...

    def __repr__(self) -> str:
        ...
