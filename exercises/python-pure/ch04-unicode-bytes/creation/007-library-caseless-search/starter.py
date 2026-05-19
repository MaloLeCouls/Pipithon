"""Une bibliothèque cherche des livres par titre, insensible à la casse
ET robuste aux formes Unicode.

Implémente `search(titles: list[str], query: str) -> list[str]` :
- renvoie les titres qui CONTIENNENT `query`,
- comparaison insensible à la casse via str.casefold() (pas .lower()),
- robuste aux variantes Unicode : normalise en NFC avant comparaison,
- l'ordre d'origine est préservé.

Piège signalé : 'ß'.lower() != 'ss' mais 'ß'.casefold() == 'ss' ; et
sans NFC, 'Café' composé ne matche pas 'Café' décomposé.
"""


def search(titles: list[str], query: str) -> list[str]:
    ...
