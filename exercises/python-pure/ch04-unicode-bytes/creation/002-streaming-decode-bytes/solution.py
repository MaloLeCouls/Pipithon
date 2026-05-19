"""Choix de design :
- .decode(encoding) explicite : décoder avec le MÊME encodage que
  l'émetteur est non négociable. Deviner mène à des Mojibake silencieux
  ou des UnicodeDecodeError — ici l'encodage est fourni, on l'utilise.
"""


def decode_title(raw: bytes, encoding: str) -> str:
    return raw.decode(encoding)
