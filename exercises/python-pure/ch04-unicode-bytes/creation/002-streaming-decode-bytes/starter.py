"""Une plateforme de streaming reçoit des titres encodés.

Implémente `decode_title(raw: bytes, encoding: str) -> str` :
- décode `raw` avec l'encodage fourni,
- renvoie une str.
"""


def decode_title(raw: bytes, encoding: str) -> str:
    ...
