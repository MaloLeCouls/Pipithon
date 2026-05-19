"""Choix de design :
- __repr__ utilise !r (repr) sur ref pour les guillemets gratuits et corrects
  même si la ref contient une apostrophe — plus robuste qu'un f-string manuel.
- price est un int : pas de !r, on veut 99 et non '99'.
"""


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        self.ref = ref
        self.price = price

    def __repr__(self) -> str:
        return f"Chair(ref={self.ref!r}, price={self.price})"
