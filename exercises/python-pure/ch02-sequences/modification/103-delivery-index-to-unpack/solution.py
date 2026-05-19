"""Choix de design :
- Un unpacking nommé en tête de fonction documente le record une fois
  pour toutes ; la logique devient lisible (express, zone...) au lieu
  d'un rébus rec[3]/rec[0]. Zéro changement de comportement.
"""


def routing_label(rec: tuple) -> str:
    tracking_id, weight_kg, zone, express = rec
    if express:
        return f"{tracking_id} [EXPRESS {zone}] {weight_kg}kg"
    return f"{tracking_id} [{zone}] {weight_kg}kg"
