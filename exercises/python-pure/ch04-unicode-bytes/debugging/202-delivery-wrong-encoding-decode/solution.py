"""Correction :
- Bug : la source est en latin-1 ; la décoder en utf-8 lève
  UnicodeDecodeError sur l'octet d'un caractère accentué (0xE9 pour 'é'
  n'est pas une séquence utf-8 valide).
- Fix : décoder avec le VRAI encodage, latin-1. Pas besoin de
  errors='replace' : le bon codec restitue le texte exact.
"""


def decode_label(raw: bytes) -> str:
    return raw.decode("latin-1")
