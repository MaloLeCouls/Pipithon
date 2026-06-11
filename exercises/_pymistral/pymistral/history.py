"""ConversationHistory — buffer circulaire de tours. Chapitres 2 (sequences) & 16 (overload).

Utilise un `collections.deque` borné par `max_turns`. Supporte iteration,
indexation, slicing, et concaténation (`+`).
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import overload


@dataclass(frozen=True, slots=True)
class Turn:
    """Un tour de conversation (role + contenu)."""

    role: str  # "user" | "assistant" | "system"
    content: str

    def __repr__(self) -> str:
        return f"Turn(role={self.role!r}, content={self.content!r})"


class ConversationHistory:
    """Buffer borné de Turns. Les plus anciens tombent quand on dépasse."""

    def __init__(
        self,
        max_turns: int = 128,
        initial: Iterable[Turn] | None = None,
    ) -> None:
        self._max_turns = max_turns
        self._turns: deque[Turn] = deque(initial or [], maxlen=max_turns)

    @property
    def max_turns(self) -> int:
        return self._max_turns

    def append(self, turn: Turn) -> None:
        self._turns.append(turn)

    def extend(self, turns: Iterable[Turn]) -> None:
        self._turns.extend(turns)

    def clear(self) -> None:
        self._turns.clear()

    def __len__(self) -> int:
        return len(self._turns)

    def __iter__(self) -> Iterator[Turn]:
        return iter(self._turns)

    @overload
    def __getitem__(self, index: int) -> Turn: ...
    @overload
    def __getitem__(self, index: slice) -> list[Turn]: ...
    def __getitem__(self, index: int | slice) -> Turn | list[Turn]:
        if isinstance(index, slice):
            return list(self._turns)[index]
        return self._turns[index]

    def __add__(self, other: ConversationHistory) -> ConversationHistory:
        """Concaténation non destructive ; max_turns hérité du membre gauche."""
        merged = ConversationHistory(max_turns=self._max_turns)
        merged.extend(self._turns)
        merged.extend(other._turns)
        return merged

    def __repr__(self) -> str:
        return f"ConversationHistory(len={len(self)}, max_turns={self._max_turns})"
