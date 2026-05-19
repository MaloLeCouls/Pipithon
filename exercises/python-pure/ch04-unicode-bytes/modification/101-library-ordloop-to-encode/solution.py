"""Choix de design :
- str.encode("utf-8") est LA primitive d'encodage : multioctet correct,
  testée, lisible. bytes([ord(c) ...]) confond code point et octet et
  lève ValueError dès qu'un code point dépasse 255 (accent, emoji).
"""


def to_bytes(title: str) -> bytes:
    return title.encode("utf-8")
