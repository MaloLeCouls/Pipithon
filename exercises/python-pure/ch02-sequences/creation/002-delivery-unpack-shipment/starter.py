"""Un service de livraison reçoit chaque colis sous forme de tuple
(tracking_id, weight_kg, eta).

Implémente `describe(shipment: tuple[str, float, str]) -> str` :
- déballe le tuple par unpacking (pas de shipment[0], shipment[1]...),
- renvoie : "ABC123 -> 2.5kg, ETA 10:00".
"""


def describe(shipment: tuple[str, float, str]) -> str:
    ...
