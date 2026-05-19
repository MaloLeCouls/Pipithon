"""Un scanner de colis lit des étiquettes parfois abîmées (octets
corrompus). Le système ne doit JAMAIS crasher dessus.

Implémente `safe_decode(raw: bytes) -> str` :
- décode `raw` en UTF-8,
- remplace les octets invalides par le caractère de remplacement
  Unicode (U+FFFD) au lieu de lever une exception,
- ne lève jamais UnicodeDecodeError.
"""


def safe_decode(raw: bytes) -> str:
    ...
