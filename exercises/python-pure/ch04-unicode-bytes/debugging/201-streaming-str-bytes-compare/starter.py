"""is_expected doit dire si le jeton reçu (bytes, depuis le réseau)
correspond au jeton attendu (str). Il renvoie toujours False.
Corrige en chirurgie, sans réécrire la fonction.
"""


def is_expected(received: bytes, expected: str) -> bool:
    return received == expected
