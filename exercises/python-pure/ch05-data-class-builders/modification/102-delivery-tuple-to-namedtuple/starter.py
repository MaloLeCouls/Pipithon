"""make_leg renvoie un tuple positionnel (origin, dest, km). Le code
appelant lit leg[0], leg[1]... illisible et fragile.

Refactor :
1. Définis `Leg` avec typing.NamedTuple (origin: str, dest: str, km: float).
2. make_leg renvoie un Leg.
Contrainte : le code tuple existant (indexation, unpacking) DOIT
continuer à marcher — un NamedTuple est un tuple.
"""


def make_leg(origin: str, dest: str, km: float):
    return (origin, dest, km)
