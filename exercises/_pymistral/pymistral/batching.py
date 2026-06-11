"""Request + BatchedRequests — groupement de requêtes. Chapitre 12 (sequences).

`BatchedRequests` est une séquence indexable/sliceable de `Request`. Sert de
base au `Scheduler` (ch12/ch19-21).
"""
from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from typing import overload

from pymistral.config import GenerationConfig
from pymistral.tokens import Token


@dataclass(slots=True)
class Request:
    """Une requête de génération : un prompt tokenisé + sa config."""

    id: str
    prompt: list[Token]
    config: GenerationConfig = field(default_factory=GenerationConfig)


class BatchedRequests:
    """Vue séquence sur un lot de Requests, immutable."""

    __slots__ = ("_requests",)

    def __init__(self, requests: Sequence[Request]) -> None:
        self._requests: tuple[Request, ...] = tuple(requests)

    @property
    def requests(self) -> tuple[Request, ...]:
        return self._requests

    def __len__(self) -> int:
        return len(self._requests)

    def __iter__(self) -> Iterator[Request]:
        return iter(self._requests)

    @overload
    def __getitem__(self, index: int) -> Request: ...
    @overload
    def __getitem__(self, index: slice) -> BatchedRequests: ...
    def __getitem__(self, index: int | slice) -> Request | BatchedRequests:
        if isinstance(index, slice):
            return BatchedRequests(self._requests[index])
        return self._requests[index]

    def __repr__(self) -> str:
        return f"BatchedRequests(size={len(self)})"
