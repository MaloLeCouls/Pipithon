"""Choix de design :
- `contextlib.suppress(KeyError)` est strictement équivalent à
  `try: ... except KeyError: pass`, mais déclaratif et borné au bloc `with`.
  Plus de risque d'avaler accidentellement une autre exception en élargissant
  le `try`.
- On itère et on supprime un par un — `dict.pop` lève `KeyError` si absent,
  exactement ce que `suppress` ignore.
"""
from __future__ import annotations

from collections.abc import Iterable
from contextlib import suppress


class Task:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id


def bulk_close(tasks: dict[str, Task], task_ids: Iterable[str]) -> None:
    for tid in task_ids:
        with suppress(KeyError):
            tasks.pop(tid)
