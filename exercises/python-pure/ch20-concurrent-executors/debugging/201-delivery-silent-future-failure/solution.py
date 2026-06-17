"""Fix : collecter les futures et appeler `.result()` sur chacune.
Si l'une a levé, le re-raise propage à l'appelant.

Convention serving : si on veut DURCIR sans crasher, on remplace
`.result()` par `.exception()` + branche d'erreur (cf. exo 006).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def deliver(tid: str) -> str:
    time.sleep(0.001)
    if tid == "FORBIDDEN":
        raise PermissionError(f"refused: {tid}")
    return f"ok:{tid}"


def dispatch(ids: list[str]) -> str:
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(deliver, tid) for tid in ids]
        for fut in futures:
            fut.result()  # re-raise toute exception
    return "all dispatched"
