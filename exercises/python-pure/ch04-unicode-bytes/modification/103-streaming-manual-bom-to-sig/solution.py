"""Choix de design :
- "utf-8-sig" encapsule exactement la règle 'consomme un BOM s'il est
  présent' et se comporte comme "utf-8" sinon. Une expression, pas de
  constante d'octets ni de slicing à maintenir (et pas de risque de
  rogner 3 octets utiles si on se trompe de condition).
"""


def decode_feed(raw: bytes) -> str:
    return raw.decode("utf-8-sig")
