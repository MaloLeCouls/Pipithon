"""`get_type_hints(BatchBuffer)` plante avec
`NameError: name 'List' is not defined`. Pourtant la classe a l'air OK.

Indices :
- `from __future__ import annotations` rend TOUTES les annotations
  des STRINGS, évaluées paresseusement.
- `get_type_hints` les évalue dans le SCOPE actuel. Si `List` n'est
  pas importé, ça plante.
- Fix : soit `from typing import List`, soit (recommandé) remplace
  `List[int]` par `list[int]` (builtin, PEP 585).

`inspect_buffer_hints()` doit renvoyer un dict des annotations
résolues. Avec la solution, c'est `{"items": list[int]}`.
"""
from __future__ import annotations

from typing import get_type_hints


class BatchBuffer:
    # BUG : `List` n'est pas importé.
    items: List[int]  # type: ignore[name-defined]

    def __init__(self, items: list[int]) -> None:
        self.items = items


def inspect_buffer_hints() -> dict[str, type]:
    return get_type_hints(BatchBuffer)
