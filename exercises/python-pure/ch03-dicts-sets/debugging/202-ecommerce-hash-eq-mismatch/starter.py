"""Coupon a 1 bug subtil : deux coupons "égaux" ne sont pas dédupliqués
dans un set, et servent mal de clé de dict.
Corrige en chirurgie, sans réécrire la classe.
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
        return hash(id(self))

    def __repr__(self) -> str:
        return f"Coupon({self.code!r}, {self.percent})"
