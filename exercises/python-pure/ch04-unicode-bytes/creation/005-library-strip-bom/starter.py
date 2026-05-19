"""Une bibliothèque importe des CSV de partenaires. Certains fichiers
(exportés sous Windows) commencent par un BOM UTF-8 (octets EF BB BF),
d'autres non.

Implémente `read_header(raw: bytes) -> str` :
- décode `raw` en UTF-8,
- si un BOM est présent, il NE doit PAS apparaître dans la str renvoyée,
- fonctionne aussi quand il n'y a pas de BOM.
"""


def read_header(raw: bytes) -> str:
    ...
