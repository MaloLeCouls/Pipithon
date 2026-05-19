"""Les étiquettes colis historiques sont encodées en latin-1.
decode_label les décode en utf-8 et plante (UnicodeDecodeError) dès
qu'un nom est accentué.
Corrige en chirurgie : même contrat, plus de crash, texte correct.
"""


def decode_label(raw: bytes) -> str:
    return raw.decode("utf-8")
