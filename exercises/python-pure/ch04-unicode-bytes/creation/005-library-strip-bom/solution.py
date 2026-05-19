"""Choix de design :
- Le codec "utf-8-sig" consomme le BOM s'il est présent et se comporte
  comme "utf-8" sinon : une seule ligne couvre les deux cas, sans test
  manuel de préfixe (raw.startswith(b'\\xef\\xbb\\xbf')) fragile et
  facile à oublier.
"""


def read_header(raw: bytes) -> str:
    return raw.decode("utf-8-sig")
