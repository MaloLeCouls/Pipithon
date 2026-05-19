"""Choix de design :
- On NORMALISE le type à l'entrée (bytes -> str via decode) puis le
  traitement commun (strip) s'applique une seule fois : c'est le patron
  'dual-mode API' — convertir tôt, traiter en str ensuite.
- Type inattendu -> TypeError explicite plutôt qu'un .decode/.strip qui
  planterait avec un message obscur.
"""


def clean_title(value: "str | bytes") -> str:
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    elif not isinstance(value, str):
        raise TypeError("str ou bytes attendu")
    return value.strip()
