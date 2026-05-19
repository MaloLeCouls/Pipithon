"""Choix de design :
- Attributs publics directs : en Python, un getter qui ne fait que `return
  self.x` est du bruit ; si une validation devient nécessaire plus tard,
  on passe à @property sans changer l'API appelante.
- __repr__ avec !r sur ref (str) et brut sur price (int).
"""


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        self.ref = ref
        self.price = price

    def __repr__(self) -> str:
        return f"Chair(ref={self.ref!r}, price={self.price})"
