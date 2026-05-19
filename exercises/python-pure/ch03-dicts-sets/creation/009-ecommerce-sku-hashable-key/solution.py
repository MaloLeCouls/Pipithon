"""Choix de design :
- __eq__ et __hash__ portent sur le MÊME couple (code, variant) : c'est
  le contrat de hashabilité (a == b => hash(a) == hash(b)). Le violer
  casse silencieusement set/dict — exactement le genre de bug qu'on
  traque en review de PR vLLM/transformers.
- hash((code, variant)) : on délègue au hash d'un tuple, déjà correct.
- build_stock s'appuie sur ce contrat : un même Sku rencontré deux fois
  est UNE seule clé, on cumule.
"""


class Sku:
    def __init__(self, code: str, variant: str) -> None:
        self.code = code
        self.variant = variant

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sku):
            return NotImplemented
        return (self.code, self.variant) == (other.code, other.variant)

    def __hash__(self) -> int:
        return hash((self.code, self.variant))

    def __repr__(self) -> str:
        return f"Sku(code={self.code!r}, variant={self.variant!r})"


def build_stock(rows: list[tuple]) -> dict:
    stock: dict[Sku, int] = {}
    for (code, variant), qty in rows:
        sku = Sku(code, variant)
        stock[sku] = stock.get(sku, 0) + qty
    return stock
