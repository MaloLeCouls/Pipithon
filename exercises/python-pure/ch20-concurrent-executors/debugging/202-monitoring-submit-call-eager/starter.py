"""Bug observé : la fn ne parallélise rien — chaque probe est appelée
en série dans le thread principal. Pourtant tu vois bien `ex.submit`.

Indices :
- `ex.submit(probe(name))` ÉVALUE `probe(name)` EN PREMIER, puis submit
  la VALEUR (un int). Le pool ne fait rien.
- `ex.submit` attend `(fn, *args, **kwargs)`, comme `functools.partial`.
- Fix : `ex.submit(probe, name)` (pas de parenthèses sur probe).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    with ThreadPoolExecutor(max_workers=4) as ex:
        # BUG : probe(name) est évalué dans le thread principal, le pool
        # reçoit l'int, pas la fn. ex.submit(int_value) lève TypeError
        # car un int n'est pas callable.
        futures = [ex.submit(probe(name)) for name in names]  # type: ignore[arg-type]
    return [f.result() for f in futures]
