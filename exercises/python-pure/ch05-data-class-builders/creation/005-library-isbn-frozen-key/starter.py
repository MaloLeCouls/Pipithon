"""Une bibliothèque indexe ses prêts par identifiant de livre.

Implémente `BookId` avec @dataclass(frozen=True) :
- champs : `isbn: str`, `copy_no: int`,
- immuable (réassigner un champ lève FrozenInstanceError),
- hashable -> utilisable comme clé de dict / élément de set.
"""

from dataclasses import dataclass  # noqa: F401


class BookId:
    ...
