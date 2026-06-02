"""Correction :
- Bug : @dataclass genere __eq__ par defaut, ce qui force __hash__
  a None -> Customer devient non hashable, set/dict refusent.
- Fix : frozen=True. Une dataclass frozen genere a la fois __eq__
  ET un __hash__ coherent (base sur le tuple des champs), et c'est
  legitime ici parce qu'un identifiant client est immutable.
- Alternative `eq=True, unsafe_hash=True` existe mais ment sur la
  mutabilite : on prefere frozen=True qui dit la verite.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    customer_id: str
    email: str


def dedupe_customers(customers: list[Customer]) -> list[Customer]:
    seen: set[Customer] = set()
    out: list[Customer] = []
    for c in customers:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out
