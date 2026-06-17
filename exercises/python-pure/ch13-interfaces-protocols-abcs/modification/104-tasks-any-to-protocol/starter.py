"""La fn `finish_task` prend `Any` parce qu'on s'est dit « ça acceptera
toute classe avec `complete()` ». OK, mais ça AVEUGLE mypy : on peut lui
passer `42` sans qu'il bronche.

Refactore : crée un `Completable(Protocol)` qui exige `complete() -> str`,
et annote `task: Completable`. Comportement runtime inchangé, garanties
de typage gagnées.

NB : `tests_form_kind: mypy` actif — la solution doit passer `mypy --strict`.
"""
from __future__ import annotations

from typing import Any


def finish_task(task: Any) -> str:
    return task.complete()
