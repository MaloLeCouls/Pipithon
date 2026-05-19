"""Une API de streaming reçoit un titre tantôt en str (front web),
tantôt en bytes UTF-8 (worker binaire). On veut UNE fonction dual-mode.

Implémente `clean_title(value: str | bytes) -> str` :
- si `value` est des bytes -> décode en UTF-8,
- si `value` est une str -> telle quelle,
- dans les deux cas : retire les espaces en début/fin (strip),
- tout autre type -> TypeError("str ou bytes attendu").
"""


def clean_title(value: "str | bytes") -> str:
    ...
