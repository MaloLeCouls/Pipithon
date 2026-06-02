"""Choix de design :
- typing.NamedTuple ajoute des noms (leg.origin) ET reste un tuple :
  l'indexation/unpacking existants ne cassent pas (compat ascendante),
  on gagne lisibilité, repr et égalité gratuits, sans toucher l'appelant.
"""

from typing import NamedTuple


class Leg(NamedTuple):
    origin: str
    dest: str
    km: float


def make_leg(origin: str, dest: str, km: float) -> Leg:
    return Leg(origin, dest, km)
