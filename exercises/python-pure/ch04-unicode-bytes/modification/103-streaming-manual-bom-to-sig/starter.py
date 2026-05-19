"""Ce code retire le BOM UTF-8 à la main avant de décoder.

Refactor `decode_feed` :
- utilise le codec 'utf-8-sig' (gère le BOM s'il existe, sinon comme utf-8),
- supprime le découpage manuel des octets,
- comportement strictement identique (avec BOM et sans BOM).
"""


def decode_feed(raw: bytes) -> str:
    bom = b"\xef\xbb\xbf"
    if raw.startswith(bom):
        raw = raw[3:]
    return raw.decode("utf-8")
