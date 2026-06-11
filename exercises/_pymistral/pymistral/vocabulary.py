"""Vocabulary — mapping bidirectionnel id<->text en O(1). Chapitre 3 (dicts).

Pas de tri, pas de fréquences : c'est un *index*. Pour étendre il faut passer
par `add` (qui dédoublonne) ; les lookups sont O(1) dans les deux sens grâce
à deux dicts maintenus en miroir.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Vocabulary:
    """Index bidirectionnel id<->text avec dédoublonnage."""

    def __init__(self, initial: Iterable[str] | None = None) -> None:
        self._text_to_id: dict[str, int] = {}
        self._id_to_text: dict[int, str] = {}
        if initial is not None:
            for text in initial:
                self.add(text)

    def add(self, text: str) -> int:
        """Ajoute `text` s'il n'existe pas, renvoie son id."""
        if text in self._text_to_id:
            return self._text_to_id[text]
        new_id = len(self._text_to_id)
        self._text_to_id[text] = new_id
        self._id_to_text[new_id] = text
        return new_id

    def text_of(self, id_: int) -> str:
        return self._id_to_text[id_]

    def id_of(self, text: str) -> int:
        return self._text_to_id[text]

    def __len__(self) -> int:
        return len(self._text_to_id)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return item in self._text_to_id
        if isinstance(item, int):
            return item in self._id_to_text
        return False

    def __iter__(self) -> Iterator[str]:
        return iter(self._text_to_id)

    def __repr__(self) -> str:
        return f"Vocabulary(size={len(self)})"
