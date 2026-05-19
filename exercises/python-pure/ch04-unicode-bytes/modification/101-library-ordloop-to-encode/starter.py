"""Ce code fabrique des octets caractère par caractère. Ça "marche" sur
de l'ASCII, mais c'est faux dès qu'un titre est accentué.

Refactor `to_bytes` :
- utilise str.encode('utf-8'),
- comportement préservé sur l'ASCII, ET correct sur l'accentué.
"""


def to_bytes(title: str) -> bytes:
    return bytes([ord(c) for c in title])
