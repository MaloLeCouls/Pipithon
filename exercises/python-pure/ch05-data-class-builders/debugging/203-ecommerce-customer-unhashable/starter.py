"""dedupe_customers doit renvoyer la liste des clients uniques en
preservant l'ordre d'apparition. Il leve TypeError: unhashable
type: 'Customer'.

La classe Customer represente un identifiant immutable (customer_id,
email). Corrige Customer pour que set(...) marche, sans casser
l'egalite champ-a-champ ni la signature de dedupe_customers.
"""

from dataclasses import dataclass


@dataclass
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
