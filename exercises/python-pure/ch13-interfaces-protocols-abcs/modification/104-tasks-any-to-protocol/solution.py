"""Choix de design :
- `Protocol` (sans runtime_checkable) suffit : on veut juste annoter
  finement, pas vérifier à runtime.
- mypy --strict valide les call sites : passer un objet sans `complete`
  devient une erreur de typage.
"""
from __future__ import annotations

from typing import Protocol


class Completable(Protocol):
    def complete(self) -> str: ...


def finish_task(task: Completable) -> str:
    return task.complete()
