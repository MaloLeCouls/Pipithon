"""Tu dispatches N livraisons. Une lève. Et pourtant `dispatch` rend
joyeusement « all dispatched » sans broncher.

Indices :
- `ex.submit(...)` rend une Future. Si tu ne LIS jamais son résultat
  (.result()) ni son exception (.exception()), Python te ne voit pas
  passer l'erreur.
- `with ... as ex:` ATTEND la fin, ne lit RIEN.
- Fix : boucle sur `futures` et appelle `fut.result()` (re-raise).
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
    # BUG : on ne lit pas les futures, donc les erreurs sont silencieuses.
    with ThreadPoolExecutor(max_workers=4) as ex:
        for tid in ids:
            ex.submit(deliver, tid)
    return "all dispatched"
