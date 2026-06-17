"""Cette `Box` stocke n'importe quoi mais perd le type côté mypy
(`Any` partout). Paramétrise-la sur `T` pour qu'un `Box(42)` donne
`unwrap() -> int`.

Solution attendue : `Box(Generic[T])` avec `value: T`.
"""
from __future__ import annotations

from typing import Any


class Box:
    def __init__(self, value: Any) -> None:
        self.value = value

    def unwrap(self) -> Any:
        return self.value
