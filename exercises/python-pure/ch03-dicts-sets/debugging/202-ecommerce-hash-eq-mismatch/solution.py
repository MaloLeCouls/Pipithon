"""Correction :
- Bug : __hash__ renvoyait hash(id(self)) -> deux Coupon égaux par
  valeur ont des hash DIFFÉRENTS. Le contrat (a == b => hash(a) ==
  hash(b)) est rompu : le set ne déduplique pas, le dict ne retrouve
  pas la clé.
- Fix : hacher exactement les champs de __eq__ : hash((code, percent)).
"""


class Coupon:
    def __init__(self, code: str, percent: int) -> None:
        self.code = code
        self.percent = percent

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coupon):
            return NotImplemented
        return (self.code, self.percent) == (other.code, other.percent)

    def __hash__(self) -> int:
        return hash((self.code, self.percent))

    def __repr__(self) -> str:
        return f"Coupon({self.code!r}, {self.percent})"
