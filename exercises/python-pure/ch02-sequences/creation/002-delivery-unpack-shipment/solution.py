"""Choix de design :
- Unpacking nommé : le tuple est un record, lui donner des noms rend la
  suite lisible et auto-documentée (vs shipment[1] cryptique).
- f-string pour assembler le message : direct et idiomatique.
"""


def describe(shipment: tuple[str, float, str]) -> str:
    tracking_id, weight_kg, eta = shipment
    return f"{tracking_id} -> {weight_kg}kg, ETA {eta}"
